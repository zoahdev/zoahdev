# Yicheng Pan

I'm Yicheng Pan, also known as **Zoah**: an 18-year-old student at **Anhui University** and the lead of **[KineWorld](https://kineworld.com)**, a research-stage world-model company in Hefei, China.

I work on formal mathematics, physical intelligence, and tools that make AI-assisted research easier to inspect and reproduce. My aim is to publish useful proofs, precise research questions, reusable verification artifacts, and practical developer tools.

**Student email:** [W326301002@stu.ahu.edu.cn](mailto:W326301002@stu.ahu.edu.cn)

**GitHub:** [@zoahdev](https://github.com/zoahdev) · **Erdos Problems:** [yichengpan](https://www.erdosproblems.com/forum/user/yichengpan)

These are my public accounts. My university affiliation identifies my student status; it does not imply institutional endorsement of these projects.

## Featured mathematics: Erdos #883, first question for every n

**[Complete all-n proof and Lean formalization](https://github.com/zoahdev/erdos883-first-question)**

Building on **Donald Della Pietra's sufficiently-large-n result and core construction**, this work completes the finite range and proves the canonical first-question statement for every natural number n. It concerns the first question only.

For every A contained in {1, ..., n} with |A| > floor(n/2) + floor(n/3) - floor(n/6), the induced coprime graph on A contains a genuine cycle of every odd length l with 3 <= l <= floor(n/3) + 1.

The final theorem is `Erdos883Verified.erdos883_firstQuestion`. A separate source rebuild compiled **all 6,831 local Lean modules** afresh with the pinned dependencies. The canonical statement check passed; the theorem's axioms are only `propext`, `Classical.choice`, and `Quot.sound`.

[Manuscript](https://github.com/zoahdev/erdos883-first-question/blob/main/paper/Erdos883_Lean_Aligned_Manuscript_20261005.pdf) · [Kernel audit](https://github.com/zoahdev/erdos883-first-question/blob/main/audit/KERNEL_RECHECK.json) · [Reproduction errata](https://github.com/zoahdev/erdos883-first-question/blob/main/REPRODUCTION_ERRATA.txt) · [Original release](https://github.com/zoahdev/erdos883-first-question/releases/tag/v1.0.0)

The contribution is an **all-n completion**, with explicit credit to the preceding asymptotic work. The [earlier forum claim and discussion](https://www.erdosproblems.com/forum/thread/883/proof-claims) matter for interpreting priority. I make no claim of historical first priority, expert endorsement, or journal acceptance. AI tools substantially assisted proof development, formalization, and the rebuild audit; kernel checking is separate from external human peer review.

## KineWorld

**[KineWorld](https://github.com/kineworld)** studies action-conditioned world models, compact predictive representations, and evaluation for planning and control. I currently lead it as a single-maintainer, part-time research organization.

Our work centers on inspectable experiments, clear baselines, and recorded failure cases. Current evidence is internal and research-stage; independent reproduction is welcome.

[Company website](https://kineworld.com) · [Organization](https://github.com/kineworld) · [Contribution guide](https://github.com/kineworld/.github/blob/main/CONTRIBUTING.md)

### KineJing

**[KineJing](https://github.com/kineworld/KineJing)** is our world-model integration and research project. It brings together a CPU motion baseline, upstream model adapters, and a trained three-view action-conditioned feature predictor using frozen DINOv2 features.

The trained predictor outputs future visual features and has no RGB decoder. Its [model card](https://github.com/kineworld/KineJing/blob/main/docs/DYNAMICS_MODEL_CARD.md) records the training setup, baselines, artifact hashes, and limitations. Adapter and integration tests establish software behavior; model-quality claims require the corresponding evaluation evidence.

[CPU quick start](https://github.com/kineworld/KineJing#quickstart) · [Experiment records](https://github.com/kineworld/KineJing/blob/main/evidence/README.md) · [Project website](https://kinejing.com)

The public repository includes the CPU demo, training code, and evaluation records. The trained predictor checkpoint is currently in a private company release; reproducing it requires checkpoint access and separately obtained upstream data and weights.

| Project | Focus |
| --- | --- |
| [Kine-JEPA](https://github.com/kineworld/kine-jepa) | Compact latent dynamics, action-conditioned rollout, and planning interfaces |
| [KINE-Bench](https://github.com/kineworld/kine-bench) | Evaluation protocols, representation diagnostics, and baselines |
| [KINE-DataPipe](https://github.com/kineworld/kine-datapipe) | Video preprocessing, motion filtering, and training-pair construction |

## Other public research

These projects have different completion levels. The descriptions below reflect the scope of their public materials; finite computations support only the checks they actually perform.

| Research | Materials and current scope |
| --- | --- |
| String-amplitude positivity | [Finite Veneziano products](research/finite-veneziano-positivity/README.md) and [follow-up research](https://github.com/zoahdev/string-amplitude-positivity): AI-assisted preprints on specified four-point, tree-level amplitude families, with exact symbolic certificates. These do not establish a physical string theory or a general ultraviolet completion. |
| Erdos #885: square sums | [Construction archive](https://github.com/zoahdev/erdos885-square-sum): explicit 5-by-4 square-sum specialization, genus-13 reduction, and a genus-three lift-curve study. Partial constructions and recomputable certificates; the k = 5 case remains unresolved. |
| Erdos #1013: structural certificates | [Certificate archive](https://github.com/zoahdev/erdos1013-structural-certificates): partial work on triangle-free six-chromatic graphs of order 34. Coverage remains incomplete, and catalogue assumptions are explicit; this does not resolve #1013. |
| Mutually unbiased bases in dimension six | [Exact reductions and certificates](https://github.com/zoahdev/physics-mub6-certificates): moment identities and counterexamples to selected relaxations. The existence question for four mutually unbiased bases in dimension six remains open. |
| Bosonic purity and extensions | [Research draft](https://github.com/zoahdev/physics-bosonic-purity): proposed balanced-projector classifications and conditional purity bounds. Finite symbolic checks do not prove the proposed universal classification. |
| Lieb-Oxford and Coulomb inequalities | [Research drafts](https://github.com/zoahdev/chemistry-lieb-oxford): conditional low-particle gap and moment-stability arguments, with reproducible finite checks. Analytic hypotheses and proof obligations remain explicit. |
| Riemann-hypothesis research | [Spectral and certificate laboratory](https://github.com/zoahdev/riemann-research-lab): local matrix inequalities, moment obstructions, and finite interval-arithmetic Weil-kernel probes. This is not a proof or disproof of the Riemann hypothesis. |
| BFSS threshold analysis | [Unfinished research](https://github.com/zoahdev/bfss-threshold-research): conditional reductions and symbolic free-channel diagnostics. The required physical channel estimates and nonperturbative bounds remain unproved. |
| SPARC data provenance | [Provenance audit](https://github.com/zoahdev/astronomy-sparc-provenance): conditional sample-alignment diagnostics with pinned inputs. It does not establish the historical selection procedure or a new result about gravity. |
| PeerDAS custody | [Conditional certificates](https://github.com/zoahdev/peerdas-custody-certificates): deterministic incidence-instance witnesses and protocol-assumption audits, tested on synthetic instances. These are not production Ethereum security estimates. |
| World-model evaluation | [Evaluation research](https://github.com/zoahdev/kineworld): exploratory Push-T checkpoint studies, confound audits, and reusable episode-provenance checks. These have no claimed external replication or official benchmark status. |
| Window certification for learned models | [Scoped technical report](https://github.com/zoahdev/kineworld/blob/26b264b0057f4f2537fbc1a16125178eb1c92358/verification/releases/KW-WORLD-MODEL-AUDITS-2026-10/prequential/REPORT.md): sequential-inference arguments under explicit model-class assumptions, counterexamples to overbroad guarantees, and bounded synthetic checks. No real-world control improvement is established. |

The [earlier #883 manuscript archive](research/erdos883-all-n/README.md) is retained alongside the final proof repository.

## Agent infrastructure and DSH plugins

I build community tools for **DeepSeek Harness (DSH)**: [Plugin Doctor](https://github.com/zoahdev/dsh-plugin-doctor) for plugin and profile checks, [Poison Guard](https://github.com/zoahdev/dsh-poison-guard) for static supply-chain risk inspection, and [Replay](https://github.com/zoahdev/dsh-replay) for session timelines and comparisons. The [ecosystem guide](https://github.com/zoahdev/dsh-ecosystem) connects the plugin, documentation, and developer-tool projects. Static scanners provide diagnostic evidence, not a guarantee that a plugin is safe.

Related work includes [KineGrant Protocol](https://github.com/zoahdev/kinegrant-protocol), an authorization and receipt protocol for physical AI, and [Axiomatter LabOps](https://github.com/zoahdev/axiomatter-labops), an auditable R&D workflow prototype using illustrative demo data. LabOps is an engineering prototype, not a validated scientific discovery system.

## Research practice and collaboration

AI assistance is substantial across my research and software work. The linked projects disclose their assumptions, sources, authorship, and verification boundaries. A Lean kernel replay, an exact finite certificate, a numerical experiment, and an unfinished analytic argument provide different kinds of evidence. External peer review and novelty require separate assessment.

I welcome precise corrections, failed reproduction reports, and collaboration on clearly scoped questions. For research correspondence, contact [W326301002@stu.ahu.edu.cn](mailto:W326301002@stu.ahu.edu.cn).
