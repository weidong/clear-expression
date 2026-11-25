# ASD-STE100 Issue 9 · Part 1 写作规则结构化提取

> 依据：`part1-writing-rules` 下 section-1 ~ section-9 共 9 个 Markdown 文件（源 PDF 第 45–128 页）。
> 约定：例子保留英文原样；原文无例句处标注「原文未给例句」；原文没有规定的主题标注「原文未涉及」。条目编号沿用原文（Rule 1.1、GR-3 等）。

## 一、每节规则清单

### Section 1 – Words（Rule 1.1–1.14，14 条）

| 编号 | 规则一句话 | 原文给的例子（英文原样） |
|---|---|---|
| R1.1 | 只可用三类词：词典批准词、技术名词、技术动词 | "The word "use" is an approved verb in the dictionary." / "The word "engine" is a technical noun." / "The word "ream" is a technical verb." |
| R1.2 | 批准词只能按词典标注的词性使用 | "Test B is an alternative to test A."（名词）；非 STE "Test the system for leaks." → "Do the leak test of the system." |
| R1.3 | 批准词只能用其批准词义 | "Obey the safety instructions."（"follow" 批准义仅 "come after, go after"，故 "Follow the safety instructions." 不合规） |
| R1.4 | 只用词典给出的动词、形容词形式 | "REMOVE (v), REMOVES, REMOVED, REMOVED"；"SLOW (adj) (SLOWER, SLOWEST)" |
| R1.5 | 技术名词须能归入 22 个类别之一 | "bolt, cable, clip, conductor, contact, engine, ferry tank, filter…"（类别1）；"Colors are adjectives, but STE identifies them as technical nouns." |
| R1.6 | 词典未批准的词，仅在作技术名词或其一部分时可用 | "Make sure that the two spigots at the bottom of the unit engage."（base→bottom）；"The base of the triangle is 5 cm."（base 作技术名词，类别7） |
| R1.7 | 技术名词不得作动词 | 非 STE "Oil the steel surfaces." → "Apply oil to the steel surfaces." |
| R1.8 | 用公司、行业或学科领域已批准的技术名词 | "The front panel of the phone has a touchscreen and a home button." |
| R1.9 | 需自选技术名词时，选短的、易懂的（不超过三个词） | 非 STE "Remove the four stainless steel pan head machine screws (10) that attach the metallic machined flange (15) to the front housing cover (20)." → "Remove the four screws (10) that attach the flange (15) to the cover (20)." |
| R1.10 | 不用地区性、俚语、行话词作技术名词 | 非 STE "attach a choker to the heavy machinery" → "attach a cable to the heavy machinery"；"do not brick the router" → "do not set the router to OFF"；"Remove your gear from the work area." → "Remove your tools and equipment from the work area." |
| R1.11 | 同一物件不得用不同技术名词 | 非 STE "servo control unit" / "actuator" / "control unit" 混用 → 全篇统一为 "actuator" |
| R1.12 | 技术动词须能归入四类：制造工艺、计算机、学科专用、法律法规 | "Ream the hole until it has a diameter of 8.00 +/- 0.003 mm."（替代非 STE "Machine the hole…"）；非 STE "If you detect broken wires, repair them." → "If you find broken wires, repair them." |
| R1.13 | 技术动词不得作名词 | 非 STE "Give the hole 0.20-inch ream." → "Ream the hole to a 0.20-inch dimension."；但过去分词可作形容词："Lubricate the reamed hole." |
| R1.14 | 用美式拼写，除其他官方指令另有规定 | 非 STE "carbon fibre reinforced plastic" → "carbon-fiber-reinforced plastic"；"colour" → "color" |

### Section 2 – Multi-word nouns（2 条）

| 编号 | 规则一句话 | 原文给的例子（英文原样） |
|---|---|---|
| R2.1 | 多词名词不超过三个词；用介词拆开长名词 | 非 STE "Runway light connection resistance calibration." → "Calibration of the resistance of the runway light connection."；非 STE "Remove the engine transmission housing attachment bolts." → "Remove the bolts that attach the transmission housing to the engine." |
| R2.2 | 技术名词超过三个词：首次出现写全称，之后用简称或批准缩写；或用连字符把作为一个单位的词连起来（连字符词算一个词） | "engage the ramp service door safety connector pin (the pin that holds the ramp service door, referred to in this procedure as the "safety connector pin")"；"Move the main-gear-door retraction-winch handle." |

### Section 3 – Verbs（7 条）

