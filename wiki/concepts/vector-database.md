---
name: 向量数据库
name_en: Vector Database
abbreviation: -
category: 数据存储 / 技术
source_count: 2
updated: 2026-09-28
---

# 向量数据库

## 定义

向量数据库是一种专门的数据库。它用于存储和检索向量嵌入。
向量数据库支持相似度搜索。它能快速找到与查询向量最相似的向量。

## 核心功能

- **向量存储**：高效存储大量高维向量。
- **相似度搜索**：根据查询向量，快速返回最相似的向量 [1]。
- **索引构建**：使用特殊索引结构加速搜索。
- **元数据过滤**：结合元数据条件过滤搜索。

## 常见索引算法

- **HNSW**：分层导航小世界图，搜索速度快，精度高。
- **IVF**：倒排文件，适合大规模数据。
- **PQ**：乘积量化，压缩向量，节省存储空间。
- **Annoy**： Spotify 开发的近似最近邻搜索库。

## 常见产品

- **Pinecone**：托管式向量数据库，使用简单。
- **Weaviate**：开源向量数据库，支持多种模块。
- **Qdrant**：开源向量数据库，Rust 编写，性能好。
- **Chroma**：轻量级开源向量数据库，适合原型开发。
- **Milvus**：开源向量数据库，功能全面。

## 应用场景

- [[检索增强生成]] 系统的文档检索
- 推荐系统的内容相似度匹配
- 图片搜索和以图搜图
- 异常检测
- 文档去重

## 相关概念

- [[向量嵌入]]
- [[检索增强生成]]

## 来源

- [1] “Vector Databases: A Beginner's Guide”, F22 Labs, 2026, https://www.f22labs.com/blogs/vector-databases-a-beginners-guide/
- [2] “Best Vector Databases in 2026: A Complete Comparison Guide”, Firecrawl, 2026, https://www.firecrawl.dev/blog/best-vector-databases
