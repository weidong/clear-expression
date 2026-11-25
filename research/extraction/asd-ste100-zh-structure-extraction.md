# ASD-STE100 中文材料结构化提取

> 分析对象（只读，未改动）：
> - [asd-ste100-writing-rules.zh-CN.md](reference/ste100/03_中文翻译/zh-translation/asd-ste100-writing-rules.zh-CN.md)（3091 行，9 节 53 条规则 + 8 条一般建议）
> - [asd-ste100-selected-dictionary.zh-CN.md](reference/ste100/03_中文翻译/zh-translation/asd-ste100-selected-dictionary.zh-CN.md)（208 行，编者选编，非逐条翻译）
> - [highlights.md](reference/ste100/02_英文提取版/ste100-markdown/front-matter/highlights.md)（Issue 9 相对旧版的全部变更清单）
> - [general-introduction.md](reference/ste100/02_英文提取版/ste100-markdown/front-matter/general-introduction.md)（定位、用途、边界）
> - [dictionary-introduction.md](reference/ste100/02_英文提取版/ste100-markdown/part2-dictionary/dictionary-introduction.md)（词典导言，本报告第二部分的骨架）
> - [sample-entries.md](reference/ste100/02_英文提取版/ste100-markdown/part2-dictionary/sample-entries.md)（A 与 W–Y 各 5 页词条实样）
>
> 标注约定：凡引号内英文/中文原句均为材料原文；凡"（分析）"字样为提取者的判断，不是原文。

---

## 一、中文版规则总览

材料自述："The writing rules (part 1) have 9 sections that contain 53 rules."（general-introduction）中文版与之一致：第 1–9 节共 14+2+7+5+5+6+3+7+4 = **53 条**，另有 8 条"一般建议（GR）"，材料明确说明 GR "不是 STE 规则"。

### 第 1 节 词汇（14 条）

| 编号 | 一句话概括 |
|---|---|
| 1.1 | 只能使用三类词：词典批准词、技术名词、技术动词。 |
| 1.2 | 批准词只能按词典标注的词性使用。 |
| 1.3 | 只能使用批准词在词典中给出的那个批准词义。 |
| 1.4 | 动词、形容词只能用词典列出的形式（含比较级/最高级）。 |
| 1.5 | 可把词归入 22 类技术名词后自由使用。 |
| 1.6 | 未批准词只有在充当技术名词或其组成部分时才允许使用。 |
| 1.7 | 技术名词不得当动词用（只能作名词或另一技术名词的修饰语）。 |
| 1.8 | 优先采用公司、行业或专业领域已批准的技术名词。 |
| 1.9 | 没有现成批准词时，自选技术名词须简短（≤3 词）且易懂。 |
| 1.10 | 不得用地域词、俚语、行话充当技术名词。 |
| 1.11 | 同一物品全文只用一个技术名词。 |
| 1.12 | 可把动词归入 4 类技术动词后使用，但须服从动词全部规则。 |
| 1.13 | 技术动词不得当名词用（过去分词可作形容词）。 |
| 1.14 | 用美式拼写，除非其他官方文件另有规定。 |

### 第 2 节 多词名词（2 条）

| 编号 | 一句话概括 |
|---|---|
| 2.1 | 多词名词不超过三个词，超长就用介词拆开。 |
| 2.2 | 超过三词的技术名词首次全写，之后用"较短形式"或"连字符成组"两种方法之一。 |

### 第 3 节 动词（7 条）

| 编号 | 一句话概括 |
|---|---|
| 3.1 | 只能用词典给出的动词形式。 |
| 3.2 | 只允许六种形式/时态：不定式、祈使式、一般现在、一般过去、一般将来、过去分词（作形容词）。 |
| 3.3 | 过去分词作形容词表示状态，不是被动语态；词典未收的过去分词不得使用。 |
| 3.4 | 不得用助动词堆出完成时、进行时、复杂被动等结构。 |
| 3.5 | "-ing" 形式只能作技术名词或技术名词中的修饰语。 |
| 3.6 | 用主动语态；描述性写作中仅当施动者不明时才可用被动。 |
| 3.7 | 动作用批准动词表达，不要名词化（indication→shows，removal→remove）。 |

### 第 4 节 句子（5 条）

| 编号 | 一句话概括 |
|---|---|
| 4.1 | 写简短清晰的句子，一句一个主题。 |
| 4.2 | 不得为求短而省略名词、动词、主语、冠词，或使用缩略形式。 |
| 4.3 | 复杂内容改垂直列表，并遵守首字母大写、末尾标点等 8 项格式要求。 |
| 4.4 | 用连接词/连接短语（and、but、then、thus、as a result）衔接相关句子。 |
| 4.5 | 名词或多词名词前按需加冠词或指示形容词（the/a/an、this/these）。 |

### 第 5 节 程序性写作（5 条）

| 编号 | 一句话概括 |
|---|---|
| 5.1 | 程序句每句最多 20 词（注释不受此限，注释上限 25 词）。 |
| 5.2 | 一句只写一条指令，除非两个以上动作同时发生。 |
| 5.3 | 指令用祈使形式；除安全或重要条件外不要加 must。 |
| 5.4 | 先决条件写在句首，用逗号与命令分开。 |
| 5.5 | 注释只提供信息，不得含指令、要求、限制或公差。 |

### 第 6 节 描述性写作（6 条）

| 编号 | 一句话概括 |
|---|---|
| 6.1 | 逐步给信息，一句一个主语。 |
| 6.2 | 用关键词和关键短语建立逻辑结构，且不得中途换词。 |
| 6.3 | 描述句每句最多 25 词。 |
| 6.4 | 用段落组织相关信息，段首写主题句。 |
| 6.5 | 一段只有一个主题。 |
| 6.6 | 一段不超过六个句子。 |

### 第 7 节 安全说明（3 条）

| 编号 | 一句话概括 |
|---|---|
| 7.1 | 用"警告/小心"等词或符号标明风险等级：warning=伤亡，caution=损坏，两者并存取 warning。 |
| 7.2 | 以清晰准确的命令或条件开头。 |
| 7.3 | 必须给出解释，说明违反后的风险或后果。 |

### 第 8 节 标点与词数（7 条）

| 编号 | 一句话概括 |
|---|---|
| 8.1 | 标准英语标点均可用，唯独分号（;）不许用。 |
| 8.2 | 用连字符连接直接相关的词（5 类情形）。 |
| 8.3 | 括号只用于 7 种用途：引图引文、项号、步骤号、缩写、单复数、解释、替代方案。 |
| 8.4 | 垂直列表中的冒号作用等同句号，冒号前与每一项各自受 20/25 词限制。 |
| 8.5 | 括号内文字在整句中算一个词，但括号内另成一句并单独计词。 |
| 8.6 | 数字、数字+单位、缩写、字母数字标识符、引用文本、标题/标牌/标签文字、专有名词各算一个词。 |
| 8.7 | 带连字符的词（组）算一个词。 |

### 第 9 节 写作实践（4 条 + 8 条 GR）

