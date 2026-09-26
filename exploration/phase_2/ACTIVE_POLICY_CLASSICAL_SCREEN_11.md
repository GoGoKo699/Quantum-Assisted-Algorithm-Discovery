# Learn the complete policy before attributing its cost to probabilities

26 September 2026. Phase 2, PRX Quantum target, manuscript on hold.
Repository base read: 418f5744b656578f572c60d320a9e4f8d65536f7.

## Decision and scope

This round trained complete question-and-action policies on public handwritten-digit data. It is a small source-aware classical workload screen, not an Action-BED reproduction, a practical image-recognition advance, a new decision-tree algorithm, or quantum-advantage evidence. No quantum algorithm was run. The result argues against using this small finite-data formulation as an advantage candidate; it does not reject active classification or all larger policy-learning problems.

The useful outcome is an executable policy: which one-bit patch measurement to request next, depending on earlier answers, and which digit to report after at most four measurements. It is not merely an estimate of the Bayes-optimal value with the decision rule omitted. The exported policy accepts only a sensor callback, so its deployed action cannot inspect the true label, unrequested pixels, or the training-row identity.

## Public task and protocol fixed before outcomes

Action-BED [1] includes partial-observation image classification. We retain that question-and-action task shape but use a different, smaller corpus and observation interface. These changes are explicitly our calibration choices, not a subset of the paper's reported experiment or independently justified engineering requirements.

The installed scikit-learn digits corpus [2,3] contains 1797 images of size 8 by 8, with integer intensities 0 through 16 and ten digit labels. This is the bundled test subset of UCI optical digits, not MNIST. We subdivide this corpus for the present screen; our held-out split is not the original benchmark split or an unseen-writer study.

There are sixteen nonoverlapping 2-by-2 patches, row-major indexed 0 through 15. A query returns whether the sum of its four intensities is at least 32. This deliberately coarse one-bit sensor discards information; the modest accuracy below must not be compared with full-image classifiers or Action-BED's different observations.

Before loading or training, PROTOCOL.md fixed the sensor, threshold, four depths, objective, deterministic split, comparators, and resource limits. Within each class, indices were sorted by SHA256 of '20260926:digits-split:' plus the original index. The first floor(2n/3) became training rows. There are 1195 training and 602 held-out rows. No hyperparameter, depth, feature or tie-break was selected using held-out performance. All four budgets were reported.

Objective: maximize exact empirical classification accuracy with at most d binary queries. Question costs are identical. Methods: an independently written exact dynamic program; native scikit-learn CART with Gini impurity and the same max depth; exhaustive best nonadaptive d-query subset with its training-majority decoder. Ties are deterministic. Unseen static answer patterns use the global training-majority label. The exact learner chooses the earliest query that strictly improves its score, preferring to stop on equal scores.

## Why the whole policy can be learned without enumerating policies

Let S be the set of training rows compatible with the observed history, and d the remaining query budget. For label k write n_k(S) for its count. The optimal number of correctly classified rows is

    F(S,0) = max_k n_k(S),
    F(S,d) = max( max_k n_k(S),
                  max_q [ F(S_(q=0),d-1) + F(S_(q=1),d-1) ] ).

Store the maximizing question and terminal labels to reconstruct the policy. Constant queries are skipped. Once a query has been asked, it is constant on all successor row sets; no separate list of past questions is needed under this fixed, deterministic, equal-cost interface. Decisions at different branches can be optimized independently because their empirical rewards add and their per-path budgets are independent. Randomizing among such policies cannot improve the maximum expected empirical accuracy.

The recurrence is exact by induction on remaining depth. Its implementation memoizes (row bitset, budget), combines branches by integer addition, and chooses leaves by label counts. Counting bits is implemented efficiently, but operations on an N-bit mask are not unit-cost operations asymptotically. Data preparation, labels and all question responses are available to both training algorithms. At deployment, only requested responses are exposed.

Caching and branch-and-bound optimal tree learning are established methods: DL8.5 [4] and STreeD [5] are stronger direct classical precedents. The present small implementation is neither those solvers nor a new general algorithm. Their full native packages were not run. Native CART was executed, and the exact recurrence was independently checked on small full-tree enumerations.

