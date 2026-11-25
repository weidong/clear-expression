# 操作日志

> 最新条目在最上方。
> 每条记录统一以 `## [YYYY-MM-DD] 类型 | 描述` 开头。

---

## [2026-11-25] update | 采纳草稿 A 类 4 条规则 + 术语口径对齐 + README 口径统一

- 采纳 research/extraction/中文技术表达规范.md（v1.0 早期草稿）的 A 类 4 条：
  - 规则 31：禁用分号。`；` / `;` 一律改成句号。
  - 规则 32：禁用虚动词名词化。虚动词黑名单：进行、做出、予以、加以、开展、实施。
  - 规则 33：模糊词分级禁令。强模糊词（可能、大概...）出现即报；弱模糊词（最好、一些...）每段 ≥3 个才报。
  - 规则 34：每句必须有明确主语。中文独有的问题，STE 不覆盖。
- 术语口径选草稿 T2 版本：英文缩写已占主导的术语（LLM、RAG、MCP、Token）正文直接用缩写，首次出现给中文全称。规则 6 补充说明，例子改为"正文统一用 LLM，首次出现写 LLM（大语言模型）"。
- `tools/lint.py` 新增三项检查：
  - `check_semicolon`（规则 31）：`python tools/lint.py --check semicolon`
  - `check_nominalization`（规则 32）：`python tools/lint.py --check nominalization`
  - `check_vague_words`（规则 33）：`python tools/lint.py --check vague`，分强弱两级
  - 规则 34（主语）暂无非自动化检查，等后续补
- 新检查首次运行发现 wiki 页面里已有 6 处名词化（`进行预训练`、`做出选择` 等）+ 7 处强模糊词（`可能`）。这些是 wiki 页面存量问题，本次不改，列入后续清理计划。
- `README.md` 4 处「写作规范/写作规则」→「表达规范/表达规则」。`schema/RULES.md` 开头两处「写作规则/写作宪法」→「表达规则/表达宪法」。口径统一：表达不限于写作。
- 规则总数：30 → 34。

---

## [2026-11-25] update | 修复 research/extraction/ 断链：旧绝对路径 → 仓库相对路径

- `reference/writing/` 8 文件：0 断链，只有 1 处外部 URL（少数派风格指南）有效。
- `research/extraction/` 4 文件：12 处断链，集中在 2 个文件，全部是收拢前的 `D:/Projects/learn-ai/asd-ste100-docs/...` / `D:/Projects/learn-ai/asd-ste100-guide/...` 绝对路径。
- `STE100-六份材料结构化提取.md`：6 处断链（读取状态表 4 处 + 5.1/5.2 节各 1 处），全部替换为 `reference/ste100/` 下的仓库相对路径。
- `asd-ste100-zh-structure-extraction.md`：6 处断链（文件开头分析对象列表），同上。
- 两个 `C:/weidong_dotfiles/...` 路径保持原样（不在收拢范围内）。
- 修复后 grep 验证：旧路径零残留。

---

## [2026-11-25] handoff | 会话交接：资料收拢完成，遗留事项清单

- 语料、分析、写作素材已全部收进本仓库，GitHub 同步完成。过程见 `docs/资料收拢记录-2026-11-25.md`。
- 四处来源目录各留一份迁移说明，写明原内容、去向与还原方法。
- 当前状态：30 条规则、10 类 lint 检查、全库 0 问题。

待办，按优先级排序：

1. 核对 `reference/writing/` 与 `research/extraction/` 内部互引是否断链。这些是外部素材搬入的，相对路径可能已失效。
2. 比对 `research/extraction/中文技术表达规范.md` 与 `schema/RULES.md`。前者是早期草稿，后者是现行 30 条，差异需要明确取舍。
3. `README.md` 仍有 3 处把规范写成「写作规范」「写作规则」，与「表达不限于写作」的定位不符，待改。
4. 规则 30 的「引用提交写提交号」没有自动检查。提交号与普通单词难分，硬做会误报，需先定规则再实现。
5. `learn-ai/expr-wiki` 是只读冷备。本仓库稳定运行一段时间后可以删除。
6. `weidong/2026-11-25` 是被进程占用的空目录，三次删除失败，可随时手工清理。
7. lint 未接入 CI。目前只在本地手动运行。

