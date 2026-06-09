# 目录

- [1 简介](#1-简介)
- [2 安装](#2-安装)
  - [2.1 Windows 系统安装](#21-windows-系统安装)
- [3 模型运行](#3-模型运行)
  - [3.1 命令行运行](#31-命令行运行)
  - [3.2 直接运行exe文件](#32-直接运行exe文件)
- [4 相关命令](#4-相关命令)
  - [4.1 完整示例](#41-完整示例)
  - [4.2 自定义模型](#42-自定义模型)
  - [4.3 服务管理](#43-服务管理)
- [5 模型交互](#5-模型交互)
- [6 API 交互](#6-api-交互)
- [7 python 使用](#7-python-使用)
  - [7.1 常用 API 方法](#71-常用-api-方法)
- [8 接入Vibe_Coding](#8-接入vibe_coding)
- [9 模型导入](#9-模型导入)
  - [9.1 从魔搭社区导入模型](#91-从魔搭社区导入模型)
- [10 Ollama Open WebUI](#10-ollama-open-webui)
- [11 Ollama Page Assist](#11-ollama-page-assist)
- [12 VLLM](#12-vllm)

---
# 1 简介
Ollama 是一个开源的大型语言模型（LLM）平台，旨在让用户能够轻松地在本地运行、管理和与大型语言模型进行交互  
Ollama 支持多种操作系统，包括 macOS、Windows、Linux 以及通过 Docker 容器运行

# 2 安装
- CPU：多核处理器（推荐 4 核或以上）。
- GPU：如果你计划运行大型模型或进行微调，推荐使用具有较高计算能力的 GPU（如 NVIDIA 的 CUDA 支持）。
- 内存：至少 8GB RAM，运行较大模型时推荐 16GB 或更高。
- 存储：需要足够的硬盘空间来存储预训练模型，通常需要 10GB 至数百 GB 的空间，具体取决于模型的大小。
- 软件要求：确保系统上安装了最新版本的 Python（如果打算使用 Python SDK）。

## 2.1 Windows 系统安装
打开浏览器，访问 Ollama 官方网站：https://ollama.com/download 下载适用于 Windows 的安装程序  
下载地址为：https://ollama.com/download/OllamaSetup.exe  
  
打开命令提示符或 PowerShell，输入以下命令验证安装是否成功：  
ollama --version   
如果需要将 Ollama 安装到非默认路径，可以在安装时通过命令行指定路径，例如：  
>```bash
>OllamaSetup.exe /DIR="d:\Ollama"  
>```

# 3 模型运行 

## 3.1 命令行运行
`ollama run <model>`或`ollama`启动后会让你选择模型

例如我们要运行 Llama 3.2 并与该模型对话可以在终端使用以下命令：
>```bash
>ollama run llama3.2    
># 执行以上命令如果没有该模型会去下载 llama3.2 模型
>```
- ollama list，查看已安装的模型   
- ollama rm Llama 3.2 删除模型  
  
等待下载完成后，我们在终端中，输入以下命令来加载 LLama3.2 模型并进行交互：    
>```bash
>writing manifest 
>success 
>>>> 你好
>Hello
>
>>>> 能讲中文吗
>是的，我可以在 Chinese 中对話。哪些话题或问题想要了解我呢？
>```
- /set：设置会话变量（如温度、上下文长度）。
- /show：显示模型信息。
- /bye：退出对话。
  
结束对话可以输入 /bye 或按 Ctrl+d 按键来结束。

## 3.2 直接运行exe文件

Ollama 支持的模型可以访问：https://ollama.com/library 并查看下载命令

# 4 相关命令
基本格式：`ollama <command> [args]`

可以用 `ollama --help` 查看包含有哪些命令

1. 使用方法  
- ollama [flags]：使用标志（flags）运行 ollama。
- ollama [command]：运行 ollama 的某个具体命令
  
2. 可用命令
- serve：启动 ollama 服务。
- create：根据一个 Modelfile 创建一个模型。
- show：显示某个模型的详细信息。
- run：运行一个模型。
- stop：停止一个正在运行的模型。
- pull：从一个模型仓库拉取(下载)一个模型。
- push：将一个模型推送到一个模型仓库。
- list/ls：列出所有模型。
- ps：列出所有正在运行的模型。
- cp：复制一个模型。
- rm/remove ：删除一个模型。
- help：获取关于任何命令的帮助信息。
  
3. 标志（Flags）
- -h, --help：显示 ollama 的帮助信息。
- -v, --version：显示版本信息。

## 4.1 完整示例
>```bash
># 1. 拉取与删除模型
># pull
># 拉取远端模型到本地。
>ollama pull <model>
>
># rm / remove
># 删除本地模型。
>ollama rm <model>
>
># list / ls
># 列出所有本地模型。
>ollama list
>
>
># 2. 运行模型
># run
># 交互模式运行模型，不退出。
>ollama run <model>
>
># 可带系统信息与 prompt：
>ollama run <model> -s "<system>" -p "<prompt>"
>
># run + script
># 从文件读取 prompt：
>ollama run <model> < input.txt
># 当你输入 ollama run 进入聊天界面后，你不再是在操作命令行，而是在和 AI 对话。这时你可以使用以 / 开头的快捷指令来控制对话：
># /bye 或 /exit：最重要！ 退出聊天界面，返回命令行。
># /clear：清空当前的上下文记忆（开启一段新的对话）。
># /show info：查看当前模型的详细参数信息。
># /set parameter seed 123：设置随机种子（高级玩法，用于复现结果）。
># /help：在聊天中查看所有可用的快捷键。
>
>
># 3. 推理接口（一次性执行）
># generate
># 执行单次推理，输出文本。
>ollama generate <model> -p "<prompt>"
>
>
># 4. 创建与修改模型
># create
># 用 Modelfile 创建本地模型。
>ollama create <model-name> -f Modelfile
>
>
># cp
># 复制一个模型为新名字。
>ollama cp <src> <dst>
>
>
># 5. 服务器相关
># serve
># 启动 Ollama 本地服务（默认 11434）。
>ollama serve
>
># run serverless
># 当 ollama run 时会自动拉起后台服务，不需单独执行。
>
>
># 6. 模型信息
># show
># 查看模型元数据、参数、模板。
>ollama show <model>
>
>
># 7. 专用参数
># 这些参数多数可用于 run/generate：
>--num-predict <number>    限制输出 token 数
>--temperature <float>     控制随机性
>--top-k <int>             采样范围
>--top-p <float>           核采样
>--seed <int>              固定随机性
>--format json             输出 JSON
>--keepalive <seconds>     会话保持时间
>--stream                  流式输出
>
>
># 8. Modelfile 指令
># 构建模型时使用：
>FROM <model>：基础模型
>SYSTEM "xxx"：设定系统提示
>PARAMETER key=value：设定默认参数
>TEMPLATE "xxx"：自定义 Chat 模板
>LICENSE "xxx"：设置 License
>ADAPTER <file> / WEIGHTS <file>：加载 LoRA 或额外权重
>
>
># 9. API（当 serve 运行时）
># REST 端点（默认 http://localhost:11434/api）：
>/api/generate：文本生成
>/api/chat：对话流式接口
>/api/pull：远程拉取
>/api/tags：本地模型列表
>
># 调用示例（curl）：
>curl http://localhost:11434/api/generate \
>  -d '{"model":"qwen2.5","prompt":"hello"}'
>
>
># 10. 进阶
># 自定义参数运行：
>ollama run <model> --temperature 0.2 --top-p 0.9
>
># 持久会话（保留上下文）：
># 会话由模型内部缓存自动管理，无需额外命令。

## 4.2 自定义模型
基于现有模型创建自定义模型  
ollama create < custom-model-name > -f < Modelfile >   
复制模型  
ollama cp < source-model-name > < new-model-name >  
推送自定义模型到模型库  
ollama push < model-name >

## 4.3 服务管理
启动 Ollama 服务以在后台运行：  
ollama serve  
  
停止正在运行的 Ollama 服务：  
ollama stop  
  
重启 Ollama 服务：  
ollama restart  
  
查看所有可用命令：  
ollama --help  
  
查看当前安装的 Ollama 版本：  
ollama version   
  
更新 Ollama 到最新版本：  
ollama update  
   
查看 Ollama 的日志信息：  
ollama logs  
  
清理 Ollama 的缓存：  
ollama clean  
  
查看指定模型的详细信息：  
ollama show < model-name >  
  
查看模型的依赖关系：  
ollama deps < model-name >  
   
查看模型的配置文件：   
ollama config < model-name >  
  
将模型导出为文件：  
ollama export < model-name > < output-file >  
  
从文件导入模型：  
ollama import < input-file >    
  
查看 Ollama 的系统信息：  
ollama system    
   
查看模型的资源使用情况：   
ollama resources < model-name >      
  
查看模型的性能指标：  
ollama perf < model-name >   
  
查看模型的历史记录：  
ollama history < model-name >  
  
检查指定模型的状态：  
ollama status < model-name >    

# 5 模型交互
**命令行交互**  
见“模型运行”

**单次命令交互**  
如果您只需要模型生成一次响应，可以直接在命令行中传递输入
>```bash
>echo "你是谁？" | ollama run deepseek-coder
># 或
>ollama run deepseek-coder "Python 的 hello world 代码？"
>```
**文件输入**  
可以将文件内容作为输入传递给模型。   

假设 input.txt 文件内容为：  
>```txt
>Python 的 hello world 代码？  
>```
将 input.txt 文件内容作为输入：  
>```bash
>ollama run deepseek-coder < input.txt  
>```

**自定义提示词**  
创建自定义模型  
编写一个 Modelfile：  
>```
>FROM deepseek-coder  
>SYSTEM "你是一个编程助手，专门帮助用户编写代码。"  
>```
然后创建自定义模型：  
>```bash
>ollama create runoob-coder -f ./Modelfile   
>```
运行自定义模型:  
>```bash
>ollama run runoob-coder  
>```

**交互日志**  
Ollama 会记录交互日志，方便调试和分析   
>```bash 
># 查看所有日志
>ollama logs   
>``` 

# 6 API 交互
Ollama 提供了基于 HTTP 的 API，允许开发者通过编程方式与模型进行交互。  
在使用 API 之前，需要确保 Ollama 服务正在运行。可以通过以下命令启动服务：
>```bash  
>ollama serve
>```  
>默认情况下，服务会运行在 http://localhost:11434  
>  
>Ollama 提供了以下主要 API 端点：  
>
>**生成文本（Generate Text）**  
>端点：POST /api/generate  
>功能：向模型发送提示词（prompt），并获取生成的文本。  
>  
>请求格式：  
>```py
>{
>  "model": "<model-name>",  // 模型名称
>  "prompt": "<input-text>", // 输入的提示词
>  "stream": false,          // 是否启用流式响应（默认 false）
>  "options": {              // 可选参数
>    "temperature": 0.7,     // 温度参数
>    "max_tokens": 100       // 最大 token 数
>  }
>}
>```
响应格式：
>```py
>{
>  "response": "<generated-text>", // 生成的文本
>  "done": true                    // 是否完成
>}
>```

**聊天（Chat）**  
端点：POST /api/chat  
功能：支持多轮对话，模型会记住上下文。  
  
请求格式：
>```py
>{
>  "model": "<model-name>",  // 模型名称
>  "messages": [             // 消息列表
>    {
>      "role": "user",       // 用户角色
>      "content": "<input-text>" // 用户输入
>    }
>  ],
>  "stream": false,          // 是否启用流式响应
>  "options": {              // 可选参数
>    "temperature": 0.7,
>    "max_tokens": 100
>  }
>}
>```
响应格式：  
>```py
>{
>  "message": {
>    "role": "assistant",    // 助手角色
>    "content": "<generated-text>" // 生成的文本
>  },
>  "done": true
>}
>```
  
**列出本地模型（List Models）**  
端点：GET /api/tags  
功能：列出本地已下载的模型。  
  
响应格式：  
>```py
>{
>  "models": [
>    {
>      "name": "<model-name>", // 模型名称
>      "size": "<model-size>", // 模型大小
>      "modified_at": "<timestamp>" // 修改时间
>    }
>  ]
>}
>```
  
**拉取模型（Pull Model）**  
端点：POST /api/pull  
功能：从模型库中拉取模型。  
  
请求格式：  
>```py
>{
>  "name": "<model-name>" // 模型名称
>}
>```
响应格式：  
>```py
>{
>  "status": "downloading", // 下载状态
>  "digest": "<model-digest>" // 模型摘要
>}
>```

## 示例  
**生成文本**  
使用 curl 发送请求  
>```
>curl http://localhost:11434/api/generate -d '{
>  "model": "deepseek-coder",
>  "prompt": "你好，你能帮我写一段代码吗？",
>  "stream": false
>}'
>```

**多轮对话**  
使用 curl 发送请求    
>```
>curl http://localhost:11434/api/chat -d '{
>  "model": "deepseek-coder",
>  "messages": [
>    {
>      "role": "user",
>      "content": "你好，你能帮我写一段 Python 代码吗？"
>    }
>  ],
>  "stream": false
>}'
>```  
>
>**列出本地模型**
>使用 curl 发送请求：
>```
curl http://localhost:11434/api/tags
>```
>
>**启用流式响应**  
>在请求中设置 "stream": true，API 会逐行返回生成的文本  
>每行返回一个 JSON 对象  
>响应格式如下  
>```json
>{
>  "response": "<partial-text>", // 部分生成的文本
>  "done": false                 // 是否完成
>}
>```
  
Python 使用 requests 库与 Ollama API 交互：  
>```python
>import requests
>
># 生成文本
>response = requests.post(
>    "http://localhost:11434/api/generate",
>    json={
>        "model": "deepseek-coder",
>        "prompt": "你好，你能帮我写一段代码吗？",
>        "stream": False
>    }
>)
>print(response.json())
>
># 多轮对话
>response = requests.post(
>    "http://localhost:11434/api/chat",
>    json={
>        "model": "deepseek-coder",
>        "messages": [
>            {
>                "role": "user",
>                "content": "你好，你能帮我写一段 Python 代码吗？"
>            }
>        ],
>        "stream": False
>    }
>)
>print(response.json())
>```


# 7 python 使用
首先，我们需要安装 Ollama 的 Python SDK  
>```bash
>pip install ollama
>```
在使用 Python SDK 之前，确保 Ollama 本地服务已经启动  
>```bash
>ollama serve
>```
使用 Ollama 的 Python SDK  
>```python
>from ollama import chat
>from ollama import ChatResponse
>
>response: ChatResponse = chat(model='deepseek-coder', messages=[
>  {
>    'role': 'user',
>    'content': '你是谁？',
>  },
>])
># 打印响应内容
>print(response['message']['content'])
>
># 或者直接访问响应对象的字段
>#print(response.message.content)
>```
流式响应
>```python
>from ollama import chat
>
>stream = chat(
>    model='deepseek-coder',
>    messages=[{'role': 'user', 'content': '你是谁？'}],
>    stream=True,
>)
>
># 逐块打印响应内容
>for chunk in stream:
>    print(chunk['message']['content'], end='', flush=True)
>```
  
创建自定义客户端  
通过 Client，你可以自定义请求的设置（如请求头、URL 等），并发送请求。
  
>```python
>from ollama import Client
>
>client = Client(
>    host='http://localhost:11434',
>    headers={'x-some-header': 'some-value'}
>)
>
>response = client.chat(model='deepseek-coder', messages=[
>    {
>        'role': 'user',
>        'content': '你是谁?',
>    },
>])
>print(response['message']['content'])
>```

异步客户端  
如果你希望异步执行请求，可以使用 AsyncClient 类，适用于需要并发的场景。  

>```python
>import asyncio
>from ollama import AsyncClient
>
>async def chat():
>    message = {'role': 'user', 'content': '你是谁?'}
>    response = await AsyncClient().chat(model='deepseek-coder', messages=[message])
>    print(response['message']['content'])
>
>asyncio.run(chat())
>```
异步客户端支持与传统的同步请求一样的功能，唯一的区别是请求是异步执行的，可以提高性能，尤其是在高并发场景下  
  
异步流式响应  
>```python
>import asyncio
>from ollama import AsyncClient
>
>async def chat():
>    message = {'role': 'user', 'content': '你是谁?'}
>    async for part in await AsyncClient().chat(model='deepseek-coder', messages=[message], stream=True):
>        print(part['message']['content'], end='', flush=True)
>
>asyncio.run(chat())
>```


## 7.1 常用 API 方法
>```py
># 1. chat 方法
># 与模型进行对话生成，发送用户消息并获取模型响应：
>ollama.chat(model='llama3.2', messages=[{'role': 'user', 'content': 'Why is the sky blue?'}])
>
># 2. generate 方法
># 用于文本生成任务。与 chat 方法类似，但是它只需要一个 prompt 参数：
>ollama.generate(model='llama3.2', prompt='Why is the sky blue?')
>
># 3. list 方法
># 列出所有可用的模型：
>ollama.list()
>
># 4. show 方法
># 显示指定模型的详细信息：
>ollama.show('llama3.2')
>
># 5. create 方法
># 从现有模型创建新的模型：
>ollama.create(model='example', from_='llama3.2', system="You are Mario from Super Mario Bros.")
>
># 6. copy 方法
># 复制模型到另一个位置：
>ollama.copy('llama3.2', 'user/llama3.2')
>
># 7. delete 方法
># 删除指定模型：
>ollama.delete('llama3.2')
>
># 8. pull 方法
># 从远程仓库拉取模型：
>ollama.pull('llama3.2')
>
># 9. push 方法
># 将本地模型推送到远程仓库：
>ollama.push('user/llama3.2')
>
># 10. embed 方法
># 生成文本嵌入：
>ollama.embed(model='llama3.2', input='The sky is blue because of rayleigh scattering')
>
># 11. ps 方法
># 查看正在运行的模型列表：
>ollama.ps()
>```

# 8 接入Vibe_Coding
>```bash
>ollama
># 选择启动方式 或
>ollama launch claude --model qwen3-coder
>```

# 9 模型导入
## 9.1 从魔搭社区导入模型
1. 下载模型
>```python
># 安装ModelScope库
>pip install modelscope
>
># 下载DeepSeek-Coder-7B（魔搭示例）
>from modelscope.hub.snapshot_download import snapshot_download
># 下载到本地目录（建议SSD，如D:\models）
>model_dir = snapshot_download(
>    model_id="deepseek-ai/deepseek-coder-7b-base",
>    cache_dir="D:/models"
>)
>print(f"模型下载路径：{model_dir}")
>```

2.转换格式（魔搭下载的模型多为pytorch格式（.bin/.safetensors），Ollama 仅支持GGUF 格式）
>```py
># 1. 安装llama.cpp依赖
>pip install llama-cpp-python
>
># 2. 下载转换脚本（Windows直接用PowerShell）
>git clone https://github.com/ggerganov/llama.cpp.git
>cd llama.cpp
>
># 3. 安装转换所需依赖
>python -m pip install -r requirements.txt
>
># 4. 执行转换
># 参数说明：
># -i：魔搭模型路径
># -o：输出GGUF文件路径
># --quantize q4_0：量化为4bit
>python convert.py D:/models --outfile D:/models/deepseek-coder-7b.gguf --quantize q4_0
>```

3. 编写 Ollama 的 Modelfile 导入 GGUF 模型  
在 GGUF 文件同目录下新建Modelfile（无后缀）  
>```
># 指定本地GGUF模型文件路径（绝对路径）
>FROM D:/models/deepseek-coder-7b.gguf
>
># 适配硬件参数
>PARAMETER num_ctx 4096
>PARAMETER num_gpu 1
>PARAMETER num_thread 8
>PARAMETER low_vram true
>PARAMETER temperature 0.2
>
># 代码模型专属提示词
>SYSTEM """
>你是专业代码助手，精通Python/Java/C++，输出规范代码+中文注释，无多余闲聊。
>"""
>```

4. 创建 Ollama 自定义模型  
打开 CMD/PowerShell，进入Modelfile所在目录，执行：
>```bash
># 创建模型（命名为my-modelscope-coder）
>ollama create my-modelscope-coder -f Modelfile
>
># 验证是否创建成功
>ollama list
># 输出中看到my-modelscope-coder:latest即为成功
>```
可直接在魔搭搜索 “GGUF 格式” 模型（部分作者已提前转换），下载后跳过步骤 2，直接从步骤 3 开始导入。

# 10 Ollama Open WebUI
Open WebUI 用户友好的 AI 界面（支持 Ollama、OpenAI API 等）  
Open WebUI 支持多种语言模型运行器，并内置了用于检索增强生成（RAG）的推理引擎，使其成为强大的 AI 部署解决方案  
Open WebUI 可自定义 OpenAI API URL，连接 LMStudio、GroqCloud、Mistral、OpenRouter 等  
Open WebUI 支持桌面、笔记本电脑和移动设备，并提供移动设备上的渐进式 Web 应用（PWA），支持离线访问  

Docker一键部署或Python环境手动安装  
- Docker
1. 下载并安装Docker Desktop,启动Docker服务
2. docker run -d -p 3000:8080 --gpus all --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:cuda
3. 打开浏览器，输入 http://localhost:3000，即可进入界面
- python
1. 安装之前，请确保使用的是 Python 3.11，以避免可能出现的兼容性问题
2. pip install open-webui
3. open-webui serve
4. http://localhost:8080

# 11 Ollama Page Assist
Page Assist 是一款开源的浏览器扩展程序，主要为本地 AI 模型提供直观的交互界面，让用户可以在任何网页上与本地 AI 模型进行对话和交互。

# 12 VLLM
Transformers 库在本地直接运行开源模型。该方法非常适合入门学习和功能验证，但其底层实现在处理高并发请求时性能有限，通常不作为生产环境的首选方案。

为了在本地实现高性能、生产级的模型推理服务，社区涌现出了 VLLM 和 Ollama 等优秀工具。它们通过连续批处理、PagedAttention 等技术，显著提升了模型的吞吐量和运行效率，并将模型封装为兼容 OpenAI 标准的 API 服务。

VLLM 是一个为 LLM 推理设计的高性能 Python 库。它通过 PagedAttention 等先进技术，可以实现比标准 Transformers 实现高出数倍的吞吐量。

