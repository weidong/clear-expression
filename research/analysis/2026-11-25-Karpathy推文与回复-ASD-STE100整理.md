# Karpathy 推文与回复整理：ASD-STE100 与 LLM 的四种输出

> 整理日期：2026-11-25
> 数据快照：2026-11-25，读取自 x.com 页面
> 用途：《简明表达规范》源头梳理的第一份材料

---

## 一、推文原文（一字不落）

**原文链接**：<https://x.com/karpathy/status/2105819303471976479>
**作者**：Andrej Karpathy（@karpathy）
**发布时间**：页面显示 上午 8:37 · 2026 年 10 月 2 日

```text
We'll be spending a lot more time trying to understand the outputs of language models. A few thoughts, tips & tricks:

Writing. Something I've had success with: Ask your LLM to explain something in ASD-STE100, it's a controlled language specification originally developed for aerospace maintenance documentation. LLMs well-versed in this language and it comes with heavy constraints on clean writing style that I often find a lot more readable. Sometimes I've tried to soften it a bit e.g. ask for "80% of the way to ASD-STE100" because the spec is quite stringent. But even better:

Diagrams / images. Instead of writing, ask your LLM to create a diagram. These can be a lot easier to process, parse, and understand. But even better:

Web pages. Ask for output "in HTML" to get a beautiful, interactive webpage. LLMs are getting really good at frontend and can create beautiful experiences, animations, etc. But even better:

Explainer videos. The output format I am most bullish on is fully custom / bespoke explainer videos generated on any arbitrary topic. Experiment with things like "Create a 3b1b style video explainer on X. Use my ElevenLabs API key for audio narration". (you'd need an API key for the latter or you can ask your LLM to find you decent free alternatives that use your local compute). This is actually starting to work!

In summary:
- As LLMs get better, they will do more and more of the legwork autonomously, and a lot more of our work will rise up the abstractions into oversight and understanding.
- Luckily, LLMs can help here too because as intelligence and code are increasingly abundant, you can ask for large, custom, discardable software artifacts (e.g., web apps, video explainers) that would have never made sense to create before. Push the boundaries here and you'll be surprised.
```

说明：第二段中 `LLMs well-versed in this language` 一句，原文如此，疑漏一个 are。为保持一字不落，未做改动。

### 互动数据（2026-11-25 快照）

| 指标 | 数值 |
| --- | --- |
| 查看 | 8,272,722 |
| 回复 | 1,711 |
| 转帖 | 8,366 |
| 喜欢 | 56,967 |
| 书签 | 82,925 |

书签数高于喜欢数，说明很多人把它当资料存下来，不只当观点点赞。

---

## 二、推文讲了什么

一句话：**AI 越来越强，读它写的东西会占掉我们更多时间；所以要换输出形式，不要死磕长文字。**

原文给出一条四层递进的路，每一层都用 "But even better" 抬一级。

| 层级 | 输出形式 | 原文理由 |
| --- | --- | --- |
| 1 | 用 ASD-STE100 写 | 受控语言，写作约束很硬，读起来更清楚 |
| 2 | 画图 | 图比文字更容易处理、解析、理解 |
| 3 | 输出 HTML 网页 | 前端能力强，可交互、有动画 |
| 4 | 定制讲解视频 | 作者最看好；可指定 3b1b 风格，用 ElevenLabs 配音 |

两个容易被忽略的细节：

1. **"80% of the way to ASD-STE100"**。作者认为规范太严，所以主动放松。这是一个调参动作，不是照抄规范。
2. **"discardable software artifacts"**。用完就丢的软件产物。视频、网页这类东西过去做一次成本太高，现在可以随手生成，所以值得为"只读一次"的场景专门做一个。

结尾的判断：工作重心会从"自己动手"上移到"监督与理解"。

---

## 三、回复概况与阅读说明

### 规模

回复 1,711 条。这个数字相对 5.6 万喜欢偏低，说明多数人只是收藏，没有下场讨论。

### 阅读方式（必读）

本机浏览器打开推文详情页时，回复列表没有渲染出来。因此改用 X 站内搜索读取，检索式是 `conversation_id:2105819303471976479` 加关键词。

共执行 14 次检索，归为 7 组：

| 检索 | 目的 |
| --- | --- |
| 热度排序（默认） | 取高赞回复 |
| 最新排序 | 取近期回复 |
| ASD-STE100 | 主题相关 |
| STE、controlled language | 术语相关 |
| video、diagram、HTML、writing | 四种输出形式各一组 |
| skill、manim、audio、80% | 工程化与折中做法 |
| from:karpathy | 查作者是否在楼下回复（结果：没有） |

### 覆盖范围的实话

1,711 条无法逐条读完。原因有三条：页面每次只加载十几条；大量回复是 @grok 的自动改写，内容高度重复；滚动加载在此环境下失效。

