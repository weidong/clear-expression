"""
简明表达规范库 摄入工具（Ingest Tool）

用途：
  将新的来源文档摄入 Wiki，生成符合简明表达规范的 Wiki 页面。

工作原理：
  1. 读取原始文档
  2. 提取核心信息（概念、实体、要点等）
  3. 生成符合简明表达规范的 Wiki 页面草稿
  4. 输出建议（需要人工或 LLM 审核后写入）

注意：
  这是一个辅助工具，生成的内容是"草稿"级别。
  正式摄入建议使用 LLM 智能体，以确保完全符合简明表达规范。

用法：
  python tools/ingest.py <raw_file_path> [--concept 概念名] [--output 输出目录]
"""

import sys
import re
import argparse
from pathlib import Path

# 添加 tools 目录到路径
sys.path.insert(0, str(Path(__file__).parent))
from wiki_common import (
    get_wiki_root, load_markdown_file, parse_frontmatter,
    count_words, load_rules, load_dict, append_log
)


def extract_title(content, filepath):
    """从文档中提取标题。"""
    # 优先取第一个一级标题
    for line in content.split('\n'):
        if line.startswith('# '):
            return line[2:].strip()
    # 否则取文件名
    return Path(filepath).stem.replace('-', ' ').title()


def extract_keywords(content, top_n=15):
    """简单的关键词提取（基于词频）。
    这是一个简化实现，实际应用中建议使用 LLM 或专门的 NLP 工具。
    """
    # 提取中文字符和英文单词
    chinese_chars = re.findall(r'[\u4e00-\u9fff]{2,}', content)
    english_words = re.findall(r'[A-Za-z][A-Za-z0-9-]{3,}', content.lower())

    # 简单的词频统计（中文：2-4字词组；英文：单词）
    freq = {}

    # 中文：用 2 字和 3 字的滑动窗口
    for phrase in chinese_chars:
        for n in [2, 3]:
            for i in range(len(phrase) - n + 1):
                w = phrase[i:i+n]
                freq[w] = freq.get(w, 0) + 1

    # 英文单词
    stop_words = {'with', 'that', 'this', 'from', 'have', 'been', 'were',
                  'which', 'their', 'will', 'they', 'them', 'these', 'those',
                  'also', 'more', 'than', 'such', 'into', 'only', 'other',
                  'then', 'over', 'what', 'when', 'where', 'your', 'about'}
    for word in english_words:
        if word not in stop_words and not word.isdigit():
            freq[word] = freq.get(word, 0) + 1

    # 按频率排序，取前 N 个
    sorted_keywords = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return [kw for kw, count in sorted_keywords[:top_n]]


def extract_summary(content, max_sentences=5):
    """提取文档摘要（取前几段的核心句子）。"""
    # 找到正文的前几段
    paragraphs = []
    current = []
    in_code = False

    for line in content.split('\n'):
        stripped = line.strip()
        if stripped.startswith('```'):
            in_code = not in_code
            continue
        if in_code:
            continue
        if stripped.startswith('#') or stripped.startswith('>') or stripped.startswith('---'):
            if current:
                paragraphs.append(' '.join(current))
                current = []
            continue
        if stripped:
            current.append(stripped)
        elif current:
            paragraphs.append(' '.join(current))
            current = []

    if current:
        paragraphs.append(' '.join(current))

    # 取前几段中比较有意义的句子
    summary_sentences = []
    for para in paragraphs:
        if len(para) < 20:
            continue
        # 简单按句号、问号、感叹号分句
        sentences = re.split(r'[。？！\.!?]', para)
        for s in sentences:
            s = s.strip()
            if len(s) >= 15 and len(s) <= 100:
                summary_sentences.append(s)
                if len(summary_sentences) >= max_sentences:
                    break
        if len(summary_sentences) >= max_sentences:
            break

    return summary_sentences


def generate_concept_page_draft(title, content, source_path):
    """生成概念页的草稿（简明表达规范模板）。"""
    keywords = extract_keywords(content, top_n=10)
    summary = extract_summary(content, max_sentences=3)

    today = Path().cwd()  # 仅用于获取日期格式
    from datetime import datetime
    date_str = datetime.now().strftime('%Y-%m-%d')

    draft = f"""---
name: {title}
name_en: TODO
abbreviation: TODO
category: TODO / TODO
source_count: 1
updated: {date_str}
---

# {title}

## 定义

{summary[0] if summary else '（请填写定义）'}

## 工作原理

1. TODO：步骤 1
2. TODO：步骤 2
3. TODO：步骤 3

## 关键组成部分

- **TODO**：描述
- **TODO**：描述
- **TODO**：描述

## 应用场景

- 场景 1
- 场景 2

## 相关概念

- [[相关概念 1]]
- [[相关概念 2]]

## 来源

- [1] [{title}]({source_path})

"""
    return draft


