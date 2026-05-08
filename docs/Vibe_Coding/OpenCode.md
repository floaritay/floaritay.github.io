# 安装 OpenCode
推荐使用npm安装：

1. 安装或更新 Node.js（v18.0 或更高版本）。

2. 在终端执行以下命令安装OpenCode
>```bash
>npm install -g opencode-ai
>```
3. 安装结束后，执行以下命令查看安装结果，若显示版本号则安装成功
>```
>opencode -v
>```

# 在 OpenCode 中配置 Coding Plan
复制以下内容，写入配置文件opencode.json中并保存。如果路径中的文件夹或文件不存在，请手动创建。

- 将<YOUR_API_KEY>替换为Coding Plan 专属 API Key

- 在baseURL中填写Coding Plan的BaseUrl。目前套餐仅支持贵阳基地二区，使用openai接口协议时，填写https://aigw-gzgy2.cucloud.cn:8443/v1

注意，不同操作系统的配置文件路径不同：

- macOS / Linux: ~/.config/opencode/opencode.json

- Windows: C:\Users\您的用户名\.config\opencode\opencode.json
>```json
>{
>  "$schema": "https://opencode.ai/config.json",
>  "provider": {
>    "myprovider": {
>      "npm": "@ai-sdk/openai-compatible",
>      "name": "AISP Coding Plan",
>      "options": {
>        "baseURL": "https://aigw-gzgy2.cucloud.cn:8443/v1",
>        "apiKey": "<YOUR_API_KEY>"
>      },
>      "models": {
>        "Qwen3.5-397B-A17B": {
>          "name": "Qwen3.5-397B-A17B",
>          "options": {
>            "thinking": {
>              "type": "enabled"
>            }
>          }
>        },
>        "glm-5": {
>          "name": "glm-5",
>          "options": {
>            "thinking": {
>              "type": "enabled"
>            }
>          }
>        },
>        "MiniMax-M2.5": {
>          "name": "MiniMax-M2.5",
>          "options": {
>            "thinking": {
>              "type": "enabled"
>            }
>          }
>        },
>        "kimi-k2.5": {
>          "name": "kimi-k2.5",
>          "options": {
>            "thinking": {
>              "type": "enabled"
>            }
>          }
>        },
>        "Qwen3-235B-A22B": {
>          "name": "Qwen3-235B-A22B",
>          "options": {
>            "thinking": {
>              "type": "enabled"
>            }
>          }
>        }
>      }
>    }
>  }
>}
>```

# 使用 OpenCode
在终端运行 opencode 启动 OpenCode
>```bash
>opencode
>```
使用以下命令来选择模型，例如Qwen3-235B-A22B。
>```bash
>/models

除已列出的工具外，Coding Plan 还支持接入兼容 OpenAI / Anthropic API 协议且支持自定义服务端点的第三方工具
