# Source and verification scope

The fixture is a line-normalized transcription of lines 4-379 (376 clauses) of
`meelgroup/manthan/benchmarks/usb-phy-fixpoint-1.qdimacs`, read through the GitHub
connection on 28 September 2026. It is a prefix, NOT a complete QDIMACS instance.
It has no DIMACS header and must not be passed to a benchmark solver as the
original problem. No upstream executable code is included.

- Pinned upstream commit: `8d7ad340436255f9d0a7f6920f54f9422e502a0a`.
- Complete upstream file Git blob: `cd6e0043b175df4247368d0e96a8e1020ed603a4`.
- Fixture SHA256: `552172c699638e32fbb5126c11d02916160ec71dfec87d1c397431662a545f15`.
- Source URL: https://github.com/meelgroup/manthan/blob/8d7ad340436255f9d0a7f6920f54f9422e502a0a/benchmarks/usb-phy-fixpoint-1.qdimacs

The header inspected separately declares 1631 variables and 4395 clauses, with
universal indices 1-334 and existential indices 335-1630. This audit does not
resolve every original signal name or the unquantified declared index 1631.
The selected definitions are all for quantified outputs 502-586, depend only
on inputs 1-119 and preceding definitions, and do not use that extra index.

The COMPLETE upstream file was not downloaded or locally hash-checked. The
optional `--source` mode verifies its Git blob and matches the inspected prefix;
that mode's successful path was NOT executed. Its rejection of a wrong file was
executed. The default mode verifies the fixed transcribed prefix and logic only.
Do not confuse the fixture digest with verification of the complete benchmark.

`verify.py` is independently written. `REPORT.json` is the final `--native` output.
The native report was regenerated twice identically. Default mode also passed;
-O/-OO, a changed fixture and an incorrect complete-source file were rejected.
Native libz3 4.13.3.0 checked the two implications between the clause prefix and
its recovered gate equations. This is not Manthan/CMSGen execution or independent
UNSAT-proof replay. Elementary reversible operations are checked on computational
basis inputs; there is no large state-vector, noisy-hardware or runtime simulation.

The benchmark's application-level provenance is not established by its USB name.
It is an encoding diagnostic from an existing synthesis suite, not a newly
validated industrial workload or a useful classical program produced here.
No native pipeline timing, training, sample-source ablation or new quantum
advantage is reported. Deterministic gate recovery and reversible evaluation
are existing techniques, not novelty claims.

## Upstream notice

The following notice is retained from the upstream repository LICENSE (Git blob
`5e004ad951777b559aa1b5980d42e2fa6b2f0ee7`). The parent repository's license does not
replace upstream attribution.

```text
Manthan --Copyright (c) 2020
    Priyanka Golia
    Subhajit Roy
    Kuldeep S Meel

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```