| 编号 | 规则一句话 | 原文给的例子（英文原样） |
|---|---|---|
| R3.1 | 只用词典给出的动词形式 | "REMOVE (v) REMOVES, REMOVED, REMOVED"；"GIVE (v) GIVES, GAVE, GIVEN" |
| R3.2 | 只允许六种形式/时态：不定式、祈使式、一般现在、一般过去、一般将来、过去分词（作形容词） | "The adjusted linkage" / "The given information"；禁用 "have/has adjusted"、"had adjusted"、"is/was adjusting" |
| R3.3 | 过去分词只作形容词，表状态，不是被动语态 | "Examine all parts of the disassembled unit for damage."；"When the unit is fully disassembled, clean all the parts." |
| R3.4 | 不用助动词构成复杂动词结构 | 非 STE "The operator has adjusted the linkage." → "The operator adjusted the linkage."；"The volume control can be adjusted." → "You can adjust the volume control." |
| R3.5 | -ing 形式只可作技术名词，或作技术名词中的修饰语 | 非 STE "When you are doing this procedure, obey all the safety precautions." → "When you do this procedure, obey all the safety precautions."；允许 "Air-conditioning system, degreasing agent, grinding wheel, polishing disc, sanding machine, switching relay, welding torch" |
| R3.6 | 用主动语态；说明文仅在施动者未知时可用被动 | 非 STE "The circuits are connected by a switching relay." → "A switching relay connects the circuits."；被动可用例 "During transmission, the data was corrupted." |
| R3.7 | 用批准动词表达动作，不用名词或其他词类 | "The ohmmeter gives an indication of 450 ohms." → "The ohmmeter shows 450 ohms."；"Before the removal of the unit…" → "Before you remove the unit…" |

### Section 4 – Sentences（5 条）

| 编号 | 规则一句话 | 原文给的例子（英文原样） |
|---|---|---|
| R4.1 | 句子短而清晰；说明文一句只一个主题，且不用祈使式 | 非 STE 长句 → "1. Remove the cover assembly (9) as follows: A. Remove the four screws (10)… B. Remove the cover (11) from the housing (12). C. Remove and discard the preformed packing (13)."；"The side stay assembly has two folding toggles. The folding toggles are attached together with hinges. …" |
| R4.2 | 不省略词、不用缩写形式（contractions） | "Cracks can have a maximum length of five inches."；"Set the rotary switch to INPUT."；"If shims are installed, remove them."；"Remove the bolt and the stop."；"do not touch the USB power adapter" |
| R4.3 | 复杂文本用竖排列表，并遵守列表标点规则 | "The wheel assembly has these parts: - The tire - The tube - The spokes - The spoke fittings - The valve - The hub." |
| R4.4 | 用连接词和连接短语连接相关话题的句子 | 批准连接词 "and," "but," "then," "thus"；连接短语 "As a result," "at the same time"；"Thus, the power unit supplies currents to the indicator on the related panel." |
| R4.5 | 名词/多词名词前应用冠词（the, a, an）或指示形容词（this, these） | 非 STE "Turn shaft assembly." → "Turn the shaft assembly."；"Tag circuit breaker 36L7."（字母数字标识符前不用 the） |

### Section 5 – Procedural writing（5 条）

| 编号 | 规则一句话 | 原文给的例子（英文原样） |
|---|---|---|
| R5.1 | 程序句最长 20 词（警告、注意等安全指令同样适用）；注释句最长 25 词 | "Install the three auxiliary screws (2) in the flange of the motor assembly (9)."（14 words）；"CAUTION: WHEN YOU REMOVE THE SHROUD (26), BE CAREFUL NOT TO CAUSE DAMAGE TO THE SURFACE OF THE FLANGE ASSEMBLY (22)."（20 words） |
| R5.2 | 一句只写一个指令，除非两个以上动作同时发生（或动作后立即出结果） | 非 STE "Set the TEST switch to the middle position and release the SHORT-CIRCUIT TEST switch." → "A. Set the TEST switch to the middle position. B. Release the SHORT-CIRCUIT TEST switch."；同时发生可合写："Hold the panel in its open position and install the fastener." |
| R5.3 | 指令用祈使式；祈使式前不加 must（除非安全上很重要或给出重要条件） | "Set the switch to ON."；"Continue the test."；非 STE "Before you remove the clamp, you must disconnect the hose." → "Before you remove the clamp, disconnect the hose."；"WARNING: IF YOU MUST CUT THE WIRE, ALWAYS USE A PROTECTIVE MASK." |
| R5.4 | 读者必须先知道的条件写在句首，用逗号与命令分开 | 非 STE "Set the switch to NORMAL when the light comes on." → "When the light comes on, set the switch to NORMAL."；逗号位置改变意义："If the Constant Speed Drive (CSD) does not operate correctly, disconnect it from the gearbox." / "If the CSD does not operate, correctly disconnect it from the gearbox." |
| R5.5 | 注释只给信息，不给指令；不得含祈使式、要求或限值 | "NOTE: The gyroscope will become stable after approximately 15 seconds."；限值须写在步骤内："B. Measure the leakage from the outlet port. The leakage must not be more than 0.5 cc/minute." |

### Section 6 – Descriptive writing（6 条）

| 编号 | 规则一句话 | 原文给的例子（英文原样） |
|---|---|---|
| R6.1 | 信息逐步给出，每句只一个主语；不使用祈使式 | 非 STE 长句 → "The Instrument Landing System (the system) on the aircraft shows data that helps the pilot during the approach to the runway. This system shows the pilot the deviations…" |
| R6.2 | 用关键词和关键短语构成逻辑结构，且全篇不得换词 | "This system shows the pilot the deviations from the localizer course and the glideslope path."（复用 "system," "show," "pilot"） |
| R6.3 | 说明文句长上限 25 词 | "A smartphone is a cellular telephone that has an integrated computer and many other functions."（15 words） |
| R6.4 | 用段落组织相关信息，段首用主题句 | "1. Lightning Strike / A. General / (1) A lightning strike can cause damage to the aircraft." |
| R6.5 | 每段只一个主题，主题句放段首 | 示例分两段：段1主题 "Data to help the pilot"，段2主题 "How this data is transmitted" |
| R6.6 | 每段不超过六句 | 燃料总管描述示例各段句数：1 / 2 / 5 / 4 / 4 / 2 句 |

