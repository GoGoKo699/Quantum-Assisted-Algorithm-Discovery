"""Learn bounded question-and-action trees on a small public image corpus.

No Action-BED reproduction, quantum execution, or advantage benchmark. The
protocol is frozen in PROTOCOL.md. NumPy and scikit-learn provide data and the
CART comparator; the exact subset dynamic program is independently written.
Outputs are created exclusively. Only a fixed training split is optimized.
"""
from __future__ import annotations
import argparse
import hashlib
import itertools
import json
from pathlib import Path
import random
import time
from typing import Any

import numpy as np
import sklearn
from sklearn.datasets import load_digits
from sklearn.tree import DecisionTreeClassifier


class ResourceLimit(RuntimeError):
    pass


def bitmask(bits: np.ndarray) -> int:
    return int.from_bytes(np.packbits(np.asarray(bits, dtype=np.uint8), bitorder='little').tobytes(), 'little')


class ExactTree:
    """Exact empirical accuracy in the at-most-depth binary-query policy class.

    State is the remaining sample subset and query budget. Previously used
    queries are constant on that subset, so no separate history is required.
    Integer row masks are machine bitsets, not a claim of unit cost for N bits.
    """
    def __init__(self, x: np.ndarray, y: np.ndarray, state_cap: int = 3_000_000,
                 seconds: float = 60.0):
        if x.ndim != 2 or len(y) != len(x) or len(x) == 0:
            raise ValueError('Expected nonempty aligned feature/label arrays.')
        if not np.isin(x, [0, 1]).all() or np.any(y < 0):
            raise ValueError('Features must be binary and labels nonnegative.')
        self.n, self.f = x.shape
        self.classes = int(y.max()) + 1
        self.qmask = [bitmask(x[:, j]) for j in range(self.f)]
        self.ymask = [bitmask(y == k) for k in range(self.classes)]
        self.all = (1 << self.n) - 1
        self.cache: dict[tuple[int, int], tuple[int, int]] = {}
        self.leaves: dict[int, tuple[int, int]] = {}
        self.state_cap, self.seconds = state_cap, seconds
        self.started = time.perf_counter()
        self.split_candidates = 0
        self.constant_skips = 0
        self.cache_hits = 0
        self.pure_states = 0

    def majority(self, s: int) -> tuple[int, int]:
        if s not in self.leaves:
            counts = [(s & m).bit_count() for m in self.ymask]
            label = max(range(self.classes), key=lambda k: (counts[k], -k))
            self.leaves[s] = (counts[label], label)
        return self.leaves[s]

    def solve(self, s: int, budget: int) -> tuple[int, int]:
        key = (s, budget)
        if key in self.cache:
            self.cache_hits += 1
            return self.cache[key]
        count, label = self.majority(s)
        # Negative decision -label-1 denotes stopping and predicting that class.
        best = (count, -label-1)
        if budget and count < s.bit_count():
            for j, m in enumerate(self.qmask):
                yes = s & m
                no = s ^ yes
                if not yes or not no:
                    self.constant_skips += 1
                    continue
                self.split_candidates += 1
                candidate = self.solve(no, budget-1)[0] + self.solve(yes, budget-1)[0]
                if candidate > best[0]:
                    best = (candidate, j)
                if best[0] == s.bit_count():
                    break  # No possible tree can classify more than every row.
        elif count == s.bit_count():
            self.pure_states += 1
        self.cache[key] = best
        if len(self.cache) > self.state_cap:
            raise ResourceLimit('State cap exceeded; no optimum asserted.')
        if len(self.cache) % 1024 == 0 and time.perf_counter()-self.started > self.seconds:
            raise ResourceLimit('Wall-time cap exceeded; no optimum asserted.')
        return best

    def tree(self, s: int, budget: int) -> dict[str, Any]:
        score, decision = self.solve(s, budget)
        if decision < 0:
            return {'label': -decision-1}
        yes = s & self.qmask[decision]
        return {'query': decision, 'no': self.tree(s ^ yes, budget-1),
                'yes': self.tree(yes, budget-1)}

    def stats(self) -> dict[str, int]:
        return dict(dynamic_states=len(self.cache), distinct_subsets=len(self.leaves),
                    split_candidates=self.split_candidates, constant_skips=self.constant_skips,
                    cache_hits=self.cache_hits, pure_states=self.pure_states)


