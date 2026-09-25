# Extracted class/method source from cornell-zhang/SmoothE src/dag_greedy.py
# at 8de74ef2b53aabbb35898400cb5eb890d9a07a54. Apache-2.0.
# Only required upstream definitions are retained. Package CLI/data-loading
# imports are omitted; the algorithm methods below are not changed.
from collections import defaultdict, deque

class CostSet:

    def __init__(self, costs=None, total=0, choice=None):
        self.costs = costs or {}
        self.total = total
        self.choice = choice


class FasterGreedyDagExtractor:

    def calculate_cost_set(self, node, costs, cost_of_node, egraph_enodes,
                           best_cost):
        if not egraph_enodes[node].eclass_id:
            return CostSet(
                {egraph_enodes[node].belong_eclass_id: cost_of_node[node]},
                cost_of_node[node], node)

        children_classes = list(
            set(child for child in egraph_enodes[node].eclass_id))

        cid = egraph_enodes[node].belong_eclass_id
        if cid in children_classes:
            return CostSet({}, float("inf"), node)

        first_cost = costs[children_classes[0]]
        if (
                # len(children_classes) == 1
                cost_of_node[node] + first_cost.total > best_cost):
            return CostSet({}, float("inf"), node)

        result = costs[children_classes[0]].costs.copy()
        for child_cid in children_classes[1:]:
            result.update(costs[child_cid].costs)

        contain = cid in result
        result[cid] = cost_of_node[node]
        result_cost = float("inf") if contain else sum(result.values())

        return CostSet(result, result_cost, node)

    # @profile
    def extract(self, cost_of_node, egraph_enodes, egraph_eclasses=None):
        "int index for elcass id and enode id"
        parents = defaultdict(list)
        analysis_pending = UniqueQueue()

        for node in egraph_enodes:
            if egraph_enodes[node].eclass_id == [] or egraph_enodes[
                    node].eclass_id == set():
                analysis_pending.insert(node)  #leaf node
            else:
                for child_class in egraph_enodes[node].eclass_id:
                    parents[child_class].append(node)

        costs = {}
        while analysis_pending:
            node = analysis_pending.pop()
            class_id = egraph_enodes[node].belong_eclass_id

            if all(child_class in costs
                   for child_class in egraph_enodes[node].eclass_id):
                if class_id in costs:
                    prev_cost = costs.get(class_id).total
                    # prev_choice = costs.get(class_id).choice
                else:
                    prev_cost = float("inf")

                cost_set = self.calculate_cost_set(node, costs, cost_of_node,
                                                   egraph_enodes, prev_cost)
                if cost_set.total < prev_cost:
                    costs[class_id] = cost_set
                    analysis_pending.extend(parents[class_id])
                # elif cost_set.total == prev_cost and prev_cost != float("inf"):
                #     if cost_set.choice < prev_choice:  # we remove the randomness
                #         costs[class_id] = cost_set
                #         analysis_pending.extend(parents[class_id])

        result = ExtractionResult()
        for cid, cost_set in costs.items():
            result.choose(cid, cost_set.choice)

        return result, costs


class UniqueQueue:

    def __init__(self):
        self.set = set()
        self.queue = deque()

    def insert(self, item):
        if item not in self.set:
            self.set.add(item)
            self.queue.append(item)

    def extend(self, items):
        for item in items:
            self.insert(item)

    def pop(self):
        if not self.queue:
            return None
        item = self.queue.popleft()
        self.set.remove(item)
        return item

    def __bool__(self):
        return bool(self.queue)


class ExtractionResult:

    def __init__(self):
        self.choices = {}
        self.final_dag = []

    def choose(self, class_id, node_id):
        self.choices[class_id] = node_id
