# Claim ledger

## Current checkpoint: classical trace acquisition, 29 September 2026

[Trace acquisition 23](exploration/phase_3/TRACE_ACQUISITION_23.md) prices one
established classical route to the response information from Note 22. For the
normalized collective raising observable, Tr[(O^dagger O)^2]=2^k k^2/2 gives a
time-uniform random-phase correlation variance bound 2/(R 2^k). The known trace
normalization is used. Global Z4 phase vectors are not random product states.
Random-phase trace estimation and dynamical typicality are explicitly prior work;
no generic new algorithm, quantum advantage or publication priority is claimed.

The SAME probes are reused across all lags. With A_2=sum a_h^2 for the existing
clock, expectation of squared readout error is at most 4 A_2/(R 2^k). Hence
R>=max(1,ceil(4 A_2/(2^k beta epsilon_stat^2))) suffices for statistical readout error
<=epsilon_stat with probability >=1-beta. No independence across lag errors or
unpriced per-time union bound is assumed. Numerical propagation, clock, wrapping,
output arithmetic and spatial errors remain separate. A once-prepared table
shares its law error across draws; a per-draw guarantee is not an M-draw guarantee.

Two ordinary Hilbert vectors per probe implement the acquisition. Matrix-free
local actions cost O(k 2^k), and one conservative grid/Taylor construction costs
O(R N k 2^k(q+1)), with q=O(W tau+log(N/delta_U)). This is an arithmetic upper bound,
not a runtime or a lower bound against all classical methods. It uses full-time
propagation and does not automatically inherit the half-time operator-tensor
advantage of Note 22. Statistical probe counts can fall while the per-probe
state-vector cost grows. A one-probe sufficient budget at a specified 26-spin
setting is analytical only, not an executed 26-spin calculation.

Existing linked-cluster/typicality combinations strengthen the comparator, but
signed cluster subtraction can amplify probe noise. No convergence or tail bound
for such a subtraction in this collective alternating-field model is established.
It cannot be relabeled as Note 21's positive finite-block mixture. A large Hilbert
space, a large sufficient block, or a failed tensor approximation remains
insufficient evidence for quantum advantage.

The [work order](work_orders/CURRENT.md) requests a bounded resolution/sample-count
decision after these stronger alternatives, not another general reconstruction
framework. Direct quantum sampling remains permitted and need not produce the
classical table. A credible useful regime, not a classical spin-off, is still the
parent objective. No new repository or manuscript is needed.

## Executed evidence and limits

The final independent NumPy diagnostic ran twice with identical JSON. One fixed
ten-spin d=J block uses eight PCG64-seeded Z4 probes and matrix-free propagation
to acquire 255 lags through t=25.5/J. The degree-16 step uses 4,080 batched H actions.
A separate magnetization-sector diagonalization supplies a diagnostic reference,
not input to the acquisition algorithm. Observed finite-clock bin TV is about
0.006989; weighted scalar error is about 0.057745 and maximum scalar error is about
0.026568. This single fixed-seed result is not a statistical confidence interval
or a 99%-success large-block demonstration. The original fine bins are retained.

The relative vector discrepancy against the independent diagonal reference is
about 2.6e-14. The ideal Taylor truncation bound does not include all rounding.
Other checks exhaust 64 two-spin global-phase classes at three times and 256
four-spin product-phase choices, verify the observable fourth trace, and reject
six invalid inputs and -O/-OO. The [report](experiments/trace_acquisition_v1/REPORT.json)
clearly labels unexecuted analytical probe-count rows. These are complex128
mathematical diagnostics, not interval certificates or performance measurements.

Checker SHA256: `debcd383b7d12d4d4de89beda35281cf2e272b9bc9a28037a8d8ffa9bfe92254`.
Report SHA256: `f8705f0d0f1ec177ffc0c4c7efdfa036071bbf71f6998da429849c4d11e7e31e`.

No native NMR or upstream typicality package, tensor algorithm, quantum circuit,
experimental spectrum, large-block run or speedup benchmark was executed. Primary
trace/typicality/linked-cluster methods were inspected as text; requested PDF
screenshots failed, so no figure/table benchmarks were newly interpreted. The
source screen is bounded, not an exhaustive novelty audit. No prior verifier was
rerun or upstream data/code imported. All prior scientific files are unchanged.

## Preserved evidence

The preceding ledger and its links are pinned at
[pre-acquisition checkpoint](https://github.com/GoGoKo699/Quantum-Assisted-Algorithm-Discovery/blob/389f9d81014be10fa3a0b6d0c8c44fd91ea39e01/STATUS.md).
Notes 15-22, previous proofs, code, reports, data and rights remain intact. Older
current/next headings refer to their own checkpoints. Climate/dynamics remain open;
Manthan is paused; battery/operator routes parked; both spin-offs independent;
Phase-2 Note 27 closed; manuscript on hold. Only the parent repository is modified.
No contact, paid/unattended work, release, merge, new repository or admin change.
