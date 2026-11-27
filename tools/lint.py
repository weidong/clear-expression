"""
简明表达规范库 整理工具（Lint Tool）

用途：
  检查 Wiki 页面的规范合规性和内容完整性。
  找出需要改进的地方，生成整理报告。

检查项：
  1. 长句检测（超过阈值的句子）
  2. 被动语态检测
  3. 术语一致性（基于 DICT.md）
  4. 缺少来源标注的事实陈述
  5. 缺少 frontmatter 的页面
  6. 孤立页面（没有入站链接）
  7. 非固定状态词（规则 26）
  8. 首句过程叙述（规则 25）
  9. 改写前后信息点对比（规则 27 配套，规则 22「不要删信息」）
 10. 证据可定位（规则 30）
 11. 禁用分号（规则 31）
 12. 虚动词名词化（规则 32）
 13. 模糊词分级（规则 33）

用法：
  python tools/lint.py [--check long-sentences|passive|terms|punctuation|dashes|status|lead|evidence|semicolon|nominalization|vague|all]
                       [--max-length 25]
  python tools/lint.py --compare 原稿.md 改写稿.md
"""

import sys
import re
import argparse
from pathlib import Path
from collections import defaultdict

sys.path.insert(0, str(Path(__file__).parent))
from wiki_common import (
    get_wiki_root, load_markdown_file, parse_frontmatter,
    list_wiki_pages, count_words
)