### Section 7 – Safety instructions（3 条）

| 编号 | 规则一句话 | 原文给的例子（英文原样） |
|---|---|---|
| R7.1 | 用 warning / caution 等词（或符号）标明风险等级：伤害或死亡→warning；设备损坏→caution；两者并存→warning | "WARNING: MAKE SURE THAT THE OXYGEN TUBES ARE FULLY CLEAN. OXYGEN AND GREASE MAKE AN EXPLOSIVE MIXTURE. AN EXPLOSION CAN CAUSE INJURY OR DEATH." |
| R7.2 | 安全指令以清晰准确的命令或条件开头（条件在前） | "CAUTION: WHEN YOU ASSEMBLE THE UNIT, DO NOT LET THE PARTS FALL."；"WARNING: WHILE YOU USE THE SPRAY PAINT, POINT THE SPRAY AWAY FROM YOUR FACE." |
| R7.3 | 给出说明，指出风险或可能后果 | "IF THEY FALL, PERMANENT DAMAGE TO THE PARTS CAN OCCUR."；"THESE CLEANING AGENTS CAN CAUSE CORROSION." |

### Section 8 – Punctuation and word count（7 条）

| 编号 | 规则一句话 | 原文给的例子（英文原样） |
|---|---|---|
| R8.1 | 可用标准英文标点，但不可用分号（;） | 非 STE "Examine the removed parts; replace the damaged ones." → "(1) Examine the removed parts for damage. (2) Replace the damaged part(s)." |
| R8.2 | 用连字符连接直接相关的词（形容词性多词定语、分数/数字、字母或数字+名词、名词性首部的动词、元音相接的前缀） | "low-altitude flight, high-pressure chamber, air-conditioned compartment"；"forty-seven, ninety-ninth"；"L-shaped bracket, O-ring, 3-prong connector"；"die-cast, arc-weld, heat-treat"；"pre-amplifier, de-icing" |
| R8.3 | 括号的七种用途：引用图表/文字、标注件号、标注步骤号、放缩写、同时给单复数、解释词句、给替代项 | "Remove the valve (10, Figure 1)."；"A Liquid Crystal Display (LCD) is a flat-panel display…"；"Do the applicable test(s)."；"Increase the pressure slowly (not more than 10 psi each minute)."；"Open the left (right) access panel L42 (R42)." |
| R8.4 | 竖排列表中冒号等同于句号，是句子边界 | 冒号前程序句 20 词、说明句 25 词；冒号后每一项各自算新句，同样受 20/25 词限制；"To extinguish a possible fire, portable fire extinguishers are installed in these areas:"（13 words） |
| R8.5 | 括号内文字在该句中算一个词，但其本身另成一句 | "Make sure that the EMER pushbutton switch is released (the EMER legend is off)."（10 words；括号内 5 words 另计） |
| R8.6 | 数字、数字+单位、缩写、字母数字标识、引文、标题/标题栏/标牌/标签文字、专有名词各算一个词 | "Do steps 13 thru 16 a minimum of three times."（10 words）；"The unit weighs 20 kg."（4 words）；"Tag circuit breaker 36L7."（4 words）；"C = (A - B) - 0.063 mm"（1 word） |
| R8.7 | 连字符词算一个词 | "Clean the surface with a soap-and-water solution."（7 words）；"Main-gear-door retraction-winch handle"（3 words） |

### Section 9 – Writing practices（4 条 + GR-1~GR-8）