def predict(tree: dict, x: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    labels, queries = [], []
    for row in x:
        node, length = tree, 0
        while 'query' in node:
            node = node['yes'] if row[node['query']] else node['no']
            length += 1
        labels.append(node['label'])
        queries.append(length)
    return np.array(labels), np.array(queries)


def size(tree: dict) -> tuple[int, int]:
    if 'label' in tree:
        return 0, 1
    a, b = size(tree['no']), size(tree['yes'])
    return 1+a[0]+b[0], a[1]+b[1]


def export_cart(clf: DecisionTreeClassifier, node: int = 0) -> dict:
    t = clf.tree_
    if t.children_left[node] == t.children_right[node]:
        k = int(np.argmax(t.value[node][0]))
        return {'label': int(clf.classes_[k])}
    if not 0 <= t.threshold[node] < 1:
        raise AssertionError('Unexpected nonbinary CART split.')
    return {'query': int(t.feature[node]), 'no': export_cart(clf, t.children_left[node]),
            'yes': export_cart(clf, t.children_right[node])}


def static_subset(x: np.ndarray, y: np.ndarray, depth: int) -> dict:
    classes = int(y.max()) + 1
    fallback = int(np.argmax(np.bincount(y, minlength=classes)))
    best, chosen, decoder = -1, None, None
    for subset in itertools.combinations(range(x.shape[1]), depth):
        codes = (x[:, subset] * (1 << np.arange(depth))).sum(axis=1)
        counts = np.bincount(codes*classes+y, minlength=(1 << depth)*classes).reshape(-1, classes)
        score = int(counts.max(axis=1).sum())
        if score > best:
            best, chosen = score, list(subset)
            decoder = counts.argmax(axis=1)
            decoder[counts.sum(axis=1) == 0] = fallback
    return dict(queries=chosen, decoder=list(map(int, decoder)), training_correct=best)


def static_predict(policy: dict, x: np.ndarray) -> np.ndarray:
    subset = policy['queries']
    codes = (x[:, subset] * (1 << np.arange(len(subset)))).sum(axis=1)
    return np.asarray(policy['decoder'])[codes]


def correctness_controls() -> dict:
    # Independently enumerate every full depth-two binary classification tree
    # on three bits: 3^3 internal-query assignments * 2^4 leaf assignments.
    x = np.array(list(itertools.product([0, 1], repeat=3)), dtype=np.uint8)
    correct = cases = 0
    rng = random.Random(2026092611)
    for _ in range(40):
        y = np.array([rng.randrange(2) for _ in range(8)], dtype=np.int64)
        brute = -1
        for root, left, right in itertools.product(range(3), repeat=3):
            leaf_ids = 2*x[:, root] + np.where(x[:, root], x[:, right], x[:, left])
            for leaf_labels in itertools.product([0, 1], repeat=4):
                labels = np.array(leaf_labels)[leaf_ids]
                brute = max(brute, int((labels == y).sum()))
                cases += 1
        solver = ExactTree(x, y)
        score = solver.solve(solver.all, 2)[0]
        tree = solver.tree(solver.all, 2)
        replay = int((predict(tree, x)[0] == y).sum())
        if brute != score or score != replay:
            raise AssertionError('Independent full-tree enumeration mismatch.')
        correct += 1
    return dict(labelings_checked=correct, full_trees_evaluated=cases,
                scope='Small binary control, exact integer accuracy. Not a performance experiment.')


def data() -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, dict]:
    d = load_digits()
    images = d.images.astype(np.uint8)
    y = d.target.astype(np.int64)
    if images.shape != (1797, 8, 8) or images.min() != 0 or images.max() != 16:
        raise AssertionError('Unexpected bundled corpus shape or scale.')
    x = (images.reshape(-1, 4, 2, 4, 2).sum(axis=(2, 4)).reshape(-1, 16) >= 32).astype(np.uint8)
    train, test = [], []
    for label in range(10):
        indices = list(map(int, np.flatnonzero(y == label)))
        indices.sort(key=lambda i: hashlib.sha256(f'20260926:digits-split:{i}'.encode('ascii')).digest())
        n = (2*len(indices))//3
        train.extend(indices[:n]); test.extend(indices[n:])
    train, test = np.array(sorted(train)), np.array(sorted(test))
    packed = np.column_stack([images.reshape(-1, 64), y]).astype(np.uint8)
    meta = dict(dataset='sklearn bundled UCI optical digits test subset',
                examples=len(y), train_examples=len(train), test_examples=len(test),
                corpus_uint8_row_sha256=hashlib.sha256(packed.tobytes()).hexdigest(),
                feature_uint8_sha256=hashlib.sha256(x.tobytes()).hexdigest(),
                train_indices_sha256=hashlib.sha256(train.astype('<u4').tobytes()).hexdigest(),
                test_indices_sha256=hashlib.sha256(test.astype('<u4').tobytes()).hexdigest(),
                train_indices=train.tolist(), test_indices=test.tolist(),
                split_scope='One deterministic within-class split; not unseen-writer validation.',
                query='row-major nonoverlapping 2x2 patch sum >= 32', query_count=16)
    return x, y, train, test, meta


