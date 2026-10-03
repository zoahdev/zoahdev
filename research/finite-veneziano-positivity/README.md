# Sharp all spin dimension bounds for finite Veneziano products

Yicheng Pan / 潘奕成  
Version 2 public AI-assisted preprint, prepared 3 October 2026

Public AI-assisted preprint. No arXiv posting, journal submission, acceptance, or external peer review is claimed. No affiliation or email address is asserted.

[Read the English manuscript](finite_veneziano_dimension_bounds.pdf) | [中文摘要](finite_veneziano_summary_zh.pdf) | [arXiv 自助投稿指南](arxiv_self_submission_zh.txt)

## Result and scope

For every integer n >= 3 in the specified finite, equally spaced Veneziano-product family, every mass level and every integer spin has nonnegative four-point tree-level partial-wave coefficients if and only if 3 < D <= d_n, with real D > 3. The endpoint is included. The number d_n is the unique level-three scalar zero; it decreases strictly to 10.

The proof combines a uniform central-factorial gap at D = 51/5, certified by a fixed 182-term positive integer polynomial, with exact finite-base certificates for n = 3,...,34: 560 non-level-three residues and 32 scalar caps. The uniform reduction covers every n >= 35. This is an analytic infinite-domain argument plus finite exact certificates, not an inference from a finite spin or level scan.

The theorem concerns four-point tree-level partial-wave positivity only. It does not establish higher-point consistency, loop unitarity, locality, a positive state-space construction, a new physical string theory, or a physical ultraviolet completion.

## Prior work and AI disclosure

The amplitude family, numerical thresholds, level-three scalar formula, and limiting value 10 are due to Shao and Vichi. The proof adapts Chen and Yin's central-factorial and Bessel first-exit method. The manuscript also credits earlier Bessel representations, positive-power-series methods, and Mansfield's exceptional-low-level strategy. The specific gap certificate and all-n application are candidates for a new proof; novelty and worldwide priority remain provisional. Full references are in the manuscript.

OpenAI AI assistance was used substantially for the research, derivations, manuscript writing, programming, and verification. Separately written and executed AI-generated checks reconstructed the algebra and certificates, including the full finite base; additional adversarial checks were also AI-assisted. These are computational and mathematical cross-checks, not human expert review, external peer review, or formal proof-assistant certification. This release does not assert that the named author has personally read or verified the complete manuscript. Specialist assessment remains necessary.

## Contents

- `finite_veneziano_dimension_bounds.pdf` and `.tex`: 12-page English manuscript and editable source
- `finite_veneziano_summary_zh.pdf` and `.txt`: readable 2-page Chinese summary and plain-text companion
- `research/`: principal scripts and exact certificates
- `verification/`: all separately written verification scripts and saved results, except the large regenerable 560-row transcript described below
- `build_chinese_summary.py` and `presentation_fonts/`: reproducible embedded-font summary
- `MANIFEST.sha256.json`: SHA-256 and byte count for every other payload file
- `RELEASE_METADATA.json`: source provenance, preservation checks, and the omitted transcript digest

## Reproduction

Use Python 3.11+ with SymPy and mpmath. Verification needs no network access. Some scripts overwrite adjacent generated JSON files, and elapsed-time fields can change digests, so run these commands in a working copy.

```sh
python research/verify_level3_theorem.py
python research/derive_level3.py
python research/verify_uniform_gap.py
python research/certify_uniform_base.py
python research/check_integer_dimension_corollary.py
python verification/independent_check.py
python verification/independent_uniform_check.py
python verification/independent_uniform_base.py
python verification/cold_check.py
python verification/boundary_check.py
```

`independent_uniform_base.py` replays all 560 residues and all 32 scalar caps, checks the n = 35 cutoff, and regenerates `verification/independent_uniform_base.json`. Only that generated audit transcript is omitted from this lightweight repository copy; every principal proof certificate and every checker script is retained. The archived transcript is 44,797,835 bytes, SHA-256 `91073ee9d2ae67731a6d7a112e3a78325d2668fc43f5cfdd31e61d073a3a01a1`. Runtime metadata can change the regenerated file's digest. The cold and boundary checkers test selected difficult cases; they do not replace the full replay or the symbolic proof.

PDF builds require pdfLaTeX with the standard packages listed in the TeX source, and ReportLab for the summary:

```sh
pdflatex -interaction=nonstopmode -halt-on-error finite_veneziano_dimension_bounds.tex
pdflatex -interaction=nonstopmode -halt-on-error finite_veneziano_dimension_bounds.tex
python build_chinese_summary.py
```

## Optional arXiv self-submission materials

[Source-only submission archive](finite_veneziano_arxiv_source_v2_public.tar.gz), [Chinese step-by-step guide](arxiv_self_submission_zh.txt), and [copyable metadata](arxiv_metadata_public.txt) are provided for the author to review. The archive contains the current `finite_veneziano_dimension_bounds.tex` at its root and reproducibility scripts/certificates under `anc/`. The extracted source compiled locally to 12 pages. This does not establish arXiv eligibility, endorsement, acceptance, or a completed submission. Any author declarations and license choice remain the submitting author's decision.

## Rights and integrity

No new license is selected or granted for the manuscript, code, or data by this preparation. The bundled presentation font retains its existing SIL Open Font License 1.1 and accompanying notices; that font license does not license the research content. No downloaded paper full text, private audit report, credentials, or account data is included.
