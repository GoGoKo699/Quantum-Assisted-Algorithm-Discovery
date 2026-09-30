# Benchmark provenance and rights

`instance.json` contains a normalized transcription of ONE numerical test instance,
`u120_00`, the first problem in OR-Library's `binpack1.txt`.

Source: J. E. Beasley's OR-Library; data contributed by E. Falkenauer.
https://people.brunel.ac.uk/~mastjjb/jeb/orlib/binpackinfo.html
https://people.brunel.ac.uk/~mastjjb/jeb/orlib/files/binpack1.txt

Retrieved 30 September 2026 through the web text interface. The 120 item sizes,
capacity 150, and reference header 48 were extracted; the rest of that collection
was not imported. The input SHA256 in REPORT.json refers to the normalized JSON,
not to a byte-for-byte download of the upstream full file. Runtime network access
failed, so no original-transfer SHA is asserted. The reference bin count is metadata
and is not used by the optimizer. The returned solution is checked independently
against volume and every original item ID.

This is a published synthetic benchmark, not operational factory data. Attribution
and any underlying source rights are retained. The parent MIT license for original
project code does not relicense third-party source collections. No BPPLIB code,
license text, solution file, or dataset was imported. No permissions for broader
redistribution of those external collections are asserted.

The verifier is independently written and uses installed NumPy/SciPy with their
own licenses. It invokes HiGHS through SciPy's public interfaces, not a copied
SCIP, knapsack, or production branch-and-price implementation. The source metadata
and this notice must travel with the extracted input.
