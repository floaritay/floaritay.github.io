# 目录
- [1 简介](#1-简介)
- [2 安装](#2-安装)
  - [2.1 安装](#21-安装)
  - [2.2 跳过登录（使用第三方API）](#22-跳过登录使用第三方api)
- [3 快速开始](#3-快速开始)
  - [3.1 开始使用](#31-开始使用)
    - [3.1.1 常用命令速查表](#311-常用命令速查表)
  - [3.2 交互模式](#32-交互模式)
  - [3.3 操作说明](#33-操作说明)
  - [3.4 会话管理](#34-会话管理)
    - [3.4.1 恢复会话](#341-恢复会话)
    - [3.3.2 删除会话](#332-删除会话)
  - [3.4 上下文窗口](#34-上下文窗口)
  - [3.5 安全机制](#35-安全机制)
- [4 API 管理](#4-api-管理)
- [5 Claude Code for VS Code](#5-claude-code-for-vs-code)
  - [5.1 安装](#51-安装)
  - [5.2 提示框](#52-提示框)
- [6 项目结构](#6-项目结构)
  - [6.1 CLAUDE.md](#61-claudemd)
  - [6.2 CLAUDE.local.md](#62-claudelocalmd)
  - [6.3 .claude/settings.json](#63-claudesettingsjson)
  - [6.4 .claude/settings.local.json](#64-claudesettingslocaljson)
  - [6.5 .claude/commands/ 自定义斜杠命令](#65-claudecommands-自定义斜杠命令)
  - [6.6 .claude/rules/](#66-clauderules)
  - [6.7 .claude/skills/](#67-claudeskills)
  - [6.8 .claude/agents/](#68-claudeagents)
- [7 记忆](#7-记忆)
  - [7.1 记忆文件的层级结构](#71-记忆文件的层级结构)
  - [7.2 claude.md](#72-claudemd)
  - [7.3 Auto Memory](#73-auto-memory)
    - [7.3.1 触发自动记忆](#731-触发自动记忆)
    - [7.3.2 开启 / 关闭 Auto Memory](#732-开启-关闭-auto-memory)
  - [7.4 /memory 命令与快捷键](#74-memory-命令与快捷键)
- [8 skills](#8-skills)
  - [8.1 工作原理](#81-工作原理)
  - [8.2 为什么需要 Skills？](#82-为什么需要-skills)
  - [8.3 执行流程](#83-执行流程)
  - [8.4 SKILL.md 基本模板](#84-skillmd-基本模板)
  - [8.5 详细结构](#85-详细结构)
  - [8.6 示例](#86-示例)
  - [8.7 市场](#87-市场)
- [9 skills 使用实例](#9-skills-使用实例)
  - [9.1 安装](#91-安装)
  - [9.2 使用](#92-使用)
- [10 skill-creator](#10-skill-creator)
  - [10.1 安装 skill-creator](#101-安装-skill-creator)
  - [10.2 用 skill-creator 创建 Skill](#102-用-skill-creator-创建-skill)
- [11 插件](#11-插件)
  - [11.1 结构](#111-结构)
    - [11.1.1 插件清单（plugin.json）](#1111-插件清单pluginjson)
    - [11.1.2 斜杠命令（commands/）](#1112-斜杠命令commands)
  - [11.2 本地测试插件](#112-本地测试插件)
  - [11.3 插件市场](#113-插件市场)
  - [11.4 插件命令](#114-插件命令)
  - [11.5 从 .claude/ 迁移到插件](#115-从-claude-迁移到插件)
  - [11.6 什么时候用插件？](#116-什么时候用插件)
- [12 子代理](#12-子代理)
  - [12.1 内置的子代理](#121-内置的子代理)
  - [12.2 创建子代理](#122-创建子代理)
  - [12.3 子代理的作用范围](#123-子代理的作用范围)
  - [12.4 文件结构](#124-文件结构)
  - [12.5 使用子代理](#125-使用子代理)
  - [12.6 使用示例](#126-使用示例)
  - [12.7 子代理上下文与恢复](#127-子代理上下文与恢复)
  - [12.8 什么时候该用子代理？](#128-什么时候该用子代理)
- [13 MCP](#13-mcp)
  - [13.1 安装 MCP 服务器](#131-安装-mcp-服务器)
  - [13.2 管理 MCP 服务器](#132-管理-mcp-服务器)
  - [13.3 配置范围](#133-配置范围)
  - [13.4 配置文件示例](#134-配置文件示例)
  - [13.5 示例](#135-示例)
  - [13.6 在对话中使用 MCP](#136-在对话中使用-mcp)
  - [13.7 注意](#137-注意)
- [14 MCP使用实例](#14-mcp使用实例)
  - [14.1  GitHub 令牌设置](#141-github-令牌设置)
  - [14.2 然后与 GitHub 协作：](#142-然后与-github-协作)
- [15 钩子](#15-钩子)
  - [15.1 钩子事件类型说明](#151-钩子事件类型说明)
  - [15.2 示例：命令日志记录](#152-示例命令日志记录)
  - [15.3 常用钩子示例](#153-常用钩子示例)
    - [15.3.1 示例一  自动格式化 TypeScript 文件](#1531-示例一-自动格式化-typescript-文件)
    - [15.3.2 示例二  自动修复 Markdown 文件格式](#1532-示例二-自动修复-markdown-文件格式)
    - [15.3.3 示例三  禁止修改敏感文件](#1533-示例三-禁止修改敏感文件)
  - [15.4 官方示例：bash 命令验证器示例](#154-官方示例bash-命令验证器示例)
- [16 钩子参考手册](#16-钩子参考手册)
  - [16.1 配置文件路径](#161-配置文件路径)
  - [16.2 配置结构](#162-配置结构)
  - [16.3 匹配器规则（仅适用于工具类事件）](#163-匹配器规则仅适用于工具类事件)
  - [16.4 特殊配置技巧](#164-特殊配置技巧)
  - [16.5 扩展配置（Skill/Agent/斜杠命令）](#165-扩展配置skillagent斜杠命令)
  - [16.6 钩子事件--工具类事件（支持匹配器）](#166-钩子事件--工具类事件支持匹配器)
  - [16.7 会话/任务类事件（无匹配器）](#167-会话任务类事件无匹配器)
  - [16.8 待续](#168-待续)
- [17 CLI 参考手册](#17-cli-参考手册)
  - [17.1 核心 CLI 命令](#171-核心-cli-命令)
  - [17.2 模型控制与环境配置](#172-模型控制与环境配置)
  - [17.3 交互式会话斜杠命令](#173-交互式会话斜杠命令)
  - [17.4 效率和快捷键](#174-效率和快捷键)
  - [17.5 部分参数讲解](#175-部分参数讲解)
    - [17.5.1 --agents](#1751---agents)
    - [17.5.2 --system-prompt](#1752---system-prompt)
- [18 快捷键](#18-快捷键)
- [19 /命令](#19-命令)
- [20 输出样式](#20-输出样式)
  - [20.1 切换输出样式](#201-切换输出样式)
  - [20.2 创建自定义输出样式](#202-创建自定义输出样式)
- [21 并行任务](#21-并行任务)
  - [21.1 Subagents](#211-subagents)
    - [21.1.1 创建 Subagent](#2111-创建-subagent)
    - [21.1.2 调用 Subagent](#2112-调用-subagent)
  - [21.2 Agent Teams](#212-agent-teams)
    - [21.2.1 启用 Agent Teams](#2121-启用-agent-teams)
    - [21.2.2 使用 Agent Team](#2122-使用-agent-team)
    - [21.2.3 Agent Teams 架构](#2123-agent-teams-架构)
  - [21.3 Git Worktree](#213-git-worktree)
    - [21.3.1 使用 Git Worktree](#2131-使用-git-worktree)
    - [21.3.2 常用管理命令](#2132-常用管理命令)
- [Claude Code GitHub Actions](#claude-code-github-actions)
- [参考](#参考)

---
# 1 简介
...

# 2 安装

## 2.1 安装
Windows PowerShell:
>```bash
>irm https://claude.ai/install.ps1 | iex
>```
Windows CMD:
>```bash
>curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
>```
安装完成后,验证一下:
>```bash
>claude --version
>```
如果显示版本号，说明安装成功!

登录：
>```bash
>claude
>```
启动后，系统会提示你登录，在 Claude Code 界面中输入:
>```bash
>/login
>```
使用 Claude 订阅账号登录

## 2.2 跳过登录（使用第三方API）
1.定位配置文件：在你的用户目录下找到 .claude.json 文件。  

Windows: C:\Users\你的用户名\.claude.json

2.编辑文件：用记事本或VS Code打开，如果文件是空的也没关系，直接覆盖写入以下内容：  
>```json
>{
>    "hasCompletedOnboarding": true
>}
>```
这一行相当于告诉软件“新手引导已通过”，直接跳过登录界面

3.配置第三方模型（需使用第三方API）  
找到并编辑配置文件 ~/.claude/settings.json，填入你的中转站地址和API Key，模型可以自己指定  
>```json
>{
>    "env": {
>        "ANTHROPIC_BASE_URL": "你的中转站地址（如：https://api.siliconflow.cn/）",
>        "ANTHROPIC_AUTH_TOKEN": "你的中转站API Key",
>        "ANTHROPIC_DEFAULT_MODEL": "想用的模型名（如：Qwen/Qwen2.5-72B-Instruct）"
>     }
>}
>```

方法 2 (使用cc-switch管理第三方API)  
参考[cc-switch](../Vibe_Coding/CC_Switch.ipynb)

方法 3 (使用本地部署的大模型)  
参考[ollama](../basic/Ollama.ipynb)

# 3 快速开始

## 3.1 开始使用
配置完成后，进入一个您的代码工作目录，在终端中执行 claude 命令即可开始使用 Claude Code

输入` / `会列出可用的命令

### 3.1.1 常用命令速查表

命令行命令

| 命令 | 功能 | 示例 |
| ---- | ---- | ---- |
| `claude` | 启动交互模式 | `claude` |
| `claude "task"` | 执行一次性任务 | `claude "fix the build error"` |
| `claude -p "query"` | 执行一次查询后退出 | `claude -p "explain this function"` |
| `claude -c` | 在当前目录继续最近的对话 | `claude -c` |
| `claude -r` | 恢复之前的对话 | `claude -r` |
| `claude commit` | 创建 Git 提交 | `claude commit` |

 交互模式内命令
 
| 命令 | 功能 | 示例 |
| ---- | ---- | ---- |
| `/clear`或`reset` | 清空当前对话上下文，相当于进入一个新对话，不删除本地历史记录文件 | `/clear` |
| `/help` | 显示可用命令 | `/help` |
| `/login` | 登录或切换账号 | `/login` |
| `/resume` | 恢复之前的对话 | `/resume` |
| `exit` 或两下 `Ctrl+C` | 退出 Claude Code | `/exit` |
| `/init` | 在项目根目录生成 CLAUDE.md 文件，用于定义项目级指令和上下文 | `/init` |
| `/status` | 查看当前模型、API Key、Base URL 等配置状态 | `/status` |
| `/model <模型名称>`或`/model` | 切换模型 | `/model qwen3-coder-next` |
| `/plan` | 进入规划模式，仅分析和讨论方案，不修改代码 | `/plan` |
| `/compact` | 压缩对话历史，释放上下文窗口空间 | `/compact` |
| `/config` | 打开配置菜单，可设置语言、主题等 | `/config` |
| `/cost`或`/usage` | 查看当前会话消耗 | - |
| `/context` | 查看上下文使用情况 | - |
| `/export` | 导出对话 | - |
| `/tasks` | 管理后台任务 | - |
| `/memory` | 编辑 CLAUDE.md | - |
| `/docs` | 让 Claude 参考指定文档 | - |
| `/review` | 检查 Git 暂存区改动 | - |

## 3.2 交互模式
- Ask 模式：只读分析
- Plan 模式：只规划，不执行
- Edit 模式：直接修改文件

在终端中使用 Claude Code 时，你不需要手动切换模式开关，Claude 会根据你的指令内容，自动判断当前应进入哪一种模式。

不过，作为使用者，你必须在 Prompt 中清楚表达自己的意图，否则 Claude 很容易做出与你预期不一致的行为。

## 3.3 操作说明

| 符号 | 类型 | 本质作用 |
| ---- | ---- | ---- |
| `/` | Command（命令） | 执行内置操作 |
| `@` | Context（上下文） | 引用文件/代码/目录 |
| `!` | Bash 模式 | 直接执行终端命令，输入 ! 就会提示进入 Bash 命令模式。例如：！ls |
| `#` | Memory（记忆注入） | 把内容持久写入 CLAUDE.md 项目记忆，跨会话长期生效，例如：#config.yaml |
| `&` | Async（异步任务） | 后台/云端异步执行任务，不阻塞当前会话，可关闭终端后在 claude.ai/code 查看进度 |
| `\+Enter`或`Ctrl+j` | Multiline（多行输入） | 换行不发送，写多行内容，长需求描述一次性写完 |
| 无前缀 | 自然语言 | 普通任务指令 |

## 3.4 会话管理

### 3.4.1 恢复会话
1、直接恢复会话（最常用）
>```bash
># 直接恢复最近的一个会话
>claude --continue
># 选择会话列表中一个会话恢复
>claude --resume
>```
- 使用相同的会话 ID，从上次中断的地方继续
- 完整聊天历史全部恢复
- 注意：会话范围的权限不会自动恢复，需要你重新批准一次

2、分叉会话（类似git分支）
>```bash
>claude --continue --fork-session
># 或
>claude --resume "会话名称或ID" --fork-session
># 对话中使用 / 命令
>/branch [name]
>```
- 创建一个全新的会话 ID
- 保留到目前为止的所有聊天历史
- 原会话完全不受影响
- 同样需要重新批准权限
- 适用场景：想试试"不同实现方式"又不想把原对话搞乱时，并可以回到分支点。

3、 多个终端同时使用同一个会话（小心使用）
- 如果你在多个终端窗口都用同一个会话：
  - 所有消息会交错混在一起，对话会变得混乱
  - 每个终端当时只能看到自己输入的消息，但后续恢复时会看到全部交错内容
- 推荐做法：使用 --fork-session，给每个终端一个干净独立的新会话。
  
### 3.3.2 删除会话
对话记录保存在 `C:\Users\用户\.claude\projects\项目\`下，每个会话都是一个jsonl文件，直接删除即可。

## 3.4 上下文窗口
>```bash
># 压缩上下文
>/compact 
># 查看当前占用情况
>/context 
>```

省空间：
- 重要规则写进 CLAUDE.md
- 用 skills 和 subagents 减少不必要的上下文占用

## 3.5 安全机制
1、检查点
>```bash
>/rewind
># 或按两次 Esc 调出回滚界面，选择某次检查点回滚
>```

2、权限模式（按 Shift + Tab 快速切换）：
- 默认：每次改文件或跑命令都问你
- 自动接受编辑：只改文件不问，但命令仍会问
- 计划模式：只分析、不动手，先给你完整计划

还可以在 .claude/settings.json 里白名单信任命令（比如 npm test 永远不用问）

# 4 API 管理
使用第三方工具 CC Switch 可以帮我们轻松管理这几个热门工具的 API 配置：https://github.com/farion1231/cc-switch/

CC Switch 是一个 Claude Code / Codex / Gemini CLI 的全方位辅助工具,所有的 API 配置都能在它这有序管理。

各平台安装包下载地址：https://github.com/farion1231/cc-switch/releases。

使用参考[cc-switch](../Vibe_Coding/CC_Switch.ipynb)

# 5 Claude Code for VS Code
在 VS Code 编辑器中安装 Claude Code

## 5.1 安装
打开 VS Code，进入扩展市场，搜索 Claude Code 安装

安装完成后，点击右上角 Claude Code 图标，即可进入 Claude Code 页面

有账号的可以使用 /login 登录

也可以在设置中搜claudeCode，勾选 Disable Login Prompt 配置来关闭登录页面
![image.png](https://www.runoob.com/wp-content/uploads/2025/12/cc-runoob-4.png)

我们可以选中文件中的代码，让 Claude Code 帮我们解析说明或修改，选中后，会提示已经选中的代码行数：

按 Option + K（Mac）或 Alt + K（Windows/Linux），就能插入带文件路径和行号的 @ 提及

![image.png](https://www.runoob.com/wp-content/uploads/2026/03/820b4038-e214-4105-8676-f833833961be.png)

当 Claude 需要修改文件时，它会自动打开并排对比视图，左边显示文件原始内容，右边显示建议修改后的内容，然后询问您是否同意修改。
![image.png](https://www.runoob.com/wp-content/uploads/2026/03/vs-code-edits.png)


## 5.2 提示框
1、权限模式：

点击提示框底部的模式指示器，就可以切换权限模式。（同Claude Code）

你也可以在 VS Code 设置里搜索 claudeCode.initialPermissionMode 来设置默认模式。

2、命令菜单：

在提示框里输入 /（或点击输入框）就能打开命令菜单。

常用选项包括：附加文件、切换模型、开启扩展思考、查看使用量（输入 /usage）。

下方的"自定义"部分还能管理 MCP servers、hooks、记忆、权限和插件。

带有 终端图标 的命令，会在 VS Code 的集成终端里直接打开。

3、上下文用量指示器：

提示框下方会实时显示你已经用了多少 Claude 的上下文窗口（context）。

Claude 会自动帮你压缩内容；如果你想手动压缩，输入 /compact 即可。

4、扩展思考（Extended Thinking）：

遇到复杂问题时，可以让 Claude 多花点时间深度思考。

通过命令菜单（输入 /）切换开启/关闭。

5、多行输入：

按 Shift + Enter 可以换行，不用立刻发送消息。

在弹出的"其他"自由文本框里也同样适用。

6、引用文件和文件夹（@ 提及功能）

输入 @ 后面跟文件名或文件夹名，Claude 就会自动读取内容，可以回答问题或直接修改。（支持模糊匹配，不用打全名）

# 6 项目结构
>```md
>your-project/
>├── CLAUDE.md                    ← 团队共享指令，提交到 git
>├── CLAUDE.local.md              ← 个人覆盖，被 git 忽略
>├── .claude/
>│   ├── settings.json            ← 权限 + 配置，提交到 git
>│   ├── settings.local.json      ← 个人权限，被 git 忽略
>│   ├── commands/                ← 自定义斜杠命令（旧，仍兼容）
>│   │   ├── review.md            →  /project:review
>│   │   ├── fix-issue.md         →  /project:fix-issue
>│   │   └── deploy.md            →  /project:deploy
>│   ├── rules/                   ← 模块化指令文件（全局生效）
>│   │   ├── code-style.md
>│   │   ├── testing.md
>│   │   └── api-conventions.md
>│   ├── skills/                  ← 自动调用的工作流
>│   │   ├── security-review/
>│   │   │   └── SKILL.md
>│   │   └── deploy/
>│   │       └── SKILL.md
>│   └── agents/                  ← 子代理角色定义
>│       ├── code-reviewer.md
>│       └── security-auditor.md
>├── src/
>│   └── CLAUDE.md          # 仅在处理 src/ 文件时加载
>└── tests/
>    └── CLAUDE.md          # 仅在处理 tests/ 文件时加载           
>```

## 6.1 CLAUDE.md　
在项目根目录执行 `/init` 命令，Claude 会自动扫描你的代码库，然后生成一份专属于项目的 CLAUDE.md 文件。

这是 Claude 进入项目时第一个读取的文件，相当于项目欢迎手册。

CLAUDE.md 放置在项目根目录，所有团队成员共享，它告诉 Claude：这个项目是什么、如何运行、有什么约定。

Claude 会自动递归读取父目录中的 CLAUDE.md。子文件夹内可再放一个 CLAUDE.md，Claude 会将两层指令合并理解。

CLAUDE.md 结构示例：


```python
# 项目名称

## 项目概述
简述这个项目的目的和功能。

## 技术栈
- Frontend: React + TypeScript
- Backend: Node.js + Express
- Database: PostgreSQL

## 目录结构
- `src/components/` - React 组件
- `src/api/`        - API 层
- `tests/`          - 测试文件

## 常用命令
- 启动开发服务器：`pnpm dev`
- 运行测试：`pnpm test`
- 代码检查：`pnpm lint`

## 开发规范
- 使用 TypeScript strict 模式
- 优先使用 interface 而非 type
- 禁止使用 any，使用 unknown 替代
```

### 文件位置与层级

项目的核心文件结构如下： 
```
your-project/
├── CLAUDE.md                  # 项目主记忆文件（团队共享）
├── .claude/
│   ├── settings.json          # Hooks、权限、环境配置
│   ├── settings.local.json    # 个人配置（建议加入 .gitignore）
│   └── commands/              # 自定义斜杠命令
│       └── my-command.md
└── .mcp.json                  # MCP 服务配置
```
```


```python
# 项目约定

## 技术栈
- 前端：Next.js 15、TypeScript 5.7、Tailwind CSS 4
- 后端：Node.js 22、Prisma 6
- 测试：Vitest 3.2

## 代码规范
- 始终使用函数式 React 组件
- 文件名使用 kebab-case
- 测试文件与源码放在同一目录

## 常用命令
- 构建：`pnpm build`
- 测试：`pnpm test`
- 启动开发服务器：`pnpm dev`

## API 约定
- 所有 API 路由以 `/api/v1/` 开头
- 错误响应格式：`{ error: string, code: number }`
```

- 使用祈使句和简短列表，而非叙述性段落
- 包含具体的版本号和命令
- 加入代码示例（5 行示例胜过 50 字说明）
- 控制在 200 行以内（超过部分不会在会话开始时加载）
- 避免模糊指令如"遵循最佳实践"或"写干净的代码"
- 避免过多通用规则（只放这个项目独有的约定）
- 过时的信息（建议每月审查一次）

## 6.2 CLAUDE.local.md
个人专属的覆盖层，叠加在 CLAUDE.md 之上。

CLAUDE.local.md 存放只与你本人相关的偏好或临时指令，不应共享给团队。

示例如下：


```python
# 我的本地覆盖

本地数据库地址：localhost:5433（非默认端口）

调试时请优先输出详细日志。

## 临时规则（本次任务用）
目前专注于重构 auth/ 模块，其他模块暂时不要改动。
```

## 6.3 .claude/settings.json
团队共享的配置文件，控制 Claude 允许或禁止执行哪些操作，作为团队安全基线。

示例如下


```python
{
  "permissions": {
    "allow": [
      "Bash(npm run *)",
      "Bash(pytest:*)",
      "Bash(git diff:*)",
      "Bash(git log:*)"
    ],
    "deny": [
      "Bash(rm -rf *)",
      "Bash(curl * | bash)"
    ]
  }
}
```

## 6.4 .claude/settings.local.json
个人本地权限覆盖，临时放开或收紧某些权限，不影响团队其他成员。

示例如下


```python
{
  "permissions": {
    "allow": [
      "Bash(rm ./tmp/*)"
    ]
  }
}
```

## 6.5 .claude/commands/ 自定义斜杠命令
目录下每个 .md 文件自动映射为一条 `/project:文件名` 命令。

示例：commands/review.md


```python
# Code Review

请对当前修改执行完整的代码审查：

1. 检查是否有安全漏洞（SQL 注入、XSS 等）
2. 验证错误处理是否完整
3. 确认测试覆盖率是否达标
4. 检查是否符合代码风格规范
5. 评估性能影响

用中文输出结构化审查报告，按严重程度排列问题。
```

## 6.6 .claude/rules/
将 CLAUDE.md 中的规则拆分模块化存放，Claude 在整个会话中始终遵守。适合存放长期稳定执行的行为约定，避免 CLAUDE.md 过于臃肿。

示例：rules/code-style.md


```python
# Code Style Rules

- TypeScript 严格模式，禁用 any 类型
- 函数长度不超过 40 行，超出则拆分
- 优先使用 const，避免使用 let
- 导入顺序：标准库 → 三方包 → 本地模块
- 所有 export 的函数/类型需要 JSDoc 注释
- 禁止使用 console.log，使用项目 logger
```

## 6.7 .claude/skills/
Skills 是更高级的复合工作流。当 Claude 判断某个任务适合某个 skill 时，会自动读取并执行对应的 SKILL.md，无需手动调用。

每个 skill 是一个子目录，目录内包含 SKILL.md。

示例：skills/security-review/SKILL.md


```python
# Security Review Skill

## 触发条件
当用户请求代码审查、代码涉及认证/授权/加密/用户输入处理时自动触发。

## 执行步骤
1. 扫描 SQL 注入风险（检查所有数据库查询）
2. 检查 XSS 防护（验证输出转义）
3. 审计权限边界（确认最小权限原则）
4. 检查敏感数据处理（日志、错误信息中是否泄露）
5. 输出 OWASP Top 10 对照检查表

## 输出格式
按 CVSS 评分排列，高危问题优先展示。
```

## 6.8 .claude/agents/
定义可被主 Claude 实例派遣的专业子代理。在复杂任务中，主代理将子任务委派给对应专家角色，实现多代理协作。子代理在隔离上下文中运行，拥有独立的权限范围。

示例：agents/code-reviewer.md


```python
---
name: code-reviewer
description: 资深代码审查员，专注代码质量与可维护性
---

# 代码审查员

## 角色定位
你是一名拥有 10 年经验的资深工程师，专注于代码可读性、性能优化和最佳实践。

## 审查重点
- 命名是否清晰表达意图
- 函数/类的单一职责原则
- 边界条件和错误处理
- 性能瓶颈（N+1 查询、不必要的循环等）

## 权限
只读访问，不直接修改文件。

## 输出格式
使用 Markdown 表格输出，包含：问题位置、严重程度、建议方案。
```

# 7 记忆
Claude Code 没有跨会话的自动记忆——每个新会话都从一个全新的上下文窗口开始。

| 机制 | 谁来写 | 适合什么 |
| --- | --- | --- |
| ./CLAUDE.md 文件 | 用户手动编写 | 用户级记忆，包括个人偏好等 |
| CLAUDE.md 文件 | 开发者手动编写 | 项目级记忆，包括项目规范、团队约定等 |
| Auto Memory（自动记忆） | Claude 自动写入 | 从你的纠正和偏好中积累的经验 |

输入`/memory`可以查看与管理这三个文件

## 7.1 记忆文件的层级结构

| 优先级 | 配置类型           | 位置/路径                                      | 特性描述                                                                 |
|--------|--------------------|-----------------------------------------------|------------------------------------------------------------------------|
| 最高   | 企业级配置         | -                                             | Enterprise policy，只读                                                  |
| 次高   | 用户级 CLAUDE.md   | `~/.claude/CLAUDE.md`                         | 对所有项目生效                                                           |
| 中等   | 项目级 CLAUDE.md   | 项目根目录                                    | 随 Git 提交共享给团队                                                    |
| 最低   | 子目录级 CLAUDE.md | `src/`、`api/`、`tests/` 等子目录            | 按上下文加载                                                             |


## 7.2 claude.md 
CLAUDE.md 是一个放在项目根目录（或子目录）的 Markdown 文件。Claude Code 在每次新会话启动时，会自动将其注入系统提示词。它是你可以配置的长期记忆。

推荐的 CLAUDE.md 结构
>```md
># 项目约定
>
>## 技术栈
>- 前端：Next.js 15、TypeScript 5.7、Tailwind CSS 4
>- 后端：Node.js 22、Prisma 6
>- 测试：Vitest 3.2
>
>## 代码规范
>- 始终使用函数式 React 组件
>- 文件名使用 kebab-case
>- 测试文件与源码放在同一目录
>
>## 常用命令
>- 构建：`pnpm build`
>- 测试：`pnpm test`
>- 启动开发服务器：`pnpm dev`
>
>## API 约定
>- 所有 API 路由以 `/api/v1/` 开头
>- 错误响应格式：`{ error: string, code: number }`
>```

- 使用祈使句和简短列表，而非叙述性段落
- 包含具体的版本号和命令
- 加入代码示例（5 行示例胜过 50 字说明）
- 控制在 200 行以内（超过部分不会在会话开始时加载）

避免：
- 模糊指令如"遵循最佳实践"或"写干净的代码"
- 过多通用规则（只放这个项目独有的约定）
- 过时的信息（建议按时审查）

## 7.3 Auto Memory

文件结构
>```md
>~/.claude/projects/<project>/memory/
>├── MEMORY.md          # 简洁的索引文件，每次会话开始时加载（前 200 行）
>├── debugging.md       # 调试模式的详细笔记
>├── api-conventions.md # API 设计决策
>└── ...                # Claude 创建的其他主题文件
>```
MEMORY.md 是整个记忆目录的索引，Claude 通过它来追踪各文件中存储的内容。

### 7.3.1 触发自动记忆
当你告诉 Claude 某些事情时，它会自动保存到记忆中：
>```md
>用户：始终使用 pnpm，不要用 npm
>用户：记住 API 测试需要本地运行 Redis 实例
>用户：我们的日期格式统一用 ISO 8601
>```

### 7.3.2 开启 / 关闭 Auto Memory
方式一：通过 /memory 命令切换（见下节）

方式二：在项目设置中配置
>```js
>// .claude/settings.json
>{
>  "autoMemoryEnabled": false
>}
>```
方式三：环境变量
>```bash
>export CLAUDE_CODE_DISABLE_AUTO_MEMORY=1
>```
注意： Auto Memory 是本地机器级别的，同一 Git 仓库的所有 worktree 和子目录共享一个记忆目录，但不会跨机器或云环境同步。

## 7.4 /memory 命令与快捷键
在 Claude Code 会话中输入 /memory，可以：
- 查看当前会话加载的所有 CLAUDE.md 和规则文件列表
- 切换 Auto Memory 的开启/关闭状态
- 打开 Auto Memory 文件夹链接
- 选择任意文件在编辑器中打开编辑

`#` 快捷键 —— 快速添加记忆  

按下 # 键，输入你想记住的内容，按回车——Claude Code 会自动将其写入对应的 CLAUDE.md 文件。

适合：
- 记录项目约定
- 保存常用 Bash 命令
- 记下代码风格细节

| 场景 | 推荐做法 |
| --- | --- |
| 团队共享规范 | 项目根目录的 CLAUDE.md，提交到 Git |
| 个人偏好 | ~/.claude/CLAUDE.md（用户级） |
| 模块特定规则 | 子目录 CLAUDE.md |
| 让 Claude 自学 | 开启 Auto Memory，口头告知偏好 |
| 临时告知上下文 | @docs/filename.md 按需引用，不要塞进 CLAUDE.md |
| 任务跟踪 | 在 Markdown 文件中使用 [ ] 复选框 |


# 8 skills
skills 本质上是一个模块化的 Markdown 文件，能教会 AI 工具执行特定任务，且支持自动触发、团队共享与工程化管理，彻底告别重复的提示词输入。

一个 Skill 就是一个文件夹，里面必须有一个 SKILL.md 文件（包含说明和元数据），可选其他资源文件（如脚本、示例、参考文档）。

简单来说，过去我们用提示词（prompt）教 AI 做事，现在用 Agent Skills 可以把提示词 + 资源打包成可复用、可共享的技能包，更高效、更可靠。

## 8.1 工作原理
渐进式披露，分三层加载：
- 层级 1：技能发现 -- AI 先读取所有技能的元数据（name 和 description），判断任务是否相关，这些元数据始终在系统提示中。
- 层级 2：加载核心指令 -- 如果相关，AI 自动读取 SKILL.md 的正文内容，获取详细指导。
- 层级 3：加载资源文件 -- 只在需要时读取额外文件（如脚本、示例），或通过工具执行脚本。

## 8.2 为什么需要 Skills？

普通 AI 代理很聪明，但缺少特定上下文时容易出错。例如：
- 团队有自己的代码规范，但 AI 每次都要手动提醒。
- 需要处理 PDF 表单、调试 GitHub Actions 等复杂流程，AI 可能不知道最佳实践。

Agent Skills 解决这些问题：
- 自动触发：AI 根据任务自动加载相关技能，无需手动输入长提示。
- 可复用 & 可共享：一次创建，全团队或社区使用，支持 Git 版本控制。
- 高效利用上下文：采用渐进式披露（progressive disclosure），只加载需要的部分，避免上下文窗口溢出。
- 跨平台：同一个 Skill 可以在 Claude、VS Code Copilot、Cursor 等工具中使用。

## 8.3 执行流程
1. 从用户指令开始，先进行 Skill 意图识别，决定是否进入受控执行路径。
2. 命中 Skill 后，系统加载 SKILL.md，建立工具权限与行为边界，再结合上下文进行推理。
3. 只有在确实需要时才调用被允许的外部工具，否则在规则内完成逻辑。
4. 最终结果经过约束整合后输出，用户的下一次输入触发新一轮完整流程。

## 8.4 SKILL.md 基本模板
>```md
>---
>name: your-skill-name
>description: What it does and when Claude should use it
>---
>
># Insert instructions below
>
>## Instructions
>Clear, concrete, actionable rules.
>
>## Examples
>- Example usage 1
>- Example usage 2
>
>## Guidelines
>- Guideline 1
>- Guideline 2
>```

元数据字段说明

| 字段 | 必填 | 说明 |
| ---- | ---- | ---- |
| name | 否 | Skill 显示名称，默认使用目录名，仅支持小写字母、数字和短横线（最长 64 字符） |
| description | 推荐 | 技能用途及使用场景，Claude 根据它判断是否自动应用 |
| argument-hint | 否 | 自动补全时显示的参数提示，如 [issue-number]、[filename] [format] |
| disable-model-invocation | 否 | 设为 true 禁止 Claude 自动触发，仅能手动 /name 调用（默认 false） |
| user-invocable | 否 | 设为 false 从 / 菜单隐藏，作为后台增强能力使用（默认 true） |
| allowed-tools | 否 | Skill 激活时 Claude 可无授权使用的工具 |
| model | 否 | Skill 激活时使用的模型 |
| context | 否 | 设为 fork 时在子代理上下文中运行 |
| agent | 否 | 子代理类型（配合 context: fork 使用） |
| hooks | 否 | 技能生命周期钩子配置 |

动态变量说明

| 变量 | 说明 |
| ---- | ---- |
| $ARGUMENTS | 调用 Skill 时传入的所有参数 |
| $ARGUMENTS[N] | 按索引访问参数，如 $ARGUMENTS[0] |
| $N | 简写方式，如 $0 表示第一个参数 |
| ${CLAUDE_SESSION_ID} | 当前会话 ID，用于日志、临时文件、关联输出 |

例如：
>```md
>---
>name: session-logger
>description: 记录当前会话活动
>---
>
>请将以下内容写入日志文件：
>
>logs/${CLAUDE_SESSION_ID}.log
>
>$ARGUMENTS
>```
调用：
>```bash
>/session-logger 用户登录成功
>```

## 8.5 详细结构
Skills 存放在 ~/.claude/skills/（个人全局）或项目目录下的 .claude/skills/（项目专用）。
>```md
>my-skill/
>├── SKILL.md
>├── reference.md
>├── examples.md    # 存放示例文件
>└── scripts/
>    └── helper.py
>```

## 8.6 示例
创建项目目录
>```bash
>mkdir claude-test
>```
进入该目录，创建 skills 的目录与文件：
>```bash
>mkdir -p .claude/skills/python-naming-standard
>```
编辑 SKILL.md
>```md
>---
>name: Python 内部命名规范技能
>description: 当用户要求重构、审查或编写 Python 代码时，请参考此规范。
>---
>
>## 指令
>1. 所有的内部辅助函数必须以 `_internal_` 前缀命名。
>2. 如果发现不符合此规则的代码，请自动提出修改建议。
>3. 在执行 `claude commit` 前，必须检查此规范。
>
>## 参考示例
>- 正确：`def _internal_calculate_risk():`
>- 错误：`def _calculate_risk():`
>- 错误：`def calculate_risk():`
>```
你也可以让Claude帮你创建skill，例如：

对 Claude 说："帮我把我刚才教你的关于 Docker 的配置逻辑总结成一个 Skill"，它会自动在相应目录为你生成文件。

你的项目现在看起来应该是这样的：
>```md
>claude-test/
>├─ src/
>│  └─ test.py              # 项目源码
>├─ .claude/
>│  ├─ skills/
>│  │  └─ python-naming-standard/
>│  │     ├─ skill.md       # Skill 定义（YAML + Instructions，机器可执行）
>│  │     └─ README.md      # Skill 说明（人类阅读，可选）
>│  └─ config.yml           # Claude 项目级配置（可选）
>├─ .gitignore
>└─ README.md               # 项目整体说明
>```
终端执行以下命令启动 Claude Code：
>```bash
>claude
>```
输入任务：
>```md
>帮我写一个计算用户折扣的函数
>```
Claude 就会会扫描已安装的 Skills，发现你的请求涉及 "Python 代码编写"，匹配了 python-naming-standard。

另外我们可以在 .claude/skills/ 下添加以下目录：

在同一文件夹添加：

- examples/：存放示例文件。
- references/：存放参考文档。
- scripts/：存放可执行脚本（例如 Python 处理 PDF）。

## 8.7 市场
官方市场：访问 https://github.com/anthropics/skills 仓库下载预设的技能

将本仓库注册官方 Skill 市场（只需一次）：
>```bash
>/plugin marketplace add anthropics/skills
>```
然后就可以使用` /plugin `查看与下载插件。


也可直接通过命令安装官方技能：
>```bash
>/plugin install document-skills@anthropic-agent-skills
>/plugin install example-skills@anthropic-agent-skills
>```
重载技能（当你添加了新的技能或修改了现有技能后）：
>```bash
>/reload-plugins
># 或重启
>```

查看已装技能
>```bash
>/skills
>```

相关资源

| 资源说明 | 链接 |
| ---- | ---- |
| Skill 聚合入口 | https://skills.sh/ |
| Skills 市场（中文界面） | https://skillsmp.com/zh |
| Agent Skills 官方标准站点 | https://agentskills.io |
| Anthropic 官方工程文章（Agent Skills 实战理念） | https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills |
| VS Code Copilot Agent Skills 文档 | https://code.visualstudio.com/docs/copilot/customization/agent-skills |
| Anthropic 官方 Skills GitHub 仓库 | https://github.com/anthropics/skills |
| Claude 技能精选列表（Awesome 系列） | https://github.com/ComposioHQ/awesome-claude-skills |
| 软件开发自动化工作流 Skills 集合 | https://github.com/obra/superpowers |
| 自动生成 Skill 的 Skill（官方示例） | https://github.com/anthropics/skills/tree/main/skills/skill-creator |

推荐skills

| Skill 名称    | 核心作用  | 安装命令|
|--------------|--------------|---------------|
| find-skills (vercel-labs)  | 技能搜索与推荐中心 | `npx skills add vercel-labs/skills`|
| vercel-react-best-practices| React / Next 性能优化规范    | `npx skills add vercel-labs/agent-skills --skill vercel-react-best-practices` |
| frontend-design (anthropics)    | 高质量 UI 设计能力 | `npx skills add anthropics/skills --skill frontend-design`   |
| web-design-guidelines | Web 可访问性与 UX 规范  | `npx skills add vercel-labs/agent-skills --skill web-design-guidelines`|
| remotion-best-practices   | React 视频制作最佳实践  | `npx skills add remotion-dev/skills --skill remotion-best-practices`   |
| brainstorming (superpowers) | 结构化思考与规划能力    | `npx skills add obra/superpowers --skill brainstorming`   |
| agent-browser| 浏览器自动化控制   | `npx skills add vercel-labs/agent-browser`  |
| browser-use  | 高性能浏览器交互   | `npx skills add browser-use/browser-use`    |
| supabase-postgres-best-practices| Supabase / PostgreSQL 优化   | `npx skills add supabase/agent-skills --skill supabase-postgres-best-practices` |
| azure-cost-optimization    | Azure 云成本优化   | `npx skills add microsoft/github-copilot-for-azure --skill azure-cost-optimization` |
| cloudflare/skills | Workers 与边缘计算实践  | `npx skills add cloudflare/skills` |
| redis/agent-skills| Redis 高级模式与反模式  | `npx skills add redis/agent-skills`|
| vercel-composition-patterns| React 组合模式规范 | `npx skills add vercel-labs/agent-skills --skill vercel-composition-patterns` |
| vercel-react-native-skills  | React Native 官方最佳实践    | `npx skills add vercel-labs/agent-skills --skill vercel-react-native-skills`   |
| sleek-design-mobile-apps   | 现代移动 App 设计指南    | `npx skills add sleekdotdesign/agent-skills --skill sleek-design-mobile-apps`  |
| ui-skills | 设计师级 UI 与交互实践  | `npx skills add ibelick/ui-skills` |
| pdf (anthropics)  | PDF 生成与解析能力 | `npx skills add anthropics/skills --skill pdf`   |
| seo-audit | SEO 审计与优化 | `npx skills add coreyhaines31/marketingskills --skill seo-audit`  |
| skill-creator| 自定义 Skill 构建能力   | `npx skills add anthropics/skills --skill skill-creator`  |
| code-review-expert| 专业级代码审查能力 | `npx skills add sanyuan0704/code-review-expert`  |


# 9 skills 使用实例
本章节我们将介绍一个支持多平台、多框架的专业级 UI/UX SKILL 插件 - UI UX Pro Max。

## 9.1 安装
通过 Claude Marketplace 安装

在 Claude Code 中执行以下两条命令

注册插件市场源：
>```bash
>/plugin marketplace add nextlevelbuilder/ui-ux-pro-max-skill
>```
安装插件：
>```bash
>/plugin install ui-ux-pro-max@ui-ux-pro-max-skill
>```

也可以使用 npx 安装
- npx skills find 关键词
- npx skills add 完整GitHub链接 --skill 技能名
- npx skills list -g
- npx skills update
>```bash
>npx skills add https://github.com/nextlevelbuilder/ui-ux-pro-max-skill --skill ui-ux-pro-max
>```
安装成功后重启 Claude Code 就可以使用了

可以使用 /skills 命令查看已经安装的skill。

通过插件安装的 Skill，目录放在 ～/.claude/plugins/marketplaces。

## 9.2 使用
直接输入需求："为宠物美容服务搭建一个着陆页，风格活泼亲和，并设置预约类行动召唤按钮。"

会提示是否使用我们安装的 skill 来设计，一路回车就好了

# 10 skill-creator
Anthropic 官方提供的 Skill 开发助手，帮助开发者创建、优化和打包技能。

GitHub 地址：https://github.com/anthropics/skills/tree/main/skills/skill-creator

## 10.1 安装 skill-creator
>```bash
>npx skills add https://github.com/anthropics/skills --skill skill-creator
>```
或者：
>```bash
>claude install anthropics/skills/skill-creator
>```
安装完成后，本地会下载该 Skill，其中包含：
>```md
>skills/skill-creator/
>├── SKILL.md          ← 核心说明文件
>├── agents/           ← 内置的评审助手
>├── eval-viewer/      ← 测试结果可视化工具
>├── references/       ← 参考文档（数据格式说明等）
>└── scripts/          ← 自动化脚本（打包、测评等）
>```
在 Claude 中调用：
>```bash
>/skill-creator
>```

## 10.2 用 skill-creator 创建 Skill
Claude 会先问你几个问题，帮你把需求想清楚。你不需要一次说完所有细节，像聊天一样回答就行。

示例：
>```md
>你：我想做一个 Skill，把会议录音的文字稿整理成结构化的会议纪要。
>
>Claude：好的，我来问几个问题帮你确认需求：
>        1. 纪要里需要包含哪些内容？（比如：时间、参与人、决议、行动事项……）
>        2. 输出格式是 Word 文档、Markdown，还是直接在对话里回复？
>        3. 有没有固定的纪要模板？
>
>你：需要包含会议主题、时间、参与人、讨论要点、决议事项、
>    下一步行动（含负责人和截止日期）。
>    输出 Word 文档。
>    有模板，我来上传。
>```

# 11 插件
插件（Plugin）是 Claude Code 中最高级别的扩展机制，用于将命令、代理、Skills、钩子、MCP、LSP 等能力打包、版本化、共享和分发。

插件 = 一组可复用的 Claude Code 扩展能力集合

先在 .claude/ 中迭代 → 稳定后打包为插件

都是斜杠 `/` 显式触发:
- 内置原生命令
- 插件和技能自带命令
- 手动装的 Skill 自定义命令

## 11.1 结构
>```
>my-plugin/
>├── .claude-plugin/
>│   └── plugin.json     # 插件清单（必需）
>├── commands/           # 斜杠命令
>├── agents/             # 子代理
>├── skills/             # Skills
>├── hooks/              # 钩子
>├── .mcp.json           # MCP 配置
>└── .lsp.json           # LSP 配置
>```
.claude-plugin/ 目录中只能放 plugin.json

其他目录必须在插件根目录

### 11.1.1 插件清单（plugin.json）

| 字段 | 作用 |
| ---- | ---- |
| name | 唯一标识 + 命令命名空间 |
| description | 插件市场中展示 |
| version | 语义化版本控制 |
| author | 可选，归属说明 |



```python
{
  "name": "my-first-plugin",
  "description": "A greeting plugin to learn the basics",
  "version": "1.0.0",
  "author": { "name": "Your Name" }
}
```

### 11.1.2 斜杠命令（commands/）
每个命令 = 一个 Markdown 文件

示例：commands/hello.md ， 对应命令 /my-first-plugin:hello

commands/hello.md内容示例:
>```
>---
>description: Greet the user with a friendly message
>---
>
>Greet the user warmly and ask how you can help them today.
>```

## 11.2 本地测试插件
- 不需要安装
- 修改后需重启 Claude Code
- 支持同时加载多个插件

使用 --plugin-dir 直接加载插件目录：`claude --plugin-dir ./my-plugin`

加载多个插件：`claude --plugin-dir ./plugin-a --plugin-dir ./plugin-b`


## 11.3 插件市场
插件通过市场分发，本质是一个插件目录仓库。

运行 `/plugin → Discover`

安装 `/plugin install plugin-name@claude-plugins-official`

安装范围

| 范围       | 说明                  |
|------------|-----------------------|
| 用户范围   | 仅你自己，所有项目    |
| 项目范围   | 当前仓库，团队共享    |
| 本地范围   | 当前仓库，仅你        |


## 11.4 插件命令
>```bash
>/plugin                # 打开插件管理器
>/plugin install         # 安装插件
>/plugin uninstall       # 卸载
>/plugin enable/disable  # 启用 / 禁用
>/plugin marketplace add # 添加市场
>/plugin marketplace rm  # 移除市场
>```

## 11.5 从 .claude/ 迁移到插件

| 原来          | 迁移后                  |
|---------------|-------------------------|
| .claude/commands | plugin/commands       |
| .claude/agents   | plugin/agents         |
| settings.json hooks | plugin/hooks/hooks.json |

迁移后：
- 插件版本优先生效
- 可删除旧 .claude/ 配置避免重复

## 11.6 什么时候用插件？
- 已经有稳定的 Claude 工作流
- 你在反复复制 .claude/
- 团队成员开始问你："这个怎么配置？"
- 你希望 Claude 像 IDE 插件一样可控

# 12 子代理
子代理（Subagent），用于处理特定类型的任务，从而获得更好的上下文管理、更强的约束控制和更高的执行效率。

子代理是运行在独立上下文窗口中的专用 AI 助手。每个子代理都可以拥有：
- 独立的系统提示（System Prompt）
- 独立的上下文（不污染主对话）
- 指定的模型（Sonnet / Haiku / Opus）
- 明确的工具访问权限
- 独立的权限模式
- 生命周期钩子（Hooks）
- 跨会话持久记忆（Memory）

当 Claude 判断你的请求符合某个子代理的描述（description）时，就会自动将任务委托给该子代理，由它独立完成并返回结果。

子代理只接收自身的系统提示和基础环境信息（如工作目录），不会继承完整的 Claude Code 系统提示。这保证了行为的纯净和可控。

## 12.1 内置的子代理
Claude Code 已内置多种子代理，通常会自动使用，你不需要手动配置。

1、Explore（探索代理）

用途：只读搜索与分析代码库
- 模型：Haiku（速度快、延迟低）
- 工具：只读工具（不能 Edit / Write）
- 场景：搜索文件、理解代码结构、查找定义和引用

Claude 会在需要看代码但不改代码时自动使用 Explore。支持不同探索深度：quick / medium / very thorough。

2、Plan（规划代理）

用途：计划模式下的代码库研究
- 模型：继承主对话
- 工具：只读工具
- 场景：在 Plan 模式中理解项目，为后续方案制定收集上下文

在不产生嵌套代理的前提下，安全收集规划所需信息。

3、General-purpose（通用代理）

用途：复杂、多步骤任务
- 模型：继承主对话
- 工具：全部工具
- 场景：需要"看 + 改 + 推理"、多步骤代码修改、综合分析后给出结论

4、其他内部代理（无需手动使用）

|代理	|说明|
|---|---|
|Bash	|在独立上下文中运行命令|
|statusline-setup	|配置状态栏|
|Claude Code Guide	|解答 Claude Code 使用问题|

## 12.2 创建子代理
使用 `/agents` 命令

1、打开子代理管理界面
>```bash
>/agents
>```
/agents 命令提供完整的子代理管理能力：查看所有可用子代理（内置/用户级/项目级/插件）、创建、编辑、查看同名冲突时哪个生效。

2、创建用户级子代理
- 选择 Create new agent
- 选择 User-level
- 保存位置：~/.claude/agents/（所有项目可用）

3、使用 Claude 自动生成

示例描述：
>```
>一个代码改进代理，扫描项目文件，
>针对可读性、性能和最佳实践提出建议，
>并给出改进示例。
>```
Claude 会生成系统提示和初始配置，你可以按 `e` 手动编辑。

4、选择工具权限
- 只做代码审查 → 仅勾选只读工具
- 需要改代码 → 保留 Edit / Write

5、选择模型

推荐：Sonnet（分析能力与速度平衡）

6、选择记忆范围（可选）
- 选择 User：在 ~/.claude/agent-memory/ 建立持久记忆，跨所有项目积累经验
- 选择 None：不保留学习成果，每次从零开始

7、保存并使用

使用 code-improver 子代理为此项目提出改进建议

子代理会独立运行并返回结果。

## 12.3 子代理的作用范围
子代理本质是带 YAML frontmatter 的 Markdown 文件，不同位置代表不同作用范围。

当同名子代理存在冲突时，优先级高的会覆盖低的。可通过 /agents 查看当前哪个版本生效。

| 位置 | 范围 | 优先级 |
| ---- | ---- | ---- |
| CLI --agents 标志 | 当前会话（临时测试 / 自动化脚本，不保留到磁盘） | 最高 |
| .claude/agents/ | 当前项目 | 高 |
| ~/.claude/agents/ | 所有项目(用户级) | 中 |
| 插件 agents | 插件作用域 | 最低 |


## 12.4 文件结构
两部分组成：YAML frontmatter（元数据与配置）+ Markdown 正文（系统提示）。

| 字段 | 类型 | 说明 |
| ---- | ---- | ---- |
| name | string（必填） | 唯一标识，也是显式调用时的名称 |
| description | string（必填） | 决定 Claude 何时自动调用此代理，务必写清楚使用场景 |
| tools | string | 工具白名单；设置后只能使用列出的工具，MCP 工具也会被排除 |
| disallowedTools | string | 工具黑名单；继承主对话全部工具，但排除列出的工具（含 MCP） |
| model | string | haiku / sonnet / opus / 完整模型 ID / inherit（默认，继承主对话） |
| permissionMode | enum | 权限行为控制（见权限模式章节） |
| memory | enum | 持久记忆范围：user / project / local（见记忆章节） |
| background | bool | 为 true 时始终以后台方式运行 |
| isolation | string | 设为 worktree 时在临时 git worktree 中运行，完全隔离主仓库 |
| skills | list | 声明在此代理启动时自动加载的 Skills 列表 |
| hooks | object | 生命周期钩子（SubagentStart / SubagentStop / PreToolUse / PostToolUse） |

示例如下


```python
---
name: code-reviewer
description: Reviews code for quality, best practices, and security issues.
             Invoke when the user asks to review, audit, or check code quality.
tools: Read, Grep, Glob
model: sonnet
permissionMode: default
memory: project
---

You are a senior code reviewer.
Analyze code and provide actionable feedback organized by severity: Critical / Major / Minor.

Update your agent memory with recurring patterns, conventions, and known issues you discover.
```

**tools 与 disallowedTools 的区别**

| 配置方式 | 行为 | 典型场景 |
| ---- | ---- | ---- |
| 两者均不设置 | 继承主对话全部工具，含 MCP 工具 | 通用代理，不需要限制 |
| 仅设置 tools | 只能使用白名单内的工具，MCP 工具被排除 | 只读分析代理、严格约束场景 |
| 仅设置 disallowedTools | 继承全部工具，但排除黑名单内的工具（MCP 工具保留） | 保留 MCP 能力但禁止写操作 |
| 两者同时设置 | 先应用 disallowedTools，再从剩余工具中按 tools 筛选 | 精细控制 |


**权限模式（permissionMode）**

| 模式 | 行为 | 适用场景 |
| ---- | ---- | ---- |
| default | 正常权限提示，每次操作前询问 | 通用场景 |
| acceptEdits | 自动接受文件编辑，无需每次确认 | 频繁改动文件的代理 |
| dontAsk | 自动拒绝未授权操作，不中断流程 | 严格只读场景 |
| bypassPermissions | 跳过所有权限检查 | 仅限完全可信、受控环境 |
| plan | 只读规划模式，不执行任何写操作 | 方案制定、架构分析 |

注意；bypassPermissions 只适合完全可信的子代理。另外，子代理会继承父会话的权限模式——如果主会话开启了 bypass，所有子代理也会跟着 bypass。

**持久记忆（Memory）**

| 范围值 | 存储位置 | 适用场景 |
| ---- | ---- | ---- |
| user | ~/.claude/agent-memory/<name>/ | 代理的知识适用于所有项目（如通用代码审查规范） |
| project | .claude/agent-memory/<name>/ | 知识与项目绑定且可 git 共享（推荐默认值） |
| local | .claude/agent-memory-local/<name>/ | 知识与项目绑定但不提交 git（个人本地经验） |

示例
>```
>---
>name: code-reviewer
>description: Reviews code for quality and best practices
>memory: user
>---
>
>You are a code reviewer.
>As you review code, update your agent memory with patterns,
>conventions, and recurring issues you discover.
>```

使用技巧：
- 开始任务时：请先查阅你的记忆，再开始审查
- 任务结束时：任务完成后，把你发现的规律保存到记忆中
- 也可直接在系统提示里写入"主动维护记忆"的指令，让代理自动执行

**隔离模式（isolation: worktree）**

设置 isolation: worktree 后，子代理会在临时 git worktree 中运行，与主仓库完全隔离。适合以下场景：
- 需要大量文件修改但不确定结果的探索性任务
- 并行跑多个方案对比，互不干扰
- 自动化测试、CI 验证等需要干净环境的操作

**后台运行（Background）**
- 前台（Foreground）：阻塞主对话直到完成，权限提示和澄清问题会透传给你。无特殊限制
- 后台（Background）：并行执行，不打断主对话；启动前会预先确认所需权限。无 MCP、无交互式澄清；权限不足时任务失败而非暂停

Claude 会根据任务特性自动决定前台还是后台。你也可以主动控制：
- Ctrl + B：将当前运行的子代理切换到后台
- Ctrl + F（按两次确认）：终止所有后台代理
- 在 frontmatter 中设置 background: true：该代理始终以后台方式运行
- 消息开头加 &：将该任务作为后台任务发送给 claude.ai 网页端
- 通过 /tasks 命令随时查看后台任务进度

**生命周期钩子（Hooks）**

| 钩子事件 | 触发时机 | 典型用途 |
| ---- | ---- | ---- |
| SubagentStart | 子代理启动时 | 记录启动日志、初始化环境 |
| SubagentStop | 子代理完成时 | 记录结果、触发下游任务、发送通知；字段含 agent_id 和 agent_transcript_path |
| PreToolUse | 工具调用前 | 校验操作合法性，退出码 2 可阻止执行 |
| PostToolUse | 工具调用后 | 格式化输出、生成变更记录 |

高级用法：通过 `PreToolUse` 动态控制工具行为。例如，让代理只允许只读 SQL 查询：
>```
>---
>name: db-analyst
>description: Read-only database analysis agent
>tools: Bash
>---
>
>You are a database analyst. Only run SELECT queries.
>
># hooks defined in .claude/settings.json:
># PreToolUse on Bash -> validate-readonly-query.sh
># Script exits with code 2 to block write operations
>```

## 12.5 使用子代理
1. 自动委托
    Claude 会根据 description 字段自动判断，无需你手动指定：
>    ```
>    帮我检查最近的代码改动质量
>    ```

2. 显式调用
    在提示中明确指定代理名称：
>    ```
>    让 code-reviewer 子代理检查最近的改动
>    ```

## 12.6 使用示例
1、隔离高输出任务
>```
>使用子代理运行测试，只返回失败的测试和根因分析
>```

2、并行研究
>```
>并行使用子代理分别分析认证模块、数据库模块和 API 模块，汇总后给出整体架构建议
>```

3、串联子代理（流水线）
>```
>先用 code-reviewer 找问题，再用 optimizer 修复问题
>```
串联工作流的设计原则：每个代理只做一件事，通过清晰的"输入 → 处理 → 输出 → 交接规则"定义接口。

完整流水线示例（来自 PubNub 的生产实践）：
- pm-spec：读取需求，生成工作规格，确认后标记 READY_FOR_ARCH
- architect-review：验证设计约束，产出架构决策记录（ADR），标记 READY_FOR_BUILD
- implementer-tester：实现代码和测试，更新文档，标记 DONE

通过 SubagentStop 钩子监听队列文件，自动触发下一个代理。

4、并行代码审查
>```
>同时启动 style-checker、security-scanner、test-coverage 三个子代理并行审查，
>将审查时间从数分钟压缩到数十秒
>```

## 12.7 子代理上下文与恢复
每次调用 = 新子代理实例（无法感知之前的调用）

子代理上下文独立存储，不污染主对话

中间工具调用和结果只留在子代理内部，主对话只收到最终摘要

可通过 session ID 和 agent ID 恢复继续执行（SDK 场景）

会话继续示例：
>```
>继续刚才的 code-reviewer 分析，重点看授权逻辑部分
>```
存储位置示例：

~/.claude/projects/{project}/{sessionId}/subagents/

## 12.8 什么时候该用子代理？
用主对话，当：
- 需要频繁来回调整，交互性强
- 多阶段任务有强依赖关系，上下文需要连续
- 快速、小改动，启动代理的开销不值得
- 实际经验：超过 3～4 个子代理后，管理成本可能反而降低效率

用子代理，当：
- 任务自包含，可以给出明确的输入和期望输出
- 输出量很大，会显著占用主对话上下文
- 需要强约束（只读、隔离 worktree 等）
- 同类任务会重复出现，值得固化为代理
- 涉及多个独立子域，可以并行处理

注意：子代理不能再创建子代理（防止无限嵌套）。如需嵌套逻辑，请使用 Skills。

# 13 MCP

| 命令 | 作用 |
| ---- | ---- |
| `claude mcp add` | 添加一个 MCP 服务器 |
| `claude mcp list` | 查看所有已配置服务器 |
| `claude mcp get <name>` | 查看某个服务器详情 |
| `claude mcp remove <name>` | 删除服务器 |
| `/mcp` | 在 Claude Code 中查看状态 / 认证 |

## 13.1 安装 MCP 服务器
MCP 服务器支持 HTTP/stdio 两种接入方式。

1. 远程 HTTP 服务器（推荐）  

    适用于云服务类工具，是最通用的方式：
>    ```bash
>    # 基础语法
>    claude mcp add --transport http <服务器名称> <服务器URL>
>
>    # 示例1：连接Notion
>    claude mcp add --transport http notion https://mcp.notion.com/mcp
>
>    # 示例2：带身份验证的HTTP服务器
>    claude mcp add --transport http secure-api https://api.example.com/mcp \
>      --header "Authorization: Bearer 你的令牌"
>    ```

3. 本地 stdio 服务器  

    适用于需要本地系统访问的工具（如本地数据库、自定义脚本）：
>    ```bash
>    # 基础语法（注意：--前是Claude参数，--后是服务器命令）
>    claude mcp add --transport stdio [--env 环境变量] <服务器名称> -- <启动命令>
>
>    # 示例：连接Airtable（需替换自己的API密钥）
>    claude mcp add --transport stdio --env AIRTABLE_API_KEY=你的密钥 airtable \
>      -- npx -y airtable-mcp-server
>    ```
注意：--transport/--env 等参数必须放在服务器名称前面，-- 用于分隔Claude参数和服务器命令，避免参数冲突。    

## 13.2 管理 MCP 服务器
>```bash
># 列出所有已配置的服务器
>claude mcp list
>
># 查看指定服务器详情（如github）
>claude mcp get github
>
># 删除指定服务器
>claude mcp remove github
>
># 在 Claude Code 中打开管理菜单，进行查看、添加、删除、启用或禁用服务器
>/mcp
>```

## 13.3 配置范围

| 范围 | 用途 | 配置文件位置 | 配置命令示例 | 优先级 |
| ---- | ---- | ---- | ---- | ---- |
| local（默认） | 仅当前项目可用，私密配置（如敏感密钥） | .claude/settings.local.json 与 ~/.claude.json | `claude mcp add --scope local ...` | 高（同名服务器，本地配置覆盖共享配置） |
| project | 团队共享，可提交版本库 | 项目根目录的.mcp.json| `claude mcp add --scope project ...` | 中 |
| user | 所有项目可用（个人全局配置） |  ~/.claude/settings.json 与 ~/.claude.json | `claude mcp add --scope user ...` | 低 |

## 13.4 配置文件示例
.mcp.json
>```json
>{
>  "mcpServers": {
>    "database-tools": {
>      "command": "${CLAUDE_PLUGIN_ROOT}/servers/db-server",
>      "args": ["--config", "${CLAUDE_PLUGIN_ROOT}/config.json"],
>      "env": {
>        "DB_URL": "${DB_URL}"
>      }
>    }
>  }
> }
>```
或内联在 plugin.json 中
>```json
>{
>  "name": "my-plugin",
>  "mcpServers": {
>    "plugin-api": {
>      "command": "${CLAUDE_PLUGIN_ROOT}/servers/api-server",
>      "args": ["--port", "8080"]
>    }
>  }
>}
>```

## 13.5 示例
示例 1：GitHub 代码审查
>```bash
>claude mcp add --transport http github https://api.githubcopilot.com/mcp/
>```
在 Claude Code 中：
>```
>> Review PR #456 and suggest improvements
>> Show me all open PRs assigned to me
>```

示例 2：Sentry 生产环境排错
>```bash
>claude mcp add --transport http sentry https://mcp.sentry.dev/mcp
>```
>```
>> /mcp   # 完成 OAuth 登录
>> What are the most common errors in the last 24 hours?
>```

示例 3：直接查 PostgreSQL
>```bash
>claude mcp add --transport stdio db \
>  -- npx -y @bytebase/dbhub \
>  --dsn "postgresql://readonly:pass@prod.db.com:5432/analytics"
>```
>```
>> Show me the schema for the orders table
>> Which users haven't purchased in 90 days?
>```

## 13.6 在对话中使用 MCP
1、使用 @ 引用 MCP 资源
>```
>> Analyze @github:issue://123 and suggest a fix
>```
支持多个资源对比：
>```
>> Compare @postgres:schema://users with @docs:file://user-model
>```

2、MCP Prompt 作为斜杠命令  
MCP 可以暴露命令：
>```
>/mcp__github__list_prs
>/mcp__jira__create_issue "Login bug" high
>```
Claude 会像执行内置命令一样执行它们。

## 13.7 注意
- 身份验证：远程MCP服务器（如GitHub/Sentry）需在Claude Code中执行 /mcp 完成OAuth 2.0授权；
- Windows兼容：本地stdio服务器若用npx，需加cmd /c包装（如-- cmd /c npx -y 包名），否则会报"Connection closed"错误；
- 第三方风险：使用非官方MCP服务器时，需确认来源可信，避免提示注入/安全风险；
- 参数顺序：stdio服务器配置时，-- 前后的参数不可颠倒，否则会执行失败。

# 14 MCP使用实例
本章我们连接 GitHub 进行代码审查

## 14.1  GitHub 令牌设置
打开您的 [GitHub 令牌设置](https://github.com/settings/personal-access-tokens) ，生成一个新的细粒度权限令牌，并授予 Claude 所需访问权限的仓库权限，然后添加服务器：
>```bash
>claude mcp add --transport http github https://api.githubcopilot.com/mcp/ --header "Authorization: Bearer YOUR_GITHUB_PAT"
>```

## 14.2 然后与 GitHub 协作：
>```bash
>审查PR#456并提出改进建议
>
>为我们刚刚发现的bug创建一个新 issue
>
>查看我的github有哪些仓库
>
>显示分配给我的所有打开的PR
>```

# 15 钩子
用户自定义的 Shell 命令，会在 Claude Code 生命周期的特定节点自动执行。

借助钩子，你可以对 Claude Code 的行为实现精准控制，确保某些操作（如代码格式化、日志记录）必定触发，而非依赖大模型自主选择是否执行。

## 15.1 钩子事件类型说明
Claude Code 内置了多个生命周期事件，你可以为不同事件绑定钩子命令。每个事件会传递不同的上下文数据，且对 Claude 行为的影响方式不同。

| 事件名称 | 触发时机 | 核心作用 |
| ---- | ---- | ---- |
| PreToolUse | 工具调用之前 | 可拦截工具执行（如阻止修改敏感文件），并向 Claude 反馈调整建议 |
| PermissionRequest | 弹出权限请求对话框时 | 自动批准或拒绝权限申请 |
| PostToolUse | 工具调用完成后 | 执行后置操作（如格式化代码、记录日志） |
| UserPromptSubmit | 用户提交提示词后、Claude 处理前 | 预处理用户输入（如补充上下文信息） |
| Notification | Claude 发送通知时 | 自定义通知方式（如桌面弹窗、短信提醒） |
| Stop | Claude 完成响应时 | 执行收尾工作（如清理临时文件） |
| SubagentStop | 子代理任务完成时 | 处理子代理的执行结果 |
| PreCompact | 即将执行上下文压缩操作时 | 自定义压缩规则 |
| SessionStart | 启动新会话或恢复旧会话时 | 初始化会话环境（如加载项目配置） |
| SessionEnd | 会话结束时 | 保存会话数据、清理环境 |

## 15.2 示例：命令日志记录
记录 Claude 执行的所有 Bash 命令

1.安装 jq 工具（用于命令行解析 JSON 数据）：
  - Linux：sudo apt install jq / sudo yum install jq

  - Windows：下载 jq 官方安装包，或通过 WSL 安装

2.打开钩子配置界面

在 Claude Code 的交互界面中，输入斜杠命令 /hooks ，回车后选择要绑定的事件 —— PreToolUse（工具调用前触发，适合记录命令）

3.添加事件匹配器

匹配器的作用是 限定钩子的触发条件，只在指定工具被调用时执行钩子命令。

- 选择 + Add new matcher…

- 输入匹配关键词 Bash，表示仅当 Claude 调用 Bash 工具时触发钩子

输入 * 可以匹配所有工具，实现全局钩子

4.添加钩子命令

选择 + Add new hook…，输入以下命令（功能：提取命令内容和描述，写入日志文件）：

> jq -r '"\(.tool_input.command) - \(.tool_input.description // "无描述信息")"' >> ~/.claude/bash-command-log.txt

命令说明：
- jq -r ...：提取 JSON 中的命令（command）和描述（description），无描述时显示"无描述信息"
- ~/.claude/...：将内容追加写入用户主目录下的日志文件

5.选择配置存储位置

配置保存位置决定钩子的生效范围：
- User settings：保存到用户级配置（~/.claude/settings.json），所有项目生效
- Project settings：保存到当前项目配置（.claude/settings.local.json），仅当前项目生效

这里我们选 User settings，实现全局命令日志记录。选择后按 Esc 键退出配置界面，钩子即注册完成。

6.验证钩子配置

再次输入 /hooks 命令，可查看已配置的钩子列表

或直接打开配置文件 ~/.claude/settings.json，会看到如下配置内容：
>```js
>{
>  "hooks": {
>    "PreToolUse": [
>      {
>        "matcher": "Bash",
>        "hooks": [
>          {
>            "type": "command",
>            "command": "jq -r '\"\\(.tool_input.command) - \\(.tool_input.description // \"无描述信息\")\"' >> ~/.claude/bash-command-log.txt"
>          }
>        ]
>      }
>    ]
>  }
>}
>```
7.测试钩子效果

在 Claude Code 中输入指令：帮我执行 ls 命令

执行完成后，在终端中查看日志文件：
>cat ~/.claude/bash-command-log.txt

若日志中出现如下内容，说明钩子配置成功：
>ls - Lists files and directories

## 15.3 常用钩子示例

### 15.3.1 示例一  自动格式化 TypeScript 文件  
功能：编辑/写入 .ts 文件后，自动用 prettier 格式化代码
>```json
>{
>  "hooks": {
>    "PostToolUse": [
>      {
>        "matcher": "Edit|Write", // 匹配“编辑”和“写入”工具
>        "hooks": [
>          {
>            "type": "command",
>            "command": "jq -r '.tool_input.file_path' | { read file_path; if echo \"$file_path\" | grep -q '\\.ts$'; then npx prettier --write \"$file_path\"; fi; }"
>          }
>        ]
>      }
>    ]
>  }
>}
>```

### 15.3.2 示例二  自动修复 Markdown 文件格式  
功能：为无语言标签的代码块自动补全标签、清理多余空行  

1.添加钩子配置
>```json
>{
>  "hooks": {
>    "PostToolUse": [
>      {
>        "matcher": "Edit|Write",
>        "hooks": [
>          {
>            "type": "command",
>            "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/markdown_formatter.py"
>          }
>        ]
>      }
>    ]
>  }
>}
>```

2.在项目目录下新建文件 .claude/hooks/markdown_formatter.py，粘贴以下代码：


```python
#!/usr/bin/env python3
"""
Markdown 格式化工具：自动补全代码块语言标签、清理多余空行
"""
import json
import sys
import re
import os

def detect_language(code):
    """根据代码内容自动检测编程语言"""
    code = code.strip()
    # 检测 JSON
    if re.search(r'^\s*[{\[]', code):
        try:
            json.loads(code)
            return 'json'
        except:
            pass
    # 检测 Python
    if re.search(r'^\s*def\s+\w+\s*\(', code, re.M) or re.search(r'^\s*(import|from)\s+\w+', code, re.M):
        return 'python'
    # 检测 JavaScript/TypeScript
    if re.search(r'\b(function\s+\w+\s*\(|const\s+\w+\s*=)', code) or re.search(r'=>|console\.(log|error)', code):
        return 'javascript'
    # 检测 Bash
    if re.search(r'^#!.*\b(bash|sh)\b', code, re.M) or re.search(r'\b(if|then|fi|for|in|do|done)\b', code):
        return 'bash'
    # 默认文本格式
    return 'text'

def format_markdown(content):
    """格式化 Markdown 内容"""
    # 为无标签代码块补全语言
    fence_pattern = r'(?ms)^([ \t]{0,3})```([^\n]*)\n(.*?)(\n\1```)\s*$'
    def add_lang(match):
        indent, info, body, closing = match.groups()
        if not info.strip():
            lang = detect_language(body)
            return f"{indent}```{lang}\n{body}{closing}\n"
        return match.group(0)
    content = re.sub(fence_pattern, add_lang, content)
    # 清理多余空行（仅清理代码块外的内容）
    content = re.sub(r'\n{3,}', '\n\n', content)
    return content.rstrip() + '\n'

if __name__ == "__main__":
    try:
        # 读取 Claude 传递的 JSON 数据
        input_data = json.load(sys.stdin)
        file_path = input_data.get('tool_input', {}).get('file_path', '')
        # 仅处理 .md/.mdx 文件
        if not file_path.endswith(('.md', '.mdx')):
            sys.exit(0)
        # 读取并格式化文件
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            formatted_content = format_markdown(content)
            # 仅在内容变化时写入
            if formatted_content != content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(formatted_content)
                print(f"已格式化 Markdown 文件：{file_path}")
    except Exception as e:
        print(f"格式化失败：{e}", file=sys.stderr)
        sys.exit(1)
```

3.赋予脚本执行权限
>```bash
>chmod +x .claude/hooks/markdown_formatter.py

### 15.3.3 示例三  禁止修改敏感文件
功能：阻止 Claude 编辑 .env、package-lock.json 等敏感文件
>```json
>{
>  "hooks": {
>    "PreToolUse": [
>      {
>        "matcher": "Edit|Write",
>        "hooks": [
>          {
>            "type": "command",
>            "command": "python3 -c \"import json, sys; data=json.load(sys.stdin); path=data.get('tool_input',{}).get('file_path',''); sys.exit(2 if any(p in path for p in ['.env', 'package-lock.json', '.git/']) else 0)\""
>          }
>        ]
>      }
>    ]
>  }
>}
>```
说明：脚本返回状态码 2 时，Claude Code 会拦截此次工具调用，从而阻止文件修改

## 15.4 官方示例：bash 命令验证器示例
https://github.com/anthropics/claude-code/blob/main/examples/hooks/bash_command_validator_example.py

# 16 钩子参考手册

## 16.1 配置文件路径

| 配置级别       | 文件路径                     | 生效范围                   |
|----------------|----------------------------|---------------------------|
| 用户级         | ~/.claude/settings.json     | 所有项目                   |
| 项目级         | .claude/settings.json       | 当前项目                   |
| 本地项目级（不提交） | .claude/settings.local.json | 当前项目，不纳入版本控制   |
| 托管策略级     | 管理员指定路径               | 企业/团队统一管控          |


## 16.2 配置结构
Hooks 按事件+匹配器组织，支持 command（执行 Shell 命令）和 prompt（调用 LLM 决策）两种类型。
>```json
>{
>  "hooks": {
>    "【钩子事件名】": [
>      {
>        "matcher": "【工具匹配规则】", // 部分事件可省略
>        "hooks": [
>          {
>            "type": "command/prompt",
>            "command": "【Shell 命令】", // type=command 时必填
>            "prompt": "【LLM 提示词】",  // type=prompt 时必填
>            "timeout": 30 // 可选，超时时间（秒）
>          }
>        ]
>      }
>    ]
>  }
>}
>```

## 16.3 匹配器规则（仅适用于工具类事件）

| 匹配规则       | 示例            | 说明                               |
|----------------|----------------|-----------------------------------|
| 精确匹配       | `Write`        | 仅匹配 `Write` 工具               |
| 多工具匹配     | `Edit | Write` | 匹配 `Edit` 或 `Write` 工具       |
| 前缀匹配       | `Notebook.*`   | 匹配所有以 `Notebook` 开头的工具  |
| 全匹配         | `*` / 空字符串  | 匹配所有工具                       |

## 16.4 特殊配置技巧

| 场景                  | 配置方法       | 示例          |
|-----------------------|--------------|----------------------|
| 引用项目内脚本        | 使用环境变量 `$CLAUDE_PROJECT_DIR`                                       | `"command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/check-style.sh"`                                   |
| 插件 Hooks            | 插件内配置 `hooks/hooks.json`，用 `${CLAUDE_PLUGIN_ROOT}` 引用插件文件   | `"command": "${CLAUDE_PLUGIN_ROOT}/scripts/format.sh"`                                               |
| 组件级 Hooks（Skill/Agent） | 在组件 `frontmatter` 中定义，作用域仅限组件生命周期                      | 见下方扩展配置表格                                                                                     |


## 16.5 扩展配置（Skill/Agent/斜杠命令）
扩展配置允许直接在 Skill、Agent 或自定义斜杠命令的定义中内嵌 Hooks 配置，这类 Hooks 仅在对应组件被激活并运行时生效，组件执行完成后会自动清理，不会影响全局会话。

仅支持 PreToolUse、PostToolUse、Stop 三类事件，与全局 Hooks 功能一致，但作用域仅限当前 Skill/斜杠命令的生命周期。

特有配置项  once: true（可选）：设置为 true 时，该 Hooks 在整个会话中仅运行一次，首次成功执行后会自动移除，避免重复触发。

示例：
>```md
># Skill/斜杠命令的基础信息
>name: secure-operations
>description: 执行Shell命令前先做安全校验的工具
># Hooks 配置段
>hooks:
>  PreToolUse:
>    # 匹配器：仅拦截Bash工具调用
>    - matcher: "Bash"
>      hooks:
>        - type: "command"
>          # 要执行的安全校验脚本
>          command: "./scripts/security-check.sh"
>          # 会话内仅执行一次
>          once: true
>          # 超时时间（秒），避免脚本卡死
>          timeout: 15
>```

Agent 中的 Hooks 配置

同样仅支持 PreToolUse、PostToolUse、Stop 三类事件，作用域仅限该子 Agent 的任务执行周期。

示例：
>```md
># Agent 的基础信息
>name: code-reviewer
>description: 自动审查代码修改并运行代码检查的子代理
># Hooks 配置段
>hooks:
>  PostToolUse:
>    # 匹配器：拦截Edit（编辑）或Write（写入）工具
>    - matcher: "Edit|Write"
>      hooks:
>        - type: "command"
>          # 代码检查脚本，执行lint校验
>          command: "./scripts/run-linter.sh"
>          # 超时时间（秒）
>          timeout: 30
>```

注意事项：
- 组件内 Hooks 的匹配器规则与全局 Hooks 完全一致：支持精确匹配（如 "Write"）、多工具匹配（如 "Edit|Write"）、通配匹配（"*"），且区分大小写；
- 组件内 Hooks 与全局 Hooks 会并行执行：若全局和组件内同时配置了针对同一事件的 Hooks，触发时两类 Hooks 会一起运行，互不冲突；
- 配置格式要求：组件内 Hooks 需写在 frontmatter（--- 包裹的区域）中，遵循 YAML 语法，缩进错误会导致配置失效；
- 脚本路径建议：优先使用相对路径（如 ./scripts/xxx.sh），或借助 $CLAUDE_PROJECT_DIR 环境变量指定绝对路径，确保组件在任意目录下都能找到脚本。

## 16.6 钩子事件--工具类事件（支持匹配器）

| 事件名          | 触发时机                     | 常见匹配器                          | 核心作用                                                                 |
|-----------------|----------------------------|-----------------------------------|-------------------------------------------------------------------------|
| `PreToolUse`    | 工具调用前                   | `Bash/Edit/Write/Read`            | 拦截工具执行、修改入参、自动批准/拒绝权限                                 |
| `PermissionRequest` | 弹出权限请求对话框时         | 同 `PreToolUse`                   | 自动处理权限申请，无需用户手动确认                                         |
| `PostToolUse`   | 工具调用成功后               | 同 `PreToolUse`                   | 执行后置操作（如代码格式化、日志记录）                                     |
| `Notification`  | Claude 发送通知时            | `permission_prompt/idle_prompt/auth_success` | 自定义通知方式（如桌面弹窗、邮件提醒）                                     |
| `PreCompact`    | 执行上下文压缩操作前         | `manual`（手动触发）/`auto`（自动触发） | 自定义压缩规则、备份重要上下文                                             |

## 16.7 会话/任务类事件（无匹配器）

| 事件名            | 触发时机                          | 核心作用                              |
|-------------------|---------------------------------|---------------------------------------|
| `UserPromptSubmit` | 用户提交提示后、Claude 处理前     | 验证提示合法性、补充上下文信息                 |
| `Stop`            | 主 Agent 完成响应时（用户中断不触发）| 智能判断是否需要继续执行任务                  |
| `SubagentStop`    | 子 Agent 任务完成时                 | 评估子任务结果，决定是否终止                  |
| `SessionStart`    | 启动/恢复会话时                     | 初始化环境、加载项目配置、设置持久化环境变量    |
| `SessionEnd`      | 会话结束时                           清理临时文件、记录会话日志、保存工作状态         |

## 16.8 待续

# 17 CLI 参考手册

## 17.1 核心 CLI 命令

| 命令类型 | 命令 / 标志 | 描述 | 示例 |
| :--- | :--- | :--- | :--- |
| **启动与会话** | `claude` | 在当前目录启动一个标准的交互式 REPL 会话。 | `claude` |
| | `claude "query"` | 启动会话并附带初始问题，立即执行。 | `claude "解释依赖注入"` |
| | `claude -p "query"` <br>`claude --print "query"` | **打印模式**，执行后直接退出，适合脚本、自动化和管道任务。 | `claude -p "这个函数做什么？"` |
| | `cat file \| claude -p` | 通过管道将内容传给 Claude 处理，用于快速分析文本文件或命令输出。 | `cat logs.txt \| claude -p "解释错误"` |
| **会话管理** | `claude -c` <br>`claude --continue` | 继续当前目录中最近的一次对话，实现断点续聊。 | `claude -c` |
| | `claude -r <session-id>` | 使用特定的会话 ID 来恢复之前的对话。 | `claude -r "abc123" "继续重构"` |
| | `claude update` | 将 Claude Code CLI 工具本身更新到最新版本。 | `claude update` |
| **认证与配置** | `claude auth login` | 登录到你的 Anthropic 账号，首次使用或会话过期时需要。 | `claude auth login` |
| | `claude auth status` | 查看当前登录状态和账户信息。 | `claude auth status` |
| | `claude mcp` | 管理与 Claude 交互的 MCP (Model Context Protocol) 服务器。 | `claude mcp` |
| | `claude doctor` | 检查 Claude Code 的安装状态和健康情况，用于诊断问题。 | `claude doctor` |

## 17.2 模型控制与环境配置

| 命令类型 | 命令 / 标志 | 描述 | 示例 |
| :--- | :--- | :--- | :--- |
| **模型选择** | `--model <name>` | 指定本次会话使用的 AI 模型，如 `sonnet`, `opus` 等。 | `claude --model opus` |
| **系统提示词** | `--system-prompt` | **完全替换**默认的系统提示词，为 Claude 设定全新的角色或规则。 | `claude --system-prompt "你是一个Python专家"` |
| | `--system-prompt-file <file>` | 从文件中读取系统提示词内容，用于完全替换默认提示词。 | `claude --system-prompt-file ./my_prompt.txt` |
| | `--append-system-prompt` | **追加**内容到默认系统提示词之后，在保留基础能力的同时添加特定要求。 | `claude --append-system-prompt "Always use TypeScript"` |
| **目录与上下文** | `--add-dir <path>` | 临时添加一个或多个额外的工作目录供 Claude 访问，用于多模块项目。 | `claude --add-dir ../lib ../apps` |
| **Agent 与 IDE** | `--agent` | 指定当前会话使用哪个预设的 Agent。 | `claude --agent my-custom-agent` |
| | `--agents '<JSON>'` | 临时传入自定义 Agents 的 JSON 定义，仅在本次会话生效。 | `claude --agents '{"reviewer":{"description":"Reviews code","prompt":"You are a code reviewer"}}'` |
| | `--ide` | 如果本机只有一个可用的 IDE，会自动进行连接。 | `claude --ide` |
| **其他实用参数** | `--dangerously-skip-permissions` | **高风险**。跳过所有权限请求，提高协作效率，但需在完全信任的安全环境中使用。 | `claude --dangerously-skip-permissions "自动修复所有lint错误"` |
| | `--verbose` | 启用详细日志记录，输出执行过程中的详细信息，便于调试。 | `claude --verbose` |

## 17.3 交互式会话斜杠命令

| 命令类型 | 命令 / 标志 | 描述 | 示例 |
| :--- | :--- | :--- | :--- |
| **会话与上下文** | `/init` | 在当前目录创建 `CLAUDE.md` 文件，固化项目规范、常用命令等上下文。 | `/init` |
| | `/compact` | **上下文压缩**。在上下文窗口将满时，压缩对话历史为摘要，节省空间。 | `/compact` |
| | `/clear` | **硬重置**。完全清除当前对话历史，从头开始一个全新的会话。 | `/clear` |
| **模型与工具** | `/model` | 在会话中动态切换 AI 模型，无需退出重启。 | `/model sonnet` |
| | `/permissions` | 管理特定文件读取或命令执行权限，平衡效率与安全。 | `/permissions` |
| | `/add-dir <path>` | 在会话中动态添加新目录，扩展 Claude 的视野。 | `/add-dir /path/to/another/project` |
| **帮助** | `/help` | 在 REPL 界面中显示所有可用的斜杠命令列表。 | `/help` |

## 17.4 效率和快捷键

| 命令类型 | 命令 / 标志 | 描述 | 示例 |
| :--- | :--- | :--- | :--- |
| **通用快捷键** | `Ctrl+C` | 中断当前正在进行的 AI 操作或模型生成。 | `Ctrl+C` |
| | `Ctrl+L` | 清空当前终端屏幕内容，但不影响对话历史和会话状态。 | `Ctrl+L` |
| | `Shift + Tab` | 在 `normal`, `auto-accept`, `plan` 等模式间切换。 | `Shift + Tab` |
| **操作与编辑** | `Esc + Esc`（双击 ESC） | 在会话中直接编辑上一次发送的消息内容，无需重新输入。 | `Esc + Esc` |
| | `Shift + Enter` | 在会话中换行输入，方便编写多行消息或粘贴代码。 | `Shift + Enter` |
| | `#` | 在行首使用 `#` 可以直接将指令或注释写入 `CLAUDE.md` 文件。 | `# 这个项目使用 async/await` |

## 17.5 部分参数讲解

### 17.5.1 --agents

接收 JSON 对象，用于定义一个或多个自定义子代理。每个子代理需配置唯一名称作为键，值为包含以下字段的对象：

| 字段 | 必填 | 描述 |
| :--- | :--- | :--- |
| `description` | 是 | 描述子代理的适用场景 |
| `prompt` | 是 | 定义子代理行为的系统提示 |
| `tools` | 否 | 子代理专属工具列表（如 `["Read", "Edit"]`，省略则继承全部工具） |
| `model` | 否 | 子代理使用模型（支持 `sonnet` / `opus` / `haiku`，省略则用默认模型） |

示例：
>```json
>claude --agents '{
>  "code-reviewer": {
>    "description": "Expert code reviewer. Use proactively after code changes.",
>    "prompt": "You are a senior code reviewer. Focus on code quality, security, and best practices.",
>    "tools": ["Read", "Grep", "Glob", "Bash"],
>    "model": "sonnet"
>  },
>  "debugger": {
>    "description": "Debugging specialist for errors and test failures.",
>    "prompt": "You are an expert debugger. Analyze errors, identify root causes, and provide fixes."
>  }
>}'
>```

### 17.5.2 --system-prompt

| 标志 | 行为 | 示例 | 典型用例 |
| :--- | :--- | :--- | :--- |
| `--system-prompt` | 替换默认系统提示 | `claude --system-prompt "你是一个Python专家"` | 完全自定义 Claude 行为指令 |
| `--system-prompt-file` | 从文件加载提示并替换 | `claude --system-prompt-file ./prompt.txt` | 团队共享提示模板、版本控制 |
| `--append-system-prompt` | 追加内容到默认提示 | `claude --append-system-prompt "Always use TypeScript"` | 保留默认功能，添加个性化指令 |

# 18 快捷键

| 分类 | 快捷键 | 功能描述 | 适用场景 |
| :--- | :--- | :--- | :--- |
| **全局通用** | `Ctrl + C` | 中断当前操作（如AI生成的内容） | AI生成的回复偏离预期，立马打断。 |
| | `Ctrl + D` | 退出当前Claude Code会话（相当于 `/exit`） | 完成工作，准备离开终端。 |
| | `Ctrl + L` | **清屏**，仅清除终端显示，会话和上下文保留 | 屏幕太乱，希望有个干净的界面。 |
| | `Ctrl + G` | 在默认外部编辑器（如Vim、VSCode）中打开当前输入框，用于长篇内容编辑 | 需要编写包含大量代码或复杂结构的提示。 |
| | `Ctrl + R` | **反向搜索**命令/输入历史（类似于终端历史搜索） | 想快速复用很久之前输入过的一条复杂指令，无需反复按 `↑` 翻找。 |
| **模式与模型切换** | `Shift + Tab` | 循环切换权限模式：普通 → 自动接受 → 计划 → 普通 | 想批量执行修改时切换到自动接受模式，或在计划模式下让Claude只出方案不执行。 |
| | `Alt + P` (Mac) / `Alt + P` (Win/Linux) | 在会话中快速切换AI模型（如 Sonnet ↔ Opus ↔ Haiku） | 处理复杂任务时需要更强大的模型（如Opus），或省钱时换用轻量模型（如Haiku）。 |
| | `Alt + T` (Mac) / `Alt + T` (Win/Linux) | 开启或关闭 **"思考模式"** （Extended Thinking），让Claude在回答前进行更深入的推理 | 处理需要严密逻辑的代码重构或复杂算法设计时。 |
| | `?` | 显示所有可用的快捷键帮助信息 | 想不起来某个快捷键时，随时查阅。 |
| **文本编辑与输入** | `Esc + Esc` (双击) | ① **清除当前输入** / ② 在空输入时，可**快速回退**（Rewind）对话状态，撤销最近的AI操作 | AI改坏了代码，想一键撤销到之前的对话状态，比Git更快。 |
| | `Shift + Enter` | 在输入框中**换行**（而不发送消息），支持多行输入 | 编写多行指令或粘贴包含换行符的代码块。 |
| | `Ctrl + A` | 光标跳到**当前行的行首** | 想修改或删除输入行开头的文字。 |
| | `Ctrl + E` | 光标跳到**当前行的行尾** | 想追加内容到当前输入的末尾。 |
| | `Ctrl + U` | **删除**从光标位置到**行首**的所有内容 | 输入了一大段，想完全推倒重来。 |
| | `Ctrl + K` | **删除**从光标位置到**行尾**的所有内容 | 删除光标之后的部分，保留光标之前的内容。 |
| | `Ctrl + W` | **删除光标前的一个单词** | 想逐个单词地修正输入，比逐字删除快。 |
| | `Alt/Option + F` | 光标**向前**移动一个**单词**（至下一个单词首） | 在长文本中快速跳转到下一个关键词。 |
| | `Alt/Option + B` | 光标**向后**移动一个**单词**（至上一个单词首） | 在长文本中快速修正之前的某个单词。 |
| **后台与任务管理** | `Ctrl + B` | 将当前任务**挂起**并放到**后台**运行，不阻塞终端的其他操作 | 让Claude在后台执行耗时的任务（如测试或编译），你可以同时去做别的事。 |
| | `Ctrl + T` | **打开/关闭**任务列表面板，查看所有后台运行的任务及其状态 | 想查看后台任务进度、停止任务或唤醒一个后台任务。 |
| | `Ctrl + F` (按两次) | **强制终止**所有后台运行的Agent进程 | 某个后台任务卡死，需要彻底关闭。 |
| | `↑` / `↓` | 在输入框中浏览**之前输入过的命令或提示词历史** | 想快速复用或微调之前输入过的复杂指令。 |
| **特殊输入前缀** | `!` | **直接执行Bash命令**，绕过Claude，命令输出会作为上下文提供给AI | 想快速执行`ls`查看文件或`git status`并将结果告诉Claude。 |
| | `/` | **呼出斜杠命令菜单**，用于快速执行内置或自定义的指令 | 执行`/init`初始化项目，或`/compact`压缩上下文。 |
| | `@` | **引用文件**，输入`@`加文件名，Claude会将文件内容包含在上下文中 | 想让Claude分析某个特定文件的内容，不用手动复制粘贴。 |

- **建议**：记住 `Ctrl + C`（中断）、`Ctrl + L`（清屏）、`Shift + Tab`（模式切换）、`Esc + Esc`（回退）这四个核心快捷键，基本就能覆盖绝大多数场景，帮助提升操作效率。

# 19 /命令

| 分类 | 命令 | 语法 / 示例 | 功能说明 |
| :--- | :--- | :--- | :--- |
| **基础操作** | `/help` | `/help` | 显示所有可用的斜杠命令及简要说明。 |
| | `/exit` 或 `/quit` | `/exit` | 退出当前的 Claude Code 交互会话。 |
| | `/clear` | `/clear` | **硬重置**，完全清除当前会话的对话历史，开始一个全新的对话。适合切换到完全不相关的任务时使用。 |
| | `/compact` | `/compact [保留重点]` | **上下文压缩**。智能压缩历史对话，提炼要点，以释放Token空间，适合会话较长时使用。可以附加说明，告知AI要保留哪部分内容。 |
| | `/model` | `/model sonnet` | 在当前会话中切换AI模型（如 `sonnet`, `opus`, `haiku`），以适应不同任务需求。 |
| | `/memory` | `/memory` | 便捷地查看和编辑`CLAUDE.md`记忆文件，为AI注入持久化的项目规则或个人偏好。 |
| | `/cost` | `/cost` | 显示当前会话的Token用量与费用统计，用于成本监控。 |
| **会话管理** | `/resume` | `/resume [会话名或ID]` | 恢复一个之前的历史对话，方便在不中断上下文的情况下继续工作。 |
| | `/rename` | `/rename 新会话名` | 为当前会话命名，便于日后通过 `/resume` 命令快速找回。 |
| | `/rewind` | `/rewind` | **时间回溯**。撤销最近的AI操作（包括文件修改和对话内容），恢复到上一个检查点。相当于一个强大的"后悔药"。 |
| | `/export` | `/export [文件名]` | 将当前的对话内容导出为Markdown文件，用于记录或分享。 |
| | `/branch` | `/branch [分支名]` | 从当前会话的某个检查点创建一个新的对话分支（别名 `/fork`），用于对比不同解决方案。 |
| | `/context` | `/context` | 以可视化方式显示当前上下文的占用情况，并给出优化建议，帮助控制Token消耗。 |
| **代码与诊断** | `/review` | `/review` | 触发Claude对当前的代码变更进行审查，是Pull Request前的自查利器。 |
| | `/diff` | `/diff` | 打开交互式差异查看器，清晰展示本次会话中所有的Git修改和文件变动。 |
| | `/security-review` | `/security-review` | 分析待提交的变更，识别并报告潜在的安全风险（如注入、权限缺陷）。 |
| | `/status` | `/status` | 查看当前会话的连接状态和基本配置信息，用于快速确认环境。 |
| | `/doctor` | `/doctor` | **健康检查**。自动诊断Claude Code的安装和配置问题，排查环境故障。 |
| | `/debug` | `/debug` | 自动分析当前报错日志，定位Bug并给出可直接使用的修复方案。 |
| | `/insights` | `/insights` | 生成项目全局洞察：技术栈、复杂度、重复代码、风险点、架构问题。 |
| | `/simplify` | `/simplify` | 自动简化代码逻辑，删除冗余，提升可读性与简洁性。 |
| | `/verify` | `/verify` | 验证当前任务是否完成、是否满足目标、是否存在错误。 |
| **工具与配置** | `/config` | `/config` | 查看或修改Claude Code的全局配置。 |
| | `/permissions` | `/permissions` | 管理文件和工具的执行权限。 |
| | `/add-dir` | `/add-dir <路径>` | 临时添加额外的工作目录，让Claude可以访问项目外的文件。 |
| | `/init` | `/init` | **项目初始化**。在项目根目录创建 `CLAUDE.md` 文件，用于存储项目关键信息和规范，建议新项目第一步执行。 |
| | `/mcp` | `/mcp` | 管理MCP（Model Context Protocol）服务器的连接与配置，扩展Claude的能力。 |
| | `/terminal-setup` | `/terminal-setup` | 一键配置终端，使 `Shift+Enter` 换行等功能正常工作。 |
| | `/vim` | `/vim` | 在交互模式中启用Vim风格的键绑定，方便Vim/Neovim用户。 |
| | `/ide` | `/ide` | 自动连接 `VS Code`、`JetBrains` 等IDE。 |
| **高级/批量任务** | `/batch` | `/batch <指令>` | **大规模代码改造**。将复杂指令拆解为多个独立任务，由后台Agent并行处理，并在隔离的git worktree中执行，最后生成PR。适合框架迁移、API替换等任务。 |
| | `/autofix-pr` | `/autofix-pr [提示词]` | **PR自动修复**。启动一个监听当前PR的云端Agent，在CI失败或收到评论时，自动尝试推回修复补丁。 |
| | `/simplify` | `/simplify [聚焦说明]` | **代码简洁化**。并行启动三个审查Agent，从不同角度检查代码并应用修改，以提升代码质量。 |
| **项目管理** | `/todos` | `/todos` | 列出当前会话中的所有待办任务项，是清晰的任务管理工具，帮助跟踪复杂任务的各个步骤和进度。 |
| **自动化与流程** | `/hooks` | `/hooks` (配置于`.claude/settings.json`) | **事件驱动的自动化钩子**。在特定事件（如工具使用前后）自动触发预定义的脚本，用于实现安全防护、代码自动格式化等工作流自动化。 |
| | `/plan` | `/plan` | **专门的项目规划模式**。执行后，Claude只会进行项目分析并输出详细的实施计划，不会编写任何代码或修改文件，让你在动手前先进行充分的风险评估和方案推演。 |
| | `/agents` | `/agents` | **管理专属AI子代理**。可创建、配置和管理专注于特定任务（如安全审计、代码审查）的子代理。在大项目中，能并行派出多个AI子代理独立完成任务，并行推进，大幅提升复杂任务的效率。 |
| | `/goal` | `/goal 完成条件` | 设置自动任务目标，AI自动循环执行直到条件满足。 |
| | `/loop` | `/loop 次数` | 固定次数自动循环执行，无需手动输入继续。 |
| **进程与输出** | `/bashes` | `/bashes` | 列出所有通过Claude Code启动的**后台Bash任务进程**及其ID，方便你统一查看、管理和终止。 |
| | `/copy` | `/copy` | **一键复制**。将当前Claude Code会话生成的最新输出内容（包括代码、说明等）直接复制到系统剪贴板，无需手动拖选，方便粘贴到其他地方，避免上下文污染。 |
| **辅助交互** | `/btw` | `/btw 你的问题` | **"By The Way"侧边聊天。** 允许你在Claude执行主任务时，**不中断原有任务**、**不污染主对话历史**地临时插入一个完全独立的问题，并在得到答案后快速清除侧边聊天记录，主任务继续无缝运行。 |
| | `/recap` | `/recap` | 自动总结当前会话：目标、已完成、问题、下一步行动。 |
| | `/tui` | `/tui` | 打开图形化交互式界面，鼠标/键盘操作，零命令记忆成本。 |
| **可扩展性** | `/skills` | `/skills` (文件创建) | **定制专属技能**。通过创建`SKILL.md`文件来定义可复用的AI能力集，可被其他斜杠命令调用，是实现复杂、可复用的自定义工作流的核心机制。 |

内置 Skills 是随 Claude Code 附带的预置 AI 工作流，与内置命令不同——它们加载详细提示词后由 Claude 推理执行，同样用 / 触发

通过插件和 MCP 服务器也可以获取更多扩展命令。


命令前缀

| 前缀 | 语法 | 功能说明 | 示例 | 对比 |
| :--- | :--- | :--- | :--- | :--- |
| `/` | `/command` | 触发内置命令、内置 Skills 或自定义 Skills/Commands | `/review` | — |
| `!` | `!<bash命令>` | 直接执行 Shell 命令，绕过 AI 处理，节省 Token | `!git status` | 等价于在终端直接运行，但比「帮我查看 git 状态」省 Token |
| `@` | `@<文件路径>` | 将文件内容注入当前上下文 | `@src/api/users.ts` | 比手动粘贴代码更精准，支持多文件 |

# 20 输出样式
定制 Claude Code 的交互风格和响应方式，使其适配软件开发之外的更多使用场景，同时保留运行本地脚本、读写文件、跟踪待办事项等核心功能。

其本质是通过修改系统提示（System Prompt），改变 Claude Code 的交互逻辑和响应风格。

内置输出样式

| 样式名称 | 适用场景 | 核心特点 |
| ---- | ---- | ---- |
| 默认样式（default） | 日常软件工程任务 | 专注高效完成编码、调试、重构等工作，回复简洁直接 |
| 解释性样式（explanatory） | 边做边学场景 | 在完成任务的同时讲解实现思路、设计模式等知识点，适合想深入理解代码的开发者 |
| 学习样式（learning） | 主动实践式学习 | 与你协作完成任务，会在关键位置添加 TODO(human) 标记，引导你亲手实现核心代码片段，而不是直接给出答案 |

切换输出样式时，Claude Code 会按以下规则调整系统提示：
- 所有样式都会移除默认的"简洁回复、高效输出"等约束指令
- 自定义样式默认会剔除"用测试验证代码"等编码相关指令（如需保留，可在样式文件中开启 keep-coding-instructions: true）
- 每种样式会在系统提示末尾追加自定义规则，覆盖默认行为
- 对话过程中会触发合规检查，确保 Claude 始终遵守当前样式的指令

## 20.1 切换输出样式
配置保存在项目目录的 .claude/settings.local.json 文件中，仅对当前项目生效：

方式一：菜单选择——输入命令后，在交互菜单中选择目标样式：
>```bash
>/output-style
>```
方式二：直接指定——在命令后直接加上样式名称，一步到位：
>```bash
>/output-style explanatory
>/output-style learning
>/output-style default
>```
除了使用命令切换，也可以直接修改 .claude/settings.local.json（项目级）或 ~/.claude/settings.json（全局级）文件的 outputStyle 字段的值来切换样式。

## 20.2 创建自定义输出样式
创建md文件（两部分组成:顶部的 YAML frontmatter（元数据配置）和下方的 Markdown 正文）
>```md
>---
>name: data-analyst               # 样式名称，显示在 /output-style 菜单中（未填则使用文件名）
>description: 专注将复杂数据转化为可视化报告和分析结论
>                                 # 样式描述，显示在菜单的说明文字中（可选）
>keep-coding-instructions: false  # 是否保留默认编码相关指令
>                                 # false（默认）：剔除编码指令，适合非开发场景
>                                 # true：保留编码指令，同时叠加自定义规则
>---
>
># 角色定位
>你是一个专业的数据分析助手，擅长使用 Python 处理各类结构化数据，
>并将复杂数据转化为简洁易懂的可视化报告。
>
>## 响应规则
>1. 所有分析必须包含「结论 + 数据支撑 + 优化建议」三部分
>2. 生成代码时必须附带详细注释，优先使用 Pandas 和 Matplotlib
>3. 避免专业术语堆砌，用通俗语言解释复杂概念
>
>## 格式要求
>1. 结论部分加粗显示
>2. 代码块使用 ```python 标签包裹
>3. 建议部分使用有序列表呈现
>
>## 特殊场景
>1. 遇到缺失数据时，主动提示用户补充关键信息，而非直接报错
>2. 生成可视化图表时，默认使用中文标签和浅色主题
>```
保存位置：
- 用户级：~/.claude/output-styles/
- 项目级：.claude/output-styles/（项目根目录下）

在 Claude Code 中执行 /output-style，即可在菜单中看到并选择新创建的样式

# 21 并行任务

| 机制          | 适用场景                           | 协作方式                  | 复杂度 |
|---------------|----------------------------------|-------------------------|-------|
| Subagents      | 专注型任务，只需关注结果           | 单向汇报（结果返回主代理） | 低    |
| Agent Teams    | 需要讨论与协作的复杂工作           | 多向通信（队友直接互发消息） | 中    |
| Git Worktree  | 多个任务需要隔离的代码环境         | 完全独立（各自的工作目录） | 中    |

## 21.1 Subagents
主 Claude 可以创建多个 Subagent，每个 Subagent 负责一个特定的子任务。  
Subagent 只能与主 Agent 通信，无法直接互相交流，适合任务相对独立、只需结果的场景。

前台与后台运行
- 前台 Subagent：阻塞主对话直到完成
- 后台 Subagent：并发运行，可按 Ctrl+B 切换

内置 Subagents：

| Agent                | 模型                        | 工具        | 用途                                           |
|----------------------|---------------------------|-----------|-----------------------------------------------|
| Explore              | Haiku（快速、低延迟）        | 只读工具    | 文件发现、代码搜索、代码库探索                   |
| Plan                 | 继承主对话                  | 只读工具    | 规划模式下的代码库研究                           |
| General-purpose      | 继承主对话                  | 所有工具    | 复杂研究、多步骤操作、代码修改                   |
| statusline-setup     | Sonnet                     | —         | 运行 /statusline 配置状态行                     |
| Claude Code Guide    | Haiku                      | —         | 回答 Claude Code 功能问题                       |

### 21.1.1 创建 Subagent
方式一：使用 /agents 命令
>```bash
>/agents
>```
按提示创建新的 Subagent：

选择 Create new agent，然后选择保存位置，描述功能后让 Claude 生成配置。

方式二：手动创建 Subagent 文件
>```yaml
>---
>name: code-reviewer
>description: Reviews code for quality and best practices
>tools: Read, Glob, Grep
>model: sonnet
>---
>
>You are a code reviewer. When invoked, analyze the code and provide
>specific, actionable feedback on quality, security, and best practices.
>```

### 21.1.2 调用 Subagent
1.使用自然语言

2.@subagent_name
>```bash
>@"code-reviewer (agent)" look at the auth changes
>```

3.命令行启动
>```bash
>claude --agent code-reviewer
>```

## 21.2 Agent Teams
协调多个 Claude Code 实例各自独立工作，拥有各自的上下文窗口，同时还能直接相互沟通。

存储位置：
- Team config: ~/.claude/teams/{team-name}/config.json  
- Task list: ~/.claude/tasks/{team-name}/

### 21.2.1 启用 Agent Teams
在 settings.json 中添加：
>```json
>{
>  "env": {
>    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
>  }
>}
>```

### 21.2.2 使用 Agent Team
用自然语言描述任务和团队结构即可。

### 21.2.3 Agent Teams 架构

| 组件        | 角色描述                                                                 |
|-------------|--------------------------------------------------------------------------|
| **Team Lead** | 创建团队、生成队友并协调工作的主 Claude Code 会话，负责整体任务分配与监控。 |
| **Teammates** | 各自处理分配任务的独立 Claude Code 实例，执行具体任务并反馈结果。          |
| **Task List** | 队友认领和完成的共享工作项列表，记录任务状态（待认领/进行中/已完成）。      |
| **Mailbox**   | 代理之间通信的消息系统，支持多向通信（如任务请求、结果汇报、状态更新等）。   |


## 21.3 Git Worktree
允许你在同一个仓库上挂载多个独立的工作目录。每个工作目录有自己的分支、自己的 HEAD、自己的暂存区，但共用同一个 .git 数据库（历史记录、对象存储）。

位置：`<repo>/.claude/worktrees/<name>`

### 21.3.1 使用 Git Worktree
输入：
>```bash
>claude --worktree feature-auth
># 或简写
>claude -w feature-auth
># 或会话里直接和Claude说
>```
会创建目录`.claude/worktrees/feature-auth/` 分支：`worktree-feature-auth` 并自动进入该目录启动 Claude。

可以在多个终端同时启动不同的工作树：
>```bash
># 终端1：做功能
>claude -w feature-auth
>
># 终端2：修bug
>claude -w bugfix-123
>
># 终端3：重构实验
>claude -w refactor-api
>```
三个会话完全隔离，可同时改代码、运行、提交。



### 21.3.2 常用管理命令
>```bash
># 查看所有 Worktree
>git worktree list
>
># 删除 Worktree（合并后删除）
>git worktree remove .claude/worktrees/feature-auth
>
>## 有未提交文件，强制删除
>git worktree remove --force .claude/worktrees/feature-auth
>
>##  清理仓库中失效的 worktree 记录
>git worktree prune
>
># 进入已有 Worktree 目录
>cd .claude/worktrees/feature-auth
>claude  # 直接启动，自动关联分支
>```

# Claude Code GitHub Actions
待续

# 参考
https://code.claude.com/docs/en/overview

https://github.com/luongnv89/claude-howto

https://github.com/affaan-m/everything-claude-code

https://github.com/shareAI-lab/learn-claude-code