| 编号 | 一句话概括 |
|---|---|
| 9.1 | 逐词替换不成立时，必须改写句子结构（四种动因、若干示范）。 |
| 9.2 | 每个批准词都要按批准词义、批准词性用在正确语境（wear=磨损、extend=增大、see=看见、turn=绕轴转）。 |
| 9.3 | 不得把两个批准词临时拼成短语动词（put out→extinguish，give off→release）。 |
| 9.4 | 同类工作步骤的术语与措辞全文保持一致。 |
| GR-1 | 尽量补出连词 that，划清主从句边界，也便于翻译。 |
| GR-2 | 介词 with 有三个批准含义，易生歧义，写完要复读。 |
| GR-3 | 代词必须有唯一先行词，否则换回名词。 |
| GR-4 | 代词 this 指代不明时，重述语境。 |
| GR-5 | 警惕假朋友（形近义异词）。 |
| GR-6 | 不用 e.g./i.e./etc. 等拉丁缩写，改用英语词或直接省略。 |
| GR-7 | 用性别中立语言；he/she、man/woman 除医学等必要语境外不允许。 |
| GR-8 | 所有格允许但要确保正确，不确定就别用。 |

> 版本注记（highlights）：Issue 9 把原 2.3 移入第 4 节成为 4.5；新增 7.1 类目 21（法律与法规）、22（动植物）；GR-7、GR-8 为新增；"technical name" 全面改称 "technical noun"。

---

## 二、词典部分怎么用

### 2.1 一个词条里有哪些字段，各自干什么

词典导言原文："The dictionary has four columns that give this information"。四栏之外还有三类附属信息（词形串、括号缩略、help 符号）。

| 位置/字段 | 原文名称 | 内容与样子 | 用途（对应规则） |
|---|---|---|---|
| 栏 1 抬头 | Word (part of speech) | `AID (n)`、`REMOVE (v)`、`ABRASIVE (adj)` | 只允许按此词性使用；这是 1.2 的执法依据。 |
| 栏 1 动词形式串 | （无专名，紧随词头） | `REMOVE (v), REMOVES, REMOVED, REMOVED`；`GIVE (v), GIVES, GAVE, GIVEN` | 依次为不定式/祈使、一般现在时、一般过去时、过去分词；未列出的形式不得使用（3.1–3.3）。 |
| 栏 1 形式封条 | `No other verb forms.` | 见于 `BE (v), IS, WAS (also ARE, WERE)`、`CAN (v), CAN, COULD`、`WILL (v)` | 明确封死其他形式（3.4 的依据）。 |
| 栏 1 形容词括号 | comparative / superlative | `SLOW (adj) (SLOWER, SLOWEST)` | 给出比较级、最高级；靠 more/most 构成的词不列，因为 more/most 本身是批准词。 |
| 栏 1 名词数 | singular only | 名词只给单数，可数名词复数默认允许（除非 help 另有说明） | 决定能否写复数。 |
| 栏 1 `(TN)` / `(TV)` | technical noun / technical verb | 只出现在**栏 2 的替代词位置**，如 `abnormality (n) → DEFECT (TN)`、`uncovered (v) → COVER (TN)` | 说明"这个替代词不是批准词，而是技术名词/技术动词"；栏 1 本身不收技术名词、技术动词。 |
| 栏 2 | Approved meaning / ALTERNATIVES | 批准词→英文释义；非批准词→全大写替代词，可为词、短语、TN/TV | 批准词用来锁定"唯一词义"（1.3）；非批准词用来找替换路径（1.2、9.1）。 |
| 栏 2 子项 | `For other meanings, use:` | 见 `ABOUT (prep)`、`ABOVE (prep)` | 该词只批准了一个含义，其他含义必须换词（ABOUT→APPROXIMATELY/AROUND；ABOVE→MORE THAN）。 |
| 栏 3 | STE EXAMPLE | 全大写（或正常大小写）的合规示范，如 `DRAIN APPROXIMATELY 2 LITERS OF FUEL FROM THE TANK.` | 示范"批准词怎么用""替代词怎么逐词换""换结构后怎么保持同义"；示例措辞只是建议，不是唯一写法。 |
| 栏 4 | Non-STE example | 标准技术英语里的错误写法，如 `The accuracy of the adjustment can vary.` | 对照理解"错在哪"；一个反例里可能同时含多个未批准词或不允许的结构。 |
| 附加 | help（灯泡符号） | 四类：①使用建议 ②受限含义 ③仅限某一语境 ④关于该词（含未批准词）的重要信息 | 例：`PUSH (v)` 的 help 要求"Use this word together with a preposition or an adverb to show direction"；`SWALLOW (v)` 的 help 说"Use this word for safety instructions only"。 |
| 不收录 | — | 反义词（"A dictionary entry does not include antonyms"）、技术名词、技术动词、缩写规则、格式、计量单位 | 别在词典里找反义词或找格式答案。 |

其他硬约定：
- 全大写 = 可用（approved）；全小写 = 不可用（not approved），"To replace this word in a text, you must use a different word or a different sentence construction."
- 拼写与标点按美式，依据 Merriam-Webster。
- 词性缩写共 8 类，材料列出并解释了 7 项：noun (n)、verb (v)、adjective (adj)、adverb (adv)、article (art)、preposition (prep)、conjunction (conj)；**第 5 项（代词 pron）在提取文本中缺失**，但词条里确有 `YOU (pron)`、`yourself (pron)`，可反证该类存在。
- 词典导言提到"如不确定用词，参见本流程图"，但**流程图本身未出现在提取文本中**（原文只有一句指引）。

### 2.2 "批准词"与"非批准词"的判定逻辑

判定链（综合 general-introduction、词典导言、规则 1.2/1.3/9.1）：

1. **先看字体**：大写→批准；小写→不批准。这是词典层面的第一道闸。
2. **再核词性**：批准词只批准一个词性（少数例外如 clean、flush 同时批准动词与形容词）。词性不符即违规，哪怕词义对。
3. **再核词义**：批准词通常只有一个批准词义；"If a meaning is not given in the dictionary, you cannot use the word with a meaning that is not approved"。同义词只保留一个（STE 用 start，不用 begin/commence/initiate/originate）。
4. **非批准词的处理顺序**：查栏 2 → 有同词性替代词就逐词替换 → 词性不同或无合适替代就改写句子结构 → 仍不行则回英语词典确认词义，再选批准词或重组句子 → 每次替换后复核句义未变。
5. **不在词典中的词**：若属于技术名词/技术动词类别（1.5/1.12）则可用；否则按"英语词典查义→找批准同义词→重组句子"处理。
6. **替代词只是建议**："These alternatives ... are only suggestions to help you." 同一非批准词常给多个替代（acceptable→PERMITTED / SATISFACTORY / SERVICEABLE），按语境选。
7. **词形陷阱优先于词义**：test、work、help、damage、check 都是"某个词性批准、另一个词性不批准"的高频坑（详见第五部分）。
8. **官方还提供"最常见错误表"**（词典导言末），把 40 余组 non-STE→STE 直接列出，可当快速判定表用。

一个词条的判定实例（sample-entries 原文）：

```
main (adj)  PRIMARY (adj)
STE:     THE PRIMARY CAUSE OF VALVE FAILURE IS CONTAMINATION OF THE FLUID.
Non-STE: The main cause of valve failure is contamination of the fluid.
```

即：main 未批准 → 栏 2 给同词性替代 PRIMARY → 栏 3 示范逐词替换 → 栏 4 保留原错句供对照。

### 2.3 技术名词与技术动词怎么界定、怎么用

**定义（1.1，与 ISO 1087:2019 对齐）**