| 编号 | 规则一句话 | 原文给的例子（英文原样） |
|---|---|---|
| R9.1 | 逐词替换不成立时，改写整个句式 | 非 STE "The oil level on the sight gauge must be visible during the test." → "During the test, make sure that you can see the oil level on the sight gauge." |
| R9.2 | 每个批准词都要用对其受限词义和词性 | "Wear protective clothing." → "Use (or put on) protective clothing"；"Do not let the pressure go below (or above) 20 psi." → "Do not let the pressure become less than (or more than) 20 psi." |
| R9.3 | 两个词组合时不得构成短语动词（phrasal verb） | 非 STE "After you put out the fire…" → "After you extinguish the fire…"；"This compound can give off poisonous fumes." → "This compound can release poisonous fumes." |
| R9.4 | 术语与措辞保持一致 | 同一指令统一为 "Apply a small quantity of oil to the threads of the two bolts."；同一件号统一为 "body assembly (9)"，拧紧统一为 "Torque each of the two bolts to 4 Nm." |
| GR-1 | 尽量使用连词 that，标出主句与从句的边界 | "Make sure that the valve is open."；"The gauge shows that the reservoir is full." |
| GR-2 | 留意 with 的三种批准义（关联、帮助/共享、手段/工具）造成的歧义 | "Lift the aircraft at the maximum takeoff weight with passengers." → "Lift the aircraft at the maximum takeoff weight (passenger weight included)." |
| GR-3 | 只用词典批准的代词；有歧义时还原为名词 | "If you engage the pins incorrectly with the seats, they can become damaged." → "…the pins can become damaged." |
| GR-4 | 用 this 时确保指代对象唯一 | "Make sure that the cover is not locked. If the cover is locked, this can cause damage to the probe." |
| GR-5 | 警惕假朋友（形似母语词、义不同） | "Obey the dispositions of the manufacturer…" → "When you use this adhesive, obey the manufacturer's instructions." |
| GR-6 | 不用拉丁缩写（e.g. / i.e. / etc.） | "Discard the standard parts (e.g., washers, screws, bolts, and nuts)…" → "Discard the standard parts (for example, washers, bolts, and nuts)…" |
| GR-7 | 用中性、包容性语言；he/she、man/woman 不允许（必要语境如医学文本除外） | 原文未给例句 |
| GR-8 | 所有格形式允许，但必须确保正确，不确定就不用 | "refer to the manufacturer's instructions" |

> 注意：原文明确说明 GR-1~GR-8 是 general recommendations，"are not STE rules"，只是帮助避免常见错误。

## 二、动作词（verbs）专门摘要

### 1. 允许的动词形式
- 只能用词典为每个动词列出的形式（R3.1）："REMOVE (v), REMOVES, REMOVED, REMOVED"；"GIVE (v), GIVES, GAVE, GIVEN"。
- 只允许六种形式/时态（R3.2）：不定式（base form）、祈使式、一般现在时、一般过去时、一般将来时、过去分词（仅作形容词）。
- 形容词给原级，括号内给比较级/最高级（R1.4）；用 more/most 构成的比较级不在词典列出，因为 more、most 本身是批准词。
- 技术动词与批准动词受同样约束（R1.12 正文："Technical verbs must obey the same rules as other approved verbs in STE."）。

### 2. 禁止项
| 禁止 | 依据 | 原文示例 |
|---|---|---|
| 现在完成时、过去完成时、进行时及一切复杂动词结构 | R3.2 | "have/has adjusted"、"had adjusted"、"is/was adjusting" |
| 用助动词构成复杂动词结构 | R3.4 | "The operator has adjusted the linkage." → "The operator adjusted the linkage." |
| 被动语态（说明文且施动者未知时例外） | R3.6 | "The temperature must be adjusted." → "Adjust the temperature." |
| -ing 形式作动词（只可作技术名词或技术名词的修饰语） | R3.5 | "When you are doing this procedure…" → "When you do this procedure…" |
| 短语动词（动词+介词产生新义） | R9.3 | "put out the fire" → "extinguish the fire"；"give off" → "release"；仅 "put on"、"come on" 等极少数被批准 |
| 技术名词当动词 | R1.7 | "Oil the steel surfaces." → "Apply oil to the steel surfaces." |
| 技术动词当名词 | R1.13 | "Give the hole 0.20-inch ream." → "Ream the hole to a 0.20-inch dimension." |
| 用非批准词性或非批准词义 | R1.2 / R1.3 / R9.2 | "work" 只批准为名词："When you work with cleaning agents…" → "When you do work with cleaning agents…" |
| 祈使式前加 must | R5.3 | "Before you remove the clamp, you must disconnect the hose." → "…disconnect the hose." |

### 3. 主动语态与被动改写
- 总则：技术文本始终用主动语态；只有说明文里施动者（agent）未知时才可用被动（R3.6）。判别法：能回答 "by whom or by what?"、句中出现 by，基本就是被动（R3.6）。
- 四种改写方法（R3.6）：
  1. 有施动者：把它提到句首作主语——"The circuits are connected by a switching relay." → "A switching relay connects the circuits."
  2. 把不定式动词改成主动动词——"These values are used by the computer to calculate the energy consumption." → "The computer calculates the energy consumption from these values."
  3. 程序文本改成祈使式——"The test can be continued by the operator." → "Continue the test."
  4. 施动者未给出：读者为施动者用 you，公司/组织为施动者用 we——"On the ground, the valve can be opened with the override handle." → "On the ground, you can open the valve with the override handle."；"Additives are not used in this type of fuel." → "We do not use additives in this type of fuel."
- 施动者确实未知时，被动合法；若要改主动，可用 "something" 作施动者，但不能把非原因的事物当施动者（"Transmission corrupted the data." 判为 incorrect）。

