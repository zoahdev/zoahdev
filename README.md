# 潘奕成 · Yicheng Pan / Zoah

**18 岁 · 安徽大学 · 世界模型公司 KineWorld 负责人**

GitHub: **[@zoahdev](https://github.com/zoahdev)** · Erdős Problems:
**[yichengpan](https://www.erdosproblems.com/forum/user/yichengpan)**.
两个账号均为潘奕成本人的公开主页。

## Erdős #883: 第一问的全 n 证明

已完成第一问对所有自然数 n 的证明及 Lean 形式化。完整源码、论文和独立复验记录现已公开：

- **[证明仓库](https://github.com/zoahdev/erdos883-first-question)** · [论文 PDF](https://github.com/zoahdev/erdos883-first-question/blob/main/paper/Erdos883_Lean_Aligned_Manuscript_20261005.pdf)
- **6,831 个本地模块独立重编译通过**，最终定理与规范的第一问完整表述一致。
- 最终公理仅为 `propext`、`Classical.choice`、`Quot.sound`；[核验记录](https://github.com/zoahdev/erdos883-first-question/blob/main/audit/KERNEL_RECHECK.json)。
- 在 **Donald Della Pietra 的充分大 n 结果及核心构造**基础上补齐有限范围，覆盖全部 n；第二问不计入本次贡献。

AI 工具实质参与了证明开发、形式化和核验。公开材料明确记录前人贡献与复现条件；不声称历史首创、专家背书或期刊录用。

## World models and physical intelligence
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

## Public research notes

- [Erdős #883 first-question all-n proof and Lean formalization](https://github.com/zoahdev/erdos883-first-question): the full canonical statement with an independent rebuild of all 6,831 local modules. [Earlier manuscript archive](research/erdos883-all-n/README.md).
- [Finite Veneziano-product positivity](research/finite-veneziano-positivity/README.md): an AI-assisted preprint and exact verification package for a specific four-point, tree-level amplitude family
- [World-model window certification](https://github.com/zoahdev/kineworld/blob/26b264b0057f4f2537fbc1a16125178eb1c92358/verification/releases/KW-WORLD-MODEL-AUDITS-2026-10/prequential/REPORT.md): a scoped technical report with explicit model-class assumptions and reproducible synthetic checks

These are public research materials without external peer review. Their scope, prior work, and substantial AI assistance are disclosed in the linked reports.

## Earlier work

My agent and security work includes [KineGrant Protocol](https://github.com/zoahdev/kinegrant-protocol), [Developer Intelligence](https://github.com/zoahdev/dsh-github-intelligence), [Agent Plugin Doctor](https://github.com/zoahdev/dsh-plugin-doctor), and [Agent Replay](https://github.com/zoahdev/dsh-replay).

These projects cover capability-based authorization, developer tools, plugin validation, and agent observability.

## Collaborate

For world-model research, useful starting points are a reproducible failure case, a baseline comparison, or a clearly scoped experiment. See [KineWorld's contribution guide](https://github.com/kineworld/.github/blob/main/CONTRIBUTING.md) for evidence requirements and how to contribute.