- 技术名词 = "a noun term that refers to a specified concept and is applicable to a subject field"（中文版："特定概念的名词术语，适用于某个专业领域"）。
- 技术动词 = "a verb term that also refers to a specified concept or process and is applicable to a subject field"。
- 词典不收它们，原因是"数量太多，且每个专业领域使用不同的技术名词/动词"；来源是公司术语表、术语数据库、官方零部件信息、工程图纸、图解零件目录。
- Issue 9 用 technical noun 全面取代旧称 technical name（highlights）。

**技术名词的 22 个类别**（能归入其一即可用）：
1 官方零部件信息；2 车辆/机器及其部位；3 工具与保障设备及其部件；4 材料、消耗品与多余物；5 设施、基础设施与物流程序；6 系统、组件、电路及其功能/配置/部件；7 数学、科学、工程术语与公式；8 导航与地理术语；9 数字、计量单位与时间（含符号）；10 引用文本（标牌、标签、显示文字）；11 专业角色、个人、团体、组织与地缘政治实体；12 身体部位；13 个人物品、食品饮料；14 医学术语；15 官方文件、文档组成部分、标准与指南；16 环境与运行条件；17 颜色；18 损伤术语；19 计算机科学、信息与通信技术；20 民用与军事运营；21 法律与法规；22 动物、植物及其他生命形式。
（类别 17 有专门 help：颜色是形容词，但 STE 归为技术名词，且不允许 blacker/the reddest 这类比较级。）

**技术动词的 4 个类别**：
1 制造工艺（a 去除材料 drill/grind/mill/ream/unsolder；b 添加材料；c 连接材料；d 改变机械强度/结构/物理性质；e 改变表面光洁度；f 改变形状）；
2 计算机流程与应用（a 输入输出；b 界面与应用流程；c 系统操作）；
3 适用专业领域（a 工程数学科学；b 医学；c 民用军事运营；d 导航；e 汽车铁路；f 能源石油天然气）；
4 法律与法规（仅用于合同、保修、证书、标准规范、法律文件）。

**使用条件（1.5–1.11、1.12–1.13）**

- 必须能归入类别；优先用公司/行业/领域**已批准**的技术名词（1.8）；没有批准词时自选，但要"简短（不超过三个词）且易于理解"（1.9）。
- 不得用地域性词、俚语、行话（1.10：choker、brick、gear 三个反例）。
- 同一物品全文一个名称（1.11：servo control unit / actuator / control unit 混用属违规）。
- 技术名词只能作名词，或作另一技术名词中的形容词性修饰语；**不得作动词**（1.7：oil→apply oil to；snow→snow will fall；clamp/grease/wire→put clamps on / apply grease to / attach ... with wire）。
- 技术动词只能作动词；**不得作名词**（1.13：0.20-inch ream → ream the hole to a 0.20-inch dimension）；过去分词可作形容词，且此时往往构成技术名词（`Lubricate the reamed hole.`）。
- 一词可"两栖"，取决于语境：drill 可作技术名词（类别 3）也可作技术动词（类别 1a）；plate 可作技术名词（类别 1）也可作技术动词（类别 1c）。判定看它在句中的功能，不看拼写。

**优先级（1.12 正文，很重要）**

1. 有批准动词能准确表达该指令/信息 → **用批准动词，不用技术动词**。
2. 能只用批准词写出同句 → 不用技术动词。
3. 必须用时，选语境精确的技术动词，不选笼统词：`Machine the hole...` → `Ream the hole...`。
4. 技术动词也必须服从第 3 节全部动词规则（形式、时态、语态、-ing 限制）。
5. 同一词形若词典已判"技术名词"，就不得再当技术动词用（clamp、grease、wire 三例）。

**TN/TV 与词典的接口**：栏 2 用 `(TN)`/`(TV)` 标注"这个替代词属于技术名词/技术动词"，例如 `uncovered (v) → COVER (TN)`（"DO NOT PUT A COVER ON THE CONTAINER."）、`abnormality (n) → DEFECT (TN)`（"EXAMINE THE SEAL FOR DEFECTS."）、`zero (v) → ZERO (TN)`（"ADJUST THE METER TO ZERO."）。这说明：非批准词不一定只能换成批准词，也可能换成技术名词/技术动词，但换过去后要按 1.5–1.13 的规则使用。

### 2.4 词典给出的替换关系（非批准词 → 批准词）

以下 36 组全部出自 dictionary-introduction 的"最常见错误表"与 sample-entries 的实际词条，例句为原文原样（大写为 STE 示范，小写为 Non-STE 反例）。