For depth four, a naive full binary-tree description has 15 question locations and 16 digit-label leaves, allowing 16^15 * 10^16, approximately 1.15e34, syntactic descriptions. This count includes many equivalent or redundant descriptions and is not discovery complexity. Even before exploiting the data, the sets produced by at most d distinct binary questions are bounded by sum_(i=0)^d 2^i binom(16,i), which is 34113 at d=4. Actual data, purity and state merging reduce the count further.

## Results actually obtained

All counts below are exact integers on the fixed split. Percentages are secondary presentations. The test set was used only after each prescribed learner had fixed its policy.

| Budget | Exact train /1195 | CART train /1195 | Static train /1195 | Exact test /602 | CART test /602 | Static test /602 |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 237 | 229 | 237 | 119 | 117 | 119 |
| 2 | 426 | 426 | 415 | 213 | 213 | 197 |
| 3 | 642 | 609 | 588 | 324 | 311 | 289 |
| 4 | 763 | 719 | 669 | 367 | 362 | 340 |

The four-query exact policy contains 15 question nodes and 16 terminal labels. It uses all four observations on this data. Its training accuracy is 63.85 percent and its held-out accuracy is 60.96 percent. CART gives 60.17 and 60.13 percent; the best static four-question policy gives 55.98 and 56.48 percent. These are one-split observations, not evidence of statistically established superiority or domain-transfer performance. In particular, the exact-versus-CART training gain is 44 rows but the held-out gain is only five rows. Exact empirical optimization is not a certificate of the true population optimum.

The exact dynamic program visits 5438 (subset,budget) states and examines 11712 nonconstant candidate splits at depth four. Its first measured fit took 0.0564 seconds. A second run took 0.0343 seconds and reproduced every deterministic output byte. These include reconstruction and solver initialization but exclude Python imports, data-loading and the separately recorded setup/checks. All four exact fits together were under 0.08 seconds in each recorded run. These are isolated local observations, not runtime predictions for a user's device or a cross-platform speed claim. We did not approach the frozen 3-million-state / 60-second limits.

CART took about 0.0028 seconds at depth four in the first run. It is faster here and has a different training criterion. The exact solver establishes the optimum empirical score for this interface, not that it is the fastest tree solver.

Even allowing every possible full sixteen-bit signature, the maximum training accuracy is 916/1195 because some identical signatures have different labels. Thus information discarded by the sensor is an explicit limit independent of computation. We did not train a full-signature test classifier or select a new sensor after examining the results.

## What this means for the quantum comparison

A square root of the syntactic policy count would be a misleading comparison. The classical solver shares the subproblems generated by different policies and determines the best leaf action directly. It does not estimate every policy's mean independently or sample a whole posterior.

Likewise, this finite empirical objective is already a small integer sum. A quantum 1/epsilon mean-estimation bound does not automatically compete with a classical 1/epsilon^2 Monte Carlo estimator: this comparator can count exactly and optimize branches jointly. Treating the empirical prior as a coherent data-preparation oracle would additionally require explicit data access and preprocessing. Eleven index qubits for 1195 training rows do not implement that memory access by themselves.

This does not imply that quantum computation cannot improve policy learning. It means the relevant quantum operation must compete with the best *shared computation across policies*, not a separate evaluator for each candidate. Existing quantum policy-gradient algorithms [6] already study improvements from coherent environment access subject to regularity assumptions. Source for a model can support quantum access after reversible compilation; an external response API or a real participant cannot be queried coherently by assertion. Those prior results are not transferred to the digit task.

A larger or genuinely interactive simulator might make the simple row-subset state insufficient, but that alone would not establish hardness. PEGASUS [7] already reuses fixed simulated scenarios across policy search and provides generalization results under stated conditions. Classical methods may share random numbers, differentiate through trajectories, cache common prefixes, approximate value functions, or train policies offline. Their reuse must be preserved.

The next useful search is for an independently motivated compact stochastic simulator whose *policy discovery* is costly even after those techniques. The current example tells us what not to charge the classical side for. It does not supply that positive workload. We will not increase depth or corrupt the data representation merely to induce a timeout.

## Verification, data and licenses