---



## [2026-11-25] update | 简明表达规范迁移收尾：清除残留旧名

- 本仓库是简明表达规范的最终落地点（原名 expr-wiki → 当前 clear-expression）。核心迁移工作已在 11-24 完成，本次只扫残留。
- `schema/WIKI-SCHEMA.md` 目录结构示例根目录名由 `expr-wiki/` 改为 `clear-expression/`。
- `viewer/index.html` 两处残留：badge 文字由 `Plain Expression` 改为 `Clear Expression Standard`；目录树根目录名由 `expr-wiki/` 改为 `clear-expression/`。
- `README.md` 规则速览段落补充说明：共 30 条规则，核心 8 条，其余 22 条覆盖拆句补衔接、句长分档、状态词固定、证据可定位等。示例内容的概念计数由 6 个对齐为实际的 13 个。
- research/ 下的历史分析文档保留旧名（ste-wiki、STE-RULES 等），属于 raw 性质的原始素材，按「原始资料只读」原则不动。
- 全库 lint 验证：总问题 0。

---

## [2026-11-25] update | 规范英文名定为 Clear Expression Standard

- 「简明表达规范」的英文名由 Plain Expression 改为 Clear Expression Standard，不设英文缩写。
- 选词理由：clear 对应「简明」，expression 对应「表达」且不限写作，standard 对应「规范」。
- `README.md` 一级标题改为 `# Clear Expression Standard`，并加中文副标题。
- `AGENTS.md` 的规范定义句同步更新。
- 历史条目中的旧英文名保留原文，不改写日志。

---

## [2026-11-25] update | 新增汇报类规则与不适用范围

- `schema/RULES.md` 新增第九节「汇报类规则」，含规则 25–30：结论先行、状态词固定、写明验证状态与方法、编号选项、不叙述过程、证据可定位。规则总数由 24 条增至 30 条。
- `schema/RULES.md` 第七节新增「不适用」清单：代码、标识符、API 名、命令与路径、原样引用的日志、他人引文保持原样。
- 规则 26 固定 10 个状态词：已完成、部分完成、未开始、进行中、已验证、未验证、失败、跳过、阻塞、未确认。
- 依据：X 平台 22 条 ASD-STE100 应用推文的对照分析。核心借鉴是 `dualface/ste-zh` 的汇报规范，以及 `Ralphis_221` 的排除条款写法。
- `AGENTS.md` 与《简明表达规范和应用手册》中的规则计数同步改为 30 条。
- `tools/lint.py` 新增三项检查：`check_status_words`（规则 26 非固定状态词，只判汇报语境）、`check_lead_sentence`（规则 25 首句是否过程叙述）、`compare_information`（改写前后信息点对比）。
- 命令行新增 `--check status`、`--check lead` 与 `--compare 原稿 改写稿`。
- 信息点对比统计数字、来源编号、双链、小节、列表项、术语六类；保留率低于 95% 提示"应拆句而不是删信息"。
- 用构造样本验证：`已基本完成→已完成`、`还在做→进行中` 命中；首句"我先看了文件"命中，结论句不命中。
- 全库 17 页复查：0 问题，无误报。
- 已知边界：状态词只在句首、冒号前后或"状态/进度"后判定；正文中间的自然叙述不报。
- `tools/lint.py` 再增一项 `check_evidence`（规则 30）：引用代码文件却没写行号、写了"第 N 行"却没写文件，计为硬问题；引用 .md 文档没写行号或章节，只作软提示。
- 证据检查用独立的切句函数，保留反引号内的路径；先剥 URL 与导航链接地址，避免把 `.html`、`.md` 网址误判成本地文件。
- 命令行新增 `--check evidence`。
- 全库复查：硬问题 0、软提示 0，总问题数 0。

---

## [2026-11-24] update | 破折号增加全篇密度统计

- `tools/lint.py` 新增 `check_dash_stats`，统计全文破折号数与每千字密度。
- 全篇密度只作参考，不计入问题数，避免主观阈值造成误报。
- 规则 24 与手册 F7 补充全篇参考值：每千字不超过 3 处。
- 实测样本文章：13 处 / 2177 字，每千字 6.0 处。
- 本库自身：0 处，检查结果仍为 0 问题。