| # | 非批准词（词性） | 批准替代 | 原文示例 / 依据 |
|---|---|---|---|
| 1 | acceptable (adj) | PERMITTED (adj) / SATISFACTORY (adj) / SERVICEABLE (adj) | `A VALUE OF 2 mm IS PERMITTED.` ← `A value of 2 mm is acceptable.` |
| 2 | accuracy (n) | PRECISION (n) | `THE PRECISION OF THE ADJUSTMENT CAN CHANGE.` |
| 3 | alternate (adj) | ALTERNATIVE (adj) | 常见错误表 |
| 4 | any (adj) | None，或改写句子 | 常见错误表 |
| 5 | avoid (v) | PREVENT (v) | 常见错误表 |
| 6 | both (adj) | THE TWO (TN) | 常见错误表 |
| 7 | check (v) | CHECK (n) | 常见错误表（`Do a check of the laptop battery.`） |
| 8 | cover (v) | COVER (TN) | 常见错误表 |
| 9 | complete (adj) | COMPLETED (adj) | 常见错误表 |
| 10 | damage (v) | DAMAGE (n) | 常见错误表 |
| 11 | ensure (v) | MAKE SURE (v) | 常见错误表 |
| 12 | fit (v) | INSTALL (v) | 常见错误表 |
| 13 | follow (v) | OBEY (v) | 常见错误表 + 规则 1.3 例句 `OBEY THE SAFETY INSTRUCTIONS.` |
| 14 | further (adj) | MORE (adj) | 常见错误表 |
| 15 | further (adv) | MORE (adv) | 常见错误表 |
| 16 | have to (v) | 改用祈使形式的实义动词 | 常见错误表 |
| 17 | however (adv) | BUT (conj) | 常见错误表 |
| 18 | insert (v) | PUT (v) | 常见错误表 |
| 19 | main (adj) | PRIMARY (adj) | `THE PRIMARY CAUSE OF VALVE FAILURE IS...` |
| 20 | may (v) | CAN (v) | 常见错误表 |
| 21 | need (v) | NECESSARY (adj) | 常见错误表 |
| 22 | now (adv) | AT THIS TIME | 常见错误表 |
| 23 | old (adj) | REMAINING (adj) / USED (adj) / EXPIRED (adj) | 常见错误表 |
| 24 | over (prep) | ABOVE (prep) / ON (prep) / ALONG (prep) | 常见错误表 |
| 25 | people (n) | PERSON (n) / PERSONNEL (n) | 常见错误表 |
| 26 | perform (v) | DO (v) | 常见错误表 |
| 27 | portion (n) | PART (n) | 常见错误表 |
| 28 | press (v) | PUSH (v) | 常见错误表 |
| 29 | reach (v) | GET (v) | 常见错误表 |
| 30 | repeat (v) | DO (v) … AGAIN | 常见错误表 |
| 31 | required (v) | NECESSARY (adj) | 常见错误表 |
| 32 | rotate (v) | TURN (v) | 常见错误表 |
| 33 | secure (v) | ATTACH (v) / SAFETY (v) | 常见错误表 |
| 34 | shall (v) | MUST (v) | 常见错误表 |
| 35 | should (v) | MUST (v) | 常见错误表 |
| 36 | since (conj) | BECAUSE (conj) | 常见错误表 |
| 37 | test (v) | TEST (n) | 常见错误表（`Do the leak test.`） |
| 38 | therefore (adv) | THUS (adv) / AS A RESULT | 常见错误表 |
| 39 | under (prep) | BELOW (prep) / IN (prep) / LESS THAN | 常见错误表 |
| 40 | using (v) | USE (v) / WITH (prep) | 常见错误表 |
| 41 | abaft (prep) | AFT OF (prep) | `THE CONTROL UNIT IS INSTALLED AFT OF THE FLIGHT COMPARTMENT.` |
| 42 | abandon (v) | GO (v) / STOP (v) | `IF THERE IS A FIRE, IMMEDIATELY GO TO A SAFE AREA.` |
| 43 | abate (v) | DECREASE (v) | `WHEN THE WIND SPEED DECREASES TO LESS THAN 30 KNOTS...` |
| 44 | ability (n) | CAN (v) | `ONE GENERATOR CAN SUPPLY POWER FOR ALL THE SYSTEMS.` |
| 45 | able (adj) | CAN (v) | `IF YOU CAN START THE ENGINE, DO THE APPLICABLE TESTS.` |
| 46 | abnormal (adj) | UNUSUAL (adj) / INCORRECT (adj) | `LISTEN FOR UNUSUAL NOISES.` |
| 47 | abnormality (n) | DEFECT (TN) | `EXAMINE THE SEAL FOR DEFECTS.` |
| 48 | abrupt (adj) | SUDDEN (adj) / SUDDENLY (adv) | `THE DAMPER PREVENTS SUDDEN MOVEMENT OF THE CONTROL.` |
| 49 | absent (adj) | MISSING (adj) / NO (adj) | `IF ONE OR MORE BLADES ARE MISSING...` |
| 50 | absolutely (adv) | FULLY (adv) | `MAKE SURE THAT THE LATCH IS FULLY ENGAGED.` |
| 51 | absorption (n) | ABSORB (v) | `MEASURE THE TIME THAT IS NECESSARY FOR THE SILICA GEL TO ABSORB THE MOISTURE.` |
| 52 | abundant (adj) | LARGE (adj) | `CLEAN YOUR SKIN WITH A LARGE QUANTITY OF CLEAN WATER.` |
| 53 | accelerate (v) | INCREASE (v) / FASTER (adj) | `A HIGHER TEMPERATURE INCREASES THE SPEED OF EVAPORATION.` |
| 54 | acceptance (n) | ACCEPT (v) | `BEFORE YOU ACCEPT THE UNIT, DO THE SPECIFIED TEST PROCEDURE.` |
| 55 | accessible (adj) | ACCESS (n) | `GET ACCESS TO THE ACCUMULATOR FOR THE No. 1 HYDRAULIC SYSTEM.` |
| 56 | accommodate (v) | LET (v) | `DIFFERENT LENGTHS OF STUDS LET YOU ATTACH DIFFERENT THICKNESSES OF SKIN.` |
| 57 | accomplish (v) | DO (v) / COMPLETE (v) | `DO THIS TASK FIRST.` |
| 58 | according to (prep) | REFER (v) | `TO CALIBRATE THE TEST SET, REFER TO THE MANUFACTURER'S INSTRUCTIONS.` |
| 59 | account for (v) | MAKE SURE (v) | `MAKE SURE THAT YOU REMOVE ALL TOOLS AND EQUIPMENT.` |
| 60 | accumulate (v) | COLLECT (v) | `IF WATER COLLECTS IN THE FILLER LINE, DRAIN IT.` |
| 61 | accumulation (n) | QUANTITY (n) / COLLECT (v) | `REMOVE LARGE QUANTITIES OF CONTAMINATION.` |
| 62 | withdraw (v) | REMOVE (v) | `REMOVE THE INDICATOR FROM THE INSTRUMENT PANEL.` |
| 63 | within (prep) | IN (prep) / IN ... OR LESS / IN LESS THAN | `LIGHT L4 COMES ON IN 5 SECONDS OR LESS.` |
| 64 | withstand (v) | RESISTANT (adj) | `THIS MATERIAL IS RESISTANT TO FIRE.` |
| 65 | work (v) | WORK (n) | `BE CAREFUL WHEN YOU DO WORK NEAR FUEL TANKS.` |
| 66 | would (v) | CAN (v) | `SOLVENTS THAT STAY ON THE PART CAN CAUSE CORROSION.` |
| 67 | wrong (adj) | INCORRECT (adj) | `THESE MARKS WILL PREVENT AN INCORRECT INSTALLATION.` |
| 68 | wrongly (adv) | INCORRECTLY (adv) | `IF THE HOSES ARE INCORRECTLY INSTALLED, DAMAGE CAN OCCUR.` |
| 69 | yet (conj) | BUT (conj) | `TIGHTEN THE NUTS, BUT KEEP THEM SUFFICIENTLY LOOSE...` |
| 70 | yet (adv) | AT THIS TIME | `DO NOT REMOVE THE FIXTURE COVER AT THIS TIME.` |
| 71 | yourself (pron) | YOU (pron) | `DO NOT USE YOUR HANDS TO PREVENT MOVEMENT OF THE LP COMPRESSOR.` |
| 72 | zero (v) | ZERO (TN) | `ADJUST THE METER TO ZERO.` |
| 73 | uncovered (v) | COVER (TN) | `DO NOT PUT A COVER ON THE CONTAINER.` |
| 74 | simultaneously (adv) | AT THE SAME TIME | `DO THESE TWO STEPS AT THE SAME TIME.` |
| 75 | maintain (v) | KEEP (v) / HOLD (v) / MAINTENANCE (n) | `KEEP THE FLUID TEMPERATURE AT 70 °F.` |
| 76 | manufacture (v) | MAKE (v) | `YOU CAN MAKE THE CLEARING TOOL LOCALLY.` |
| 77 | addition (n) | ADD (v) | `ADD SPECIAL SHIMS, AS NECESSARY.` |
| 78 | briskly (adv) | QUICKLY (adv) | `RUB THE SURFACE QUICKLY WITH A SOFT, DRY CLOTH.` |
| 79 | build (v) | ASSEMBLE (v) | `ASSEMBLE THE UNIT.` |

> 注意三点（分析）：①同一条目常给多个替代词，选择权在语境；②替代词未必同词性（ability→CAN、able→CAN、withstand→RESISTANT），此时必须改句子结构而不是逐词换；③部分条目会写 `None` 或"Frequently, an alternative for this word is not necessary."（如 already），即"这个词根本不必出现"。

---

## 三、中文翻译暴露的适配问题

总判断：**英文原版与中文版都没有给出"用中文写作时怎么套用"的任何说明**。general-introduction 的定位是"write technical documentation"的受控英语，全部示例、词数、词性、形态都以英语为对象；中文版是逐节直译，未加译者注、未作本土化改写。以下问题按"是否可直接套用"分级列出。

### 3.1 完全无法直接套用（英语形态依赖）

