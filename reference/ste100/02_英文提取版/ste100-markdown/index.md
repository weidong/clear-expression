# ASD-STE100 Issue 9 — Markdown 版提取总索引

> 提取来源：ASD-STE100 Issue 9 官方 PDF（434 页）
> 提取日期：2026-10-04
> 说明：本目录为原始英文文档的 Markdown 结构化提取版本，便于 AI 工具检索使用。

---

## 📁 目录结构

```
ste100-markdown/
├── front-matter/                  # 前置内容
│   ├── general-introduction.md     #   总论（STE是什么、历史、适用范围）
│   └── highlights.md               #   Issue 9 变更要点
├── part1-writing-rules/           # 第一部分：写作规则（53 条 + 8 条 GR）
│   ├── section-1-words.md          #   第 1 节 词汇（14 条规则）
│   ├── section-2-multi-word-nouns.md  # 第 2 节 多词名词（2 条规则）
│   ├── section-3-verbs.md          #   第 3 节 动词（7 条规则）
│   ├── section-4-sentences.md      #   第 4 节 句子（5 条规则）
│   ├── section-5-procedural-writing.md  # 第 5 节 程序性写作（5 条规则）
│   ├── section-6-descriptive-writing.md # 第 6 节 描述性写作（6 条规则）
│   ├── section-7-safety-instructions.md # 第 7 节 安全说明（3 条规则）
│   ├── section-8-punctuation-and-word-count.md # 第 8 节 标点与词数（7 条规则）
│   └── section-9-writing-practices.md # 第 9 节 写作实践（4 条规则 + 8 条 GR）
├── part2-dictionary/              # 第二部分：受控词典
│   ├── dictionary-introduction.md  #   词典使用说明（20 页）
│   └── sample-entries.md           #   样本词条（结构分析用）
└── data/                           # 结构化数据（待补充）
    └── (TBD)                       #   词条 JSON 等
```

---

## 📋 Part 1 — 写作规则速览

| 节 | 主题 | 规则数 | PDF 页码 | 内容摘要 |
|----|------|--------|---------|---------|
| 1 | Words 词汇 | 14 条 | 18 页 | 批准词、批准含义、词性、技术名词分类、技术动词分类、拼写 |
| 2 | Multi-word nouns 多词名词 | 2 条 | 4 页 | 多词名词长度限制、长名词的处理方法 |
| 3 | Verbs 动词 | 7 条 | 10 页 | 动词形式与时态、祈使句、被动语态、-ing 形式、情态动词 |
| 4 | Sentences 句子 | 5 条 | 10 页 | 句子主题、长度、垂直列表、连接词、冠词/指示形容词 |
| 5 | Procedural writing 程序性写作 | 5 条 | 8 页 | 步骤结构、警告/注意、注释 |
| 6 | Descriptive writing 描述性写作 | 6 条 | 8 页 | 信息结构、关键短语、段落主题 |
| 7 | Safety instructions 安全说明 | 3 条 | 4 页 | 警告/注意/提示三级分类 |
| 8 | Punctuation & word count 标点与词数 | 7 条 | 8 页 | 标点符号使用、词数统计规则 |
| 9 | Writing practices 写作实践 | 4 条 + 8 GR | 14 页 | 句式转换、一致性、通用建议（GR-1 到 GR-8） |

**总计**：53 条正式规则 + 8 条通用建议（General Recommendations）

---

## 📖 Part 2 — 受控词典速览

| 项目 | 数量 |
|------|------|
| 批准词 (approved words) | 875 个 |
| 非批准词 (non-approved words) | 1,274 个 |
| 合计词条数 | 约 2,149 个 |
| 词典页数 | 286 页（A-Y，无 X、Z） |

### 词条四列结构

| 列 | 内容 | 说明 |
|----|------|------|
| 列 1 | Word (part of speech) | 批准词全大写，非批准词小写；8 种词性 |
| 列 2 | Approved meaning / ALTERNATIVES | 批准词给词义，非批准词给替代词 |
| 列 3 | STE EXAMPLE | 正确用法示例 |
| 列 4 | Non-STE example | 错误用法示例（批准词此列为空） |

---

## 🔍 如何使用本提取版

### 给 AI 工具 / LLM 使用

1. **理解规则**：读取 `part1-writing-rules/` 下的全部 9 个文件
   - 全部 9 个 Section 约 5-6 万字，可一次性放入大多数 100K+ 上下文的模型

2. **查词典**：
   - 先读 `part2-dictionary/dictionary-introduction.md` 了解使用方法
   - 具体词的查询建议配合向量检索或直接查官方 PDF
   - **精选 100 词**：见 `../zh-translation/asd-ste100-selected-dictionary.zh-CN.md`（中文精选）

3. **推荐用法**：
   - 将 `section-1-words.md` 到 `section-9-writing-practices.md` 作为 RAG 的知识库
   - 或者将写作规则浓缩后放入系统提示词中
   - 词典按需检索，不需要全量加载

### 给人类阅读使用

- 中文完整翻译：`../zh-translation/asd-ste100-writing-rules.zh-CN.html`（推荐）
- 中文精选词典：`../zh-translation/asd-ste100-selected-dictionary.zh-CN.html`
- AI 应用手册：`../ai-handbook/ste100-ai-handbook.zh-CN.html`

---

## 📝 提取说明

- 使用 **pypdf** 库从原始 PDF 提取文本
- 已清理页眉页脚（"ASD-STE100 Simplified Technical English"、"Issue 9"、日期、页码等）
- 保留了原文的章节结构、规则编号、例句
- 词典部分因体量较大（286 页），仅提取了 Introduction 和样本词条用于结构分析
- 如需完整词典的结构化数据，建议配合 OCR + 表格识别工具进一步处理

---

*本提取版仅供学习和研究使用。ASD-STE100 为 ASD（Aerospace, Security and Defence Industries Association of Europe）的注册商标。*