### 4. 动词怎么选
- 优先用词典里的批准动词；能用批准词写出的句子，就不要用技术动词（R1.12）：非 STE "If you detect broken wires, repair them." → "If you find broken wires, repair them."。
- 技术动词只限四类（R1.12）：1) 制造工艺（去材/加材/连接/改机械性能/改表面/改形状，如 drill, weld, anneal, polish, cast）；2) 计算机过程与应用（输入输出、界面、系统操作，如 click, save, install）；3) 学科专用（工程数学科学、医学、军民业务、导航、汽车铁路、能源油气）；4) 法律法规。
- 技术动词要具体、不许笼统（R1.12）：非 STE "Machine the hole until it has a diameter of 8.00 +/- 0.003 mm." → "Ream the hole…"。
- 能不用技术动词就不用；可用"批准动词 + 技术名词"（R1.12）："Clamp the cable in position." → "Put clamps on the cable to hold it in position."；"Grease the fasteners." → "Apply grease to the fasteners."；"Wire the cable to the structure." → "Attach the cable to the structure with wire."。
- 非批准词作技术动词须落在类别内，换语境即失效（R1.12）："Enter your password."（合规）vs "Do not enter the engine test area without approval."（不合规）→ "Do not go into the engine test area…"。
- 技术动词的过去分词可作形容词（R1.13）："Lubricate the reamed hole."（"reamed" 是过去分词，"reamed hole" 是技术名词）。

### 5. 名词化（verb → noun）的处理
- 核心规则 R3.7：有批准动词描述动作时，用动词，不用名词或其他词类——"The ohmmeter gives an indication of 450 ohms." → "The ohmmeter shows 450 ohms."；"Before the removal of the unit, make sure that the power supply is OFF." → "Before you remove the unit, make sure that the power supply is OFF."。
- 反向限制：该词若未批准为动词，不能硬当动词用，只能换句式——非 STE "Check the laptop battery." → "Do a check of the laptop battery."（check 在此只批准为名词）。
- 技术动词同样不许名词化（R1.13），技术名词同样不许动词化（R1.7），两个方向都堵死。

### 6. 情态动词
- 原文未给情态动词白名单。只可确认：例句中出现 can / must / will（如 "You can adjust the volume control."、"the operator must adjust the oil temperature."、"You will adjust the valve during the test."）；助动词不得用于构成复杂结构（R3.4）；祈使式前不用 must（R5.3）。除此之外的用法，原文未涉及。

### 7. 过去分词作形容词 ≠ 被动语态
- R3.3：过去分词作形容词只表示状态，可放在名词前，或放在 to be / to become / to stay 之后；不得使用词典未列出的过去分词。词典中另有以 "(adj)" 标注的过去分词形形容词，如 "permitted"、"damaged"。

### 8. 允许的 -ing 词（R3.5 明列）
- 名词：lighting, opening, routing, servicing；形容词：mating, missing, remaining；代词：something；介词：during。
- 作技术名词（含标题/小标题）：Cleaning, Testing and Fault Isolation, Handling, Packaging, Shipping, Troubleshooting。
- 作技术名词中的修饰语：Air-conditioning system, degreasing agent, grinding wheel, polishing disc, sanding machine, switching relay, welding torch。

## 三、名词与名词短语

- **最大长度**：多词名词最多三个词（R2.1）；中心词（head noun）通常是最后一个词。超过三个词读者要连着解析多个修饰语，非英语母语读者尤其困难（因其母语中心词常在前）。
- **拆分手法**（R2.1）：用介词 of / on / in / for 把长名词拆成短块——"Runway light connection resistance calibration." → "Calibration of the resistance of the runway light connection."；也可改成从句——"Remove the engine transmission housing attachment bolts." → "Remove the bolts that attach the transmission housing to the engine."。
- **超长技术名词**（R2.2）：先按官方文件原样写全称，再解释，然后全文用简称或批准缩写；缩写不是越多越好（"A text full of abbreviations in a procedure, although shorter, is not easy to read."）。三个词以内的技术名词不必用缩写。
- **连字符**（R2.2 / R8.2）：把作为一个单位的一组词连起来，使其符合三词上限（"cutoff-switch power connection"）。但不得用连字符硬凑超过三个词（非 STE "main-gear-door-retraction-winch handle" → "main-gear-door retraction-winch handle"）；官方技术名词自带的连字符不得删除（"inward-outward valve"）；三词以内的批准名词不必加连字符（不写 "diaphragm-assembly"，写 "diaphragm assembly"）。
- **冠词与指示形容词**（R4.5）：该用的时候必须用 the / a / an / this / these，不得为省字数省略（"Turn shaft assembly." → "Turn the shaft assembly."）。例外与细节：
  - 泛指、抽象概念前不用冠词——"Solvents can cause damage to paint."、"The machine operates with high efficiency."、"This software increases performance."。
  - 短句里每个名词都加冠词更清楚——"Install the nuts (2) and the bolts (3)."。
  - 长串列举只在第一个名词前加冠词——"Discard the O-rings (3), gaskets (4), seals (7), and washers (9)."。
  - 冠词位置会改变语义：只加在首个名词前表示整串都"新"，逐个加表示只有第一个"新"（"Install the new O-rings (15), spacers (14), nut (13), and safety pin (12)." vs "Install the new O-rings (15), the spacers (14), the nut (13), and the safety pin (12)."）。
  - 名词后带字母数字标识符时不用定冠词——"Tag circuit breaker 36L7."（不写 "the circuit breaker 36L7"）。
