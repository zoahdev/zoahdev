# Zoah

**DeepSeek Harness 生态基础设施 · Physical-AI 授权（KineGrant）· AI-native tools.**

我在给 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)（`dsh`）补社区最缺的「地基层」：插件市场、安全、可观测、自检、教程、上游修复——并全部开源成可安装、带中文说明的仓库。

## 数字速览

- **56** 个公开仓库 · **28+** 个 DSH 生态项目 · 生态注册表 **916** 插件
- **42** 个上游 cherry-pick-ready 补丁（每个带根因 + 回归测试）
- **15+** 个 npm 包
- **8** 个项目入选 [awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) · **10** 个进入 [awesome-deepseek-harness](https://github.com/0xsline/awesome-deepseek-harness)
- 官方 RFC：#1814（`dsh plugin check` / `dsh doctor` 采纳）、#2486（上游补丁队列）

📝 技术博客（证据优先的深度工程分析）：https://zoahdev.github.io/blog/

## 旗舰项目

| 项目 | 一句话 | 入口 |
| --- | --- | --- |
| [dsh-github-intelligence](https://github.com/zoahdev/dsh-github-intelligence) | 196+ 只读工具 × 16 生态（GitHub/npm/PyPI/ArXiv…），零 key，带缓存 | [在线目录](https://zoahdev.github.io/dsh-github-intelligence/) · [npm](https://www.npmjs.com/package/dsh-github-intelligence) |
| [dsh-plugin-doctor](https://github.com/zoahdev/dsh-plugin-doctor) | 插件体检 + 宿主遮蔽检测 + 环境诊断 = 实用的 `dsh plugin check` | [Repo](https://github.com/zoahdev/dsh-plugin-doctor) |
| [dsh-poison-guard](https://github.com/zoahdev/dsh-poison-guard) | 安装前投毒扫描：AST + 去混淆 + 启发式 | [npm](https://www.npmjs.com/package/dsh-poison-guard) |
| [dsh-subscribe](https://github.com/zoahdev/dsh-subscribe) | Steam 式插件市场，一条命令同步 | [npm](https://www.npmjs.com/package/dsh-subscribe) |
| [dsh-artifacts](https://github.com/zoahdev/dsh-artifacts) | Markdown + JSON → 自包含 HTML（文档/卡片/仪表盘/画廊） | [demo](https://zoahdev.github.io/dsh-artifacts/) · [npm](https://www.npmjs.com/package/dsh-artifacts) |
| [dsh-replay](https://github.com/zoahdev/dsh-replay) | 时间旅行调试器：解码 session 全轨迹并可视化 | [npm](https://www.npmjs.com/package/dsh-replay) |
| [dsh-browser-use](https://github.com/zoahdev/dsh-browser-use) | Browser Use 驱动的网页自动化（109k★ 生态） | [npm](https://www.npmjs.com/package/dsh-browser-use) |
| [dsh-zh](https://github.com/zoahdev/dsh-zh) | 中文思考系统提示词（兼容官方预设） | [npm](https://www.npmjs.com/package/dsh-zh) |

## 2026-08-18 · 8 个新验证插件（一天流水线）

> 全部 npm 0.1.0 · CI 全绿 · fresh profile 安装验证 · 教程见 [zh-24-pipeline](https://github.com/zoahdev/dsh-tutorials/blob/main/zh-24-pipeline.md)

| 插件 | 一句话 | npm |
| --- | --- | --- |
| [dsh-dep-audit](https://github.com/zoahdev/dsh-dep-audit) | 依赖供应链卫生审计（peer 可解析 / dist-tag 矛盾 / 过期 / 许可证 / 漂移） | [npm](https://www.npmjs.com/package/dsh-dep-audit) |
| [dsh-llms-forge](https://github.com/zoahdev/dsh-llms-forge) | 从 package.json + README 生成 llms.txt | [npm](https://www.npmjs.com/package/dsh-llms-forge) |
| [dsh-readme-forge](https://github.com/zoahdev/dsh-readme-forge) | 从 package.json + cordis.patch.yml 生成 README | [npm](https://www.npmjs.com/package/dsh-readme-forge) |
| [dsh-cn-boot](https://github.com/zoahdev/dsh-cn-boot) | 国内网络引导：探测 + 镜像/代理推荐 | [npm](https://www.npmjs.com/package/dsh-cn-boot) |
| [dsh-timesheet](https://github.com/zoahdev/dsh-timesheet) | 从会话日志做 turn 级时间跟踪 | [npm](https://www.npmjs.com/package/dsh-timesheet) |
| [dsh-discussions-radar](https://github.com/zoahdev/dsh-discussions-radar) | 官方 Discussions 雷达 | [npm](https://www.npmjs.com/package/dsh-discussions-radar) |
| [dsh-firstrun](https://github.com/zoahdev/dsh-firstrun) | 首次运行体检（工具链/API Key/工作区 + 下一步） | [npm](https://www.npmjs.com/package/dsh-firstrun) |
| [dsh-disk-audit](https://github.com/zoahdev/dsh-disk-audit) | dsh 数据目录磁盘占用审计 | [npm](https://www.npmjs.com/package/dsh-disk-audit) |
## DeepSeek Harness 全栈

- **市场分发**：dsh-subscribe、dsh-plugin-search、dsh-github-release-radar
- **开发工具链**：dsh-plugin-template、dsh-plugin-doctor、dsh-rule-evolve
- **安全**：dsh-poison-guard、dsh-redact、dsh-sandbox-audit
- **可观测**：dsh-replay、dsh-trace、dsh-shelf、dsh-compose-viz
- **生态情报**：dsh-ecosystem、dsh-docs、dsh-tutorials、dsh-github-intelligence
- **生态桥接（借力大项目）**：dsh-browser-use（Browser Use）、dsh-firecrawl（Firecrawl）

完整中文导航（关系图 + 新手路线）→ [dsh-ecosystem 中文总览](https://github.com/zoahdev/dsh-ecosystem#deepseek-harness-全家桶中文总览)

## 上游贡献 & 官方采纳

- **42 个上游补丁**：`deepseek-ai/deepseek-harness` 的 cherry-pick-ready 修复，每个带根因与回归测试 → [补丁账本](https://github.com/zoahdev/dsh-docs/blob/main/docs/specs/upstream-patches.md) · [RFC #2486](https://github.com/deepseek-ai/deepseek-harness/discussions/2486)
- **官方采纳提案**：[#1814](https://github.com/deepseek-ai/deepseek-harness/discussions/1814) 建议把 dsh-plugin-doctor 采纳为官方 `dsh plugin check` + `dsh doctor`（对齐 #1629 / #1719）

## KineGrant — 物理 AI 授权基础设施

[KineGrant Protocol](https://github.com/zoahdev/kinegrant-protocol) — 面向物理 AI（机器人 / ROS2 / 硬件）的开放式授权与问责基础设施：短生命周期能力、本地动作门控、防重放、签名回执、后量子 ML-DSA-65、机群策略/吊销分发，以及零依赖离线浏览器验证器。

- 官网：https://kinegrant.com
- 仓库：https://github.com/zoahdev/kinegrant-protocol

## 其他项目

[X Reply Janitor](https://github.com/zoahdev/x-reply-janitor)（隐藏 X 垃圾回复）· [llms-txt-forge](https://github.com/zoahdev/llms-txt-forge)（生成 `llms.txt`）· [repo-signal](https://github.com/zoahdev/repo-signal)（仓库就绪度评分）· [noise-score](https://github.com/zoahdev/noise-score)（噪声评分）

## 原则

```text
signal > noise
local  > extractive
clear  > clever
shipping > theater
```

Good tools should feel quiet: they remove a problem without becoming the next one.
