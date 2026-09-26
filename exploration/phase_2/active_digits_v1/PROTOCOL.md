# Frozen protocol before training or viewing outcomes

26 September 2026. This is a small classical empirical-policy screening experiment, not a quantum advantage test or an Action-BED reproduction.

Data: scikit-learn bundled load_digits(), all 1797 8-by-8 images and 10 classes. No image selection. Input intensities are integers from 0 to 16.

Sensor: 16 non-overlapping 2-by-2 patches in row-major order. Query j returns one iff the sum of the four pixel intensities is at least 32. This threshold, pooling, discrete observation protocol, and small corpus are our chosen calibration restrictions, not Action-BED settings or asserted engineering requirements. Full images are available during training and to the held-out evaluator. A deployed policy receives only the result of its chosen sensor.

Split: within each class, sort original row indices by SHA256 of ASCII '20260926:digits-split:' followed by the index. Put floor(2*n_class/3) in training, all remaining in test. Test rows are not used for optimization or tie-breaking. This is one corpus-level split, not evidence of cross-writer generalization.

Budget: at most 1, 2, 3, or 4 binary queries, each costing one. Objective: maximize exact number of correct training classifications. No numerical Monte Carlo objective. No hyperparameter changes after test evaluation.

Methods: (1) exact dynamic programming on surviving training-row sets, returning a deterministic binary decision tree and majority-class leaves; (2) native sklearn CART, Gini criterion, same binary features and max depth, random_state 20260926; (3) best nonadaptive subset of exactly d of the 16 questions by training accuracy, with exact pattern-majority decoder. Unseen static patterns predict the global training-majority class. All ties deterministic. Stopping early is allowed for adaptive trees.

Report actual training/test counts, policy size, exact dynamic-programming counters, isolated measured runtimes, and source/data hashes. Timings are observations, not portable expected values or comparisons to hardware. Exact training optimality is not a statistical generalization claim.

Resource ceiling: 3,000,000 dynamic states or 60 seconds per depth, if reached report resource limit rather than infeasibility. No change in settings to manufacture failure. Additional tests: small explicit decision-tree enumeration and independent policy replay.
