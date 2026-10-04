# Erdős 883 all-n odd-cycle proof candidate

**Yicheng Pan (潘奕成) · Version 3 · 4 October 2026 UTC**

This is a public, computer-assisted proof candidate for the first question in Erdős Problem 883. It has not received external peer review or formal verification. No first-solution, novelty, or priority claim is made.

The manuscript, computational certificates, and review preparation were developed with substantial AI assistance, including AI-assisted adversarial checks and separately implemented checkers. Those checks do not substitute for independent external mathematical review.

## Read and reproduce

- [Review manuscript PDF, 18 pages](Erdos883_review_manuscript_v3_2026-10-04.pdf)
- [Exact v3 plain-text manuscript](Erdos883_all_n_proof_candidate_v3.txt)
- [Complete proof, certificate, and scientific-audit package](Erdos883_all_n_proof_candidate_v3_2026-10-04.zip)
- [LaTeX review sources and documented v2-to-v3 changes](Erdos883_review_sources_v3_2026-10-04.zip)
- [Browsable verification code and certificate outputs](verification/README.md)
- [Reproduction guide](README.txt) and [SHA-256 checksums](SHA256SUMS.txt)

The downloadable archives are preserved byte-for-byte. The complete proof package retains v1/v2 texts, exact revision records, and historical scientific audits with their actual target hashes; an earlier audit is not relabeled as a v3 audit. The typesetting source archive contains a dated preparation note written before public release. This page records the public release of those artifacts on 4 October 2026.

## Proposed statement and coverage

For every integer n ≥ 0 and every A ⊆ {1,…,n} with

|A| > floor(n/2) + floor(n/3) − floor(n/6),

the graph on distinct elements of A joined when their gcd is 1 contains a simple cycle of every odd length L with 3 ≤ L ≤ n/3 + 1.

The proposed argument combines an explicit analytic proof for n ≥ 2,000,000 with exact sufficient-condition certificates covering every smaller required n and every permitted subset A:

- n = 0,…,5: no required odd-cycle length
- n = 6,…,2300: 71 contiguous passing intervals
- n = 2301,…,2,000,000: 84 contiguous passing intervals

The finite certificates are not a sample of subsets. Every proof-affecting program comparison uses integer or exact rational arithmetic. Printed decimal approximations and timings are diagnostic. The separate complete-tripartite question is not a new claim here.

## Prior work

The argument explicitly adapts Donald Della Pietra's missing-even smoothing, totient profiles, prime signatures, and ordered-Hall method from his [27 July 2026 public manuscript](https://github.com/donalddellapietra/erdos-883-proof/blob/1f26276d7850fc9afe68e9d7edecf24aa7cc597d/paper/main.tex). That pinned, unrefereed version states a sufficiently-large-n theorem. The claimed addition here is the explicit threshold and exact finite completion, subject to external review.

The sole non-elementary arithmetic input is Ahlswede–Khachatrian (1996), Theorem 2(i), [Sets of integers and quasi-integers with pairwise common divisor](https://doi.org/10.4064/aa-74-2-141-153). Full references and the exact application conditions appear in the manuscript.

## Review status and rights

This publication makes the candidate and its evidence available for scrutiny. It does not report journal acceptance, an arXiv posting, human expert endorsement, or a formally checked proof. The computational checks verify the stated finite certificates and guards; they do not by themselves validate the entire mathematical argument.

No new license is granted by this release. This directory does not add an open-source or other reuse license, and it makes no license claim over cited third-party work.
