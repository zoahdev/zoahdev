# Hi, I'm Zoah.

I'm building [KineWorld](https://github.com/kineworld), a research-stage world-model company.

My current focus is **action-conditioned prediction, compact latent dynamics, and reproducible evaluation for physical intelligence**. I also build the agent tooling and security infrastructure that make experiments easier to inspect and repeat.

勘境 / KineJing is our world-model integration and research project. Start with the code, then follow the model cards and experiment records.

## Start here

| Project | What to explore |
| --- | --- |
| **[KineJing · 勘境](https://github.com/kineworld/KineJing)** | CPU motion baseline, model adapters, and a trained three-view action-conditioned feature predictor |
| **[Kine-JEPA](https://github.com/kineworld/kine-jepa)** | Compact latent-model prototypes, action-conditioned rollout, and planning interfaces |
| **[KINE-Bench](https://github.com/kineworld/kine-bench)** | Evaluation protocols, representation diagnostics, baselines, and recorded negative findings |
| **[KINE-DataPipe](https://github.com/kineworld/kine-datapipe)** | Video preprocessing, motion filtering, event-candidate mining, and pair construction |

- **Try the CPU workflow:** [KineJing quick start](https://github.com/kineworld/KineJing#quickstart)
- **Inspect the trained predictor:** [model card](https://github.com/kineworld/KineJing/blob/main/docs/DYNAMICS_MODEL_CARD.md)
- **Check the experiments:** [evidence records](https://github.com/kineworld/KineJing/blob/main/evidence/README.md)
- **Understand the organization:** [KineWorld](https://github.com/kineworld) · [website](https://kineworld.com)

## Research boundaries

Current results are internal and research-stage. The trained KineJing predictor outputs future visual features; it has no RGB decoder. Its model card records the data split, baselines, weight hashes, and limitations.

The trained predictor checkpoint is currently retained in a private company release. The public repository provides the CPU demo, training code, and evaluation records; reproducing the trained predictor requires checkpoint access and separately obtained upstream data and weights.

Public demos, software tests, and model-quality evaluations answer different questions. I keep those distinctions visible and welcome independent reproduction, including failed attempts.

## Earlier work

My agent and security work includes [KineGrant Protocol](https://github.com/zoahdev/kinegrant-protocol), [Developer Intelligence](https://github.com/zoahdev/dsh-github-intelligence), [Agent Plugin Doctor](https://github.com/zoahdev/dsh-plugin-doctor), and [Agent Replay](https://github.com/zoahdev/dsh-replay).

These projects cover capability-based authorization, developer tools, plugin validation, and agent observability.

## Collaborate

For world-model research, useful starting points are a reproducible failure case, a baseline comparison, or a clearly scoped experiment. See [KineWorld's contribution guide](https://github.com/kineworld/.github/blob/main/CONTRIBUTING.md) for evidence requirements and how to contribute.
