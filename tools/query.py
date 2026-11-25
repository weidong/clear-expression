"""
简明表达规范库 查询工具（Query Tool）

用途：
  在 Wiki 中搜索相关页面，并综合回答问题。

工作原理：
  1. 读取 index.md 获取所有页面列表
  2. 基于关键词匹配查找相关页面
  3. 读取相关页面的内容
  4. 输出结构化的答案

注意：
  这是一个基于关键词的简单查询工具。
  更智能的查询建议使用 LLM + 向量数据库（RAG）。

用法：
  python tools/query.py "你的问题" [--top N]
"""

import sys
import re
import argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from wiki_common import (
    get_wiki_root, load_markdown_file, parse_frontmatter,
    extract_sections, get_all_pages_with_meta
)


def tokenize(text):
    """简单的分词（中文按字/2字词，英文按单词）。"""
    tokens = set()

    # 英文单词
    english_words = re.findall(r'[A-Za-z][A-Za-z0-9-]+', text.lower())
    tokens.update(english_words)

    # 中文：2 字词组
    chinese = re.findall(r'[\u4e00-\u9fff]+', text)
    for phrase in chinese:
        for n in [2, 3]:
            for i in range(len(phrase) - n + 1):
                tokens.add(phrase[i:i+n])

    return tokens


def score_page(page_meta, query_tokens):
    """计算页面与查询的相关度得分。"""
    score = 0

    # 读取页面内容
    page_path = get_wiki_root() / 'wiki' / page_meta['path']
    try:
        content = load_markdown_file(page_path)
    except Exception:
        return 0

    content_lower = content.lower()
    fm, body = parse_frontmatter(content)

    # 标题匹配（权重高）
    name = fm.get('name', page_meta['name']).lower()
    name_tokens = tokenize(name)
    name_match = len(query_tokens & name_tokens)
    score += name_match * 10

    # 正文匹配
    body_tokens = tokenize(body)
    body_match = len(query_tokens & body_tokens)
    score += body_match * 1

    # 完全匹配加分
    for token in query_tokens:
        if len(token) >= 2 and token in name:
            score += 15

    return score


def search_pages(query, top_n=5):
    """搜索最相关的 Wiki 页面。"""
    all_pages = get_all_pages_with_meta()
    query_tokens = tokenize(query)

    if not query_tokens:
        return []

    scored = []
    for page in all_pages:
        s = score_page(page, query_tokens)
        if s > 0:
            scored.append((s, page))

    scored.sort(key=lambda x: x[0], reverse=True)
    return scored[:top_n]


def extract_answer_from_page(page_path, query, max_chars=500):
    """从页面中提取与查询相关的段落。"""
    content = load_markdown_file(page_path)
    fm, body = parse_frontmatter(content)
    sections = extract_sections(body)

    query_tokens = tokenize(query)
    best_section = None
    best_score = 0

    for section_name, section_content in sections.items():
        section_tokens = tokenize(section_name + ' ' + section_content[:500])
        score = len(query_tokens & section_tokens)
        if score > best_score:
            best_score = score
            best_section = (section_name, section_content)

    result = []
    if best_section:
        name, content_text = best_section
        # 截取最相关的部分
        paragraphs = content_text.split('\n\n')
        for para in paragraphs[:3]:
            para = para.strip()
            if para and not para.startswith('#'):
                result.append(para[:max_chars])

    return result


def format_answer(query, results):
    """格式化查询结果。"""
    output = f"""
{'='*60}
  🔍 简明表达规范库 查询结果
{'='*60}

  查询：{query}
  找到 {len(results)} 个相关页面

{'─'*60}
"""

    for i, (score, page) in enumerate(results, 1):
        page_path = get_wiki_root() / 'wiki' / page['path']

        output += f"""
  📄 [{i}] {page['name']}
      分类：{page['category']}
      相关度：{score}
      摘要：{page['summary']}
      路径：wiki/{page['path']}
"""

        # 提取相关内容片段
        snippets = extract_answer_from_page(page_path, query)
        if snippets:
            output += f"      相关片段：\n"
            for snippet in snippets[:2]:
                # 清理格式
                clean = re.sub(r'\n+', ' ', snippet)[:200]
                output += f"        • {clean}...\n"

    output += f"""
{'='*60}
  提示：
    • 用 Obsidian 打开 wiki/ 目录查看完整页面
    • 更深入的问答建议使用 LLM + RAG
    • 查询后有价值的答案可以归档回 Wiki
{'='*60}
"""
    return output


def main():
    parser = argparse.ArgumentParser(description='简明表达规范库 查询工具')
    parser.add_argument('query', help='查询内容')
    parser.add_argument('--top', type=int, default=5,
                        help='返回的最大页面数（默认 5）')
    args = parser.parse_args()

    print(f"\n🔍 简明表达规范库 查询工具")
    print(f"   查询: {args.query}")
    print()

    results = search_pages(args.query, top_n=args.top)

    if not results:
        print("  😕 未找到相关页面。")
        print()
        print("  建议：")
        print("    • 尝试使用不同的关键词")
        print("    • 检查拼写是否正确")
        print("    • 可能该主题尚未摄入 Wiki")
        print()
        return

    answer = format_answer(args.query, results)
    print(answer)


if __name__ == '__main__':
    main()