def generate_ingest_report(filepath, title, keywords, summary):
    """生成摄入分析报告。"""
    content = load_markdown_file(filepath)
    word_count = count_words(content)

    report = f"""
╔══════════════════════════════════════════════════════════════╗
║            简明表达规范库 摄入分析报告                        ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  来源文件：{Path(filepath).name:<44}║
║  文档标题：{title[:32]:<44}║
║  总字数：  {word_count:<44}║
║                                                              ║
╠══════════════════════════════════════════════════════════════╣
║  提取的关键词（Top 10）                                       ║
╠══════════════════════════════════════════════════════════════╣
"""
    for i, kw in enumerate(keywords[:10], 1):
        report += f"║  {i:2d}. {kw:<54}║\n"

    report += f"""╠══════════════════════════════════════════════════════════════╣
║  核心摘要                                                     ║
╠══════════════════════════════════════════════════════════════╣
"""
    for i, s in enumerate(summary, 1):
        report += f"║  {i}. {s[:52]:<54}║\n"

    report += f"""╠══════════════════════════════════════════════════════════════╣
║  建议创建/更新的页面                                          ║
╠══════════════════════════════════════════════════════════════╣
║  • 概念页：{title[:46]:<48}║
║  • （可能需要更多概念页，取决于内容）                           ║
║                                                              ║
║  下一步：将草稿交由 LLM 审核和润色，确保符合简明表达规范      ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
"""
    return report


def main():
    parser = argparse.ArgumentParser(description='简明表达规范库 摄入工具')
    parser.add_argument('source', help='原始来源文件路径')
    parser.add_argument('--type', default='concept',
                        choices=['concept', 'entity', 'article'],
                        help='内容类型（默认 concept）')
    parser.add_argument('--dry-run', action='store_true',
                        help='仅生成分析报告，不写入文件')
    args = parser.parse_args()

    source_path = Path(args.source)
    if not source_path.exists():
        print(f"错误：文件不存在 - {source_path}")
        sys.exit(1)

    print(f"\n📥 简明表达规范库 摄入工具")
    print(f"   来源文件: {source_path}")
    print(f"   内容类型: {args.type}")
    print()

    # 读取和分析
    content = load_markdown_file(source_path)
    title = extract_title(content, source_path)
    keywords = extract_keywords(content)
    summary = extract_summary(content)

    # 生成报告
    report = generate_ingest_report(source_path, title, keywords, summary)
    print(report)

    if args.dry_run:
        print("\n[dry-run] 仅生成分析报告，未写入文件。")
        return

    # 生成页面草稿
    if args.type == 'concept':
        draft = generate_concept_page_draft(title, content, str(source_path))

        # 输出到 wiki/concepts/ 目录
        output_dir = get_wiki_root() / 'wiki' / 'concepts'
        output_dir.mkdir(parents=True, exist_ok=True)

        # 生成文件名（标题转小写，用连字符连接）
        filename = title.lower().replace(' ', '-').replace('/', '-') + '.md'
        # 简单清理文件名中的特殊字符
        filename = re.sub(r'[^\w\-\u4e00-\u9fff]', '', filename)

        output_path = output_dir / filename

        if output_path.exists():
            print(f"\n⚠️  页面已存在：{output_path}")
            choice = input("是否覆盖？(y/N): ").strip().lower()
            if choice != 'y':
                print("已取消写入。")
                return

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(draft)

        print(f"\n✅ 页面草稿已生成：{output_path}")
        print(f"   注意：这是草稿，请用 LLM 审核并完善，确保符合简明表达规范。")

        # 记录日志
        append_log('ingest', f'摄入草稿：{title}', [
            f'生成草稿页面：[[{title}]]',
            f'来源：{source_path.name}',
            '待审核：需 LLM 检查规范合规性'
        ])
    else:
        print(f"\nℹ️  类型 '{args.type}' 的草稿生成功能开发中。")
        print("   目前仅支持 concept 类型。")


if __name__ == '__main__':
    main()