- **代词**：只能用词典批准的代词；he、she 不允许（GR-3、GR-7）。代词可能指代多个名词时必须还原为名词——"If you engage the pins incorrectly with the seats, they can become damaged." → "…the pins can become damaged."。"this" 指代不明时补出语境（GR-4）。
- **复合名词构造**：
  - 技术名词可作名词，也可作另一个技术名词中的形容词性成分，但不得作动词（R1.7）。
  - 技术名词来自 22 个类别（R1.5）；未批准词只有在充当技术名词或其一部分时才可用（R1.6，如 "main landing gear"、"relative angular positions"）。
  - 同一物件全篇只能用一个技术名词（R1.11）；优先用公司/行业/学科已批准词（R1.8）；需自选时取短的（R1.9）；不用地区词、俚语、行话（R1.10）。
  - 颜色在 STE 中被归类为技术名词，且颜色的比较级/最高级不允许（"blacker," "the reddest"）（R1.5 类别17）。
  - 引文（标牌、标签、屏幕文字）按原样保留，即使拼写是英式也不改（R1.14，引至 R8.6）。
  - 所有格形式允许但要确保正确，不确定就不用（GR-8）。

## 四、句子层面

- **句长上限**：程序句 ≤ 20 词（R5.1）；说明文句 ≤ 25 词（R6.3）；注释句 ≤ 25 词（R5.5，注释不受 R5.1 约束）。安全指令（warning/caution）同样受 20 词限制（R5.1）。
- **一句一个指令**（R5.2）：一句只给一个指令，用编号或字母显示步骤顺序；例外只有两种——多个动作同时发生（"Cut and remove the wire."），或动作后立即产生结果（"Measure the leakage from the outlet port. The leakage must not be more than 0.5 cc/minute."）。
- **一句一个主题**（R4.1 / R6.1）：说明文每句只一个主语/主题，后句逐步补充信息，不得使用祈使式。
- **语序**：
  - 程序句以祈使动词开头（R5.3）；
  - 条件/前提放句首，逗号分隔后再给命令（R5.4、R7.2）；
  - 主动句把施动者放句首作主语（R3.6 Method 1）；
  - 逗号位置会改变副词修饰对象，进而改变句义（R5.4："…does not operate correctly, disconnect…" vs "…does not operate, correctly disconnect…"）。
- **条件句写法**（R5.4、R7.2）：先写条件（When / If / While 从句），逗号，再写命令；不得把条件甩到句尾（非 STE "Set the switch to NORMAL when the light comes on."）。
- **连接词**（R4.4、R6.2）：批准连接词 "and," "but," "then," "thus"；批准连接短语 "as a result," "at the same time"；指示形容词 this/these 也可作连接手段（"This method will help you…"、"THIS PRECAUTION WILL PREVENT INJURY."）。原文措辞是 "Some of the connecting words that are approved in the dictionary are…"，不是穷尽清单。关键词/关键短语要原样复用，不得中途换说法（R6.2、R9.4）。
- **时态**（R3.2）：只用一般现在、一般过去、一般将来、祈使式、不定式；过去分词只作形容词。完成时、进行时、其他复杂结构一律不许。
- **完整性与缩写**（R4.2）：不省名词、不省动词、不省主语、不省冠词、不用 don't / isn't / aren't 之类缩写——"Can be a maximum of five inches long." → "Cracks can have a maximum length of five inches."；"Rotary switch to INPUT." → "Set the rotary switch to INPUT."；"If installed, remove the shims." → "If shims are installed, remove them."。
- **避免抽象**（R4.1）：不写无法执行的空话——"No leaks are permitted." → "Make sure that there are no leaks."；"Different temperatures will change the cure time." → "When the temperature increases, the cure time will decrease."。

## 五、标点与字数

- **标点**：
  - 可用全部标准英文标点，唯独分号（;）禁止（R8.1）；替代办法永远是拆成两句。理由：分号容易写出超长句，且不易用对。
  - 连字符（-）用于连接直接相关的词，五类情形见 R8.2；连字符不是破折号（dash），破折号用于分隔意思、表示范围或停顿（R8.2 末段）。
  - 括号七种用途见 R8.3（引图表/文字、标件号、标步骤号、放缩写、同时给单复数如 "test(s)"、解释词句、给替代项如 "left (right)"）。
  - 原文不规定一般标点体系，指向 Chicago Manual of Style、Gregg Reference Manual 等外部手册（Section 8 开篇）。
- **列表写法**（R4.3）：
  - 第一句末尾用冒号引出列表；
  - 每项用数字、字母、破折号或圆点标识；
  - 每项首字母大写；
  - 适用时每项主语名词前加冠词；
  - 整句才加句号，非整句不加句号；项末不加逗号或分号；最后一项加句号；
  - 同一列表内不得混用程序性内容和说明性内容；
  - 安全指令中每一项都要各自带否定命令（DO NOT PUT YOUR FEET ON THE APU LINE. / DO NOT USE THE APU LINE AS A HANDLE.）；
  - 每项必须与冒号前的引导句语法衔接；不得嵌套二级列表，同级处理（把子项并入括号）。
  - 列表中的项可以含动词但不是完整句，此时不加句号（"One check valve that prevents the backflow of fluid"）。