def strip_markdown_structure(content):
    """剥离 frontmatter、代码块、链接语法、表格与列表标记。

    只保留需要检查句长的正文文本。
    """
    _, body = parse_frontmatter(content)

    # 代码块与行内代码
    body = re.sub(r'```.*?```', '', body, flags=re.DOTALL)
    body = re.sub(r'`[^`\n]*`', '', body)
    # 图片
    body = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', body)
    # 链接保留可见文字
    body = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', body)
    body = re.sub(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', r'\1', body)

    lines = []
    for raw in body.split('\n'):
        line = raw.strip()

        # 表格分隔行
        if re.fullmatch(r'\|[\s:\-|]+\|', line):
            continue

        # 表格数据行：按单元格拆开，每格当作独立句子
        if line.startswith('|'):
            cells = [c.strip() for c in line.strip('|').split('|')]
            cells = [c for c in cells if c and c != '-']
            if cells:
                lines.append('。'.join(cells) + '。')
            continue

        # 标题、引用、列表、分隔线标记
        line = re.sub(r'^#{1,6}\s*', '', line)
        line = re.sub(r'^>\s?', '', line)
        line = re.sub(r'^([-*+]|\d+[.)])\s+', '', line)
        if re.fullmatch(r'[-*_]{3,}', line):
            continue
        # 加粗、斜体
        line = re.sub(r'\*{1,3}([^*]+)\*{1,3}', r'\1', line)
        lines.append(line)

    return '\n'.join(lines)


def split_sentences(text):
    """将正文分割成句子。

    中文标点后通常没有空格，因此不能依赖空格切分。
    """
    text = strip_markdown_structure(text)

    # 中文/英文句末标点后断行
    text = re.sub(r'([。！？!?])', r'\1\n', text)
    # 英文句号：仅在前一个字符是字母/数字/右括号时断句，避免切开小数点
    text = re.sub(r'(?<=[A-Za-z0-9\)\]])\.[ \t]+', '.\n', text)

    sentences = []
    for chunk in text.split('\n'):
        chunk = chunk.strip()
        if not chunk:
            continue
        if not re.search(r'[\u4e00-\u9fffA-Za-z]', chunk):
            continue
        sentences.append(chunk)
    return sentences


def check_long_sentences(content, max_length=30):
    """检测长句。
    返回 [(sentence, word_count), ...]
    """
    sentences = split_sentences(content)
    long_sentences = []

    for s in sentences:
        wc = count_words(s)
        if wc > max_length:
            long_sentences.append((s, wc))

    return long_sentences


def check_passive_voice(content):
    """检测被动语态。

    中文被动语态的常见标志：被、由、为……所、受到、遭到。
    "得到"在中文里多为主动用法（得到一个模型），不计入被动标志。
    返回 [(sentence, pattern), ...]
    """
    sentences = split_sentences(content)
    passive_patterns = ['被', '由', '为…所', '受到', '遭到']

    findings = []
    for s in sentences:
        for pattern in passive_patterns:
            if pattern not in s:
                continue

            # '被' 作构词成分时不是被动
            if pattern == '被':
                if '被动' in s or '被子' in s:
                    continue
                # '被审对象''被调查人'这类名词性用法
                if re.search(r'被[^，。；：、]{0,4}(对象|人员|人|方|告|申请人|调查者)', s):
                    continue
                # '被……的人/事'是定语从句，按规则 19 不改
                if re.search(r'被[^。]{0,20}的(人|事)', s):
                    continue

            # '由' 的常见非被动词
            if pattern == '由' and re.search(r'由于|理由|自由|由来', s):
                continue

            findings.append((s, pattern))
            break

    return findings


def check_punctuation(content):
    """检查中文正文中的英文直引号。返回问题行列表。"""
    text = strip_markdown_structure(content)
    issues = []
    for line in text.splitlines():
        cleaned = re.sub(r'`[^`]*`', '', line)
        if '❌' in cleaned:
            continue
        if '"' in cleaned:
            issues.append(cleaned.strip()[:80])
    return issues


def check_dash_density(content, max_per_paragraph=1):
    """检查每段落的破折号密度。返回 (段落摘要, 数量) 列表。"""
    text = strip_markdown_structure(content)
    issues = []
    for line in text.splitlines():
        line = line.strip()
        if not line or '❌' in line:
            continue
        count = line.count('——')
        if count > max_per_paragraph:
            summary = line[:60] + ('...' if len(line) > 60 else '')
            issues.append((summary, count))
    return issues


def check_dash_stats(content):
    """统计破折号总数与全文密度。返回 (破折号数, 字数, 每千字密度)。"""
    text = strip_markdown_structure(content)
    dashes = 0
    chars = 0
    for line in text.splitlines():
        if '❌' in line:
            continue
        dashes += line.count('——')
        chars += len(re.sub(r'\s', '', line))
    per_k = round(dashes / chars * 1000, 1) if chars else 0.0
    return dashes, chars, per_k


STATUS_VARIANTS = {
    '已经完成': '已完成',
    '已基本完成': '已完成',
    '基本完成': '已完成',
    '搞定了': '已完成',
    '弄好了': '已完成',
    '做完了': '已完成',
    '部分已完成': '部分完成',
    '完成了一半': '部分完成',
    '已经验证': '已验证',
    '验证过了': '已验证',
    '尚未开始': '未开始',
    '还没开始': '未开始',
    '尚未完成': '进行中',
    '还在做': '进行中',
    '没有验证': '未验证',
    '未做验证': '未验证',
    '没测试': '未验证',
    '卡住了': '阻塞',
    '跳过不做': '跳过',
    '不太确定': '未确认',
}


def check_status_words(content):
    """检查非固定状态词（规则 26）。

    只在"汇报语境"里判定：状态词出现在句首、冒号之后，或紧跟在
    "状态""进度"后面。正文里"Agent 正在做任务"这类普通叙述不算。
    返回 [(sentence, variant, fixed), ...]
    """
    sentences = split_sentences(content)
    findings = []
    for s in sentences:
        if '❌' in s:
            continue
        for variant, fixed in STATUS_VARIANTS.items():
            idx = s.find(variant)
            if idx < 0:
                continue
            prefix = s[:idx].rstrip()
            suffix = s[idx + len(variant):].lstrip()
            at_head = not prefix
            after_colon = bool(prefix) and prefix[-1] in '：:'
            after_label = bool(re.search(r'(状态|进度)$', prefix))
            # 标准汇报格式是"状态词：范围"
            before_colon = suffix.startswith(('：', ':'))
            if at_head or after_colon or after_label or before_colon:
                findings.append((s, variant, fixed))
                break
    return findings


PROCESS_MARKERS = ['我先', '我首先', '首先我', '我们首先', '接下来我',
                   '接着我', '然后我', '刚才我', '刚刚我', '我先看',
                   '我读了', '我看了']


def check_lead_sentence(content):
    """检查正文首句是不是过程叙述（规则 25：结论先行）。

    跳过标题块与分隔线，取第一个真正的正文段落，只看它的第一句。
    返回 [(sentence, marker), ...]，最多一条。
    """
    _, body = parse_frontmatter(content)
    body = re.sub(r'```.*?```', '', body, flags=re.DOTALL)

    for block in re.split(r'\n\s*\n', body):
        lines = [ln.strip() for ln in block.splitlines() if ln.strip()]
        if not lines:
            continue
        # 纯标题块、纯分隔线块不算正文
        if all(re.match(r'^#{1,6}\s', ln) or re.fullmatch(r'[-*_]{3,}', ln)
               for ln in lines):
            continue
        sentences = split_sentences(block)
        if not sentences:
            continue
        first = sentences[0]
        for marker in PROCESS_MARKERS:
            if first.startswith(marker):
                return [(first, marker)]
        return []
    return []


def count_information_points(content):
    """统计一篇文章的信息点，用于改写前后对比（规则 22「不要删信息」）。

    返回 dict，包含数字、来源编号、双链、小节标题、列表项五个集合，
    以及术语命中集合。用集合而非计数，便于定位"哪一条没了"。
    """
    _, raw = parse_frontmatter(content)
    raw_no_code = re.sub(r'```.*?```', '', raw, flags=re.DOTALL)

    numbers = set(re.findall(r'\d+(?:\.\d+)?\s*(?:%|倍|个|种|条|篇|页|年|月|日|天|小时|分钟|字|词)?',
                             re.sub(r'\[\d+\]', '', raw_no_code)))
    numbers = {n.replace(' ', '') for n in numbers if n.strip()}

    sources = set(re.findall(r'\[(\d+)\]', raw_no_code))
    links = set(re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', raw_no_code))
    headings = set(re.findall(r'^#{2,6}\s+(.+)$', raw_no_code, flags=re.MULTILINE))
    list_items = set()
    for line in raw_no_code.splitlines():
        if re.match(r'^\s*([-*+]|\d+[.)])\s+\S', line):
            list_items.add(re.sub(r'^\s*([-*+]|\d+[.)])\s+', '', line).strip())

    terms = set()
    for alt, standard in load_term_alternatives().items():
        if standard in raw_no_code:
            terms.add(standard)

    return {
        '数字': numbers,
        '来源': sources,
        '双链': links,
        '小节': headings,
        '列表项': list_items,
        '术语': terms,
    }


def compare_information(old_content, new_content):
    """比较两版文本的信息点，返回 (旧统计, 新统计, 减少项, 新增项)。"""
    old = count_information_points(old_content)
    new = count_information_points(new_content)

    lost, gained = {}, {}
    for key in old:
        lost[key] = sorted(old[key] - new[key])
        gained[key] = sorted(new[key] - old[key])
    return old, new, lost, gained


def format_compare(old_path, new_path, old_content, new_content):
    """格式化改写前后信息点对比结果。"""
    old, new, lost, gained = compare_information(old_content, new_content)

    total_old = sum(len(v) for v in old.values())
    total_new = sum(len(v) for v in new.values())
    ratio = round(total_new / total_old * 100, 1) if total_old else 100.0

    lines = [f"\n{'='*60}", "  🔍 改写前后信息点对比", f"{'='*60}", ""]
    lines.append(f"  原稿：{old_path}")
    lines.append(f"  改写：{new_path}")
    lines.append("")
    lines.append(f"  {'维度':<8}{'原稿':>6}{'改写':>6}{'减少':>6}")
    for key in old:
        lines.append(f"  {key:<8}{len(old[key]):>6}{len(new[key]):>6}{len(lost[key]):>6}")
    lines.append("")
    lines.append(f"  信息点合计：{total_old} → {total_new}，保留 {ratio}%")

    lost_total = sum(len(v) for v in lost.values())
    if lost_total:
        lines.append(f"\n  ⚠️  疑似删掉的信息点：{lost_total} 项")
        for key, items in lost.items():
            for item in items[:5]:
                lines.append(f"    • [{key}] {item}")
    else:
        lines.append("\n  ✅ 没有检测到信息点减少")

    if ratio < 95:
        lines.append(f"\n  ⚠️  保留率 {ratio}% 低于 95%，按规则 22 应拆句而不是删信息。")
    lines.append(f"{'='*60}")
    return '\n'.join(lines)


CODE_FILE_RE = re.compile(
    r'[\w./\\-]+\.(?:py|js|ts|tsx|jsx|mjs|cjs|json|ya?ml|toml|sh|bash|ps1|bat|'
    r'css|html|java|go|rs|c|h|cpp|hpp|sql|ini|cfg)\b'
)
MD_FILE_RE = re.compile(r'[\w./\\-]+\.md\b')
LINE_REF_RE = re.compile(r'[:：]\s*\d+(?:\s*[-–~]\s*\d+)?')
BARE_LINE_RE = re.compile(r'第\s*\d+\s*行')
SECTION_REF_RE = re.compile(r'#L?\d+|第\s*[\d一二三四五六七八九十]+\s*[节章]')


def _raw_sentences(content):
    """按句切分，但保留行内代码。

    split_sentences 会删掉反引号内容，而路径通常写在反引号里，
    所以证据检查必须另用一套切句。
    """
    _, body = parse_frontmatter(content)
    body = re.sub(r'```.*?```', '', body, flags=re.DOTALL)
    body = re.sub(r'([。！？!?])', r'\1\n', body)
    return [ln.strip() for ln in body.split('\n') if ln.strip()]


def check_evidence(content):
    """检查证据是否可定位（规则 30）。

    三类硬问题：
      A. 引用了代码文件，但整句没有行号。
      B. 写了"第 N 行"，但整句没有文件。
      C. 显式说"commit/提交"，但没附 7–40 位 hex 短 hash。
    一类软提示（不计入问题数）：
      D. 引用了 .md 文档，但没有行号、锚点或章节号。
    返回 (硬问题列表, 软提示列表)，元素为 (句子, 说明)。

    URL 里的 .html、.md 不是本地文件引用，先剥掉再判断；
    来源区是文献标题，整段跳过。
    """
    hard, soft = [], []
    _, body = parse_frontmatter(content)
    body = re.split(r'\n## 来源', body, maxsplit=1)[0]

    # 规则 30 提交号检查：显式标记触发（方案 A）
    # 句子里有 git commit 命令 → 整句是命令语境，跳过触发检查
    # 否则裸 commit/提交/提交号/commit号 是触发词，要求同句有 7-40 位 hex
    GIT_CMD_RE = re.compile(r'\bgit\s+commit\b', re.IGNORECASE)
    COMMIT_TRIGGER = re.compile(r'commit号|提交号|提交|\bcommit\b', re.IGNORECASE)
    HASH_RE = re.compile(r'\b[0-9a-f]{7,40}\b')

    for s in _raw_sentences(body):
        if '❌' in s:
            continue
        s_clean = re.sub(r'https?://\S+', '', s)
        # 导航链接的目标不属于正文引用，去掉链接地址再判断
        s_clean = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', s_clean)
        has_code_file = bool(CODE_FILE_RE.search(s_clean))
        has_md_file = bool(MD_FILE_RE.search(s_clean))
        has_line = bool(LINE_REF_RE.search(s_clean))
        has_section = bool(SECTION_REF_RE.search(s_clean))

        if has_code_file and not has_line:
            hard.append((s, '引用代码文件但没写行号'))
            continue

        if BARE_LINE_RE.search(s_clean) and not (has_code_file or has_md_file):
            hard.append((s, '写了行号但没写文件名'))
            continue

        # 提交号检查：显式说"commit/提交"但没附 hash
        # 整句有 git commit 命令 → 命令语境，跳过
        if not GIT_CMD_RE.search(s_clean):
            if COMMIT_TRIGGER.search(s_clean) and not HASH_RE.search(s_clean):
                hard.append((s, '提到 commit/提交但没附 7-40 位短 hash'))
                continue

        if has_md_file and not (has_line or has_section):
            soft.append((s, '引用文档但没写行号或章节'))

    return hard, soft


def check_semicolon(content):
    """检查分号（规则 31）。
    返回 [(行摘要,)]。
    """
    text = strip_markdown_structure(content)
    issues = []
    for line in text.splitlines():
        line = line.strip()
        if not line or '❌' in line:
            continue
        # 代码块里的分号不属于正文问题，strip_markdown_structure 已剥离
        if '；' in line or ';' in line:
            issues.append((line[:80],))
    return issues


NOMINALIZATION_PATTERN = re.compile(
    r'(进行|做出|予以|加以|开展|实施)\s*[一-龥A-Za-z]+'
)


def check_nominalization(content):
    """检查虚动词名词化（规则 32）。
    返回 [(句子, 模式)]。
    """
    sentences = split_sentences(content)
    findings = []
    for s in sentences:
        if '❌' in s:
            continue
        m = NOMINALIZATION_PATTERN.search(s)
        if m:
            findings.append((s[:80], m.group(0)))
    return findings


STRONG_VAGUE = ['可能', '大概', '也许', '或许', '好像', '似乎',
                '看起来', '想必', '不一定', '不太可能']
WEAK_VAGUE = ['最好', '可以考虑', '一些', '若干', '之类的', '类似的',
              '等等', '非常', '极其', '相当', '十分', '无比', '颇为']


def check_vague_words(content):
    """检查模糊词分级（规则 33）。
    强模糊词：出现 1 次即报。
    弱模糊词：同一段落 ≥3 个才报。
    例外一：明确标注的建议或推荐场景。
    例外二：同时写了条件与来源的真实不确定性。
    返回 (强模糊词问题列表, 弱模糊词问题列表)。
    """
    text = strip_markdown_structure(content)
    strong_issues = []
    weak_issues = []

    for line in text.splitlines():
        line = line.strip()
        if not line or '❌' in line:
            continue

        advice_context = '（建议' in line or '（推荐' in line
        has_source = bool(re.search(r'\[\d+\]', line))
        has_condition = bool(re.search(r'如果|当|若|在.{0,20}时', line))
        hedged_uncertainty = has_source and has_condition

        found_strong = [w for w in STRONG_VAGUE if w in line]
        if found_strong and not advice_context and not hedged_uncertainty:
            strong_issues.append((line[:80], found_strong))

        found_weak = [w for w in WEAK_VAGUE if w in line]
        if len(found_weak) >= 3 and not advice_context:
            weak_issues.append((line[:80], found_weak))

    return strong_issues, weak_issues


def load_term_alternatives():
    """从 DICT.md 中提取术语及其同义表达。

    DICT.md 中各张表的列数不一致，因此按表头定位"同义表达"列，
    不能假设固定的列序号。
    返回 {同义表达: 标准术语} 的字典。
    """
    dict_path = get_wiki_root() / 'schema' / 'DICT.md'
    if not dict_path.exists():
        return {}

    content = load_markdown_file(dict_path)
    alternatives = {}
    headers = None

    for raw in content.split('\n'):
        line = raw.strip()

        # 非表格行：结束当前表格
        if not line.startswith('|'):
            headers = None
            continue

        # 表格分隔行
        if re.fullmatch(r'\|[\s:\-|]+\|', line):
            continue

        cells = [c.strip() for c in line.split('|')[1:-1]]

        # 新表的表头
        if headers is None:
            headers = cells
            continue

        # 按表头定位同义表达列
        alt_idx = None
        for i, h in enumerate(headers):
            if '同义' in h:
                alt_idx = i
                break
        if alt_idx is None or len(cells) <= alt_idx:
            continue

        standard_term = cells[0]
        alt_text = cells[alt_idx]

        # 跳过表头残留与占位符
        if not standard_term or standard_term == '标准术语':
            continue
        if not alt_text or alt_text in ('-', '—'):
            continue

        for alt in re.split(r'[、，,]', alt_text):
            alt = alt.strip()
            if alt and alt != standard_term and len(alt) >= 2:
                alternatives[alt] = standard_term

    return alternatives


def check_term_consistency(content):
    """检查术语一致性。
    找出使用了非标准术语的地方。
    返回 [(sentence, non_standard_term, standard_term), ...]
    """
    alternatives = load_term_alternatives()
    if not alternatives:
        return []

    # 来源区是文献标题，属专有名词，不参与术语一致性检查
    body = re.split(r'\n## 来源', content, maxsplit=1)[0]
    sentences = split_sentences(body)
    findings = []

    for s in sentences:
        for alt, standard in alternatives.items():
            if alt not in s or standard in s:
                continue
            # 英文缩略词只在独立出现时才算命中，避免 ASD-STE100、text-embedding-3
            if re.search(r'[A-Za-z]', alt):
                pattern = r'(?<![A-Za-z0-9-])' + re.escape(alt) + r'(?![A-Za-z0-9-])'
                if not re.search(pattern, s, flags=re.IGNORECASE):
                    continue
            findings.append((s, alt, standard))
            break

    return findings


def check_missing_sources(content):
    """检测可能缺少来源标注的陈述。
    简单启发式：包含数字、百分比、研究表明等，但没有 [来源编号] 格式的引用。
    """
    sentences = split_sentences(content)
    suspicious = []

    # 可能表示事实陈述的关键词
    fact_keywords = ['表明', '显示', '证明', '发现', '达到', '提升', '降低',
                     '增加', '减少', '占', '约', '超过', '根据', '研究', '报告']

    for s in sentences:
        # 已经有来源标注
        if re.search(r'\[\d+\]', s) or re.search(r'\[[^\]]+\d+[^\]]*\]', s):
            continue

        # 包含数字或百分比 + 事实关键词
        has_number = bool(re.search(r'\d+%|\d+个|\d+种|\d+倍|\d+亿|\d+万', s))
        has_fact_kw = any(kw in s for kw in fact_keywords)

        if has_number and has_fact_kw:
            suspicious.append(s)
        elif has_fact_kw and len(s) > 20:
            suspicious.append(s)

    return suspicious[:10]  # 最多返回 10 条


def check_frontmatter(content, filepath):
    """检查页面是否有完整的 frontmatter。"""
    fm, body = parse_frontmatter(content)

    issues = []
    required_fields = ['name', 'category', 'updated']

    for field in required_fields:
        if field not in fm or not fm[field]:
            issues.append(f"缺少必填字段：{field}")

    if not body or len(body.strip()) < 50:
        issues.append("页面内容过短")

    return issues


def _page_keys(stem, fm):
    """生成一个页面可能被链接到时的全部候选名称。"""
    keys = {stem, stem.lower(), stem.lower().replace(' ', '-')}
    for field in ('name', 'title', 'name_en'):
        value = (fm.get(field) or '').strip()
        if value and value != '-':
            keys.add(value)
            keys.add(value.lower())
    return {k for k in keys if k}


def check_links():
    """检查双向链接。

    页面文件名是英文 slug，而双链里常用中文标题，因此必须同时用
    文件名和 frontmatter 的 name/title 建立索引，否则全部会判为孤立页。
    返回 (孤立页面列表, 断链列表)。
    """
    wiki_root = get_wiki_root() / 'wiki'
    root_index = get_wiki_root() / 'index.md'

    path_of_key = {}
    for md_file in wiki_root.rglob('*.md'):
        content = load_markdown_file(md_file)
        fm, _ = parse_frontmatter(content)
        rel_path = str(md_file.relative_to(wiki_root))
        for key in _page_keys(md_file.stem, fm):
            path_of_key.setdefault(key, rel_path)

    sources = list(wiki_root.rglob('*.md'))
    if root_index.exists():
        sources.append(root_index)

    inbound = defaultdict(set)
    broken = []

    for src in sources:
        content = load_markdown_file(src)
        # 代码块与行内代码里的 [[...]] 是示例，不是链接
        link_text = re.sub(r'```.*?```', '', content, flags=re.DOTALL)
        link_text = re.sub(r'`[^`\n]*`', '', link_text)
        if src == root_index:
            src_rel = str(root_index.relative_to(get_wiki_root()))
        else:
            src_rel = str(src.relative_to(wiki_root))

        for link in re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', link_text):
            target = link.strip().split('/')[-1]
            candidates = [target, target.lower(), target.lower().replace(' ', '-')]
            hit = next((path_of_key[c] for c in candidates if c in path_of_key), None)
            if hit is None:
                broken.append((src_rel, link.strip()))
            elif hit != src_rel:
                inbound[hit].add(src_rel)

    orphans = []
    for md_file in wiki_root.rglob('*.md'):
        rel_path = str(md_file.relative_to(wiki_root))
        if md_file.stem.lower() == 'index':
            continue
        if not inbound.get(rel_path):
            orphans.append(rel_path)

    return orphans, broken


def run_lint(check_type='all', max_sentence_length=25):
    """运行整理检查。"""
    wiki_root = get_wiki_root() / 'wiki'
    all_pages = list(wiki_root.rglob('*.md'))

    report = {
        'total_pages': len(all_pages),
        'long_sentences': [],
        'passive_voice': [],
        'term_issues': [],
        'missing_sources': [],
        'frontmatter_issues': [],
        'orphan_pages': [],
        'broken_links': [],
        'punctuation_issues': [],
        'dash_issues': [],
        'dash_stats': [],
        'status_issues': [],
        'lead_issues': [],
        'evidence_issues': [],
        'evidence_soft': [],
        'semicolon_issues': [],
        'nominalization_issues': [],
        'vague_strong': [],
        'vague_weak': [],
    }

    for page_path in all_pages:
        content = load_markdown_file(page_path)
        rel_path = str(page_path.relative_to(wiki_root))

        if check_type in ['all', 'long-sentences']:
            long_sents = check_long_sentences(content, max_sentence_length)
            for s, wc in long_sents:
                report['long_sentences'].append({
                    'page': rel_path,
                    'sentence': s[:80] + ('...' if len(s) > 80 else ''),
                    'word_count': wc
                })

        if check_type in ['all', 'passive']:
            passive = check_passive_voice(content)
            for s, pattern in passive:
                report['passive_voice'].append({
                    'page': rel_path,
                    'sentence': s[:80] + ('...' if len(s) > 80 else ''),
                    'pattern': pattern
                })

        if check_type in ['all', 'terms']:
            terms = check_term_consistency(content)
            for s, non_std, std in terms:
                report['term_issues'].append({
                    'page': rel_path,
                    'sentence': s[:80] + ('...' if len(s) > 80 else ''),
                    'non_standard': non_std,
                    'standard': std
                })

        if check_type in ['all', 'sources']:
            missing = check_missing_sources(content)
            for s in missing:
                report['missing_sources'].append({
                    'page': rel_path,
                    'sentence': s[:80] + ('...' if len(s) > 80 else ''),
                })

        if check_type in ['all', 'status']:
            for s, variant, fixed in check_status_words(content):
                report['status_issues'].append({
                    'page': rel_path,
                    'sentence': s[:80] + ('...' if len(s) > 80 else ''),
                    'variant': variant,
                    'fixed': fixed
                })

        if check_type in ['all', 'lead']:
            for s, marker in check_lead_sentence(content):
                report['lead_issues'].append({
                    'page': rel_path,
                    'sentence': s[:80] + ('...' if len(s) > 80 else ''),
                    'marker': marker
                })

        if check_type in ['all', 'evidence']:
            hard, soft = check_evidence(content)
            for s, issue in hard:
                report['evidence_issues'].append({
                    'page': rel_path,
                    'sentence': s[:80] + ('...' if len(s) > 80 else ''),
                    'issue': issue
                })
            for s, issue in soft:
                report['evidence_soft'].append({
                    'page': rel_path,
                    'sentence': s[:80] + ('...' if len(s) > 80 else ''),
                    'issue': issue
                })

        if check_type in ['all', 'semicolon']:
            for row in check_semicolon(content):
                report['semicolon_issues'].append({
                    'page': rel_path,
                    'line': row[0]
                })

        if check_type in ['all', 'nominalization']:
            for s, pattern in check_nominalization(content):
                report['nominalization_issues'].append({
                    'page': rel_path,
                    'sentence': s[:80],
                    'pattern': pattern
                })

        if check_type in ['all', 'vague']:
            strong, weak = check_vague_words(content)
            for line, words in strong:
                report['vague_strong'].append({
                    'page': rel_path,
                    'line': line,
                    'words': words
                })
            for line, words in weak:
                report['vague_weak'].append({
                    'page': rel_path,
                    'line': line,
                    'words': words
                })

        if check_type in ['all', 'punctuation']:
            for line in check_punctuation(content):
                report['punctuation_issues'].append({
                    'page': rel_path,
                    'line': line
                })

        if check_type in ['all', 'dashes']:
            for para, count in check_dash_density(content):
                report['dash_issues'].append({
                    'page': rel_path,
                    'paragraph': para,
                    'count': count
                })
            dashes, chars, per_k = check_dash_stats(content)
            report['dash_stats'].append({
                'page': rel_path,
                'dashes': dashes,
                'chars': chars,
                'per_k': per_k
            })

        if check_type in ['all', 'frontmatter']:
            fm_issues = check_frontmatter(content, rel_path)
            for issue in fm_issues:
                report['frontmatter_issues'].append({
                    'page': rel_path,
                    'issue': issue
                })

    if check_type in ['all', 'backlinks']:
        orphans, broken = check_links()
        report['orphan_pages'] = orphans
        report['broken_links'] = broken

    return report


def format_report(report):
    """格式化整理报告。"""
    output = f"""
{'='*60}
  🧹 简明表达规范库 整理报告
{'='*60}

  检查页面总数：{report['total_pages']}

{'─'*60}
"""

    # 长句
    n = len(report['long_sentences'])
    output += f"\n  📏 长句问题（超过阈值）：{n} 处\n"
    if n > 0:
        for item in report['long_sentences'][:5]:
            output += f"    • [{item['page']}] ({item['word_count']}字) {item['sentence']}\n"
        if n > 5:
            output += f"    ... 还有 {n-5} 处\n"
    else:
        output += "    ✅ 未发现明显长句问题\n"

    # 被动语态
    n = len(report['passive_voice'])
    output += f"\n  🔄 被动语态：{n} 处\n"
    if n > 0:
        for item in report['passive_voice'][:5]:
            output += f"    • [{item['page']}] [{item['pattern']}] {item['sentence']}\n"
        if n > 5:
            output += f"    ... 还有 {n-5} 处\n"
    else:
        output += "    ✅ 未发现明显被动语态\n"

    # 术语一致性
    n = len(report['term_issues'])
    output += f"\n  📖 术语不一致：{n} 处\n"
    if n > 0:
        for item in report['term_issues'][:5]:
            output += f"    • [{item['page']}] \"{item['non_standard']}\" → \"{item['standard']}\"\n"
        if n > 5:
            output += f"    ... 还有 {n-5} 处\n"
    else:
        output += "    ✅ 术语使用一致\n"

    # 缺少来源
    n = len(report['missing_sources'])
    output += f"\n  📚 可能缺少来源标注：{n} 处\n"
    if n > 0:
        for item in report['missing_sources'][:5]:
            output += f"    • [{item['page']}] {item['sentence']}\n"
        if n > 5:
            output += f"    ... 还有 {n-5} 处\n"
    else:
        output += "    ✅ 来源标注良好\n"

    # 标点
    n = len(report['punctuation_issues'])
    output += f"\n  ✏️  英文直引号：{n} 处\n"
    if n > 0:
        for item in report['punctuation_issues'][:5]:
            output += f"    • [{item['page']}] {item['line']}\n"
        if n > 5:
            output += f"    ... 还有 {n-5} 处\n"
    else:
        output += "    ✅ 中文标点使用正确\n"

    # 破折号
    n = len(report['dash_issues'])
    output += f"\n  🚧 破折号过密：{n} 处\n"
    if n > 0:
        for item in report['dash_issues'][:5]:
            output += f"    • [{item['page']}] ({item['count']} 处) {item['paragraph']}\n"
        if n > 5:
            output += f"    ... 还有 {n-5} 处\n"
    else:
        output += "    ✅ 破折号密度正常\n"

    # 破折号全篇密度（只作参考，不计入问题数）
    stats = report.get('dash_stats', [])
    if stats:
        total_d = sum(s['dashes'] for s in stats)
        total_c = sum(s['chars'] for s in stats)
        overall = round(total_d / total_c * 1000, 1) if total_c else 0.0
        output += (f"    📈 全篇密度：{total_d} 处 / {total_c} 字，"
                   f"每千字 {overall} 处（参考值 ≤ 3）\n")
        for s in stats:
            if s['per_k'] > 3:
                output += f"    ⚠️  [{s['page']}] 每千字 {s['per_k']} 处\n"

    # 非固定状态词
    n = len(report.get('status_issues', []))
    output += f"\n  🔖 非固定状态词：{n} 处\n"
    if n > 0:
        for item in report['status_issues'][:5]:
            output += (f"    • [{item['page']}] \"{item['variant']}\" → "
                       f"\"{item['fixed']}\" {item['sentence']}\n")
        if n > 5:
            output += f"    ... 还有 {n-5} 处\n"
    else:
        output += "    ✅ 状态词使用规范\n"

    # 首句过程叙述
    n = len(report.get('lead_issues', []))
    output += f"\n  🥇 首句疑似过程叙述：{n} 处\n"
    if n > 0:
        for item in report['lead_issues'][:5]:
            output += f"    • [{item['page']}] [{item['marker']}] {item['sentence']}\n"
    else:
        output += "    ✅ 首句都是结论\n"

    # 证据可定位
    n = len(report.get('evidence_issues', []))
    output += f"\n  📍 证据不可定位：{n} 处\n"
    if n > 0:
        for item in report['evidence_issues'][:5]:
            output += f"    • [{item['page']}] {item['issue']}：{item['sentence']}\n"
        if n > 5:
            output += f"    ... 还有 {n-5} 处\n"
    else:
        output += "    ✅ 证据都能定位\n"
    soft = report.get('evidence_soft', [])
    if soft:
        output += f"    ℹ️  另有 {len(soft)} 处引用文档未写行号或章节（不计入问题数）\n"

    # 禁用分号
    n = len(report.get('semicolon_issues', []))
    output += f"\n  ✂️  禁用分号：{n} 处\n"
    if n > 0:
        for item in report['semicolon_issues'][:5]:
            output += f"    • [{item['page']}] {item['line']}\n"
    else:
        output += "    ✅ 正文无分号\n"

    # 虚动词名词化
    n = len(report.get('nominalization_issues', []))
    output += f"\n  🧩 虚动词名词化：{n} 处\n"
    if n > 0:
        for item in report['nominalization_issues'][:5]:
            output += f"    • [{item['page']}] ({item['pattern']}) {item['sentence']}\n"
    else:
        output += "    ✅ 动作词使用明确\n"

    # 模糊词
    strong = report.get('vague_strong', [])
    weak = report.get('vague_weak', [])
    n = len(strong)
    output += f"\n  🌫️  模糊词（强）：{n} 处\n"
    if n > 0:
        for item in strong[:5]:
            output += f"    • [{item['page']}] {', '.join(item['words'])} — {item['line']}\n"
    else:
        output += "    ✅ 无强模糊词\n"
    if weak:
        output += f"    ℹ️  另有 {len(weak)} 处弱模糊词段落（≥3 个/段，不计入问题数）\n"

    # frontmatter
    n = len(report['frontmatter_issues'])
    output += f"\n  📋 Frontmatter 问题：{n} 处\n"
    if n > 0:
        for item in report['frontmatter_issues'][:5]:
            output += f"    • [{item['page']}] {item['issue']}\n"
    else:
        output += "    ✅ 所有页面 frontmatter 完整\n"

    # 孤立页面
    n = len(report['orphan_pages'])
    output += f"\n  🏝️  孤立页面（无入站链接）：{n} 个\n"
    if n > 0:
        for page in report['orphan_pages'][:5]:
            output += f"    • {page}\n"
        if n > 5:
            output += f"    ... 还有 {n-5} 个\n"
    else:
        output += "    ✅ 所有页面都有入站链接\n"

    # 断链
    n = len(report['broken_links'])
    output += f"\n  🔗 断链（双链指向不存在的页面）：{n} 处\n"
    if n > 0:
        for src, link in report['broken_links'][:10]:
            output += f"    • [{src}] → [[{link}]]\n"
        if n > 10:
            output += f"    ... 还有 {n-10} 处\n"
    else:
        output += "    ✅ 所有双链都能解析\n"

    # 总结
    total_issues = (
        len(report['long_sentences']) +
        len(report['passive_voice']) +
        len(report['term_issues']) +
        len(report['missing_sources']) +
        len(report['punctuation_issues']) +
        len(report['dash_issues']) +
        len(report['frontmatter_issues']) +
        len(report['broken_links']) +
        len(report.get('status_issues', [])) +
        len(report.get('lead_issues', [])) +
        len(report.get('evidence_issues', [])) +
        len(report.get('semicolon_issues', [])) +
        len(report.get('nominalization_issues', [])) +
        len(report.get('vague_strong', []))
    )

    output += f"""
{'─'*60}
  📊 总问题数：{total_issues}
"""

    if total_issues == 0:
        output += "  🎉 太棒了！Wiki 状态良好，完全符合简明表达规范。\n"
    elif total_issues < 5:
        output += "  🙂 状态不错，只有少量问题需要修复。\n"
    elif total_issues < 20:
        output += "  🤔 有一些问题，建议安排一次整理。\n"
    else:
        output += "  ⚠️  问题较多，建议进行全面整理。\n"

    output += f"{'='*60}\n"
    return output


def main():
    parser = argparse.ArgumentParser(description='简明表达规范库 整理工具')
    parser.add_argument('--check', default='all',
                        choices=['all', 'long-sentences', 'passive',
                                 'terms', 'sources', 'punctuation', 'dashes',
                                 'status', 'lead', 'evidence',
                                 'semicolon', 'nominalization', 'vague',
                                 'frontmatter', 'backlinks'],
                        help='检查类型（默认 all）')
    parser.add_argument('--max-length', type=int, default=25,
                        help='长句阈值（字/词数，默认 25）')
    parser.add_argument('--compare', nargs=2, metavar=('原稿', '改写稿'),
                        help='比较两版文本的信息点，检查改写是否删了信息')
    args = parser.parse_args()

    if args.compare:
        old_path, new_path = (Path(p) for p in args.compare)
        for p in (old_path, new_path):
            if not p.exists():
                print(f"❌ 文件不存在：{p}")
                sys.exit(1)
        print(format_compare(
            old_path, new_path,
            load_markdown_file(old_path), load_markdown_file(new_path)
        ))
        return

    print(f"\n🧹 简明表达规范库 整理工具")
    print(f"   检查类型: {args.check}")
    print(f"   长句阈值: {args.max_length} 字/词")
    print()

    report = run_lint(check_type=args.check, max_sentence_length=args.max_length)
    print(format_report(report))


if __name__ == '__main__':
    main()