def evaluate_tree(tree, xtr, ytr, xte, yte):
    ptr, ntr = predict(tree, xtr); pte, nte = predict(tree, xte)
    return dict(training_correct=int((ptr == ytr).sum()), test_correct=int((pte == yte).sum()),
                training_queries_total=int(ntr.sum()), test_queries_total=int(nte.sum()),
                query_nodes=size(tree)[0], leaves=size(tree)[1], max_queries_test=int(nte.max()),
                tree=tree)


def run() -> tuple[dict, dict]:
    t = time.perf_counter()
    controls = correctness_controls()
    x, y, tr, te, meta = data()
    xtr, ytr, xte, yte = x[tr], y[tr], x[te], y[te]
    prep_time = time.perf_counter()-t
    results, timings = [], []
    # Fixed protocol: no choice below depends on held-out outcomes.
    for depth in (1, 2, 3, 4):
        t = time.perf_counter()
        solver = ExactTree(xtr, ytr)
        optimum = solver.solve(solver.all, depth)[0]
        tree = solver.tree(solver.all, depth)
        solve_seconds = time.perf_counter()-t
        stats = solver.stats()
        t = time.perf_counter()
        clf = DecisionTreeClassifier(criterion='gini', max_depth=depth, random_state=20260926)
        clf.fit(xtr, ytr)
        ctree = export_cart(clf)
        cart_seconds = time.perf_counter()-t
        t = time.perf_counter()
        fixed = static_subset(xtr, ytr, depth)
        static_seconds = time.perf_counter()-t
        # Only now evaluate all fitted policies on the held-out split.
        exact = evaluate_tree(tree, xtr, ytr, xte, yte)
        cart = evaluate_tree(ctree, xtr, ytr, xte, yte)
        if not np.array_equal(predict(ctree, xte)[0], clf.predict(xte)):
            raise AssertionError('Native CART export mismatch.')
        fixed['test_correct'] = int((static_predict(fixed, xte) == yte).sum())
        if int((static_predict(fixed, xtr) == ytr).sum()) != fixed['training_correct']:
            raise AssertionError('Static policy training replay mismatch.')
        if exact['training_correct'] != optimum or optimum < max(cart['training_correct'], fixed['training_correct']):
            raise AssertionError('Exact tree did not dominate admissible empirical comparators.')
        if exact['max_queries_test'] > depth:
            raise AssertionError('Query-budget violation.')
        exact['dynamic_programming'] = stats
        row = dict(budget=depth, exact=exact, cart=cart, nonadaptive=fixed)
        results.append(row)
        timings.append(dict(budget=depth, exact_fit_seconds=solve_seconds,
                            cart_fit_seconds=cart_seconds, static_fit_seconds=static_seconds))
        print(json.dumps(dict(depth=depth, train=[exact['training_correct'], cart['training_correct'], fixed['training_correct']],
              test=[exact['test_correct'], cart['test_correct'], fixed['test_correct']],
              states=stats['dynamic_states'], exact_seconds=solve_seconds)), flush=True)
    # Full 16-bit-signature ceiling for an empirical classifier. This is computed
    # only as a training upper bound, not tuned or evaluated as a new test method.
    codes = (xtr.astype(np.uint32)*(1 << np.arange(16, dtype=np.uint32))).sum(axis=1)
    counts = np.bincount((codes*10+ytr).astype(int), minlength=(1 << 16)*10).reshape(-1, 10)
    ceiling = int(counts.max(axis=1).sum())
    report = dict(scope='Classical policy-discovery screen on real small data. No quantum advantage or Action-BED reproduction.',
                  protocol='PROTOCOL.md', data=meta, correctness_controls=controls,
                  full_signature_training_ceiling=ceiling, results=results)
    observations = dict(numpy=np.__version__, sklearn=sklearn.__version__,
                        setup_and_controls_seconds=prep_time, fit_timings=timings,
                        timing_scope='One local serial run; imports excluded, controls/data included separately. Not portable fixtures or hardware forecasts.')
    return report, observations


if __name__ == '__main__':
    if not __debug__:
        raise SystemExit('Do not use Python -O/-OO.')
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--observations', type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists() or args.observations.exists():
        raise SystemExit('Refusing to overwrite existing reports.')
    report, observations = run()
    for path, obj in ((args.output, report), (args.observations, observations)):
        with path.open('x', encoding='utf8') as f:
            json.dump(obj, f, indent=2, sort_keys=True); f.write('\n')
