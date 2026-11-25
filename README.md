# Clear Expression Standard

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Python 3](https://img.shields.io/badge/Python-3-3776AB.svg)](https://www.python.org/)

> 简明表达规范。让信息只有一种读法。

基于 **ASD-STE100** 受控语言规范改编的个人知识库系统原型。本库的写作规范定名为 **简明表达规范**，英文名 **Clear Expression Standard**，不设英文缩写。

## 什么是简明表达

- 简 = 句法简单：一句话只说一件事，修饰语不叠加。
- 明 = 语义明确：指代清楚，前提写出来，术语前后一致。

本规范不限语种。中文写作适用，中英混排同样适用。

> 把航空级的清晰写作规范注入知识库的每一层，让你积累的不仅是“存下来的知识”，更是“读得懂、用得上、无歧义”的高质量知识。

## ✨ 核心特性

- 🏛️ **三层架构**：原始来源层 / Wiki 层 / 规范层
- 📝 **写作规范**：所有页面遵循基于 ASD-STE100 改编的简明表达规范
- 📖 **受控词典**：一词一义，消除术语歧义
- 🧩 **标准化页面模板**：概念页、实体页、操作指南、对比分析、综合分析
- 🔍 **三大工具**：摄入（ingest）、查询（query）、整理（lint）
- 🌐 **Web 查看器**：美观的阅读界面，实时规范评分展示
- 📊 **索引 + 日志**：内容导向的索引 + 时间导向的操作日志

## 📁 目录结构

```
expr-wiki/
├── raw/                    # 第 1 层：原始来源（只读）
│   ├── articles/           #   网页文章剪藏
│   ├── papers/             #   学术论文
│   ├── books/              #   书籍章节
│   ├── notes/              #   个人笔记
│   └── images/             #   图片素材
│
├── wiki/                   # 第 2 层：Wiki 页面（LLM 写入，人类阅读）
│   ├── concepts/           #   概念页面
│   ├── entities/           #   实体页面（人/组织/产品/项目）
│   ├── how-to/             #   操作指南页面
│   ├── comparisons/        #   对比分析页面
│   └── synthesis/          #   综合分析页面
│
├── schema/                 # 第 3 层：规范层（LLM 的"宪法"）
│   ├── RULES.md            #   简明表达规范（写作规则）
│   ├── DICT.md             #   简明词表（领域术语表）
│   └── WIKI-SCHEMA.md      #   Wiki 模式规范
│
├── tools/                  # Python 工具脚本
│   ├── wiki_common.py      #   通用工具函数
│   ├── ingest.py           #   摄入工具
│   ├── query.py            #   查询工具
│   └── lint.py             #   整理工具
│
├── viewer/                 # Web 查看器
│   └── index.html          #   单页 Wiki 浏览器
│
├── docs/                   # 说明文档（给人读）
│   ├── 简明表达规范和应用手册.md   #   规范全解与实操指南
│   ├── 搭建方案.md
│   └── 原理大白话-为什么一份gist能搭出整套LLM-Wiki.md
│
├── index.md                # Wiki 索引（内容导向）
├── log.md                  # 操作日志（时间导向）
└── README.md               # 本文件
```

## 🚀 快速开始

### 1. 浏览 Wiki

直接用浏览器打开 `viewer/index.html`，即可查看所有示例页面。

也可以用 **Obsidian** 打开 `expr-wiki/` 目录，获得更完整的双链和图谱体验。

### 2. 使用命令行工具

> 要求：Python 3.8+

#### 查询（Query）

```bash
# 搜索与"RAG"相关的页面
python tools/query.py "RAG"

# 搜索与"向量"相关的页面，返回前 3 个
python tools/query.py "向量" --top 3
```

#### 整理（Lint）

```bash
# 运行所有检查
python tools/lint.py

# 只检查长句
python tools/lint.py --check long-sentences

# 自定义长句阈值
python tools/lint.py --check long-sentences --max-length 25

# 检查术语一致性
python tools/lint.py --check terms
```

#### 摄入（Ingest）

```bash
# 分析一篇新文章，生成概念页草稿
python tools/ingest.py raw/articles/rag-overview-2026.md --dry-run

# 实际写入（生成草稿页面）
python tools/ingest.py raw/articles/rag-overview-2026.md
```

> **注意**：摄入工具生成的是“草稿”级别内容。
> 正式使用建议配合 LLM 智能体，确保完全符合简明表达规范。

## 📖 简明表达规范速览

所有 Wiki 页面遵循以下核心规则（摘自 `schema/RULES.md`）：

| # | 规则 | 说明 |
|---|------|------|
| 1 | 使用短句 | 每句只表达一个意思，10-20 字/词 |
| 2 | 主动语态 | 明确指出谁做什么 |
| 3 | 具体名词 | 避免模糊指代，该重复就重复 |
| 4 | 常用词汇 | 优先使用简单常见的词 |
| 5 | 一词一义 | 一个术语只有一个含义 |
| 6 | 术语定义 | 首次出现必须明确定义 |
| 7 | 编号步骤 | 操作用编号，特性用项目符号 |
| 8 | 来源追溯 | 每条事实都标注来源 |

完整规则见 `schema/RULES.md`。

## 🔧 与 LLM 配合使用

本系统设计为 **LLM 辅助**的知识库。推荐用法：

### 摄入新内容
1. 将文章/论文放入 `raw/` 对应目录
2. 调用 LLM 智能体，加载 `schema/` 下的三份规范
3. 让 LLM 阅读来源并生成符合简明表达规范的 Wiki 页面
4. LLM 更新 `index.md` 和 `log.md`

### 回答问题
1. 向 LLM 提问
2. LLM 搜索 `index.md`，阅读相关页面
3. LLM 按简明表达规范给出答案
4. 有价值的答案归档回 wiki

### 定期整理
1. 定期运行 `python tools/lint.py` 做基础检查
2. 让 LLM 做深度整理——统一术语、修复长句、补全来源
3. LLM 输出整理报告并执行修复

## 📚 示例内容

当前 Wiki 包含以下示例页面：

### 概念（6 个）
- 检索增强生成（RAG）
- 大语言模型（LLM）
- 向量嵌入
- 微调
- 提示词
- 向量数据库

### 实体（2 个）
- Obsidian
- ASD-STE100

### 操作指南（1 个）
- 如何搭建一个简单的 RAG 系统

### 对比分析（1 个）
- RAG 与微调的对比

## 🎯 设计理念

**知识的价值 = 内容的价值 × 清晰度**

同样的内容，写得越清晰、越无歧义，你能从中榨出的价值就越高。
ASD-STE100 提供了一套经过航空工业几十年验证的“清晰度标准”，
而 LLM 让这套标准的执行成本接近于零。

随着 Wiki 越来越大，简明表达规范的价值也会越来越明显——
当你有几百个页面时，统一的语言和结构就是可维护性的基石。

## 📝 参考资料

- [ASD-STE100 官方网站](https://www.asd-ste100.org/)
- Karpathy 关于个人知识库的 [推文](https://x.com/karpathy/status/2039805659525644595) 和 [Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- Karpathy 关于 ASD-STE100 的 [推文](https://x.com/karpathy/status/2105819303471976479)

---

## 📄 License

© 2026 weidong. 本项目采用 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 许可协议，全文见 [LICENSE](LICENSE)。

你可以自由复制、修改、商用，条件只有一个：注明来源。

---

*本项目是一个概念验证原型，用于展示简明表达规范与个人知识库的结合方式。*