---

## [2026-11-24] update | 规则 23/24 落地到 RULES 与 lint

- `schema/RULES.md` 新增规则 23（使用中文标点）与规则 24（控制破折号密度），共 24 条。
- `tools/lint.py` 新增两项检查：`check_punctuation`、`check_dash_density`。
- 命令行新增 `--check punctuation` 和 `--check dashes`。
- 检查器跳过 `❌` 反例行，避免把故意写坏的例子当成问题。
- 破折号按行统计，避免列表项被合并成一个段落。
- 全库 15 个文件的英文直引号转换为中文引号。
- `raw/` 目录保持只读，未做任何修改。
- 全库检查结果：0 问题。

---

## [2026-11-24] update | 手册补充四条规则并用真实文章验证

- 用第一篇公众号文章测试第九章清单，发现四个漏项。
- 格式层新增 `F6 用中文标点`：中文标点用全角，引号用“”。
- 格式层新增 `F7 控制破折号密度`：每段不超过 1 处。
- 自检清单新增四条：中文标点、破折号、并列改列表、读者定位。
- 全文直引号转换为中文引号，共 16 对。
- 手册自检仍为 2 处长句，均为 `❌` 反例。

---

## [2026-11-24] add | 新增《简明表达规范和应用手册》

- 新增 `docs/简明表达规范和应用手册.md`，全文约 6,100 字，十一个章节。
- 内容覆盖词汇层、句法层、语义层、格式层，以及三类写作场景。
- 第七节专门对比简明表达与大白话，说明三个相同点、四个不同点与适用边界。
- 手册本身按简明表达规范书写，已用 `tools/lint.py` 的切句与被动检测自检。
- 仅保留两处长句，均为用于演示的 `❌` 反例。
- `README.md` 目录树补充 `docs/` 说明。

---

## [2026-11-24] update | 规范更名为「简明表达规范」

- 规范正式定名「简明表达规范」，英文名 Plain Expression，不设英文缩写。
- `schema/STE-RULES.md` 更名为 `schema/RULES.md`，一级标题改为 `# 简明表达规范`。
- `schema/STE-DICT.md` 更名为 `schema/DICT.md`，一级标题改为 `# 简明词表`。
- 目录 `ste-wiki/` 更名为 `expr-wiki/`，文档与命令里的路径同步更新。
- `tools/ste_wiki_common.py` 更名为 `tools/wiki_common.py`，导入语句同步更新。
- ASD-STE100 是原始国际标准，保留原名，实体页 `entities/asd-ste100.md` 不并入本次更名。
- 正文中原本指代本规范的 STE 表述，统一改为「简明表达规范」或「简明表达规范库」。

---

## [2026-11-24] update | 联网核实剩余 7 条来源

- 核实 7 个标题，涉及 fine-tuning、large-language-model、prompt、vector-embedding、how-to-build-rag 五个页面。
- 全部找到可核查原文，未核实标记由 7 条降为 0 条。
  - 换用 IEEE 论文、Microsoft Learn、State of AI Report 官网、DAIR.AI 指南、Redis 博客、arXiv:2412.09165、LangChain 官方文档。
- 修复检查器：来源区文献标题不参与术语一致性检查。原先把 “Prompt Engineering Guide” 中的 prompt 误判为术语。
- 检查结果：0 问题。
- 说明：核实依据为检索结果中的标题与链接，未逐篇通读全文。

---

## [2026-11-24] update | 联网核实 RAG 与向量数据库相关来源

- 核实 5 个标题，对应 6 条来源条目，涉及 3 个页面。
- 查证结果：3 个标题存在真实原文，2 个查无此文。
- 处理方式：存在原文的补作者、出版方与链接；查无此文的替换为真实可查的等价来源。
  - rag-vs-fine-tuning：改为 arXiv 综述 2312.10997 与 RAFT 2403.10131。
  - retrieval-augmented-generation：改为 Dyyota 架构指南与 Neel Mishra 对比文。
  - vector-database：改为 F22 Labs 入门指南与 Firecrawl 对比指南。
- 未核实标记由 13 条降为 7 条，检查结果维持 0 问题。
- 说明：核实依据为检索结果中的标题与链接，未逐篇通读全文。