1. **词数上限（5.1 的 20 词、6.3 的 25 词、5.5 注释 25 词；8.4–8.7 的计词规则）**
   汉语没有词边界，无法用空格切词，"每句最多 20 个词"在中文里没有可操作口径。中文版的所有词数示范都只对英文原句计数，例如 `（25 个词）`、`（本句有 14 个词。）`、`（"twenty-one" 是一个数字，算作一个词。）`；8.5 的例子甚至解释"本句有 10 个词，因为括号中的文本算作一个词"——这些判断在中文译文里无从复核。**原文未涉及**汉语计词；中文版也未给出等价口径（如"字"或"停顿单位"）。

2. **"-ing" 规则（3.5）与过去分词规则（3.3）**
   3.5 通篇讲英语 -ing 形式的三种功能（进行体、形容词、名词/名词短语），并列出"具有 -ing 形式的批准词"（lighting、opening、routing、servicing、mating、missing、remaining、something、during）。汉语没有 -ing 形态，规则整体失效；中文版只能原样保留 "-ing"，未说明汉语中"动名词/动词作定语"是否受同等限制。**原文未涉及**。

3. **冠词与指示形容词（4.5）**
   汉语无冠词，这条规则在中文写作中没有对象。最能说明问题的是 4.5 自己给的一组对比例句：
   - `Install the new O-rings (15), spacers (14), nut (13), and safety pin (12).`（冠词表明系列中所有项目都是新的）
   - `Install the new O-rings (15), the spacers (14), the nut (13), and the safety pin (12).`（冠词表明只有 O 形圈是新的）
   两句中文译文在材料里**一字不差**（"安装新的 O 形圈 (15)、隔圈 (14)、螺母 (13) 和安全销 (12)。"），英文靠 the 的重复所承载的区别在译文中完全消失，示例失去示范力。同节末"字母数字标识符前不加定冠词"（`Tag circuit breaker 36L7.` vs `Tag the circuit breaker 36L7.`）在中文里也无从体现。**原文未涉及**汉语无冠词场景。

4. **被动语态的识别与改写（3.6）**
   原文的判定法是"思考'由谁或由什么'""句中出现介词 by 就是很好的被动指示"，改写四法都建立在 be+过去分词上。汉语被动可由"被/由/受/加以"标记，也大量使用意义被动（"阀门已调整"），原文的识别法与四步改写不能直接迁移；而汉语技术文本省略施动者极为常见，3.6"只有施动者不明时才可被动"这一约束在中文里难以核查。**原文未涉及**。

5. **多词名词"不超过三个词"（2.1/2.2、1.9 的"不超过三个词"）**
   中文对应物是"定语+中心语"的定中结构，长度单位是字或定语项，不是 word。材料自己的例子"跑道灯连接电阻校准"是 10 个字，读者无法判断它相当于几个"词"，也就无法执行"三词上限"。**原文未涉及**；中文版把 multi-word noun 直译为"多词名词"，未解释汉语里怎么数。

6. **连字符规则（2.2 方法 2、8.2、8.7）**
   8.7 整条是"带连字符的词算作一个词"，2.2 方法 2 是"用连字符把成组词并成一个词"，8.2 列出 5 类必须加连字符的搭配（low-altitude flight、O-ring、air-to-air refueling 等）。汉语没有连字符构词传统，这三条在中文写作里基本无处落地；中文版只能定义"连字符是连接词或词的一部分的标点符号"。**原文未涉及**。

7. **美式拼写（1.14）**
   规则针对 fibre/fiber、colour/color 这类英美差异。中文正文不存在拼写选择，只有嵌入的英文术语、缩写、引用文本才相关；中文版未说明"中文文本中的英文术语仍按美式拼写"这一层。**原文未涉及**。

8. **单复数装置（8.3 第 5 项、名词条目只给单数）**
   8.3 允许用 `test(s)`、`component(s)` 同时表达单复数，1.4 允许可数名词复数。汉语无单复数标记，写成"测试""组件"会丢掉这一信息，`test(s)` 的中文对译无法保留"可能是一项也可能是多项"的提示。**原文未涉及**。

### 3.2 依赖英语词类同形，汉语里判定标准不同

9. **"一词一性"（1.2、9.2）**
   规则的核心是英语同形词跨类：`Test` 批准为名词、不批准为动词；`work` 批准为名词、不批准为动词；`help` 批准为动词、不批准为名词；`damage` 批准为名词、不批准为动词；`clean`、`flush` 同时批准两类。汉语"测试/工作/帮助/损坏"本身就跨类且无形态标记，规则不能按词逐条映射，只能改写成"同一术语在句中只承担一种功能"这类功能表述——中文版没有做这个转换。**原文未涉及**汉语词类问题。

10. **批准词义受限（1.3、9.2）**
    这些限制是英语词义史的产物：follow=跟在后面（不能表"遵循"）、wear=因摩擦损坏（不能表"穿戴"）、see=看见（不能表"了解"）、turn=绕轴转（不能表"变成"）、extend=增大（不能表"适用于"）、above/below 只表物理位置（不能表数值上下限）。汉语对应词（遵循、穿戴、了解、变成、适用、高于/低于）并无同样限制，照译会出现"中文里这条规则为什么存在"的困惑。**原文未涉及**。

### 3.3 有出口，但材料没写

11. **安全说明的分级词（7.1）**
    原文规定 warning=伤亡风险、caution=损坏风险、两者并存取 warning，并明确"其他行业或领域可能使用不同的词汇或类别"（danger、attention、notice），援引 ISO 45001:2018、ANSI Z535、ISO 3864。这其实是留给本地化的口子，但**未给出中文/中国标准的映射**（中文"警告/小心"的语力并不完全对等，"小心"在中文里常弱化为提示）。中文版照译，未加注。

12. **缩写、格式、计量单位不归 STE 管**
    general-introduction 明确三问三答："Does STE give rules for abbreviations? No."、"Does STE regulate text formatting? No."、"Does STE regulate units of measurement? No."，并说这些由技术出版物规范、风格指南、官方指令决定。这是中文适配最合法的出口（中文标点、字号、计量单位都可另定），但中文版只是把这段译出，未提示"中文排版可依此另立规范"。

13. **GR 系列基本是"非英语母语者写英语"的补丁**
    GR-1 补 that（理由是"在许多其他语言中，不可能省略对应的词"，且便于翻译）、GR-5 假朋友（举例只用意大利语 disposizione、西班牙语 disposición）、GR-6 拉丁缩写、GR-8 所有格（"其他语言没有这种所有格形式"）。这些建议对"用中文写作"不适用；原文与中文版都**未涉及**汉语假朋友（如 actual/实际、eventually/最终）或汉语无冠词、无形态带来的反向问题。

### 3.4 中文版自身的缺失与失真（与语言适配无关，但影响可用性）

14. **Issue 9 新增的 help 机制在中文规则版中整体缺失**
    highlights 对第 1–9 节几乎每条都记有 "Help added"；词典导言用整节说明 help 的四类用法。但中文规则版全文检索"help/灯泡/帮助"只有普通行文义（"帮助你选择技术名词"等），**没有一处对应"help（灯泡符号）"这一机制**。也就是说，读者拿中文版无法知道某些规则还附带官方补充说明。

15. **中文版未交代术语更名**
    highlights 明确："The term 'technical noun' fully replaces the previous term 'technical name' in all parts of the document." 中文版直接使用"技术名词"，未提示旧资料里的 technical name 是同一个概念；而 1.1 的定义句又写成"技术名词是指特定概念的名词术语"，把 technical noun 与 noun term 混在同一句里，读者容易以为是两个层级。

