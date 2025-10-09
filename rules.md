# Translation Rules and Guidelines | 翻译规则和指南

## Project Overview | 项目概述

本项目旨在将《Agentic Design Patterns: A Hands-On Guide to Building Intelligent Systems》完整翻译为中英文对照版本，为中文读者提供优质的智能体设计模式学习资源。

## Core Principles | 核心原则

### 1. Accuracy and Faithfulness | 准确性和忠实性
- 翻译内容必须与原文含义完全一致
- 不得随意添加、删除或修改原文内容
- 保持原文的逻辑结构和论述顺序

### 2. Readability and Localization | 可读性和本土化
- 使用地道的简体中文表达
- 减少不必要的长句，适当断句
- 避免过多的口语化和不必要的过渡词
- 减少不必要的强调（加粗文本仅在非常必要时使用）

## Format Requirements | 格式要求

### 1. Document Structure | 文档结构
- 使用相同的格式（包含标题、内容概要、目录和正文）
- 各部分之间使用横线分隔（`---`）
- 在二级标题之间增加横线分隔，提升阅读体验

### 2. Markdown Syntax | Markdown 语法
- 使用正确的 Markdown 语法
- 避免因前后空格导致无法渲染的问题
- 所有代码块必须使用正确的格式标记

### 3. Bilingual Layout | 双语布局

#### For Short Content (致谢等短章节)
使用完整英文 + 完整中文的分隔格式：
```markdown
## English | 英文
[完整英文内容]

---

## Chinese | 中文
[完整中文翻译]
```

#### For Long Content (正文章节等)
使用段落对照格式：
```markdown
[English paragraph 1]

[对应的中文翻译段落 1]

[English paragraph 2]

[对应的中文翻译段落 2]
```

### 4. Highlighting System | 高亮系统

#### 主要方案（推荐）
- **HTML `<mark>` 标签**：`<mark>中文内容</mark>`
  - ✅ GitHub 完美支持
  - ✅ 黄色高亮背景，视觉效果佳
  - ✅ 所有现代浏览器兼容
  - 📝 使用场景：所有中文翻译内容

#### 特殊场景格式
- **表格对照**：适用于术语表、短句对比
- **引用块 + 粗体**：`> **中文内容**` 适用于重要强调
- **当前分隔格式**：长章节可保持 English/中文 分区结构

### 5. Mark + Markdown Rendering | 高亮与 Markdown 渲染
- <mark> 内不要依赖 Markdown 语法渲染加粗/斜体；请使用 HTML 标签：
  - 加粗：`<mark><strong>文本</strong></mark>`
  - 斜体：`<mark><em>文本</em></mark>`
- 列表标记必须在 <mark> 外，保证语义与渲染正确：
  - 无序：`- <mark>条目内容</mark>`（而非 `<mark>- 条目内容</mark>`）
  - 有序：`1. <mark>条目内容</mark>`（而非 `<mark>1. 条目内容</mark>`）
- 图注统一格式：`<mark><strong>图 N：</strong>说明文字</mark>`。
- 在中文段内引用英文缩写或术语时，使用中文全角括号：`大语言模型（LLM）`、`检索增强生成（RAG）`、`小语言模型（SLM）`。
- 中文引号统一为「」；避免在中文段中使用英文直引号（""）。
- 若需在高亮内显示强调性小标题（如「什么/为什么/经验法则/可视化总结」），使用：`<mark><strong>小标题：</strong>后续说明</mark>`。
- 不在正文中加入进度或编辑性标注（如「已完成/代码正常」），此类信息仅出现在 PR 描述或 Issue 中。

### 6. Lists & Emphasis Patterns | 列表与强调规范
- 列表内的关键短语可加粗，但仍放在 <mark> 中：`- <mark><strong>用例：</strong>说明……</mark>`。
- 需要中英文并列的行内强调时，中文放 <mark> 内，英文保持原样；不要在 <mark> 内再嵌套 Markdown 语法。
- 斜体文本在 <mark> 内请使用 `<em>`；避免使用 `*斜体*`。

### 7. Names, Titles & Captions | 姓名、头衔与标题
- 中文段中的人名/头衔如需加粗：`<mark><strong>姓名 / 头衔</strong></mark>`。
- 段内术语的第一次出现可使用「中文（EN）」形式；后续保持一致，不要在同一章节中变更写法。

### 8. Tone & Pronouns | 语气与人称
- 中文段优先使用「你/你的」保持一致；避免同段混用「您/你」。
- 技术用语直译不通顺时，优先保证中文可读性与专业性。

