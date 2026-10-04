# Exact verification sources

These files are unchanged copies from the [complete v3 package](../Erdos883_all_n_proof_candidate_v3_2026-10-04.zip). That archive also contains the full historical scientific-audit record, revision checks, and additional bounded foundational checks.

Use a fresh copy because some scripts regenerate outputs. Verify the parent directory's SHA256SUMS.txt first. Python 3 standard library and a C++17 compiler supporting `__int128` are sufficient.

Run from this directory:

```sh
python3 check_interval_cover.py
python3 independent_signature_audit.py
python3 independent_adaptive_density_audit.py
python3 verify_adaptive_tail_lemma.py
python3 totient_repair/check_guarded_finite_cdf.py

mkdir -p build
g++ -O3 -std=c++17 -Wall -Wextra -Werror adaptive_bridge.cpp -o build/bridge
build/bridge 2000000

g++ -O2 -std=c++17 adversarial_audit/independent_small.cpp -o build/small_independent
build/small_independent adversarial_audit/small_intervals.txt
g++ -O2 -std=c++17 adversarial_audit/independent_bridge.cpp -o build/bridge_independent
build/bridge_independent adaptive_bridge_2301_2000000_output.txt
python3 adversarial_audit/independent_constants.py
python3 adversarial_audit/analytic_numeric_guards.py
```

Expected coverage is 71 contiguous passing intervals for n = 6,…,2300 and 84 for n = 2301,…,2,000,000. All exact-rational guards should pass. n = 0,…,5 is vacuous; the manuscript supplies the analytic argument for n ≥ 2,000,000. The overlap is deliberate.

`REJECT` lines in diagnostic output are wider attempted intervals that were split. They are not counterexamples and leave no gap in the final covers. Printed decimals and timings are diagnostic; they do not determine certificate acceptance.

These programs verify finite sufficient conditions and arithmetic bounds. Their success does not replace external mathematical review or formal verification of the complete proof candidate.