16. **精选词典（zh）不能当合规判据**
    该文件是编者选编而非翻译，存在四类问题：
    - **数量与宣称不符**：封面称"100 个最常用批准词"，实际正文 30+25+20+15 = **90 个**，另加 10 组非批准词速查。
    - **例句多为自拟**：如 `Start the application.`、`Get the data from the API.`、`The model gives the answer.`，与官方词条例句不同；官方 START/GIVE 的示范并非这些句子。
    - **自创内容**："6.4 浓度调节"给出 100%/80%/50%/20–30% 四档"推荐浓度"，**原文完全没有**这套分级，属编者发挥。
    - **与 Part 1 直接冲突**（四处，均可核对）：
      1. 把 **TEST 列为批准动词 (v)**（"examine qualities"），而规则 1.2 明写"Test 是批准的名词，但不是批准的动词"，官方批准动词表 A–Z 中也没有 TEST；
      2. 把 **CHECK 列为批准动词 (v)**，而规则 3.7 的示例正以 `Check the laptop battery.` 为 **非 STE**，正确写法是 `Do a check of the laptop battery.`，官方批准动词表同样没有 CHECK；
      3. PROCEDURE 词条例句 `Follow the installation procedure.` 使用了 follow 的非批准词义，而规则 1.3 明令 `Follow the safety instructions.` 应改为 `Obey the safety instructions.`；
      4. 第 2 节把 **PERFORMANCE 列为批准名词**，第 5 节又把 perform / performance 列入"非批准词速查"；而官方常见错误表只给 perform (v) → DO (v)，未确认 performance 的地位。
    结论：该文件适合"入门速查"，不能作为 STE 合规依据。

17. **译文层面的可读性代价**
    为贴近原文，中文版大量保留英文词形与括号原文（如"动词的 '-ing' 形式"、`(TN)`、`STE EXAMPLE`、`Non-STE`），并在每节前加"规则总览"再逐条重复，篇幅约 18.5 万字节；对只读中文的读者，规则正文与示例之间存在双重编码负担。这不影响规则正确性，但影响"照着做"的效率。

---

## 四、术语表（中英对照，56 条）

| # | 英文 | 中文 | 一句话解释（依据材料） |
|---|---|---|---|
| 1 | approved word | 批准词 | 词典中以全大写给出、可在 STE 中使用的词（875 个）。 |
| 2 | word that is not approved / not approved word | 非批准词 | 词典中以小写给出、不得使用的词（1274 个），须换词或换结构。 |
| 3 | approved meaning | 批准词义 | 栏 2 给出的唯一定义；未给出的词义一律不批准。 |
| 4 | alternative / approved alternative | 批准替代词 | 栏 2 为非批准词建议的替换词，仅为建议，可多选。 |
| 5 | word-for-word replacement | 逐词替换 | 找到同词性替代词后原位替换的做法。 |
| 6 | different sentence construction | 不同的句子结构 | 无法逐词替换时必须改写句式（规则 9.1）。 |
| 7 | part of speech | 词性 | 括号内的 n/v/adj/adv/art/prep/conj（及 pron），决定该词只能怎么用。 |
| 8 | technical noun (TN) | 技术名词 | 指特定概念、适用于某专业领域的名词术语，词典不收。 |
| 9 | technical verb (TV) | 技术动词 | 指特定概念或过程、适用于某专业领域的动词术语，词典不收。 |
| 10 | technical name | 技术名称（旧称） | Issue 9 前的旧术语，已被 technical noun 全面取代。 |
| 11 | noun term | 名词术语 | general-introduction/1.1 用来定义技术名词的上位表述。 |
| 12 | verb term | 动词术语 | 用来定义技术动词的上位表述。 |
| 13 | multi-word noun | 多词名词 | 由多个词共同充当一个名词性成分的词组，限三词以内。 |
| 14 | noun cluster | （材料未出现） | 本次材料未使用该英文术语；对应概念即 multi-word noun。 |
| 15 | gerund | （材料未出现） | 本次材料未使用 gerund 一词，相应内容表述为"动词的 -ing 形式"（规则 3.5）。 |
| 16 | subject field | 专业领域 | 技术名词/动词的适用范围，ISO 1087:2019 语境下的特定知识领域。 |
| 17 | controlled dictionary | 受控词典 | 第 2 部分，只收批准词与非批准词条目，不收技术名词/动词。 |
| 18 | controlled natural language | 受控自然语言 | STE 的自我定位：词汇与句式都受限的英语。 |
| 19 | writing rules | 写作规则 | 第 1 部分，9 节 53 条，管语法与文体。 |
| 20 | procedural writing | 程序性写作 | 给读者指令的文本（程序、工作步骤），受 20 词上限约束。 |
| 21 | descriptive writing | 描述性写作 | 提供信息而非指令的文本（描述、报告、注释），受 25 词上限约束。 |
| 22 | safety instruction | 安全说明 | 提示危险或损坏风险的文本，含 warning 与 caution 两级。 |
| 23 | warning | 警告 | 存在受伤或死亡风险时使用的级别。 |
| 24 | caution | 小心 | 存在物品损坏风险时使用的级别。 |
| 25 | imperative form | 祈使形式 | 指令句的动词形式，程序性写作的默认句式。 |
| 26 | active voice | 主动语态 | 语法主语同时是施动者；STE 的默认语态。 |
| 27 | passive voice | 被动语态 | 主语承受动作；仅描述性写作中施动者不明时可用。 |
| 28 | past participle | 过去分词 | 词典第四个动词形式，可作形容词表状态，不等于被动。 |
| 29 | base form / infinitive | 基本形式 / 不定式 | 词典第一个动词形式，(to) adjust 之类。 |
| 30 | simple present / past / future | 一般现在时 / 过去时 / 将来时 | 唯一允许的三种时态。 |
| 31 | regular verb | 规则动词 | 靠 -ed 构成过去式与过去分词。 |
| 32 | irregular verb | 不规则动词 | 不按 -ed 规则构成，如 GIVE/GAVE/GIVEN。 |
| 33 | auxiliary verb | 助动词 | 如 BE/HAVE，用于构成时态；不得用来堆复杂结构。 |
| 34 | modal verb (defective modal verb) | 情态动词（缺项情态动词） | CAN、WILL 等，形式不全，词典标 "No other verb forms." |
| 35 | comparative / superlative | 比较级 / 最高级 | 形容词括号内形式；用 more/most 构成者不列。 |
| 36 | singular / plural | 单数 / 复数 | 名词只列单数，可数名词复数默认允许。 |
| 37 | countable noun | 可数名词 | 复数形式被允许的名词类别。 |
| 38 | vertical list | 垂直列表 | 复杂项目或步骤的分行列表，有 8 项格式要求。 |
| 39 | connecting word / connecting phrase | 连接词 / 连接短语 | and、but、then、thus / as a result、at the same time。 |
| 40 | article | 冠词 | a、an、the，标明名词是新信息还是已知信息。 |
| 41 | demonstrative adjective | 指示形容词 | this、these，兼作句子间衔接手段。 |
| 42 | preposition | 介词 | 表示名词性成分与句中其他成分的关系，如 with、above。 |
| 43 | conjunction | 连词 | 连接词、短语、从句，如 that、because。 |
| 44 | pronoun | 代词 | 指代已出现的人/地/物；先行词必须唯一。 |
| 45 | adverb | 副词 | 修饰动词、形容词或另一副词。 |
| 46 | adjective | 形容词 | 说明名词/名词短语/多词名词的性质、大小、颜色、数量。 |
| 47 | -ing form | 动词的 -ing 形式 | 只允许作技术名词或技术名词中的修饰语。 |
| 48 | help | 帮助（灯泡符号） | 规则与词条旁的图形符号 + 说明文字，分四类。 |
| 49 | STE EXAMPLE / Non-STE example | STE 示例 / 非 STE 示例 | 词典第 3、4 栏；前者合规示范，后者保留错误写法。 |
| 50 | hyphen / dash | 连字符 / 破折号 | 前者连接直接相关的词，后者分隔思想、表范围或停顿。 |
| 51 | alphanumeric identifier | 字母数字标识符 | 如 36L7、No. 1，计词时算一个词，前面不加定冠词。 |
| 52 | quoted text | 引用文本 | 标牌、标签、显示文字、公式等不可改文本，计词时算一个词。 |
| 53 | proper noun of individuals, groups, organizations, geopolitical entities | 个人/团体/组织/地缘政治实体的专有名词 | 计词时整体算一个词。 |
| 54 | acronym / initialism | 首字母缩略词 / 首字母缩拼词 | 如 NASA、VPN，计词时各算一个词。 |
| 55 | topic sentence | 主题句 | 段落第一句，点明该段主题并衔接上文。 |
| 56 | keyword / key phrase | 关键词 / 关键短语 | 重复出现以连接不同思想的词或短语，中途不得换。 |
| 57 | false friend | 假朋友 | 形近义异词，如英语 disposition 不等于意大利语 disposizione。 |
| 58 | inclusive language | 包容性语言 | 性别中立表述；he/she、man/woman 原则不允许。 |
| 59 | possessive form (Saxon genitive) | 所有格形式（撒克逊属格） | 加撇号和 s，允许但要确保正确。 |
| 60 | Latin abbreviation | 拉丁语缩写 | e.g.、i.e.、etc.，STE 建议不用。 |

