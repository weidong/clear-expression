---
name: 向量嵌入
name_en: Vector Embedding
abbreviation: -
category: 人工智能 / 技术
source_count: 2
updated: 2026-09-28
---

# 向量嵌入

## 定义

向量嵌入是一种技术。它将文本、图像等数据转换为数学向量。
向量可以表示数据的语义含义。语义相似的数据，其向量在空间中的距离更近。

## 工作原理

1. 将输入文本送入嵌入模型。
2. 模型将文本编码为一个高维向量（通常为 256-2048 维）。
3. 向量的每个维度表示文本的某种语义特征。
4. 两个向量之间的距离表示对应文本的语义相似度。

## 常见相似度计算方法

- **余弦相似度**：衡量两个向量方向的相似程度。它的取值范围是 -1 到 1。
- **欧氏距离**：衡量两个向量在空间中的直线距离。
- **点积**：两个向量对应元素相乘后求和。

## 应用场景

- 语义搜索：根据含义而非关键词搜索文档。
- 推荐系统：根据用户行为推荐相似内容。
- 聚类分析：将相似的数据自动分组。
- 异常检测：识别与大多数数据不同的异常点。
- [[检索增强生成]]：检索相关文档供大语言模型使用。

## 嵌入模型

- **OpenAI text-embedding-3**：商用，效果好，成本适中。
- **BGE**：开源，中英文效果好。
- **Cohere Embed**：商用，多语言支持好。
- **all-MiniLM**：开源轻量，速度快。

## 相关概念

- [[向量数据库]]
- [[检索增强生成]]
- [[大语言模型]]

## 来源

- [1] “Vector Embeddings Explained”, Redis, 2026, https://redis.io/blog/vector-embeddings-explained/
- [2] “When Text Embedding Meets Large Language Model: A Comprehensive Survey”, arXiv:2412.09165, 2024, https://arxiv.org/abs/2412.09165
