---
name: 大语言模型
name_en: Large Language Model
abbreviation: LLM
category: 人工智能 / 基础模型
source_count: 4
updated: 2026-09-28
---

# 大语言模型

## 定义

大语言模型是一种人工智能模型。它基于大规模文本数据训练。
它能够生成和理解人类语言。它还可以执行写作、翻译、编程等多种任务。

## 核心原理

大语言模型使用 Transformer 神经网络架构。它在大量文本数据上进行预训练。
训练过程中，模型学习语言的统计规律和世界知识。训练完成后，模型可以通过提示词完成各种任务。

## 主要特性

- **语言生成**：可以生成连贯、自然的文本。
- **上下文理解**：能够理解对话或文档中的上下文信息。
- **少样本学习**：只需要几个示例就能完成新任务。
- **多语言支持**：可以处理多种自然语言。
- **推理能力**：能够进行逻辑推理和数学计算。

## 常见应用

- 内容写作和编辑
- 代码生成和调试
- 语言翻译
- 智能客服
- 知识问答
- 数据分析

## 重要概念

- **预训练**：在大规模通用数据上进行的初始训练阶段。
- **微调**：在特定任务数据上进一步训练，提升特定能力 [3]。
- **上下文窗口**：模型单次能处理的最大 token 数量。
- **Token**：模型处理文本的基本单位。

## 局限性

- 可能生成虚假信息（幻觉）。
- 知识有截止日期，不包含训练后的新信息。
- 推理能力有限，复杂问题可能出错。
- 可能产生有偏见或不当的输出。

## 相关概念

- [[检索增强生成]]
- [[微调]]
- [[提示词]]
- [[上下文窗口]]
- [[智能体]]
- [[Token]]

## 来源

- [1] “Attention Is All You Need”, Transformer 原论文, 2017
- [2] “GPT-4 Technical Report”, OpenAI, 2023
- [3] “LLM Fundamentals”, Microsoft Learn, https://learn.microsoft.com/en-us/agent-framework/journey/llm-fundamentals
- [4] “State of AI Report 2026”, Benaich & Air Street Capital, https://www.stateof.ai