### 9. Quick QA Checks | 快速自检
- 搜索加粗在高亮内是否使用了 `<strong>`：`rg -n "<mark><strong>"`。
- 搜索列表是否把标记放在 <mark> 外：
  - 有序：`rg -n "^<mark>\s*\d+\."` 应为 0；
  - 无序：`rg -n "^<mark>\s*[-*+]"` 应为 0。
- 搜索图注是否使用统一格式：`rg -n "<mark><strong>图\s*\d+："`。
- 搜索中文段中的英文直引号：`rg -n "<mark>.*\".*"` 并替换为「」。
- 术语括注是否为中文全角括号：`（LLM）/（RAG）/（SLM）`。

### 10. PR Review Checklist | PR 审阅清单
- 双语对照是否一一对应，中文段均使用 `<mark>` 包裹。
- 高亮内的加粗/斜体是否使用 `<strong>/<em>`，未混用 Markdown。
- 列表、有序/无序格式是否正确（标记在 <mark> 外）。
- 图注格式是否统一；编号与正文引用一致。
- 术语（LLM/RAG/SLM 等）与括号、引号风格是否一致。
- 无进度性标注或注释性语句混入正文。

## Translation Guidelines | 翻译指南

### 1. Technical Terms | 技术术语
- 重要术语保留英文原文，用括号标注中文
- 例：智能体 (Agent)，提示链 (Prompt Chaining)
- 建立统一的术语表，确保前后一致

### 2. Spacing Rules | 空格规则
- 中文和英文之间增加一个空格
- 中文和数字之间增加一个空格
- 例：AI 系统，GPT 4 模型，21 个章节

### 3. Punctuation | 标点符号
- 中文语境下使用中文标点符号
- 保持原文的标点逻辑和节奏
- 引号使用中文样式：「」或 ""

### 4. Cultural Adaptation | 文化适配
- 适应中文读者的阅读习惯
- 保持专业性和准确性
- 避免过度本土化影响原意

## Quality Control | 质量控制

### 1. Review Process | 审校流程
- 每章完成后进行自我审校
- 检查术语一致性
- 验证格式规范性
- 确保链接和引用正确

### 2. Consistency Checks | 一致性检查
- 术语翻译保持统一
- 格式标准保持一致
- 文档结构保持规范

## File Naming Convention | 文件命名规范

```
00-Table-of-Contents.md                    # 目录
01-Dedication.md                          # 致谢
02-Acknowledgment.md                      # 鸣谢
03-Foreword.md                           # 前言
04-Thought-Leader.md                     # 思想领袖观点
05-Introduction.md                       # 介绍
06-What-Makes-Agent.md                   # 什么是智能体
07-Chapter-01-Prompt-Chaining.md        # 第一章：提示链
08-Chapter-02-Routing.md                 # 第二章：路由
09-Chapter-03-Parallelization.md        # 第三章：并行化
10-Chapter-04-Reflection.md              # 第四章：反思
11-Chapter-05-Tool-Use.md                # 第五章：工具使用
12-Chapter-06-Planning.md                # 第六章：规划
13-Chapter-07-Multi-Agent-Collaboration.md # 第七章：多智能体协作
...
rules.md                                 # 本规则文档
```

## Git Workflow | Git 工作流程

### 1. Commit Messages | 提交信息
使用清晰的英文提交信息：
```
Add: [chapter name] translation
Update: [chapter name] formatting
Fix: [specific issue] in [chapter name]
```

### 2. File Organization | 文件组织
- 保持仓库结构清晰
- 及时提交进度
- 添加适当的说明文档

## Common Translation Patterns | 常用翻译模式

### Technical Terms Dictionary | 技术术语词典
| English | 中文 | 备注 |
|---------|------|------|
| Agent | 智能体 | 核心概念 |
| Prompt Chaining | 提示链 | |
| Routing | 路由 | |
| Parallelization | 并行化 | |
| Reflection | 反思 | |
| Tool Use | 工具使用 | |
| Planning | 规划 | |
| Multi-Agent | 多智能体 | |
| Memory Management | 内存管理 | |
| Human-in-the-Loop | 人在回路中 | |
| RAG | 检索增强生成 | 保留英文缩写 |

## Quality Standards | 质量标准

### 1. Translation Quality | 翻译质量
- 准确性：100% 忠实原文
- 流畅性：符合中文表达习惯
- 专业性：保持技术文档的严谨性

### 2. Format Compliance | 格式合规性
- Markdown 语法正确率：100%
- 双语对照格式统一
- 高亮标记使用恰当

### 3. Consistency | 一致性
- 术语翻译前后统一
- 格式标准贯穿全文
- 文档结构保持规范

---

## Version History | 版本历史

- v1.0 (2025-01-09): 初始版本，建立基础规则和格式标准

---

*本规则文档将随着项目进展持续更新和完善。*