---

## 五、高频反例（原文英文 + 中文错因）

以下英文均摘自材料原文的 Non-STE 栏或"不要写"示例；中文错因为提取者按对应规则所作说明。

### 5.1 词性误用（词本身批准，但用错词性）

| 英文原例 | 正确写法（原文） | 错在哪 |
|---|---|---|
| `Test the system for leaks.` | `Do the leak test of the system.` | test 只批准为名词，不能当动词（1.2）。 |
| `Dim the lights.` | `Set the lights to the dim position.` | dim 只批准为形容词，不能当动词。 |
| `Check the laptop battery.` | `Do a check of the laptop battery.` | check 只批准为名词（3.7）。 |
| `When you work with cleaning agents, use breathing equipment.` | `When you do work with cleaning agents, ...` | work 只批准为名词（9.2）。 |
| `Install the cover with the help of a second person.` | `... with the aid of a second person.` | help 只批准为动词，不能当名词。 |
| `Be careful not to damage the sleeve.` | `Be careful not to cause damage to the sleeve.` | damage 只批准为名词，不能当动词。 |
| `Give the hole 0.20-inch ream.` | `Ream the hole to a 0.20-inch dimension.` | ream 是技术动词，不能当名词（1.13）。 |
| `Oil the steel surfaces.` | `Apply oil to the steel surfaces.` | oil 是技术名词，不能当动词（1.7）。 |
| `Clamp the cable in position.` | `Put clamps on the cable to hold it in position.` | clamp 是技术名词，被误用为技术动词（1.12）。 |
| `Grease the fasteners.` | `Apply grease to the fasteners.` | grease 是技术名词，不能当动词。 |
| `Wire the cable to the structure.` | `Attach the cable to the structure with wire.` | wire 是技术名词，不能当动词。 |
| `Zero the meter.` | `ADJUST THE METER TO ZERO.` | zero 在词典中只给出 ZERO (TN) 这一替代路径。 |

### 5.2 词义越界（词批准了，但用的不是批准词义）

| 英文原例 | 正确写法（原文） | 错在哪 |
|---|---|---|
| `Follow the safety instructions.` | `Obey the safety instructions.` | follow 只批准"跟随、跟在后面"（1.3）。 |
| `Wear protective clothing.` | `Use (or put on) protective clothing.` | wear 的批准词义是"因摩擦而损坏"（9.2）。 |
| `This regulation extends to all units.` | `This regulation is applicable to all units.` | extend 批准词义是"在尺寸或范围上增加"。 |
| `When the pressure goes down, lift the cover.` | `When the pressure decreases, lift the cover.` | go down 指物理运动/指示器下降，不指压力降低。 |
| `Make sure that the probe went through more than 500 °C.` | `Make sure that the temperature of the probe increased to more than 500 °C.` | go through 只指物理穿过，不能表条件或经历。 |
| `Move the tube to see if the inner connection is tight.` | `Move the tube to make sure that the inner connection is tight.` | see 只能"用眼睛看见"，不能表"了解"。 |
| `The indicator turns green.` | `The color of the indicator changes to green.` | turn 只指绕轴或点转动。 |
| `Do not let the pressure go below (or above) 20 psi.` | `Do not let the pressure become less than (or more than) 20 psi.` | above/below 只表物理位置，不表数值上下限。 |
| `Just apply very light pressure to the surface.` | `Only apply very light pressure to the surface.` | just 的替代词 immediately 会改变指令意思，须选 only。 |

### 5.3 时态、语态与复杂动词结构

| 英文原例 | 正确写法（原文） | 错在哪 |
|---|---|---|
| `The operator has adjusted the linkage.` | `The operator adjusted the linkage.` | 现在完成时未批准（3.2/3.4）。 |
| `The volume control can be adjusted.` | `You can adjust the volume control.` / `Adjust the volume control.` | 情态动词 + 被动构成复杂结构（3.4）。 |
| `The temperature must be adjusted.` | `Adjust the temperature.` | 同上，且程序句应用祈使式（5.3）。 |
| `The sleeve will be adjusted by the robot.` | `The robot will adjust the sleeve.` | 被动句应把施动者提到主语位（3.6 方法 1）。 |
| `The seat is to be installed before you install the cushion.` | `Before you install the cushion, install the seat.` | be to do 结构未批准，且次序应显式化。 |
| `The test can be continued by the operator.` | `Continue the test.` | 程序性写作应改祈使式（3.6 方法 3）。 |
| `Oil and grease are to be removed with a degreasing agent.` | `Remove oil and grease with a degreasing agent.` | 同上。 |
| `When you are doing this procedure, obey all the safety precautions.` | `When you do this procedure, obey all the safety precautions.` | 进行时未批准（3.5）。 |
| `The circuits are connected by a switching relay.` | `A switching relay connects the circuits.` | 有施动者却用被动（3.6）。 |
| `Additives are not used in this type of fuel.` | `We do not use additives in this type of fuel.` | 无施动者的被动；改用 we 作主语。 |

### 5.4 省略、缩略与冠词缺失

