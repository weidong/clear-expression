"""
简明表达规范库 通用工具函数
"""

import os
import re
from pathlib import Path
from datetime import datetime


def get_wiki_root():
    """获取 Wiki 根目录路径。"""
    # tools/ 目录的上一级就是 wiki 根目录
    return Path(__file__).parent.parent


def load_markdown_file(filepath):
    """读取 Markdown 文件内容。"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def parse_frontmatter(content):
    """解析 Markdown 文件的 frontmatter。
    返回 (frontmatter_dict, body_text)。
    """
    if not content.startswith('---'):
        return {}, content

    parts = content.split('---', 2)
    if len(parts) < 3:
        return {}, content

    fm_text = parts[1].strip()
    body = parts[2].strip()

    fm = {}
    for line in fm_text.split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()
            fm[key] = value

    return fm, body


def extract_sections(body):
    """从 Markdown 正文中提取二级标题和对应的内容。"""
    sections = {}
    current_section = None
    current_lines = []

    for line in body.split('\n'):
        if line.startswith('## '):
            if current_section:
                sections[current_section] = '\n'.join(current_lines).strip()
            current_section = line[3:].strip()
            current_lines = []
        elif current_section is not None:
            current_lines.append(line)

    if current_section:
        sections[current_section] = '\n'.join(current_lines).strip()

    return sections


def list_wiki_pages(wiki_subdir=None):
    """列出 Wiki 中的所有页面。
    如果指定 wiki_subdir，只列出该子目录下的页面。
    """
    wiki_root = get_wiki_root() / 'wiki'
    if wiki_subdir:
        wiki_root = wiki_root / wiki_subdir

    pages = []
    if wiki_root.exists():
        for md_file in wiki_root.rglob('*.md'):
            rel_path = md_file.relative_to(get_wiki_root() / 'wiki')
            pages.append(rel_path)

    return sorted(pages)


def get_all_pages_with_meta():
    """获取所有 Wiki 页面及其元数据。"""
    wiki_root = get_wiki_root() / 'wiki'
    pages = []

    for md_file in wiki_root.rglob('*.md'):
        content = load_markdown_file(md_file)
        fm, body = parse_frontmatter(content)
        rel_path = md_file.relative_to(wiki_root)
        category = str(rel_path.parent)

        # 从正文提取第一句话作为摘要
        first_para = ''
        for line in body.split('\n'):
            line = line.strip()
            if line and not line.startswith('#') and not line.startswith('>'):
                first_para = line
                break

        pages.append({
            'path': str(rel_path),
            'category': category,
            'name': fm.get('name', fm.get('title', md_file.stem)),
            'source_count': fm.get('source_count', '0'),
            'updated': fm.get('updated', ''),
            'summary': first_para[:80] + ('...' if len(first_para) > 80 else ''),
        })

    return pages


def count_chinese_chars(text):
    """统计文本中的中文字符数。"""
    return len(re.findall(r'[\u4e00-\u9fff]', text))


def count_words(text):
    """统计文本中的词数（中文按字符计，英文按单词计）。"""
    chinese = count_chinese_chars(text)
    # 去掉中文字符后统计英文单词
    english_text = re.sub(r'[\u4e00-\u9fff]', ' ', text)
    english_words = len(english_text.split())
    return chinese + english_words


def load_rules():
    """加载简明表达规范写作规则。"""
    rules_path = get_wiki_root() / 'schema' / 'RULES.md'
    if rules_path.exists():
        return load_markdown_file(rules_path)
    return ''


def load_dict():
    """加载简明词表。"""
    dict_path = get_wiki_root() / 'schema' / 'DICT.md'
    if dict_path.exists():
        return load_markdown_file(dict_path)
    return ''


def load_wiki_schema():
    """加载 Wiki 模式规范。"""
    schema_path = get_wiki_root() / 'schema' / 'WIKI-SCHEMA.md'
    if schema_path.exists():
        return load_markdown_file(schema_path)
    return ''


def append_log(entry_type, description, details=None):
    """向 log.md 追加一条日志记录。"""
    log_path = get_wiki_root() / 'log.md'
    today = datetime.now().strftime('%Y-%m-%d')

    new_entry = f"\n## [{today}] {entry_type} | {description}\n"
    if details:
        for detail in details:
            new_entry += f"- {detail}\n"

    if log_path.exists():
        content = load_markdown_file(log_path)
        # 在 --- 分隔符之后插入新记录
        if '---' in content:
            parts = content.split('---', 1)
            updated = parts[0] + '---' + new_entry + parts[1]
        else:
            updated = content + new_entry
    else:
        updated = f"# 操作日志\n\n> 最新条目在最上方。\n\n---\n{new_entry}"

    with open(log_path, 'w', encoding='utf-8') as f:
        f.write(updated)

    print(f"[日志] 已记录: {entry_type} - {description}")
