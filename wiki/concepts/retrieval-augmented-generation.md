---
name: 检索增强生成
name_en: Retrieval-Augmented Generation
abbreviation: RAG
category: 大语言模型 / 技术
source_count: 3
updated: 2026-09-28
---

# 检索增强生成

## 定义

检索增强生成是一种技术。它将信息检索与文本生成相结合。
系统先从文档库中检索相关内容。然后，把这些内容提供给大语言模型。
大语言模型根据检索到的信息生成更准确的答案 [1]。

## 工作原理

1. 用户提出问题。
2. 系统将问题转换为向量嵌入。
3. 系统在向量数据库中搜索相似的文档片段。
4. 系统将检索到的文档片段与用户问题组合成提示词。
5. 大语言模型根据提示词生成答案。
6. 系统返回答案，并标注信息来源。

## 关键组成部分

- **向量数据库**：存储文档的向量表示，支持相似度搜索。
- **检索器**：根据用户查询，从向量数据库中查找相关文档 [2]。
- **生成器**：接收检索结果和用户问题，生成最终答案。
- **嵌入模型**：将文本转换为向量表示的模型。

## 主要优势

- 答案基于真实文档，减少幻觉。
- 知识可以实时更新，不需要重新训练模型。
- 可以引用具体来源，便于验证。
- 适用于企业内部知识库、客服等场景。

## 局限性

- 检索质量直接影响答案质量。
- 处理需要多步推理的复杂问题时效果不足。
- 上下文窗口有限，能放入的文档数量有限。
- 需要维护向量数据库和文档索引。

## 应用场景

- 企业内部知识问答系统
- 客服自动回复
- 法律文档检索与分析
- 医疗知识问答
- 学术文献综述

## 相关概念

- [[大语言模型]]
- [[向量嵌入]]
- [[向量数据库]]
- [[提示词]]
- [[智能体]]
- [[微调]]

## 来源

- [1] Lewis et al., “Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks”, NeurIPS 2020
- [2] “RAG Architecture for Enterprise: A Practical Guide”, Dyyota, 2026, https://dyyota.com/blog/rag-architecture-guide
- [3] “RAG vs Fine-Tuning: When to Use Which”, Neel Mishra, https://neelmishra.github.io/blog/mlops/rag/rag-vs-fine-tuning.html