---

## [2026-11-24] update | 按方案 B 降级标注未核实来源

- 13 条来源条目加“（未核实）”标记。这些条目只有体裁和年份，缺作者、出版方与链接。
- 涉及 8 个页面：rag-vs-fine-tuning、how-to-build-rag、fine-tuning、large-language-model、prompt、retrieval-augmented-generation、vector-database、vector-embedding。
- 保留引用编号，检查结果仍为 0 问题。
- 未标记的条目具备可核查要素：LoRA（ICLR 2022）、Attention Is All You Need、GPT-4 Technical Report、Lewis et al.（NeurIPS 2020）、Chain-of-Thought（NeurIPS 2022）、ASD-STE100 官方规范、Obsidian 官网。

---

## [2026-11-24] update | 补全 7 处来源标注，问题数归零

- 为 7 处事实陈述补上引用编号，来源取自各页面已列出的来源条目。
- 涉及页面：rag-vs-fine-tuning、fine-tuning、large-language-model、retrieval-augmented-generation、vector-database、obsidian。
- 检查结果：总问题 7 → 0。
- 待办：其中 5 条来源条目缺少作者、出版方或链接，需人工核对后补全或降级标注。

---

## [2026-11-24] update | 建立一键改写流程并清理存量问题

- 新增 `schema/REWRITE-PROMPT.md`：可直接复制的改写指令，含范围、红线、输出格式、常见失败模式。
- 改写 6 处超长句（微调、RAG、向量数据库、向量嵌入、ASD-STE100、RAG 搭建指南）。
- `STE-DICT.md` 删除三个过宽的同义表达（指令、上下文限制、向量存储），减少误报。
- `lint.py` 术语检测增加英文词边界，避免命中 STE-RULES、text-embedding-3。
- `AGENTS.md` 增加改写入口指引。

---

## [2026-11-24] update | 修复断链（14 处 → 0 处）

- 新建 7 个概念页：[[智能体]]、[[上下文窗口]]、[[Token]]、[[受控语言]]、[[双向链接]]、[[Markdown]]、[[个人知识库]]。
- `entities/asd-ste100.md` 中指向规范文件的双链改为路径链接（STE-RULES、STE-DICT）。
- `tools/lint.py` 断链检测跳过代码块与行内代码里的双链示例。
- 更新 `index.md`，页面总数由 10 增至 17。

---

## [2026-11-24] update | 修复检查脚本、补充规则、合并第二套库

- 修复 `tools/lint.py` 五个缺陷：中文切句、frontmatter 与表格剥离、词典列定位、双链匹配、断链检测。
- 被动语态检测排除名词用法与定语从句，样本误报由 9 处降到 7 处。
- `schema/STE-RULES.md` 新增第八节（规则 19–22）：只改真被动、表格单元格长度、拆句补衔接、句长分档。
- 长句默认阈值由 30 字改为 25 字。
- 新增 `AGENTS.md`，作为 AI 在本库工作时的入口文件。
- 建立 `docs/`，并入原 `weidong-llm-wiki` 的两份说明文档。

---

## [2026-09-28] init | 初始化 STE-Wiki 知识库

- 创建目录结构（raw/、wiki/、schema/、tools/）
- 创建核心规范文件：
  - `schema/STE-RULES.md` — STE 写作规则摘要
  - `schema/STE-DICT.md` — 受控词典（术语表）
  - `schema/WIKI-SCHEMA.md` — Wiki 模式规范
- 创建 6 个概念页：
  - [[检索增强生成]]
  - [[大语言模型]]
  - [[向量嵌入]]
  - [[微调]]
  - [[提示词]]
  - [[向量数据库]]
- 创建 2 个实体页：
  - [[Obsidian]]
  - [[ASD-STE100]]
- 创建 1 个对比页：
  - [[RAG 与微调的对比]]
- 创建 1 个操作指南页：
  - [[如何搭建一个简单的 RAG 系统]]
- 摄入来源文章 1 篇：`raw/articles/rag-overview-2026.md`
- 创建 `index.md` 索引文件
- 创建 Web 查看器：`viewer/index.html`
- 创建工具脚本：`tools/` 目录下 ingest.py、query.py、lint.py