- **数字与单位**：
  - 数字、数字+计量单位、缩写、字母数字标识符、引文、标题/标题栏/标牌/标签文字、专有名词，各算一个词（R8.6）；
  - 单位通常紧跟数字（"10 mA"），"10 °C" 与 "10 degrees Celsius" 计数相同（R8.6）；
  - 公式算引文，计一个词（"C = (A - B) - 0.063 mm"）；
  - 段落号、步骤号不计入句长；
  - 数字/单位的书写格式（小数位、千分位、单位前空格等）原文未涉及，指向适用的技术出版物规范。
- **单词计数规则**：
  - 竖排列表中的冒号作用等于句号（R8.4）：冒号前受 20/25 词限制，冒号后每一项各自算新句，同样受 20/25 词限制；
  - 括号内文字在该句中算一个词，但括号内文字本身另成一句单独计数（R8.5）；括号中的标识符、缩写也各算一个词；
  - 连字符连接的一组词算一个词（R8.7）；
  - 例："Make sure that the EMER pushbutton switch is released (the EMER legend is off)." 计 10 词，括号内 5 词另计。

## 六、写作实践（Section 9）

- **R9.1 何时必须换句式**：词典给出同词性替代词时可逐词替换（"A value of 2 mm is acceptable." → "A value of 2 mm is permitted."）；出现以下四种情况必须改写整句：
  1. 换成替代词后语法结构必须变——"The oil level on the sight gauge must be visible during the test." → "During the test, make sure that you can see the oil level on the sight gauge."（visible→see，同时 must be→make sure that you can）；
  2. 逐词替换后语义不通——"cannot be sure" / "cannot be known" 不是好英文，改为 "Without this modification, it is possible that the service life of this unit will be shorter than usual."；
  3. 替代词改变了原意——"just" 的批准替代是 "immediately"，但 "Immediately apply very light pressure…" 改变了指令含义，应写 "Only apply very light pressure to the surface."；
  4. 要替换的词根本不在词典——"The incidence of water in fuel is dangerous." → "Water in fuel is dangerous."。
- **R9.1 的操作方法**：先问两个问题——"What is the meaning of the word 'clear' in this context?"、"What is the action that a reader must do?"；必要时查普通英文词典定位词义，再决定用哪个动作动词。允许的工程手段：拆长句、删不必要信息、向工程师补信息；改完要检查对其他段落没有负面影响。
- **R9.1 的完整案例**（裂纹修理表）：非 STE 原句 24 词、被动、"perform/within/certain/detect" 均非批准词、缺冠词、非祈使式。逐词替换后仍是坏英文，最终解法是把指令挪进表头："If you find cracks, refer to the table that follows:" + 表头 "If the crack is of this length | Do the repair before"，并把具体小时数放表中，避免同一信息说两遍。
- **R9.2 词义受限**：批准词通常只有一个批准义，其他普通英文义不批准。反例：wear（批准义是"摩擦损坏"，不能表示"穿着"）→ 用 use / put on；extend（"在尺寸或范围上增大"）不能表示"适用于"→ 用 is applicable to；go down（只指指示器物理下行）→ 压力用 decrease；go through（只指物理穿过）→ 温度用 increased to；see（只用眼睛看）不能表示"查明"→ 用 make sure；turn（绕轴转动）不能表示"变色"→ 用 the color changes to green；above/below（只表物理位置）不能表限值→ 用 more than / less than。
- **R9.2 词性固定**：work 只批准为名词、help 只批准为动词、damage 只批准为名词——"Be careful not to damage the sleeve." → "Be careful not to cause damage to the sleeve."。少数词批准为多词性（flush 动词/形容词），靠句中位置区分。
- **R9.3 短语动词**：批准词组合出新义即违规（put out、give off）；词典通常不把短语动词列为"未批准"，需自己识别；仅 put on、come on 等极少数被批准且有受限词义。
- **R9.4 一致性**：同类工步每次用同一措辞与同一术语。反例列出三类不一致：同一件号三种叫法（main body / body / body assembly）、拧紧两种说法（torque / torque-tighten）、润滑两种句式（lubricate the XX bolts / apply a small quantity of oil to the threads of the XX bolts）。选定一种后重复使用。
- **GR-1 ~ GR-8 的具体避歧义手法**：补出连词 that 标从句边界（GR-1，且利于翻译）；警惕 with 的三义（GR-2，必要时改条件从句并把主要动作动词放回谓语，如 "Seal the opening with tool TS9867." 而非 "Use tool TS9867 to seal the opening."）；代词指代唯一否则还原名词（GR-3）；this 指代唯一否则重述语境（GR-4）；警惕假朋友（GR-5）；不用 e.g./i.e./etc.（GR-6）；性别中性（GR-7）；所有格不确定就不用（GR-8）。
- **段落**：Section 9 未规定段落写法；段落规则在 Section 6（R6.4 用段落组织相关信息、R6.5 每段一个主题且主题句在段首、R6.6 每段不超过六句）。原文未涉及段落词数上限。

## 七、可直接迁移到中文的 10 条