实际读到并去重后约 60 条，其中有信息量的约 30 条。下面的整理以这 30 条为准。**未覆盖的部分主要是 @grok 的回答和纯表情回复。**

### 回复的四个类型

| 类型 | 占比判断 | 价值 |
| --- | --- | --- |
| 让 @grok 用 STE100 重写这段话 | 最多 | 低，重复演示 |
| 补充自己的实践经验 | 少 | 高 |
| 质疑某一层建议 | 很少 | 高 |
| 把方法做成工具或 skill | 少 | 高 |

---

## 四、有价值的回复

### 4.1 真动手做了实验的人

这是最有价值的一组。他们验证了第 4 层（视频）确实可行。

| 账号 | 做了什么 | 技术路线 | 链接 |
| --- | --- | --- | --- |
| Favio Vázquez | 做了 ASD-STE100 主题的 3b1b 风格讲解片 | Kokoro 本地语音 + Manim + showtime，单机渲染，零 API key；解说词本身用 STE 写 | [原帖](https://x.com/FavioVaz/status/2106245948502319366) |
| Erick P. | 做了随机微积分的 3b1b 风格讲解片 | 未披露 | [原帖](https://x.com/bondsnbourbon/status/2105892170263650792) |
| Anish | 把这条推文本身做成 3 分钟讲解片，并加深 STE100 部分 | Ngram 平台；脚本、画面、ElevenLabs 配音都从推文生成 | [原帖](https://x.com/Anish_m/status/2105870492532093105) |
| Carlos E. Perez | 用 Opus 5.5 做讲解视频 | 未披露 | [原帖](https://x.com/IntuitMachine/status/2105822832567734409) |
| Justin.md | 把 Claude 当老师，产出视频讲解 | 未披露 | [原帖](https://x.com/JustinPerea/status/2105825705754055013) |
| Gavin Purcell | 让 Opus 5.5 独立完成一支完整片：写稿、选角色、生成与挑选视频、剪辑、配乐 | 多轮往返修改 | [原帖](https://x.com/gavinpurcell/status/2106158451496018065) |

其中 Favio 的回复信息量最大，因为它给出了完整可复现的免费路线。他的原话要点：

- 走的是作者说的"免费替代"路线。
- 语音用 Kokoro，动画用 Manim，全部在本机渲染。
- 解说词自己就是用 STE 写的，形成了自指。
- 工具是他自己的开源项目 showtime。

### 4.2 对"画图"这一层的反驳

作者说图比文字好读。回复里有人不同意，而且理由具体。

| 账号 | 观点 |
| --- | --- |
| Osman（最高赞回复之一） | AI 生成的图，尤其是渲染出来的 Mermaid，反而难懂；排版好的 HTML 产物才真正好用。他说自己从没想过还能要视频，准备试。 |
| Pawan Poolla | 图首选 ASCII 或 HTML，可以跳过 Mermaid；音频摘要或播客适合深挖长论文的某一段；Opus 5.5 加 HyperFrames 生成的视频很适合出要点。 |
| Grady Booch | 一句话反讽："还有种东西叫 UML。" |

这一组的共同点：**反对的不是"图"，而是"Mermaid 这类自动渲染的图"。** 手写 ASCII 和手工排版的 HTML 仍然被认可。

### 4.3 关于 ASD-STE100 本身的讨论

| 账号 | 内容 |
| --- | --- |
| Daniel（@introdev_io） | 提出一个关键问题：STE100 应该设成全局指令，让所有输出都这样写；还是只在解释复杂内容时用？此问题在可见回复中无人回答。 |
| Rudra Satani | 认为"80% 接近 STE100"是最实用的细节，并反问作者是否试过完整的 3b1b 视频路线。 |
| Abdul Osman | 指出 HTML 不在 STE100 词表里，质疑作者把两件事混在一起。 |
| @grok（多条） | 负责答疑：STE100 是受控语言，53 条规则，约 900 个许可词，每句 20 到 25 词，主动语态。这些说法已在第六节对照官方来源核实。 |
| 0xbadhash | 玩笑式对比：先让模型说"原始人语"，再说 STE100。Grok 照做，给出了两句对照。 |

Daniel 的问题值得单独记住。它其实是在问：**规范是"文体选项"，还是"全局默认"？** 这直接关系到我们自己那套规范怎么用。

### 4.4 被工程化的产物

回复里出现了一批把方法固化成工具的动作。这类回复数量不多，但指向明确。

| 账号 | 产物 |
| --- | --- |
| Ankit Gaurav | 提议做一个叫 `asd-explain` 的 skill，输入主题就按 STE100 风格解释，省得每次重写提示词。Grok 当场给出了可用的 skill 文本。 |
| Mukul | 让 Grok 直接生成 skill.md 文件。 |
| Maksymilian Gajda | 把 STE 规则写进 Hermes agent 的 SOUL.md 或 skill prompt 里，做成常驻风格。 |
| Talat UYARER | 推荐 @mattpocockuk 的 wait-what skill。 |
| Matt Kaan | 提到 ELI5 skill，说它什么都能教。 |
| Boris Starkov | 提示 ElevenLabs 已有托管 MCP，配音可以免 API key。 |
| Abram2k11 | 反向疑问：自己的 Claude 还在用 2011 年的 TTS，说没有直接可用的语音接口。 |

这一组说明：**社区的第一反应不是"多写几篇文章"，而是"把风格做成常驻配置"。**

### 4.5 一两句话的洞见

| 账号 | 原话要点 |
| --- | --- |
| Abhishek Parolkar | 好结果是设计良好的约束的结果；好系统就是一组好约束。 |
| Mike Koker | 一个返回图而不是摘要的 agent，才是他真会读的输出；ASD-STE100 他是头一次听说。 |
| 剑的 AI 实验室 | 每个解释都要配一个短例子和预期答案，用来对齐。做水浒手游时踩过同样的坑。 |
| Azy | "做成讲解视频吧，这段对我的花生大脑太长了。" |

Abhishek 那句可以看作整条推文的注脚：约束不是限制，是让结果稳定的手段。

---

## 五、回复中引用的链接及阅读结果

| 链接 | 提出者 | 实际内容 | 与本主题关系 |
| --- | --- | --- | --- |
| [github.com/FavioVazquez/showtime](https://github.com/FavioVazquez/showtime) | Favio Vázquez | 面向编码 Agent 的本地视频工作室。描述一句话，Agent 导演，本机渲染。支持动效、配音、音乐、字幕、素材剪辑与多平台导出。无云服务、无 API key、不上传。可在 Claude Code、Codex、Cursor、Devin、OpenCode 中调用。 | 第 4 层"视频"的开源落地路径 |
| [ngram.com](https://ngram.com) | Anish | Agent 式视频生成平台。把想法、文档、链接或录屏变成成片，自动做调研、分镜、脚本、配音，支持 16:9、9:16、1:1 导出。 | 第 4 层的商业产品形态 |
| [asd-ste100.org](https://www.asd-ste100.org/) | 间接 | ASD-STE100 官方站。Issue 9，2025 年 1 月 15 日发布。ASD 拥有，STEMG 维护。 | 规范本体，见第六节 |
| [elevenlabs.io/mcp](https://elevenlabs.io/mcp) | Boris Starkov | 回复称 ElevenLabs 已提供托管 MCP，可免 key 生成配音。未逐页核实。 | 配音环节的成本降低 |
| GitHub 上的 ELI5 skill 仓库 | @grok | 回复列出 Anthropic 社区插件版、DreambigOu 版、pjerryhu 版等。未逐个打开。 | 同类"解释器"skill 先例 |

---

## 六、ASD-STE100 事实核对

回复里关于 STE100 的数字很多，容易以讹传讹。以下逐条对照官方站。

| 说法 | 官方核实 | 结论 |
| --- | --- | --- |
| 53 条写作规则 | 官方写明 53 条，分 9 节，覆盖选词、语法、句子结构、风格 | 属实 |
| 约 900 个许可词 | 官方写明约 900 个，另有约 1200 个不许可词并给出替代建议 | 属实 |
| 一词一义、一词性 | 官方写明每个词只有一个含义，且只批准一种词性 | 属实 |
| Issue 9，2025 年 | 官方写明 Issue 9，2025 年 1 月 15 日 | 属实 |
| 源自航空航天维修文档 | 官方写明 1970 年代末由 AECMA 为航空维修文档开发 | 属实 |
| 1986 年首版 | 官方写明首版为 1986 年的 AECMA 文件 | 属实 |
| 2005 年成为国际规范，2025 年成为国际标准 | 官方历史页写明 | 属实 |
| 技术名词可以超出词表 | 官方写明技术名词与技术动词另有规则 | 属实，这解释了 HTML 之争 |

修正一处细节：@grok 说"每句不超过 20 到 25 词"。官方文档的句长规则按文本类型分档，并非单一数字。引用时应写成"按文档类型规定句长上限"。

---

## 七、对《简明表达规范》的三点启示

这一节只记录从这条推文得到的方向性判断，不展开方法。

### 7.1 我们做的事，方向被验证了

作者的做法是给模型一个外部约束，逼它写清楚。这和我们把规范做成可检查的规则集，是同一个思路。区别在于他借的是别人的规范，我们做的是自己的。

### 7.2 "80%" 比 "100%" 更值得学

作者自己承认规范太严，主动打折。这说明规则的价值不在严格，而在可调。

对应到我们的体系：句长阈值分档、破折号密度只报参考值不计问题数，这些做法方向一致。**规则要留出松紧档位，否则会被绕过。**

### 7.3 输出形式是规范之外的另一半

作者的四层递进说明：有些内容，改文字改不好，换形式就好了。

我们的规范目前只管文字。可以考虑在手册里加一条兜底建议：当一段文字反复改仍不清晰时，改用表格、图或网页。这不用改规则，只需要加一句提示。

### 7.4 一个待回答的问题

Daniel 那个问题值得我们先定下来：**规范是写作时的文体选项，还是所有输出的默认设置？**

这个问题不解决，后面所有"怎么用"的讨论都会反复。建议单独列一次讨论。

---

## 八、回复清单（附录）

按信息量排序，去重后保留 26 条。Grok 的自动回答只保留有事实价值的两条。

| # | 账号 | 要点 | 链接 |
| --- | --- | --- | --- |
| 1 | Favio Vázquez | STE100 主题视频，本地全流程，零 key | [查看](https://x.com/FavioVaz/status/2106245948502319366) |
| 2 | Osman | Mermaid 难懂，HTML 好用 | [查看](https://x.com/osmannyildiz/status/2124802532094464095) |
| 3 | Pawan Poolla | ASCII、HTML 优于 Mermaid；音频适合长论文 | [查看](https://x.com/pawanpoolla/status/2105875977356312693) |
| 4 | Anish | 推文转 3 分钟讲解片，用 Ngram | [查看](https://x.com/Anish_m/status/2105870492532093105) |
| 5 | Daniel | 问 STE100 是否该做全局指令 | [查看](https://x.com/introdev_io/status/2107101437629198789) |
| 6 | Abhishek Parolkar | 好系统是一组好约束 | [查看](https://x.com/parolkar/status/2106911639442424065) |
| 7 | Rudra Satani | 80% 折中很实用 | [查看](https://x.com/rudraxx13/status/2105870659893203410) |
| 8 | Erick P. | 做出随机微积分讲解片 | [查看](https://x.com/bondsnbourbon/status/2105892170263650792) |
| 9 | Gavin Purcell | Opus 5.5 独立完成整支片 | [查看](https://x.com/gavinpurcell/status/2106158451496018065) |
| 10 | Grady Booch | 反讽 UML | [查看](https://x.com/Grady_Booch/status/2105864893887082857) |
| 11 | Mike Koker | 返回图的 agent 才会被读 | [查看](https://x.com/rekokylnoeht/status/2105880139926028489) |
| 12 | 剑的 AI 实验室 | 每个解释配短例子与预期答案 | [查看](https://x.com/swordBluesy/status/2122843128629789076) |
| 13 | Ankit Gaurav | 提议 asd-explain skill | [查看](https://x.com/theankitgaurav/status/2105945337563410483) |
| 14 | Mukul | 生成 skill.md | [查看](https://x.com/mukulksachdeva/status/2106119153107263937) |
| 15 | Maksymilian Gajda | 写进 Hermes 的 SOUL.md | [查看](https://x.com/UGII_Auvere/status/2106090610255909076) |
| 16 | Boris Starkov | ElevenLabs 托管 MCP | [查看](https://x.com/ktoya_me/status/2106011146373546284) |
| 17 | Abdul Osman | HTML 不在词表里 | [查看](https://x.com/Osman808s/status/2105999827473735987) |
| 18 | Talat UYARER | 推荐 wait-what skill | [查看](https://x.com/talatuyarer/status/2105826020762992948) |
| 19 | Matt Kaan | 提到 ELI5 skill | [查看](https://x.com/mattkaanai/status/2106032064222937598) |
| 20 | Carlos E. Perez | Opus 5.5 讲解视频 | [查看](https://x.com/IntuitMachine/status/2105822832567734409) |
| 21 | Justin.md | 把 Claude 当老师 | [查看](https://x.com/JustinPerea/status/2105825705754055013) |
| 22 | Abram2k11 | 质疑 TTS 可用性 | [查看](https://x.com/abram2k1/status/2106077891234873383) |
| 23 | 0xbadhash | 原始人语对 STE100 | [查看](https://x.com/0xbadhash/status/2106254075524501697) |
| 24 | Azy | 要视频，嫌文字太长 | [查看](https://x.com/therealazy/status/2105820134690431472) |
| 25 | Grok | STE100 事实说明 | [查看](https://x.com/grok/status/2105989708505313436) |
| 26 | Grok | skill 模板示例 | [查看](https://x.com/grok/status/2106119300331323663) |

---

## 九、一句话收尾

这条推文的价值不在于推荐了 STE100，而在于示范了一件事：**给模型加外部约束，再换更合适的输出形式，人读起来就轻松了。**

回复区补充了三个我们容易忽略的事实：图不一定好读，视频已经真的能做，社区会第一时间把方法做成常驻配置。