The new reference check enumerates every full depth-two tree on three binary features and two possible labels for each of forty seeded labelings: 17280 tree evaluations. It matches the dynamic program and independent policy replay. This does not enumerate all labelings or establish a new theorem.

The saved four-query tree was also replayed through the sensor-callback-only interface on all 1797 rows, with a maximum of four queries and no repeated queries along a path. The test code supplies the hidden row to the callback, never directly to the policy. All learned policies and the full report are retained in the downloadable checkpoint. Corpus, features, split and result digests are recorded.

The preceding decision_policy_check.py from the supplied checkpoint was rerun and reproduced its exact report. The full historical/root verifier was not run, and no claim of refreshing historical arithmetic, sorting, e-graph or other numerical evidence is made.

The experiment uses the installed NumPy 2.3.5 and scikit-learn 1.8.0. The data load is offline; raw internet download failed in this environment. No raw images or upstream solver code are imported into our repository. Dataset source: E. Alpaydin and C. Kaynak, UCI Optical Recognition of Handwritten Digits, DOI 10.24432/C50P49, CC BY 4.0 as listed by UCI. Our sensor and train/test split are derived transformations. Original repository MIT license and other branches remain unchanged.

    python exploration/phase_2/active_digits_v1/verify.py

Default verification regenerates results in temporary files. Timings are observations and are not asserted byte-identical. The result digest includes native CART choices and therefore pins the tested software version; alternative versions may need an explicitly reviewed new reference rather than alteration of the old evidence.

## Research status

Complete small policy learning has now been executed on real data, rather than only checking identities. This is a calibrated classical baseline, not a new practical application or quantum advantage. The central question remains whether a quantum mechanism can discover a useful classical policy at lower total cost after the comparator exploits its structure and the required statistical generalization is included. Manuscript work remains on hold.

A concrete example from the user's own work could help select the next test: a short simulator or notebook used repeatedly to decide which experiment, computation or candidate to try next. This is not a request for a new quantum idea, a large run, or a guarantee of a hard instance. Source complexity, actual evaluation cost and the desired decision quality would be more useful than a large nominal number of possibilities.

## Primary sources inspected

[1] T. Rossa, A. Phillips, T. Rainforth, Action-BED: Task-Driven Bayesian Experimental Design with Singly Intractable Objectives, arXiv:2606.23662v1 (2026), Sections 4 and 6.3 and masked-classification description. Task shape inspected; no neural training or paper result reproduced. https://arxiv.org/html/2606.23662v1

[2] scikit-learn official load_digits documentation. Dataset shape, integer scale and source subset checked. https://scikit-learn.org/1.5/modules/generated/sklearn.datasets.load_digits.html

[3] E. Alpaydin and C. Kaynak, Optical Recognition of Handwritten Digits, UCI Machine Learning Repository, DOI 10.24432/C50P49. Attribution/license and corpus description checked. https://archive.ics.uci.edu/dataset/80/optical+recognition+of+handwritten+digits

[4] G. Aglin, S. Nijssen, P. Schaus, Learning Optimal Decision Trees Using Caching Branch-and-Bound Search, AAAI (2020), DOI 10.1609/aaai.v34i04.5711. Primary abstract inspected; no DL8.5 run. https://ojs.aaai.org/index.php/AAAI/article/view/5711

[5] J. G. M. van der Linden, M. M. de Weerdt, E. Demirovic, Necessary and Sufficient Conditions for Optimal Decision Trees using Dynamic Programming, NeurIPS (2023). Author-institution artifact description and algorithm scope inspected; no STreeD run. https://research.tudelft.nl/en/datasets/source-code-and-data-for-the-paper-necessary-and-sufficient-condi/

[6] S. Jerbi, A. Cornelissen, M. Ozols, V. Dunjko, Quantum Policy Gradient Algorithms, TQC (2023), DOI 10.4230/LIPIcs.TQC.2023.13. Primary abstract and coherent-access/regularity scope inspected, not theorem transfer to this workload. https://doi.org/10.4230/LIPIcs.TQC.2023.13

[7] A. Y. Ng, M. I. Jordan, PEGASUS: A Policy Search Method for Large MDPs and POMDPs, UAI (2000); later arXiv deposit 1301.3878. Primary abstract and proceedings metadata checked; no native implementation. https://arxiv.org/abs/1301.3878
