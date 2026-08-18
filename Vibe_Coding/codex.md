# 目录

- [1 介绍](#1-介绍)
- [2 安装](#2-安装)
  - [2.1 安装Codex 应用](#21-安装codex-应用)
  - [2.2 安装Codex CLI](#22-安装codex-cli)
  - [2.3 其他安装方式略](#23-其他安装方式略)
- [3 桌面应用界面概览与配置](#3-桌面应用界面概览与配置)
- [4 斜杠命令](#4-斜杠命令)
- [5 computer use](#5-computer-use)
- [6 速查表](#6-速查表)
- [7 Codex Web](#7-codex-web)
  - [7.1 设置脚本](#71-设置脚本)
  - [7.2 环境变量与 Secrets](#72-环境变量与-secrets)
  - [7.3 网络访问控制](#73-网络访问控制)
  - [7.4 容器缓存](#74-容器缓存)
- [8 skills、子代理、MCP、Rules 与 钩子](#8-skills子代理mcprules-与-钩子)
- [9 worktrees](#9-worktrees)

---
# 1 介绍
在 [Claude](../Vibe_Coding/Claude.ipynb) 基础上编写。

Codex同Claude一样是一个 AI 编程代理。

Codex 提供四种使用方式

| 方式 | 说明 | 适用场景 |
| --- | --- | --- |
| App（桌面应用） | macOS/Windows 桌面客户端 | 完整功能、多项目并行 |
| IDE 扩展 | VS Code、Cursor、Windsurf 插件 | 深度集成开发环境 |
| CLI（命令行） | 终端交互式工具 | 终端爱好者、脚本自动化 |
| Web（云端） | chatgpt.com/codex 网页版 | 远程访问、并行任务 |

架构：略

基本概念：略

# 2 安装
## 2.1 安装Codex 应用
访问：https://chatgpt.com/codex 下载应用。

登录 ChatGPT 账号或配置base_url，key等。如果使用 API Key 登录，部分云端功能可能不可用。

或使用cc-switch，参考[cc-switch](../Vibe_Coding/CC_Switch.ipynb)。

## 2.2 安装Codex CLI
```bash
sudo npm install -g @openai/codex
# 使用国内镜像安装更快
sudo npm install -g @openai/codex --registry=https://registry.npmmirror.com
```
安装完成后运行：
```bash
codex
```
即可使用

## 2.3 其他安装方式略

# 3 桌面应用界面概览与配置
**界面结构**

略

**运行模式**

| 模式 | 说明 | 适用场景 |
| --- | --- | --- |
| Local | 在本地项目目录工作 | 日常开发、直接查看结果 |
| Worktree | 在独立 Git worktree 中工作 | 隔离变更、并行开发 |
| Cloud | 在云端隔离环境运行 | 远程委派、并行处理 |

**权限**

| 权限模式 | 能做什么 | 会不会询问你 | 适合场景 |
| --- | --- | --- | --- |
| 默认权限 | 可以读写当前项目、执行基础命令 | 遇到危险操作会询问 | 日常开发（推荐） |
| 自动审查 | AI 自动判断风险，低风险直接执行 | 高风险才询问 | 提高效率 |
| 完全访问权限 | 几乎等于把电脑控制权交给 Codex | 基本不问 | 高级用户 / 隔离环境 |

**配置**

略

配置文件位置

| 层级 | 路径 | 作用范围 | 优先级 |
| --- | --- | --- | --- |
| 用户级 | ~/.codex/config.toml | 全局默认配置 | 低 |
| 项目级 | .codex/config.toml | 项目特定配置 | 中 |
| 托管级 | 企业下发 | 企业统一配置 | 高 |

**AGENTS.md**

AGENTS.md 是项目级的 Agent 指令文件，定义 Codex 在该项目中的行为规范。功能与使用都类似CLAUDE.md。

可以在子目录放置 AGENTS.override.md。同一目录下，AGENTS.override.md 存在时，同级的 AGENTS.md 会被跳过。

AGENTS.md 大小限制为 32 KiB，超过会被截断。

**skill**

可复用的自定义能力，封装常用任务逻辑。

技能目录位置

| 位置 | 路径 | 作用 |
| --- | --- | --- |
| REPO | .agents/skills/ | 项目级技能 |
| USER | ~/.agents/skills/ | 用户级技能 |
| ADMIN | /etc/codex/skills/ | 系统级技能 |
| SYSTEM | 内置 | 官方预置技能 |

技能结构
```md
skill-name/
├── SKILL.md       # 技能定义（必需）
├── scripts/       # 可选脚本
├── references/    # 可选参考文档
└── assets/        # 可选资源
```

**Subagents**

**Rules**

规则使用 Starlark 语言，示例：
```md
# ~/.codex/rules/default.rules

# 允许 Git 命令
prefix_rule(
    pattern = ["git"],
    decision = "allow",
    justification = "Git commands are safe"
)

# 禁止 rm -rf /
prefix_rule(
    pattern = ["rm", "-rf", "/"],
    decision = "forbidden",
    justification = "Prevent system damage"
)

# 询问 npm 命令
prefix_rule(
    pattern = ["npm"],
    decision = "prompt",
    justification = "npm may modify dependencies"
)
```

**Hooks**

# 4 斜杠命令
在对话框中输入/符号后，系统会立即弹出命令面板，列出所有可用命令及其说明。只要输入 / 然后选择对应的功能即可。

常用命令速览

| 命令 | 功能 | 速记说明 |
| --- | --- | --- |
| /compact | 压缩上下文 | 长对话 token 不足时，智能摘要历史记录 |
| /status | 查看状态 | 对话 ID、token 用量、剩余额度一览 |
| /review | 代码审查 | AI 自动检查 bug、安全、性能、风格 |
| /side | 侧边对话 | 临时分支中安全探索，不污染主线 |
| /fork | 派生分支 | 创建 Git 分支或新工作树，并行演进 |
| /mcp | MCP 状态 | 查看外部服务连接和工具可用情况 |
| /reasoning | 推理强度 | 低 / 中 / 高三档可调，命令后显示当前档位 |
| /model | 切换模型 | 切换底层 AI 模型，命令后显示当前模型名 |
| /persona | 设置个性 | 调整 AI 回复语气和风格 |
| /feedback | 提交反馈 | 向 Anthropic 报告问题或建议 |
| /pet | 桌面宠物 | 唤醒或收起内置桌面宠物（彩蛋功能） |


# 5 computer use
Computer Use（电脑操控） 是 Codex 提供的一项功能，允许 Codex 查看和操作 macOS 或 Windows 上的图形用户界面（GUI）。可以直接与图形界面交互，包括点击按钮、输入文字、浏览菜单等操作。

打开 Codex 设置，找到 Computer Use 选项，点击 Install 安装 Computer Use 插件。

安装完成后即可让 Codex 开始操作桌面应用。

在 Windows 上，Computer Use 无法在后台运行。如果你需要同时继续使用桌面，建议使用虚拟机或第二台设备。

# 6 速查表
**命令速查表**

CLI 基础命令

| 命令 | 说明 |
| --- | --- |
| `codex` | 启动交互式 TUI |
| `codex "任务"` | 启动并执行指定任务 |
| `codex exec "任务"` | 非交互模式执行任务 |
| `codex --version` | 显示版本信息 |
| `codex --help` | 显示帮助信息 |

斜杠命令 (Slash Commands)

| 命令 | 说明 |
| --- | --- |
| `/model <name>` | 切换模型 |
| `/fast` | 切换 Fast 模式 |
| `/plan` | 进入计划模式 |
| `/review` | 审查代码变更 |
| `/new` | 开始新会话 |
| `/resume` | 恢复历史会话 |
| `/fork` | 克隆当前会话 |
| `/compact` | 压缩上下文 |
| `/status` | 显示会话状态 |
| `/clear` | 清除屏幕 |
| `/quit` | 退出 Codex |
| `/approval <mode>` | 切换审批模式 |

CLI 参数

| 参数 | 说明 |
| --- | --- |
| `-m <model>` | 指定模型 |
| `--sandbox <mode>` | 设置沙箱模式 |
| `--approval-mode <mode>` | 设置审批模式 |
| `-i <file>` | 附加图片 |
| `-o <file>` | 输出到文件（exec） |
| `--full-auto` | 全自动执行 |
| `--ephemeral` | 不保存会话文件 |
| `--reasoning-effort <level>` | 推理强度 |

Shell 命令执行

| 格式 | 说明 |
| --- | --- |
| `! <command>` | 在 Codex 中执行 Shell 命令 |
| `! git status` | 查看 Git 状态 |
| `! npm test` | 运行测试 |

**配置文件路径**

配置文件位置

| 文件 | 路径 | 作用 |
| --- | --- | --- |
| 用户配置 | `~/.codex/config.toml` | 全局默认配置 |
| 项目配置 | `.codex/config.toml` | 项目特定配置 |
| 项目指令 | `AGENTS.md` | 项目行为规范 |
| 日志目录 | `~/.codex/log/` | 运行日志 |
| 会话目录 | `~/.codex/sessions/` | 会话记录 |

技能目录

| 位置 | 路径 |
| --- | --- |
| 项目级 | `.agents/skills/` |
| 用户级 | `~/.agents/skills/` |
| 系统级 | `/etc/codex/skills/` |

**快捷键**

CLI 快捷键

| 快捷键 | 功能 |
| --- | --- |
| `Enter` | 发送消息 |
| `Shift+Enter` | 换行 |
| `Ctrl+C` | 中断操作 |
| `Ctrl+C` (两次) | 退出 Codex |
| `Ctrl+D` | 退出（输入空时） |
| `Ctrl+R` | 搜索历史 |
| `Up/Down` | 浏览历史 |
| `Tab` | 自动补全 |
| `Esc Esc` | 编辑上一条消息 |
| `Ctrl+O` | 复制最后回复 |

App 快捷键

| 快捷键 | 功能 |
| --- | --- |
| `Cmd/Ctrl+N` | 新建会话 |
| `Cmd/Ctrl+Shift+N` | 新建窗口 |
| `Cmd/Ctrl+W` | 关闭窗口/标签 |
| `Cmd/Ctrl+[` | 上一个标签 |
| `Cmd/Ctrl+]` | 下一个标签 |

# 7 Codex Web
云端版本，让你从任何设备访问 Codex，在隔离环境中运行任务。

访问云端 Codex：https://chatgpt.com/codex

使用前提
- ChatGPT Plus / Pro / Business / Enterprise 计划
- 或使用 OpenAI API Key

使用 API Key 时，部分云端功能可能不可用。

在云端中，每个环境是一个隔离的工作空间。

创建环境
1. 连接 GitHub 账号
2. 选择一个仓库
3. 配置设置脚本和环境变量
4. 选择网络访问策略

云端任务按以下流程执行：
1. 创建容器，克隆仓库到选定分支
2. 运行设置脚本安装依赖
3. 应用网络访问设置
4. Agent 执行任务（编辑代码、运行命令、验证结果）
5. 显示结果和文件变更

云端支持并行运行多个任务

## 7.1 设置脚本
Codex 自动识别项目类型并执行相应依赖安装

自定义设置脚本
```md
# Setup Script
# 在环境设置中配置

npm install
npm run build
pip install -r requirements.txt
```

设置脚本与 Agent 在不同的 Bash 会话中运行，export 命令不会持久化。

## 7.2 环境变量与 Secrets
环境变量在整个任务期间可用：
```bash
# Environment Variables
NODE_ENV=production
DEBUG=false
API_ENDPOINT=https://api.example.com
```

Secrets 用于存储敏感信息：
- 额外加密存储
- 仅在任务执行时解密
- 只在设置脚本中可用
- Agent 阶段自动移除

## 7.3 网络访问控制
默认设置

| 阶段 | 网络访问 |
| --- | --- |
| 设置脚本 | 允许（安装依赖需要） |
| Agent | 禁止（默认） |

Agent 网络访问选项

| 设置 | 说明 |
| --- | --- |
| Off | 完全禁止网络访问 |
| On | 允许网络访问（可限制域名） |


域名白名单
```md
# 网络配置

# 白名单预设
domain_allowlist = "common-dependencies"
# 包含：github.com, npmjs.com, pypi.org 等

# 自定义域名
domain_allowlist = [
    "github.com",
    "api.mycompany.com"
]

# 限制 HTTP 方法
allowed_methods = ["GET", "HEAD", "OPTIONS"]
```

启用 Agent 网络访问会增加风险,仅在必要时启用 Agent 网络访问，并使用域名白名单限制。

## 7.4 容器缓存
- 缓存最多 12 小时
- 设置脚本或环境变量变化时自动失效
- 新任务启动更快

# 8 skills、子代理、MCP、Rules 与 钩子
略

# 9 worktrees
Worktrees 允许你在 Git 仓库中创建多个工作目录，使你能够并行处理不同的任务而不会相互干扰。

- 并行开发多个功能，适合大型项目
- 保持主分支干净
- 同时进行开发和代码审查

在 Codex 应用中创建 Worktree
1. 选择项目
2. 点击 "New" -> "Worktree"
3. 输入分支名称
4. 点击创建

在创建线程时选择 Worktree 模式，在独立的 Git worktree 中工作

Worktree 管理
```bash
# 查看 worktree 列表
git worktree list

# 创建新的 worktree
git worktree add ../feature-branch -b feature-branch

# 删除 worktree
git worktree remove ../feature-branch
```

提示
- 为每个功能或修复创建独立的 Worktree
- 使用描述性的分支名称
- 完成后及时清理不需要的 Worktree

# 自动化与 CI/CD

# 工作流示例 与 提示词实践

# GitHub 集成
