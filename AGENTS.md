# Research continuation contract

Read README.md, STATUS.md, PROVENANCE.md, docs/current-design.md, and work_orders/CURRENT.md first. Run `python verify.py` and record what was actually rerun.

Preserve LICENSE. Do not overwrite historical source data or reference outputs to make tests pass. Imported files are tracked by provenance/import-manifest.json; put substantive new work in a versioned successor directory and keep the old evidence available. Use temporary directories for generated data and benchmarks. Do not run assertions-dependent code under -O or -OO.

The objective is a useful reusable classical output discovered more efficiently with a circuit-model quantum computer. Matrix multiplication is a testbed, not the objective. There is currently no established advantage, new multiplication identity, complete guided circuit resource estimate or hardware result. Do not transfer raw-search estimates to guided search.

Retain strong classical deductions and realistic baselines. Treat seed choice, horizon, initialization, marked-set definition, coefficient domain, readout and all access costs as explicit model choices. Verify published claims from primary sources before relying on them for new research. Attribute standard methods and the public reference certificate. Do not treat unit tests, local rediscovery, or stored benchmark success frequencies as novelty or speedup.

Keep commits scoped and preserve provenance. Update the claim ledger and work order when evidence changes. Never promise unattended background work. No external contact, paid computation, or repository administrative changes are authorized by this continuation contract.