1. **一句一动作（R5.2 / R4.1）**——把并列动作拆成编号步骤，读者（或 AI）不会漏做。
   英文：非 STE "Set the TEST switch to the middle position and release the SHORT-CIRCUIT TEST switch." → STE "A. Set the TEST switch to the middle position. B. Release the SHORT-CIRCUIT TEST switch."
   中文：❌"把测试电门置于中间位并松开短路测试电门。" → ✅"1. 将 TEST 电门置于中间位置。2. 松开 SHORT-CIRCUIT TEST 电门。"

2. **条件前置，逗号断句（R5.4 / R7.2）**——先给触发条件，再给动作，避免"做完才发现有条件"。
   英文：非 STE "Set the switch to NORMAL when the light comes on." → STE "When the light comes on, set the switch to NORMAL."
   中文：❌"将电门置于 NORMAL，当灯亮时。" → ✅"当灯亮时，将电门置于 NORMAL。"

3. **主动语态、写明执行者（R3.6）**——谁做、做什么，一目了然；给 AI 的指令尤其需要明确施动者。
   英文："The volume control can be adjusted." → "You can adjust the volume control." / "Adjust the volume control."；"The sleeve will be adjusted by the robot." → "The robot will adjust the sleeve."
   中文：❌"音量控制可以被调节。" → ✅"调节音量控制。"／"由机器人调节套筒。"

4. **动词优先，拒绝名词化（R3.7 / R1.13）**——"做出指示""进行拆卸"这类空壳动词会把动作藏起来。
   英文："The ohmmeter gives an indication of 450 ohms." → "The ohmmeter shows 450 ohms."；"Before the removal of the unit…" → "Before you remove the unit…"
   中文：❌"欧姆表对 450 欧姆给出一个指示。" → ✅"欧姆表显示 450 欧姆。"；❌"在设备的拆卸之前……" → ✅"拆卸设备之前……"

5. **一词一义、一词一性（R1.2 / R1.3 / R9.2）**——同一个词不在文中兼职，避免读者按另一个义项理解。
   英文：非 STE "Test the system for leaks."（test 只批准为名词）→ STE "Do the leak test of the system."；"Wear protective clothing."（wear 批准义为"摩擦损坏"）→ "Use (or put on) protective clothing"
   中文：❌"泄漏测试一下系统。"（"测试"当动词、又当名词）→ ✅"对系统做泄漏测试。"

6. **术语全篇一致（R1.11 / R9.4）**——同一对象只用一个名字，否则读者以为是两个东西。
   英文：非 STE 混用 "servo control unit" / "actuator" / "control unit" → STE 全篇 "actuator"。
   中文：❌"伺服控制组件……作动筒……控制单元"混用 → ✅ 全篇统一为"作动筒"；同理"拧紧螺栓"与"给螺栓施加力矩"择一。

7. **名词短语不超过三个词，用介词拆（R2.1 / R2.2）**——长定语链是中文和英文共同的歧义源。
   英文：非 STE "Runway light connection resistance calibration." → STE "Calibration of the resistance of the runway light connection."
   中文：❌"跑道灯连接电阻校准作业规程" → ✅"跑道灯连接处电阻的校准方法"（一层一层说）。

8. **代词指代必须唯一，否则还原名词（GR-3 / GR-4）**——"它/其/该"是歧义高发区。
   英文："If you engage the pins incorrectly with the seats, they can become damaged." → "…the pins can become damaged."
   中文：❌"如果销子与座安装不正确，它们可能损坏。" → ✅"如果销子与座安装不正确，销子可能损坏。"

9. **逻辑关系显性化（R4.4 / GR-1）**——用"因此/但是/然后/同时"和明确的从句边界，代替靠语序暗示。
   英文："If the pressure increases, it changes the electrical currents in the transmitter. Thus, the power unit supplies currents to the indicator on the related panel."；"The gauge shows that the reservoir is full."
   中文：❌"压力升高变送器电流变化电源组件给指示器供电。" → ✅"如果压力升高，变送器中的电流会变化。因此，电源组件向相关面板上的指示器供电。"

10. **列表写成"引导句 + 冒号 + 平行项"（R4.3 / R8.4 / R8.5）**——冒号即句界，每项结构一致、首字母大写、只有完整句才加句号。
    英文："The wheel assembly has these parts: - The tire - The tube - The spokes - The valve - The hub."
    中文：❌"轮组件包括轮胎、内胎、辐条、气门和轮毂等等。" → ✅"轮组件包括以下零件：\n- 轮胎\n- 内胎\n- 辐条\n- 气门\n- 轮毂"

---

### 附：原文未涉及 / 不宜外推的点
- 中文写作、中文标点、中英对照规则：原文未涉及（本报告第七节是迁移建议，不是原文规则）。
- 情态动词白名单：原文未涉及（仅见 can / must / will 的例句与 R3.4、R5.3 的限制）。
- 数字与计量单位的书写格式（小数位、千分位、单位空格）：原文未涉及，只规定计数方式。
- 段落词数上限：原文未涉及（仅有每段 ≤ 6 句）。
- 具体词表本身：在 Part 2 词典，不在这 9 个文件内。
- 排版/字号/大小写格式：原文明确说 "STE does not give rules for formatting."（Section 7）。