| 英文原例 | 正确写法（原文） | 错在哪 |
|---|---|---|
| `Rotary switch to INPUT.` | `Set the rotary switch to INPUT.` | 省略动词，动作不明（4.2）。 |
| `If installed, remove the shims.` | `If shims are installed, remove them.` | 省略主语，读者不知谁/什么被安装。 |
| `Can be a maximum of five inches long.` | `Cracks can have a maximum length of five inches.` | 省略主语（4.2）。 |
| `Remove the bolt and stop.` | `Remove the bolt and the stop.` | 省略冠词导致 bolt/stop 关系歧义。 |
| `If your hands are wet, don't touch the USB power adapter.` | `If your hands are wet, do not touch the USB power adapter.` | 缩略形式不易理解（4.2）。 |
| `Turn shaft assembly.` | `Turn the shaft assembly.` | 名词前缺冠词（4.5）。 |
| `Data module tells you how to operate unit.` | `This data module tells you how to operate the unit.` | 缺指示形容词与冠词（4.5）。 |
| `WARNING: ... IF NOT, THIS CAN CAUSE INJURY TO PERSONS.` | `... A PRESSURIZED SYSTEM CAN CAUSE INJURY TO PERSONS.` | "If not"指代不清，须重述条件。 |

### 5.5 多词名词过长、名词化与短语动词

| 英文原例 | 正确写法（原文） | 错在哪 |
|---|---|---|
| `Runway light connection resistance calibration.` | `Calibration of the resistance of the runway light connection.` | 5 词多词名词，修饰关系不明（2.1）。 |
| `Remove the engine transmission housing attachment bolts.` | `Remove the bolts that attach the transmission housing to the engine.` | 5 词堆叠，用 that 从句拆开。 |
| `Install the forward turbine overheat thermocouple terminal tags.` | `Install the terminal tags on the forward overheat thermocouple of the turbine.` | 6 词，读者要越过四个修饰语才到中心词。 |
| `Move the main-gear-door-retraction-winch handle.` | `Move the main-gear-door retraction-winch handle.` | 全连字符成串，反而更难读（2.2）。 |
| `The laptop has these main parts:` | `The laptop has these primary parts:` | main 未批准，且 main part 不是技术名词（1.6）。 |
| `The ohmmeter gives an indication of 450 ohms.` | `The ohmmeter shows 450 ohms.` | 名词化，动作应直接用动词（3.7）。 |
| `Before the removal of the unit, ...` | `Before you remove the unit, ...` | 同上。 |
| `Cycle the unit twice to remove air from the lines.` | `Operate the unit for two cycles to remove air from the lines.` | cycle 未批准为动词，须改用 operate + 名词。 |
| `After you put out the fire, ...` | `After you extinguish the fire, ...` | put out 是短语动词，含义偏离 put/out 的批准词义（9.3）。 |
| `This compound can give off poisonous fumes.` | `This compound can release poisonous fumes.` | give off 同上。 |
| `Lift the seat so that it clears the track locks.` | `Lift the seat until it is away from the track locks.` | clear 的替代词 clean 义不符，须换结构（9.1）。 |
| `Without this modification, the service life of the unit can be uncertain.` | `... it is possible that the service life of this unit will be shorter than usual.` | 逐词替换会造出 cannot be sure / cannot be known 这类病句。 |

### 5.6 标点、列表与注释

| 英文原例 | 正确写法（原文） | 错在哪 |
|---|---|---|
| `(1) Examine the removed parts; replace the damaged ones.` | 拆成 `(1)` `(2)` 两句 | 分号禁用（8.1），且一句两指令（5.2）。 |
| `The battery is not user-replaceable; it can only be replaced by an approved service station.` | `Users cannot replace the battery. Only specialists at approved service stations can replace it.` | 分号 + 被动 + 长句三错叠加。 |
| `Do not use acetone for cleaning these parts after the repair: - the service cabinet, ...` | `After the repair, do not use acetone to clean: ...` | 列表项与冒号前文字衔接不清（4.3）。 |
| `Remove these parts: ... - The flange (2) that includes: - ...` | 把嵌套项并入括号 | 垂直列表不得嵌套层级（4.3）。 |
| `CAUTION: WHEN YOU GET ACCESS ... DO NOT: - PUT YOUR FEET ...` | 每项各写 `DO NOT ...` | 否定命令须逐项给出（4.3）。 |
| `NOTE: Make sure that the avionics ventilation system continues to operate correctly.` | 改为工作步骤 `(6) Make sure that ...` | 注释含祈使式，实质是指令（5.5）。 |
| `NOTE: When you connect the lines, do not bend them too much. ...` | 改为 `CAUTION: ...` | 涉及损坏风险，注释不能承担安全说明（5.5）。 |
| `NOTE: The leakage must not be more than 0.5 cc/minute.` | 并入工作步骤正文 | 注释不得给限制、公差或结果（5.5）。 |
| `CAUTION: EXTREME CLEANLINESS OF OXYGEN TUBES IS IMPERATIVE.` | `WARNING: MAKE SURE THAT THE OXYGEN TUBES ARE FULLY CLEAN. ...` | 风险等级错（应 warning）、句子抽象、无解释（7.1/7.2/7.3）。 |
| `The report must include each of the following: a completed REC-1 form, ...` | 改为 4 项垂直列表 | 并列项挤在句中，难读（4.3）。 |

### 5.7 不一致与"假朋友"

| 英文原例 | 正确写法（原文） | 错在哪 |
|---|---|---|
| 同一程序里 `servo control unit` / `actuator` / `control unit` 混用 | 全程 `actuator` | 同一物品多个技术名词（1.11）。 |
| 同一程序里 `main body` / `body` / `body assembly`，`torque` / `torque-tighten` | 统一为 `body assembly`、`torque each of ...` | 措辞不一致（9.4）。 |
| `Obey the dispositions of the manufacturer ...` | `... obey the manufacturer's instructions.` | 假朋友：英语 disposition 无"指令"义（GR-5）。 |
| `Discard the standard parts (e.g., washers, screws, bolts, and nuts) ...` | `(for example, washers, bolts, and nuts)` | 拉丁缩写（GR-6）。 |
| `The manufacturer recommends you prepare the mixture ...` | `... recommends that you prepare ...` | 缺连词 that（GR-1）。 |
| `Make sure the valve is open.` | `Make sure that the valve is open.` | 缺 that，主从句边界不清。 |
| `Lift the aircraft at the maximum takeoff weight with passengers.` | `... (passenger weight included).` | with 三义歧义，产生笑话式误读（GR-2）。 |
| `If you engage the pins incorrectly with the seats, they can become damaged.` | 把 they 换成 the pins / the seats / the pins and seats | 代词先行词不唯一（GR-3）。 |
| `Make sure that the cover is not locked (this can cause damage to the probe).` | `... If the cover is locked, this can cause damage ...` | this 指代不明（GR-4）。 |

---

## 附：材料未涉及的内容（明确列出，避免误引）

- 汉语/中文写作场景的任何规则或示例：**原文未涉及**。
- 中文计词口径（字、词、停顿单位）：**原文未涉及**。
- "noun cluster" 这一英文术语：**本次材料未出现**（对应概念为 multi-word noun）。
- "gerund" 这一英文术语：**本次材料未出现**（相应内容为"动词的 -ing 形式"）。
- 词典导言提到的"选词流程图"：**正文只有一句指引，图未出现**。
- 8 类词性中的第 5 项（代词 pron）：**提取文本缺该条**，仅有词条 `YOU (pron)` 可反证。
- STE 对缩写、格式、计量单位的规定：**明确声明不管**，交由技术出版物规范/风格指南/官方指令。
- 中文版对上述任何一点的译者注或适配说明：**没有**（全文无"译者注"字样）。
