# 1 基础
先参考[Agent](../Agent/Agent.ipynb)章节，了解Agent的基本概念和使用方法。

OpenAI的reponse：
```json
{
  "id": "chatcmpl-abc123",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Hello! How can I help?"
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 10,
    "completion_tokens": 15,
    "total_tokens": 25
  },
  "created": 1234567890,
  "model": "gpt-3.5-turbo"
}
```

# 目录
  - [1.1 对话](#11-对话)
  - [1.2 记忆](#12-记忆)
  - [1.3 工具调用](#13-工具调用)
    - [1.3.1 Function Calling](#131-function-calling)
    - [1.3.2 联网搜索](#132-联网搜索)
    - [1.3.3网页抓取](#133网页抓取)
    - [1.3.4 代码解释器](#134-代码解释器)
    - [1.3.5 知识库检索](#135-知识库检索)
    - [1.3.6 MCP](#136-mcp)
- [2 推理与规划](#2-推理与规划)
  - [2.1 ReAct 框架](#21-react-框架)
  - [2.2 CoT（Chain of Thought）](#22-cotchain-of-thought)
  - [2.3 ToT（Tree of Thoughts）](#23-tottree-of-thoughts)
  - [2.4 任务规划与 MCTS](#24-任务规划与-mcts)
  - [2.5 Reflexion（自我反思）](#25-reflexion自我反思)
  - [2.6 任务分解](#26-任务分解)
    - [2.6.1 递归任务分解](#261-递归任务分解)
    - [2.6.2 平行任务分解](#262-平行任务分解)
    - [2.6.3 层次任务分解](#263-层次任务分解)
  - [2.7 Plan-and-Execute](#27-plan-and-execute)
- [3. RAG](#3-rag)
  - [3.1 基础 RAG](#31-基础-rag)
  - [3.2 Advanced RAG](#32-advanced-rag)
  - [3.3 混合检索](#33-混合检索)
  - [3.4 GraphRAG](#34-graphrag)

---



## 1.1 对话


```python
from openai import OpenAI
import os

api_key = os.getenv('DASHSCOPE_API_KEY')
# print(api_key)

client = OpenAI(
    api_key =  api_key,
    base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1",
)

reponse = client.chat.completions.create(
    model = 'qwen3.5-plus-2026-04-20',
    messages = [
        {'role':'system','content':'You are a helpful assistant'},
        {'role':'user','content':'你好'}
    ],
    stream = False
)

print(reponse.choices[0].message.content.strip())

```

    你好！有什么我可以帮你的吗？
    

## 1.2 记忆


```python
import os
from typing import List, Dict, Any
from openai import OpenAI

class MemoryAgent:
    def __init__(self,model:str='qwen3.5-plus-2026-04-20'):
        api_key = os.getenv('DASHSCOPE_API_KEY')
        base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1"
        if not api_key :
            raise ValueError('请设置 DASHSCOPE_API_KEY 环境变量')
        
        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url
        )
        self.model=model
        self.conversation_history:List[Dict[str,str]] = []
        self.system_prompt = '你是一个有用的助手，能够好的回答用户的问题'

    def add_history(self,role:str,content:str):
        """添加消息到对话历史"""
        self.conversation_history.append({
            'role':role,
            'content':content
        })

        if len(self.conversation_history)>10: # 保留最后10个
            self.conversation_history = self.conversation_history[-10:]

    def ask(self,question:str)->str:
        self.add_history('user',question)

        messages = [
            {'role':'system','content':self.system_prompt},
        ]
        messages.extend(self.conversation_history)

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            max_tokens=500,
        )
        answer = response.choices[0].message.content

        self.add_history('assistant',answer)

        return answer
    
    def clear_history(self):
        """清空对话历史"""
        self.conversation_history.clear()
```


```python
def test_MemoryAgent():
    """测试基础问答 Agent"""
    print("=== 开始测试 ===")

    agent = MemoryAgent()

    questions = [
        '你好',
        '我最喜欢的动物是小狗',
        '介绍一下你自己',
        '我喜欢什么动物'
    ] # 能记住我们喜欢的动物

    for question in questions:
        answer = agent.ask(question)
        print(f"user:{question}")
        print(f"assistant:{answer}")

    print("\n测试完成")

if __name__ == "__main__":
    test_MemoryAgent()
```

    === 开始测试 ===
    'user':你好
    assistant:你好！有什么我可以帮你的吗？
    'user':我最喜欢的动物是小狗
    assistant:小狗确实非常可爱又忠诚！它们不仅能给人带来很多快乐，还能成为特别贴心的陪伴。你养过小狗吗？或者有没有特别偏好的犬种？比如温顺的金毛、活泼的柯基、聪明的边境牧羊犬，还是憨萌的柴犬之类的？
    
    如果你愿意的话，也可以和我分享你和狗狗之间的小故事，或者你最喜欢狗狗的哪个特点～ 😊🐶
    'user':介绍一下你自己
    assistant:你好！我是通义千问（英文名 Qwen），由阿里巴巴集团旗下通义实验室自主研发的大语言模型。你可以把我当成一个随时在线的思考伙伴和多功能助手。
    
    我主要擅长这些方面：
    🔹 **知识解答与学习辅导**：覆盖科学、人文、技术、生活等各个领域，能帮你理清概念、梳理重点。  
    🔹 **逻辑推理与问题解决**：处理数学计算、推理题、复杂任务拆解等，尽力给出清晰、可追溯的思路。  
    🔹 **创作与写作辅助**：无论是文章、邮件、报告、故事还是策划案，我都可以帮你起草、润色或提供灵感。  
    🔹 **代码与开发支持**：支持多种编程语言的编写、调试、解释和架构建议，也能帮你理解技术文档。  
    🔹 **多语言与长文本处理**：流畅支持全球一百多种语言，同时能一次性理解超长上下文（最多约 256K token），适合处理长文档或连续对话。  
    🔹 **视觉与内容解析**：可以识别图片中的文字、图表、数学公式，并提取关键信息或进行深度分析。
    
    我的风格是**专业、耐心、务实**，会尽量根据你的使用场景调整回答的深度和表达方式。不追求“说很多”，而是力求“说得准、用得上”。
    
    如果你有任何具体问题、想探讨的话题，或者需要我帮你完成某项任务，随时告诉我就好。今天有什么我可以帮你的吗？😊
    'user':我喜欢什么动物
    assistant:根据你刚才告诉我的，你最喜欢的动物是**小狗**🐶！狗狗忠诚、活泼又充满陪伴感，确实是很多人的心头好。你养过狗狗吗？或者有没有特别偏好的犬种呢？
    
    测试完成
    

## 1.3 工具调用

### 1.3.1 Function Calling


```python
import os
import json
import requests
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# ---------------------- 心知天气工具类（调用真实的API查询天气） ----------------------
class SeniverseWeather:
    BASE_URL = "https://api.seniverse.com/v3"

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.session = requests.Session()

    def _get(self, endpoint: str, **params) -> dict:
        params["key"] = self.api_key
        params.setdefault("language", "zh-Hans")
        params.setdefault("unit", "c")
        resp = self.session.get(f"{self.BASE_URL}/{endpoint}", params=params, timeout=10)
        resp.raise_for_status()
        results = resp.json().get("results", [])
        return results[0] if results else {}

    def now(self, location: str) -> dict:
        return self._get("weather/now.json", location=location)

    def daily(self, location: str, days: int = 3) -> dict:
        return self._get("weather/daily.json", location=location, days=days)

    def life(self, location: str) -> dict:
        return self._get("life/suggestion.json", location=location, days=1)

# ---------------------- 格式化函数 ----------------------
def format_now(data: dict) -> str:
    if "error" in data:
        return data["error"]
    loc = data.get("location", {}).get("name", "未知")
    now = data.get("now", {})
    return f"{loc}当前天气: {now.get('text', '?')} {now.get('temperature', '?')}°C"

def format_daily(data: dict) -> str:
    if "error" in data:
        return data["error"]
    loc = data.get("location", {}).get("name", "未知")
    lines = [f"{loc}天气预报:"]
    for d in data.get("daily", []):
        date = d.get("date", "?")
        lines.append(f"  {date}: {d.get('text_day', '?')} {d.get('high', '?')}°C / {d.get('text_night', '?')} {d.get('low', '?')}°C")
    return "\n".join(lines)

def format_life(data: dict) -> str:
    if "error" in data:
        return data["error"]
    loc = data.get("location", {}).get("name", "未知")
    labels = {"dressing": "穿衣", "uv": "紫外线", "car_washing": "洗车", "travel": "旅游", "flu": "感冒", "sport": "运动"}
    lines = [f"{loc}生活指数:"]
    for s in data.get("suggestion", []):
        for key, label in labels.items():
            if key in s:
                lines.append(f"  {label}: {s[key].get('brief', '?')}")
    return "\n".join(lines)

# ---------------------- Function Calling Agent ----------------------
class WeatherAgent:
    MODEL = "qwen-plus"

    def __init__(self):
        self.weather = SeniverseWeather(os.environ["SENIVERSE_API_KEY"])
        self.client = OpenAI(
            api_key=os.environ["DASHSCOPE_API_KEY"],
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        )
        self.conversation_history = []
        self.system_prompt = "你是友好的天气助手，可以调用工具查询天气。"

    def get_tools(self):
        return [
            {
                "type": "function",
                "function": {
                    "name": "get_weather_info",
                    "description": "查询天气，current=实时，forecast=预报，life=生活指数",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "location": {"type": "string"},
                            "wtype": {"type": "string", "enum": ["current", "forecast", "life"]}
                        },
                        "required": ["location", "wtype"]
                    }
                }
            }
        ]

    def get_weather_info(self, location: str, wtype: str):
        fetchers = {
            "current": (self.weather.now, format_now),
            "forecast": (self.weather.daily, format_daily),
            "life": (self.weather.life, format_life),
        }
        fetcher, formatter = fetchers.get(wtype)
        return formatter(fetcher(location))

    def chat(self, user_message: str):
        self.conversation_history.append({"role": "user", "content": user_message})
        messages = [{"role": "system", "content": self.system_prompt}]
        messages.extend(self.conversation_history)

        # 第一次调用
        response = self.client.chat.completions.create(
            model=self.MODEL, messages=messages, tools=self.get_tools(), tool_choice="auto"
        )

        msg = response.choices[0].message

        if msg.tool_calls:
            tool_call = msg.tool_calls[0]
            func_args = json.loads(tool_call.function.arguments)
            result = self.get_weather_info(func_args["location"], func_args["wtype"])

            messages.append(msg)
            messages.append({"role": "tool", "tool_call_id": tool_call.id, "content": result})

            # 第二次调用
            final = self.client.chat.completions.create(model=self.MODEL, messages=messages)
            answer = final.choices[0].message.content
        else:
            answer = msg.content

        self.conversation_history.append({"role": "assistant", "content": answer})
        return answer
```


```python
# ==================== 测试 ====================
agent = WeatherAgent()
agent.chat("查询长沙未来三天的天气状况，哪一天适合外出运动")
```




    '根据长沙未来三天的天气预报：\n\n- **5月8日（周四）**：阴，15°C～23°C，体感较凉润，云量多、无阳光，适合轻度户外活动，但光照不足可能影响运动兴致；  \n- **5月9日（周五）**：多云，15°C～24°C，气温适中，云量减少，紫外线温和，风力较小，是**最适宜外出运动的一天**；  \n- **5月10日（周六）**：多云，18°C～26°C，白天气温略高，午后体感稍暖，但仍在舒适范围内，也适合运动（建议避开中午高温时段，优选清晨或傍晚）。\n\n✅ **综合推荐：5月9日（周五）最适合外出运动**——温度宜人、云量适中、昼夜温差适中（9℃），且无降水风险，利于耐力型或户外锻炼（如慢跑、骑行、球类等）。\n\n需要我为你规划一个晨练/傍晚运动小贴士（比如穿衣建议、补水提醒）吗？ 😊'



### 1.3.2 联网搜索
千问自带搜索功能，传递 enable_search: true 参数可启用联网搜索功能。

更多请参考：https://help.aliyun.com/zh/model-studio/web-search#312c12c262fsr 包括强制联网，标注来源，时效性，搜索范围等等


```python
api_key = os.getenv('DASHSCOPE_API_KEY')
# print(api_key)

client = OpenAI(
    api_key =  api_key,
    base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1",
)

reponse = client.chat.completions.create(
    model = 'qwen3.5-plus-2026-04-20',
    messages = [
        {'role':'user','content':'今天北京天气怎么样'}
    ],
    stream = False,
    extra_body={'enable_search':True}
)

print(reponse.choices[0].message.content)
```

    根据您提供的知识库信息（数据主要集中于2026年5月上旬），北京今天（以近期5月7日-8日预报为参考）的天气概况如下：
    
    🌤 **天气状况**：白天以晴为主，夜间晴间多云。
    🌡 **气温区间**：最高气温约 **24℃～27℃**，最低气温约 **10℃～14℃**，早晚温差明显。
    💨 **风力与预警**：偏北风3～4级，阵风6～7级，山区局地阵风可达8级以上。气象台已发布**大风蓝色预警**。风干物燥，外出请注意防风，谨防高空坠物，并注意用火用电安全。
    👕 **生活提示**：
    - 紫外线较强，建议涂抹防晒霜、佩戴墨镜或遮阳帽；
    - 花粉浓度目前处于中低水平（主要为松科、杨柳科等），过敏人群建议佩戴口罩；
    - 早晚体感偏凉，建议采用“洋葱式”穿衣，方便随时增减。
    
    ⚠️ **温馨提示**：知识库中的天气数据为特定时间点的预报快照。天气变化较快，如需获取您**确切查询日期**的实时天气，建议您直接打开“中国天气网”或搜索“气象北京”官方渠道查看最新实况与预警。如有具体出行日期或地点（如景区、郊区），告诉我可为您进一步匹配详细预报。
    

### 1.3.3网页抓取

### 1.3.4 代码解释器

### 1.3.5 知识库检索

### 1.3.6 MCP

# 2 推理与规划

## 2.1 ReAct 框架
ReAct = Reason（推理） + Act（行动）

参考[点击跳转到1.3.1 Function-Calling](#131-Function-Calling)

Reason 大模型推理(要不要调用工具、调用哪个、参数是什么) -> Act 行动(程序执行工具查询天气) -> 再次 Reason(把工具结果丢给大模型，整理成最终回答)

其中调用了两次LLM，
- 第一次：把用户问题 + 工具列表给模型，输出 tool_calls
- 第二次：把工具返回的天气结果塞回对话 → 模型基于真实数据，整理成自然语言回答

这是最简单的单轮 ReAct ，只会最多调用一次工具，走完两轮 LLM 就结束，适合查天气、查汇率等

完整 ReAct 是多轮while循环
- 思考要不要调用工具
- 调用工具
- 拿到结果
- 再思考还需不需要调用其他工具，再循环
- 直到模型判断「不用工具了，可以直接回答」才退出循环
- 加上最大循环次数，防止死循环

ReAct 模式的优势在于它的灵活性，能够根据每一步的执行结果动态调整后续行动。但这也意味着执行路径可能不稳定，适合需要探索的任务。


```python
import os
import json
import datetime
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

class ReActAgent:
    def __init__(self,model:str="qwen-plus",max_loops:int= 5):  # 设置多轮循环最大循环次数，防止死循环
        self.client = OpenAI(
            api_key=os.environ["DASHSCOPE_API_KEY"],
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        )
        self.model=model
        self.max_loops=max_loops
        self.conversation_history = [] # 对话记忆
        self.system_prompt = "你是一个能调用工具的智能助手。根据用户的问题判断是否需要调用工具来回答，需要工具就调用，不需要就直接回答。"

    # 工具定义
    def get_tools(self):
        return [
            {
                "type": "function",
                "function": {
                    "name": "get_local_time",
                    "description": "获取当前本机时间：小时、分钟、秒",
                    "parameters": {"type": "object", "properties": {}}
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "calculator",
                    "description": "数学计算器",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "expr": {"type": "string", "description": "数学表达式，例如 10 + 20"}
                        },
                        "required": ["expr"]
                    }
                }
            }
        ]

    # 工具实现
    def get_local_time(self):
        now = datetime.datetime.now()
        return f"当前时间：小时={now.hour}, 分钟={now.minute}, 秒={now.second}"

    def calculator(self, expr):
        try:
            return str(eval(expr, {"__builtins__": None}, {}))
        except:
            return "计算失败"

    # 工具调用分发
    def execute_tool(self, func_name, args):
        if func_name == "get_local_time":
            return self.get_local_time()
        elif func_name == "calculator":
            return self.calculator(args.get("expr"))
        return "未知工具"

    # ========== ReAct 核心：带循环的主逻辑 ==========
    def chat(self, user_query):
        self.conversation_history.append({"role": "user", "content": user_query})
        messages = [{"role": "system", "content": self.system_prompt}]
        messages.extend(self.conversation_history)

        loop_count = 0

        while loop_count < self.max_loops:
            loop_count += 1
            print(f"\n 第 {loop_count} 次推理循环")

            # 1. 让模型思考：是否需要调用工具
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                tools=self.get_tools(),
                tool_choice="auto"
            )

            ai_msg = response.choices[0].message

            # 如果没有工具调用 → 直接结束循环，返回答案
            if not ai_msg.tool_calls:
                final_answer = ai_msg.content
                break

            # 2. 模型要调用工具 → 执行
            print("模型决定调用工具...")
            for tool_call in ai_msg.tool_calls:
                func_name = tool_call.function.name
                func_args = json.loads(tool_call.function.arguments)

                # 本地执行
                tool_result = self.execute_tool(func_name, func_args)
                print(f"执行 {func_name}({func_args}) → {tool_result}")

                # 把结果加入对话
                messages.append(ai_msg)
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": tool_result
                })

        # 超过最大循环
        if loop_count >= self.max_loops:
            final_answer = "已达到最大循环次数，停止推理。"

        # 保存历史
        self.conversation_history.append({"role": "assistant", "content": final_answer})
        return final_answer
```


```python
agent = ReActAgent()
question = "将本机时间的小时和分钟相加得出结果"
print(agent.chat(question))
```

    
     第 1 次推理循环
    模型决定调用工具...
    执行 get_local_time({}) → 当前时间：小时=21, 分钟=37, 秒=45
    
     第 2 次推理循环
    模型决定调用工具...
    执行 calculator({'expr': '21 + 37'}) → 58
    
     第 3 次推理循环
    本机时间的小时和分钟相加的结果是 58。
    

## 2.2 CoT（Chain of Thought）
Zero-shot CoT 是一种无需示例即可激发逐步推理能力的方法。

通过在提示词中添加 "让我们一步一步地思考","展示思考过程" 这样的触发语句实现


```python
Zero_shot_CoTAgent = MemoryAgent() # 
answer = Zero_shot_CoTAgent.ask('问题：小明有 5 个苹果，小红给了他 3 个，小明吃掉了 2 个，还剩多少个？让我们一步一步地思考：')
print(answer)
```

    让我们一步一步地思考：
    
    1. **初始状态**：小明一开始有 5 个苹果。
    2. **增加数量**：小红给了他 3 个苹果，此时小明手上的苹果数变为：`5 + 3 = 8`（个）。
    3. **减少数量**：小明吃掉了 2 个苹果，剩下的苹果数为：`8 - 2 = 6`（个）。
    
    因此，最后小明还剩下 **6** 个苹果。
    

Few-shot CoT 通过提供包含详细推理过程的示例，帮助模型学习特定的推理模式。


```python
Few_shot_CoTAgent = MemoryAgent() # 
answer = Few_shot_CoTAgent.ask(
    '''示例 1：
    问题：小张有 10 元钱，买了 3 本书，每本 2 元，还剩多少？
    让我们一步一步地思考：
    - 小张原来有 10 元
    - 每本书 2 元，买了 3 本，花费 3 × 2 = 6 元
    - 10 - 6 = 4 元
    答案：还剩 4 元

    示例 2：
    问题：一只猫每小时抓 2 只老鼠，8 小时抓了多少只？
    让我们一步一步地思考：
    - 每小时抓 2 只老鼠
    - 8 小时抓了 8 × 2 = 16 只
    答案：抓了 16 只

    问题：小明有 5 个苹果，小红给了他 3 个，小明吃掉了 2 个，还剩多少个？
    让我们一步一步地思考：''')
print(answer)
```

    - 小明原来有 5 个苹果
    - 小红给了他 3 个，现在有 5 + 3 = 8 个
    - 吃掉了 2 个，还剩 8 - 2 = 6 个
    答案：还剩 6 个
    

## 2.3 ToT（Tree of Thoughts）
思维树是思维链的扩展，它不再局限于线性推理。

ToT 在每个推理节点探索多条可能的路径，形成树状结构。

这使得 Agent 能够进行多路径探索、回溯和全局评估。


```python
import os
import json
import re
from openai import OpenAI

# ------------------------------------------------------------------------------
# 1. 思维树节点：存储每一步思考
# ------------------------------------------------------------------------------
class ThoughtNode:
    def __init__(self, content: str, depth: int, parent=None):
        self.content = content   # 思考内容
        self.depth = depth       # 深度
        self.parent = parent     # 父节点
        self.score = 0.0         # 评估分数

    def __repr__(self):
        return f"[{self.depth}] {self.content[:40]}... (score={self.score:.1f})"

# ------------------------------------------------------------------------------
# 2. ToT LLM 包装器：生成下一步想法 & 评估
# ------------------------------------------------------------------------------
class ToTLLM:
    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv("DASHSCOPE_API_KEY"),
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
        )
        self.model = "qwen3.5-flash-2026-02-23"

    def generate_thoughts(self, state: str, n: int = 3) -> list[str]:
        """根据当前状态，生成 N 条下一步想法"""
        prompt = f"""
        你是思维树智能体，当前状态：
        {state}

        请生成 {n} 个可能的下一步推理步骤，每行一个，简洁明确。
        """
        resp = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        text = resp.choices[0].message.content.strip()
        return [line.strip() for line in text.splitlines() if line.strip()][:n]

    def evaluate(self, state: str) -> float:
        """给当前状态打分 0~10 分"""
        prompt = f"""
        评估以下推理状态是否接近正确答案，0~10 分：
        {state}
        只输出数字。
        """
        resp = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        text = resp.choices[0].message.content.strip()
        match = re.search(r"(\d+(\.\d+)?)", text)
        return float(match.group(1)) if match else 0.0

# ------------------------------------------------------------------------------
# 3. 评估器：给所有想法打分排序
# ------------------------------------------------------------------------------
class ToTEvaluator:
    def __init__(self, llm: ToTLLM):
        self.llm = llm

    def rank(self, nodes: list[ThoughtNode]) -> list[ThoughtNode]:
        for node in nodes:
            node.score = self.llm.evaluate(node.content)
        return sorted(nodes, key=lambda x: x.score, reverse=True)

# ------------------------------------------------------------------------------
# 4. Tree of Thoughts 主 Agent
# ------------------------------------------------------------------------------
class ToTAgent:
    def __init__(self, llm: ToTLLM, max_depth=4, beam_size=3):
        self.llm = llm
        self.evaluator = ToTEvaluator(llm)
        self.max_depth = max_depth
        self.beam_size = beam_size

    def is_solution(self, nodes: list[ThoughtNode]) -> bool:
        """判断是否已经得到答案（可根据任务改写）"""
        for node in nodes:
            if "答案" in node.content or "结果" in node.content or "=" in node.content:
                return True
        return False

    def backtrack_best(self, nodes: list[ThoughtNode]) -> list[str]:
        """回溯最优路径"""
        best = max(nodes, key=lambda x: x.score)
        path = []
        while best:
            path.append(best.content)
            best = best.parent
        return path[::-1]  # 反转得到从根到答案

    def solve(self, problem: str):
        print(f"【ToT 启动】问题：{problem}")
        root = ThoughtNode(problem, depth=0)
        frontier = [root]

        for depth in range(self.max_depth):
            print(f"\n======= 深度 {depth+1}/{self.max_depth} =======")
            all_candidates = []

            # 扩展每个前沿节点
            for node in frontier:
                thoughts = self.llm.generate_thoughts(node.content, n=self.beam_size)
                for t in thoughts:
                    all_candidates.append(ThoughtNode(t, depth+1, parent=node))

            # 评估 + 剪枝（只保留 beam_size 个最优）
            frontier = self.evaluator.rank(all_candidates)[:self.beam_size]

            print("当前最优候选：")
            for n in frontier:
                print(f"  {n}")

            # 终止判断
            if self.is_solution(frontier):
                print("\n 已找到答案！")
                break

        # 返回最优路径
        return self.backtrack_best(frontier)

# ------------------------------------------------------------------------------
# 测试：24 点游戏（ToT 经典任务）
# ------------------------------------------------------------------------------
llm = ToTLLM()
agent = ToTAgent(llm, max_depth=4, beam_size=3)

problem = "数字：4, 3, 8, 2。请用加减乘除算出24点，写出思考过程。"
best_path = agent.solve(problem)

print("\n==================== 最优思维路径 ====================")
for i, step in enumerate(best_path):
    print(f"{i+1}. {step}")
```

    【ToT 启动】问题：数字：4, 3, 8, 2。请用加减乘除算出24点，写出思考过程。
    
    ======= 深度 1/4 =======
    当前最优候选：
      [1] 3. 尝试分组计算，验证 (8-4) 与 (3×2) 的乘积是否等于 24。... (score=10.0)
      [1] 2. 尝试保持 4 不变，分析 8、3 和 2 是否能组合出 6。... (score=9.0)
      [1] 1. 尝试保持 3 和 8 相乘，分析 4 和 2 是否能抵消或变为 1。... (score=3.0)
    
    ======= 深度 2/4 =======
    当前最优候选：
      [2] 1. 验证 8 ÷ 4 ÷ 2 的结果是否为 1。... (score=10.0)
      [2] 3. 验证通过则记录解法并终止该分支搜索。... (score=8.0)
      [2] 计算 8 减 2 得 6，分析剩余数字 3 能否参与运算且结果仍为 6。... (score=8.0)
    
    ✅ 已找到答案！
    
    ==================== 最优思维路径 ====================
    1. 数字：4, 3, 8, 2。请用加减乘除算出24点，写出思考过程。
    2. 1. 尝试保持 3 和 8 相乘，分析 4 和 2 是否能抵消或变为 1。
    3. 1. 验证 8 ÷ 4 ÷ 2 的结果是否为 1。
    

## 2.4 任务规划与 MCTS
蒙特卡洛树搜索（Monte Carlo Tree Search, MCTS）是一种用于复杂决策问题的启发式搜索算法。

MCTS 通过模拟随机来评估每个决策节点的潜在价值。它不需要评估所有可能的路径，而是通过抽样和统计来指导搜索方向。

- 第一步，选择：从根节点开始，递归选择最优子节点直到达到叶节点。选择时使用 UCB（Upper Confidence Bound）公式平衡探索与利用。

- 第二步，扩展：在叶节点添加一个或多个子节点。

- 第三步，模拟：从新节点开始，随机模拟游戏直到结束。

- 第四步，反向传播：更新模拟路径上所有节点的统计信息。

MCTS 的计算成本较高，适合需要深度规划但有明确终止条件的场景。对于实时性要求高的任务，可能需要限制模拟次数或使用其他方法。

## 2.5 Reflexion（自我反思）
适合
- 需要持续改进的任务，如对话系统、代码生成等。
- 错误代价高但重试成本低的场景。
- 需要从失败中学习的情况。


```python
from openai import OpenAI
import os

class LLM:
    def __init__(self,model:str='qwen3.5-flash-2026-02-23'):
        self.client = OpenAI(
            api_key = os.getenv('DASHSCOPE_API_KEY'),
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
        )
        self.model = model

    def chat(self,prompt):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {'role':'user','content':prompt}
            ],
            max_tokens=500
        )
        return response.choices[0].message.content.strip()

class ReflexionAgent:
    def __init__(self,max_try):
        self.llm = LLM()
        self.max_try = max_try
        
    def run(self,task):
        history = ""
        for i in range(self.max_try):
            print(f"====第{i+1}次尝试===")

            # 回答
            answer = self.llm.chat(prompt=f"问题：{task}\n经验与反思：{history}，直接回答答案")
            print(f"回答:{answer}\n")

            # 判断是否正确
            check = self.llm.chat(prompt=f"问题：{task}\n回答：{answer}\n回答是否正确，直接回复是或否")
            if '是' in check:
                return f"回答正确，回答如下：\n{answer}"
            
            # 反思
            print("回答错误，开始反思")
            reflect = self.llm.chat(f"问题：{task}\n错误回答{answer}，简短反思错误原因，该怎么做")
            print(f"反思{reflect}")
            history += f"\n反思{reflect}"

        return "超过最大次数"

agent = ReflexionAgent(max_try=2)
task = "3个人3天用3桶水，9个人9天用几桶水？"
final = agent.run(task)
print("最终结果： \n",final)         
```

    ====第1次尝试===
    回答:27 桶
    
    最终结果： 
     回答正确，回答如下：
    27 桶
    

## 2.6 任务分解
复杂任务通常需要分解为可管理的子任务。

### 2.6.1 递归任务分解
将任务递归地分解为更小的子任务，直到子任务可以直接执行。


```python

```

### 2.6.2 平行任务分解
识别可以并行执行的独立子任务，提高执行效率。

是加速任务执行的关键策略。


```python
import os
import asyncio
from openai import OpenAI

# 封装 LLM 同步+异步调用
class LLM:
    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv("DASHSCOPE_API_KEY"),
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
        )
        self.model = "qwen3.5-flash-2026-02-23"

    def chat(self, prompt: str) -> str:
        resp = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )
        return resp.choices[0].message.content.strip()

    async def achat(self, prompt: str) -> str:
        # 异步包装，适合并行
        return self.chat(prompt)

# 任务分解 + 并行执行智能体
class ParallelTaskAgent:
    def __init__(self):
        self.llm = LLM()

    # 1. 拆解任务
    def decompose(self, task: str) -> list[str]:
        prompt = f"""
        把下面复杂任务拆成若干个独立、可以**并行执行**的子任务，
        每条一行，只列子任务，不要多余解释：
        {task}
        """
        lines = self.llm.chat(prompt).splitlines()
        return [t.strip() for t in lines if t.strip()]

    # 2. 单个子任务异步执行
    async def run_subtask(self, idx: int, subtask: str) -> tuple[int, str, str]:
        res = await self.llm.achat(f"完成子任务：{subtask},回答简短精要")
        return idx, subtask, res

    # 3. 并行执行所有子任务
    async def run_parallel(self, subtasks: list[str]):
        tasks = []
        for i, st in enumerate(subtasks):
            tasks.append(self.run_subtask(i, st))
        # 并行等待全部完成
        results = await asyncio.gather(*tasks)
        # 按原顺序排序
        return sorted(results, key=lambda x: x[0])

    # 4. 汇总所有子任务结果
    def summary(self, main_task: str, results) -> str:
        content = ""
        for idx, st, res in results:
            content += f"子任务{idx+1}：{st}\n结果：{res}\n\n"

        prompt = f"""
        总任务：{main_task}
        下面是各并行子任务的结果：
        {content}
        请整合所有内容，输出一份完整、流畅的最终答案。
        """
        return self.llm.chat(prompt)

    # 入口
    async def run(self, main_task: str):
        print(f"总任务：{main_task}\n")

        # 拆解
        subtasks = self.decompose(main_task)
        print("拆解为并行子任务：")
        for i, t in enumerate(subtasks, 1):
            print(f"  {i}. {t}")

        # 并行执行
        print("\n开始并行执行所有子任务...")
        results = await self.run_parallel(subtasks)

        # 打印各子任务结果
        print("\n各子任务完成结果：")
        for idx, st, res in results:
            print(f"--- 子任务{idx+1} ---")
            print(f"{res}\n")

        # 汇总
        final = self.summary(main_task, results)
        print("最终汇总结果：\n", final)
        return final
```


```python
# ---------------- 测试 ----------------
agent = ParallelTaskAgent()
# asyncio.run(agent.run("分别介绍杭州的景点、特色美食、历史文化、气候特点"))
await agent.run("分别介绍杭州的景点、特色美食、历史文化、气候特点")
```

    总任务：分别介绍杭州的景点、特色美食、历史文化、气候特点
    
    拆解为并行子任务：
      1. 搜索并整理杭州主要景点信息
      2. 搜索并整理杭州特色美食信息
      3. 搜索并整理杭州历史文化信息
      4. 搜索并整理杭州气候特点信息
    
    开始并行执行所有子任务...
    
    各子任务完成结果：
    --- 子任务1 ---
    **杭州主要景点概览**
    
    *   **西湖景区**：城市名片，世界遗产。打卡三潭印月、苏堤春晓、雷峰塔，建议游船或骑行环湖。
    *   **灵隐寺**：千年古刹，位于飞来峰下。香火鼎盛，建筑与石刻艺术精湛。
    *   **西溪湿地**： “城市绿肺”。推荐乘坐摇橹船深入腹地，体验野趣与民俗。
    *   **宋城**：人造主题公园。主打宋代文化，必看《宋城千古情》大型演出。
    *   **河坊街/南宋御街**：历史商业街。聚集传统小吃、老字号及特色伴手礼。
    *   **龙井问茶**：包括龙井村、梅家坞。品明前龙井，赏茶园梯田风光。
    
    --- 子任务2 ---
    **杭州特色美食概览**
    
    🍽️ **经典名菜**
    *   **东坡肉**：肥而不腻，酱香浓郁。
    *   **西湖醋鱼**：酸甜鲜嫩，蟹粉风味。
    *   **龙井虾仁**：茶香清雅，虾仁爽滑。
    *   **叫花鸡**：荷叶包裹，泥烤醇香。
    
    🥢 **地道小吃**
    *   **片儿川**：雪菜笋片浇头的牛肉/猪肉面。
    *   **葱包桧**：春卷皮裹油条，葱段压扁油炸。
    *   **定胜糕**：松软微甜，寓意吉祥。
    *   **猫耳朵**：面块状似猫耳，汤鲜味美。
    
    💡 **口味特点**
    隶属浙菜系，讲究“鲜嫩”，调味清淡略带甜味，重在突出食材本味。
    
    🏪 **推荐去处**
    *   **老字号**：楼外楼、知味观、山外山。
    *   **街区**：河坊街、南山路、武林路。
    
    --- 子任务3 ---
    **杭州历史文化精要**
    
    *   **历史地位**：吴越国都、南宋行在，素有“人间天堂”之美誉，七朝古都。
    *   **世界遗产**：坐拥**良渚古城遗址**（中华文明起源实证）、**西湖文化景观**（中国首个文化类双遗产）、**京杭大运河**（杭州段）。
    *   **文化符号**：**宋韵文化**（雅致美学）、**茶文化**（西湖龙井）、**丝绸文化**（中国丝绸之都）。
    *   **人文印记**：白居易、苏东坡治理水利；岳飞、于谦忠烈精神；历代文人墨客题咏不绝。
    *   **现代定位**：数字经济第一城，国际风景旅游城市，古今交融的现代化大都市。
    
    --- 子任务4 ---
    **杭州气候特点：**
    
    *   **气候类型**：北亚热带季风气候。
    *   **气温特征**：四季分明，冬暖夏热，春秋季短；年均气温约 17℃。
    *   **降水特征**：雨量充沛，年降水量约 1400 毫米；春季多雨，6-7 月进入“梅雨”期，夏秋偶受台风影响。
    *   **体感总结**：空气湿润，夏季湿热，冬季阴冷潮湿。
    
    最终汇总结果：
     # 杭州全景指南：千年古都与现代都市的交响
    
    杭州，一座被公认为“人间天堂”的城市，既是拥有七朝古都历史的文明宝库，也是数字经济蓬勃发展的现代之都。它完美融合了自然山水之美、深厚人文底蕴与独特生活韵味。以下将从历史文化、旅游景点、特色美食及气候特点四个维度，为您全面解读杭州。
    
    ---
    
    ### 一、深厚的历史文化底蕴
    
    杭州的历史地位显赫，曾是吴越国都、南宋行在，素有“人间天堂”的美誉。这里不仅是**中国首个文化类世界双遗产**地（西湖文化景观），更坐拥**良渚古城遗址**（中华文明起源实证）与**京杭大运河**（杭州段）。
    
    在文化符号上，杭州以**宋韵文化**著称，展现出独特的雅致美学；作为**中国丝绸之都**与**西湖龙井茶乡**，其丝绸与茶文化闻名遐迩。历史上，白居易、苏东坡等治理水利，留下了苏堤等千古佳话；岳飞、于谦的忠烈精神在此传承；历代文人墨客的题咏不绝。如今，杭州已转型为数字经济第一城，是一座古今交融的国际化大都市。
    
    ### 二、绝美的旅游景点概览
    
    杭州的景点遍布全城，既有自然人文景观，也有现代休闲体验：
    
    *   **西湖景区**：杭州的城市名片与世界遗产核心。必打卡点包括三潭印月、苏堤春晓和雷峰塔。建议乘坐游船或骑行环湖，深入体验“淡妆浓抹总相宜”的美景。
    *   **灵隐寺**：位于飞来峰下的千年古刹，香火鼎盛。其建筑与石刻艺术精湛，是感受佛教文化与山水结合的上佳之地。
    *   **西溪湿地**：被誉为“城市绿肺”。推荐乘坐摇橹船深入腹地，体验野趣十足的自然风光与江南民俗。
    *   **宋城**：一个主打宋代文化的人造主题公园，大型演出《宋城千古情》必看，适合快速沉浸式体验宋朝风情。
    *   **河坊街/南宋御街**：历史悠久的商业街，聚集了传统小吃、老字号商铺及特色伴手礼，是感受市井烟火气的好去处。
    *   **龙井问茶**：包含龙井村、梅家坞等地，可品明前龙井好茶，赏层层叠叠的茶园梯田风光。
    
    ### 三、地道的舌尖风味
    
    杭州菜隶属浙菜系，口味讲究“鲜嫩”，调味清淡略带甜味，重在突出食材本味。
    
    🍽️ **经典名菜**
    *   **东坡肉**：肥而不腻，酱香浓郁，承载着苏东坡的美食传说。
    *   **西湖醋鱼**：酸甜鲜嫩，带有独特的蟹粉风味。
    *   **龙井虾仁**：茶香清雅，虾仁爽滑，是茶菜结合的典范。
    *   **叫花鸡**：荷叶包裹，泥烤而成的鸡肉醇香可口。
    
    🥢 **地道小吃**
    *   **片儿川**：雪菜笋片浇头的牛肉/猪肉面，鲜味十足。
    *   **葱包桧**：春卷皮裹油条，夹葱段压扁油炸，酥脆香辣。
    *   **定胜糕**：松软微甜，寓意吉祥，常作为伴手礼。
    *   **猫耳朵**：面块状似猫耳，汤鲜味美，造型独特。
    
    🏪 **推荐去处**
    想吃正宗杭州味，首选老字号如**楼外楼、知味观、山外山**，或者漫步**河坊街、南山路、武林路**等街区寻觅小店。
    
    ### 四、宜人的气候与环境特点
    
    了解杭州的气候有助于规划最佳旅行时间：
    
    *   **气候类型**：属于北亚热带季风气候。
    *   **四季特征**：四季分明，但春秋两季较短。年均气温约 17℃，冬暖夏热。
    *   **降水情况**：雨量充沛，年降水量约 1400 毫米。**春季多雨**，6-7 月进入“梅雨”期，夏秋季节偶受台风影响。
    *   **体感总结**：空气整体湿润，夏季湿热，冬季阴冷潮湿。
    
    ---
    
    ### 结语
    
    杭州是一座值得细细品味的城市。若想欣赏最美春色，建议选择清明至谷雨期间，此时柳浪闻莺，烟雨朦胧；若偏爱清秋，则十月的桂花与凉风最为宜人。无论您是追寻历史足迹、探寻山水美景，还是品味地道美食，杭州都能以其独特的魅力，带给您难忘的旅程。
    




    '# 杭州全景指南：千年古都与现代都市的交响\n\n杭州，一座被公认为“人间天堂”的城市，既是拥有七朝古都历史的文明宝库，也是数字经济蓬勃发展的现代之都。它完美融合了自然山水之美、深厚人文底蕴与独特生活韵味。以下将从历史文化、旅游景点、特色美食及气候特点四个维度，为您全面解读杭州。\n\n---\n\n### 一、深厚的历史文化底蕴\n\n杭州的历史地位显赫，曾是吴越国都、南宋行在，素有“人间天堂”的美誉。这里不仅是**中国首个文化类世界双遗产**地（西湖文化景观），更坐拥**良渚古城遗址**（中华文明起源实证）与**京杭大运河**（杭州段）。\n\n在文化符号上，杭州以**宋韵文化**著称，展现出独特的雅致美学；作为**中国丝绸之都**与**西湖龙井茶乡**，其丝绸与茶文化闻名遐迩。历史上，白居易、苏东坡等治理水利，留下了苏堤等千古佳话；岳飞、于谦的忠烈精神在此传承；历代文人墨客的题咏不绝。如今，杭州已转型为数字经济第一城，是一座古今交融的国际化大都市。\n\n### 二、绝美的旅游景点概览\n\n杭州的景点遍布全城，既有自然人文景观，也有现代休闲体验：\n\n*   **西湖景区**：杭州的城市名片与世界遗产核心。必打卡点包括三潭印月、苏堤春晓和雷峰塔。建议乘坐游船或骑行环湖，深入体验“淡妆浓抹总相宜”的美景。\n*   **灵隐寺**：位于飞来峰下的千年古刹，香火鼎盛。其建筑与石刻艺术精湛，是感受佛教文化与山水结合的上佳之地。\n*   **西溪湿地**：被誉为“城市绿肺”。推荐乘坐摇橹船深入腹地，体验野趣十足的自然风光与江南民俗。\n*   **宋城**：一个主打宋代文化的人造主题公园，大型演出《宋城千古情》必看，适合快速沉浸式体验宋朝风情。\n*   **河坊街/南宋御街**：历史悠久的商业街，聚集了传统小吃、老字号商铺及特色伴手礼，是感受市井烟火气的好去处。\n*   **龙井问茶**：包含龙井村、梅家坞等地，可品明前龙井好茶，赏层层叠叠的茶园梯田风光。\n\n### 三、地道的舌尖风味\n\n杭州菜隶属浙菜系，口味讲究“鲜嫩”，调味清淡略带甜味，重在突出食材本味。\n\n🍽️ **经典名菜**\n*   **东坡肉**：肥而不腻，酱香浓郁，承载着苏东坡的美食传说。\n*   **西湖醋鱼**：酸甜鲜嫩，带有独特的蟹粉风味。\n*   **龙井虾仁**：茶香清雅，虾仁爽滑，是茶菜结合的典范。\n*   **叫花鸡**：荷叶包裹，泥烤而成的鸡肉醇香可口。\n\n🥢 **地道小吃**\n*   **片儿川**：雪菜笋片浇头的牛肉/猪肉面，鲜味十足。\n*   **葱包桧**：春卷皮裹油条，夹葱段压扁油炸，酥脆香辣。\n*   **定胜糕**：松软微甜，寓意吉祥，常作为伴手礼。\n*   **猫耳朵**：面块状似猫耳，汤鲜味美，造型独特。\n\n🏪 **推荐去处**\n想吃正宗杭州味，首选老字号如**楼外楼、知味观、山外山**，或者漫步**河坊街、南山路、武林路**等街区寻觅小店。\n\n### 四、宜人的气候与环境特点\n\n了解杭州的气候有助于规划最佳旅行时间：\n\n*   **气候类型**：属于北亚热带季风气候。\n*   **四季特征**：四季分明，但春秋两季较短。年均气温约 17℃，冬暖夏热。\n*   **降水情况**：雨量充沛，年降水量约 1400 毫米。**春季多雨**，6-7 月进入“梅雨”期，夏秋季节偶受台风影响。\n*   **体感总结**：空气整体湿润，夏季湿热，冬季阴冷潮湿。\n\n---\n\n### 结语\n\n杭州是一座值得细细品味的城市。若想欣赏最美春色，建议选择清明至谷雨期间，此时柳浪闻莺，烟雨朦胧；若偏爱清秋，则十月的桂花与凉风最为宜人。无论您是追寻历史足迹、探寻山水美景，还是品味地道美食，杭州都能以其独特的魅力，带给您难忘的旅程。'



### 2.6.3 层次任务分解
将任务分为不同抽象层次，高层任务调用低层任务，形成任务层次树。

适合需要多层抽象的复杂系统。

## 2.7 Plan-and-Execute
将规划与执行分离的架构模式。

Agent 首先完整地规划整个任务流程，然后按计划执行。

ReAct 是边推理边执行，更灵活但路径可能不稳定。Plan-and-Execute 是先规划后执行，更稳定但缺乏动态调整能力。


```python
import os
from openai import OpenAI

class Plan_Execute_Agent:
    def __init__(self,model:str="qwen3.5-flash-2026-02-23"):
        self.client = OpenAI(
            api_key=os.getenv("DASHSCOPE_API_KEY"),
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
        )
        self.model = model

    def ask(self,prompt):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {'role':'user','content':prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    
    def run(self,task):
        # 制定计划
        plan = self.ask(f'''
        请为以下复杂任务制定一份简短明了的分步执行计划：
        任务：{task}

        要求：
        1. 拆成有序的步骤列表
        2. 每一步只做一件事
        3. 按顺序编号，不要多余解释''')
        print(f'Plan如下：\n{plan}\n')
        steps = [s.strip() for s in plan.splitlines() if s.strip()]

        # 分步执行
        result = []
        for step in steps:
            step_result = self.ask(f'''
            总任务背景：{plan}
            请完成当前这一个步骤，直接给出简要结果：
            步骤：{step}
            ''')
            print(f'当前步骤完成如下：{step_result}\n')
            result.append(step_result)

        # 汇总
        final = self.ask(f"""
        总任务：{task}
        已按计划完成所有步骤，步骤及结果如下：
        {result}

        请整合所有步骤结果，输出一份简短明了的最终答案。
        """)
        return final
```


```python
agent = Plan_Execute_Agent()
print(agent.run("写一份南京两日旅游攻略，包含每日行程、必吃美食、住宿推荐"))
```

    Plan如下：1. 搜集南京各景点的开放时间与门票信息
    2. 筛选并安排第一天景点的游览顺序
    3. 筛选并安排第二天景点的游览顺序
    4. 汇总南京地道特色美食及推荐店铺
    5. 对比并推荐适合的住宿区域或酒店
    6. 将行程与食宿信息整合生成攻略文稿
    7. 复核内容并优化排版格式输出
    
    当前步骤完成如下：### 步骤 1 结果：南京主要景点开放时间与门票信息汇总
    
    | 景点名称 | 开放时间 | 门票价格 | 备注/预约要求 |
    | :--- | :--- | :--- | :--- |
    | **侵华日军南京大屠杀遇难同胞纪念馆** | 周二至周日 9:00-16:30<br>(16:00 停止入馆) | **免费** | 需微信公众号提前 7 天预约；**周一闭馆** |
    | **中山陵景区** | 8:30-17:00<br>(2月除外另有规定) | 陵寝 **免费**<br>音乐台 20 元 | 需“钟山风景区”小程序预约；**周一闭馆** |
    | **明孝陵景区** | 6:30-18:00<br>(旺季延长至 18:30) | **70 元** | 含梅花山、石象路；与中山陵联票更优 |
    | **南京博物院** | 9:00-17:00<br>(16:00 停止入馆) | **免费** | **极难预约**，需提前 7 天在官微抢票；**周一闭馆** |
    | **总统府** | 8:30-18:00<br>(17:00 停止入园) | **35 元** | 建议下午游览，避免上午人流高峰 |
    | **夫子庙秦淮风光带** | 全天开放 (建筑 8:30-17:00) | 街区 **免费**<br>大成殿 15 元 | 夜游秦淮河画舫约 120 元/人 |
    | **鸡鸣寺** | 08:00-17:30 | **10 元** (赠香) | 适合傍晚去，可看日落和夜景 |
    | **中华门城堡** | 08:00-17:00 | **30 元** | 保存最完整的古代瓮城，适合历史爱好者 |
    | **玄武湖公园** | 06:00-22:00 | **免费** | 进出无需检票，内部游船单独收费 |
    | **牛首山文化旅游区** | 09:00-17:30 | **160 元** | 较远，设施新，拍照出片，需预留半天 |
    | **美龄宫** | 8:30-17:30 | **30 元** | 位于中山陵景区内，可一并游玩 |
    
    **重要提示：**
    1. 以上时间均为常规运营时间，法定节假日或特殊天气可能调整，出发前务必关注官方公众号。
    2. 博物馆及热门景点均需实名预约，建议至少提前 3-5 天规划。
    
    当前步骤完成如下：**步骤 2 结果：第一天景点筛选与游览顺序安排**
    
    **【主题】**：民国风云与古城夜韵（市中心历史核心区）
    **【路线逻辑】**：由东向西，由昼至夜，顺路且劳逸结合。
    
    | 时间段 | 景点名称 | 活动重点 | 备注/提示 |
    | :--- | :--- | :--- | :--- |
    | **09:00 - 12:00** | **南京总统府** | 参观太平天国天王府及国民政府旧址 | ⚠️**需提前预约**，门票较紧俏；建议开馆即入。 |
    | **12:00 - 13:30** | **午餐 & 转场** | 品尝附近新街/常府街风味小吃 | 距下一景点约 6km，建议打车前往。 |
    | **14:30 - 16:30** | **中华门瓮城 & 明城墙** | 登城俯瞰市区，感受防御工程 | 位于城南，紧邻夫子庙，体力消耗适中。 |
    | **18:30 - 21:00** | **夫子庙 & 秦淮河** | 晚餐（鸭血粉丝汤等）、游船或漫步灯景 | 🌙核心亮点：**夜游秦淮**，避开白天人流高峰。 |
    
    **【筛选理由】**：
    1.  **地理位置连贯**：三条线路沿南北轴线分布，减少往返折返时间。
    2.  **体验层次丰富**：涵盖室内博物馆（总统府）、户外徒步（城墙）、休闲景观（秦淮），避免单一疲劳。
    3.  **时间管理合理**：上午精力充沛看展馆，下午适应步行，晚上享受夜景。
    
    **【特别提醒】**：南京各热门景点周一多闭馆，若行程遇周一请将“总统府”调整为“南京博物院”（需极早抢票）或“美龄宫”。
    
    当前步骤完成如下：### 步骤 3：筛选并安排第二天景点的游览顺序
    
    **推荐主题：民国风情与古都夜色**
    
    1.  **上午 (09:00 - 12:00)：南京总统府**
        *   *理由*：核心近代历史建筑群，需预留充足时间深度参观，建议尽早入园避开人流高峰。
    2.  **中午 (12:00 - 13:30)：午餐休憩**
        *   *安排*：在总统府周边品尝当地面点，随后打车前往老门东区域（约 15 分钟车程）。
    3.  **下午 (14:00 - 17:00)：老门东历史文化街区**
        *   *理由*：保留明代格局的老城南片区，适合悠闲漫步，打卡特色小吃与传统手作。
    4.  **晚上 (17:30 - 20:30)：夫子庙步行街 & 秦淮河夜游**
        *   *理由*：紧邻老门东，晚间乘画舫夜游秦淮河是南京精华体验，灯火璀璨，适合行程收尾。
    
    **路线逻辑**：由市中心严肃的历史场馆过渡至南城的民俗生活气息，最后以秦淮河畔的夜景结束全天，地理位置顺路，交通成本最低。
    
    当前步骤完成如下：### 步骤 4：汇总南京地道特色美食及推荐店铺
    
    #### 🥢 四大经典必吃
    1. **盐水鸭/金陵烤鸭**
       - *特点*：皮白肉嫩，咸香适口。
       - *推荐*：**韩复兴**、**章云板鸭**、**项记全家福**（切配现吃）。
    2. **鸭血粉丝汤**
       - *特点*：酸辣鲜香，配料丰富。
       - *推荐*：**小潘记**、**鸭得堡**、**小郑家**。
    3. **牛肉锅贴**
       - *特点*：底脆肉嫩，汁水丰盈。
       - *推荐*：**李记清真馆**（水西门老店）、**安乐园**、**奇芳阁**。
    4. **皮肚面**
       - *特点*：面条劲道，浇头大碗豪爽。
       - *推荐*：**易记干挑面**、**七仙居**、**同来轩**。
    
    #### 🍰 特色风味小吃
    - **点心类**：鸡鸣汤包（**鸡鸣汤包店**）、梅花糕（**陆氏梅花糕**）、糖芋苗（**莲湖甜食店**）。
    - **素食类**：素什锦、开洋干拌面（**尹氏鸡汁汤包**）。
    
    #### 🗺️ 美食地图推荐
    - **科巷**：本地居民食堂，早餐与平价小吃极多，性价比高。
    - **老门东**：历史街区，环境好，汇聚正宗老字号及网红打卡店。
    - **夫子庙/秦淮河**：游客首选，夜宵氛围浓，但建议慎选景区核心区大排档。
    
    当前步骤完成如下：**步骤 5. 住宿区域对比与推荐**
    
    ### 📍 核心住宿区域对比
    
    | 区域 | 优势 | 劣势 | 推荐指数 |
    | :--- | :--- | :--- | :--- |
    | **新街口商圈** | 地铁枢纽（1/2 号线），交通最便，吃喝玩乐集中，通勤效率高 | 物价较高，人流密集 | ⭐⭐⭐⭐⭐ |
    | **夫子庙/老门东** | 紧邻秦淮河，夜景绝美，文化氛围浓郁，部分酒店带景观房 | 节假日拥堵严重，夜间嘈杂，旺季房价高 | ⭐⭐⭐⭐ |
    | **大行宫/鸡鸣寺** | 靠近总统府/博馆，环境清幽，文艺气息，性价比高 | 餐饮娱乐不如新街口丰富 | ⭐⭐⭐⭐ |
    
    ### 🏨 酒店具体推荐
    
    1.  **高性价比首选**
        *   **全季酒店 / 亚朵酒店（新街口地铁站店）**：服务标准化，隔音较好，位置居中。
    2.  **体验式住宿**
        *   **颐和公馆（颐和路片区）**：别墅风格建筑，民国风情，适合预算充足的游客。
        *   **夫子庙精品民宿**：入住老建筑改造的客栈，感受江南水乡风情（需注意甄别卫生状况）。
    3.  **高端舒适型**
        *   **南京威斯汀大酒店**：位于珠江路，交通便利，设施完善。
        *   **金鹰国际酒店**：新街口地标，俯瞰城市夜景。
    
    ### 💡 选住建议
    *   **第一天+第二天均在此地**：建议锁定**新街口地铁站 1000 米范围内**，减少路途奔波。
    *   **看重夜景**：可安排第一晚住夫子庙，次日换至新街口退房继续游玩。
    
    当前步骤完成如下：# 南京两日深度游全攻略
    
    ## 一、住宿推荐
    - **首选区域：新街口**
      - **理由**：地铁枢纽（1/2号线），交通极便利，商场餐饮丰富。
      - **推荐类型**：亚朵酒店、全季酒店或如家商旅（性价比高）。
    - **备选区域：夫子庙/三山街**
      - **理由**：夜景观赏方便，靠近秦淮河夜景，但周末可能较喧闹。
      - **推荐类型**：南京颐和公馆（高端）、金陵客栈（特色民宿）。
    
    ---
    
    ## 二、行程安排
    
    ### 📅 第一天：历史与近代风云
    - **09:00 | 中山陵**
      - **门票**：免费（需提前预约）。
      - **提示**：建议早去避开人流，乘坐观光车上山。
    - **11:00 | 音乐台 & 美龄宫**
      - **门票**：音乐台 10 元；美龄宫 30 元。
      - **亮点**：喂鸽群、拍摄“项链”航拍视角。
    - **14:30 | 总统府**
      - **门票**：35 元（必约）。
      - **耗时**：约 2-3 小时，民国建筑核心代表。
    - **18:30 | 夫子庙 & 老门东**
      - **活动**：逛明清建筑群，体验秦淮灯会氛围（若夜晚开放）。
      - **晚餐**：老门东内解决。
    
    ### 📅 第二天：古都风韵与现代活力
    - **09:00 | 南京博物院**
      - **门票**：免费（需提前 7 天小程序预约）。
      - **重点**：历史馆、民国馆（拍照出片）。
    - **13:00 | 玄武湖公园**
      - **门票**：5 元/人。
      - **路线**：从解放门进入，环湖散步，远眺紫峰大厦与明城墙。
    - **16:30 | 鸡鸣寺**
      - **门票**：10 元。
      - **亮点**：求签祈福，登上药师佛塔俯瞰南京城。
    - **19:00 | 科巷夜市**
      - **活动**：结束行程前的最后觅食。
    
    ---
    
    ## 三、地道美食推荐
    | 品类 | 推荐店铺 | 必点菜品 |
    | :--- | :--- | :--- |
    | **鸭血粉丝汤** | 叶新小吃（科巷店） | 鸭血粉丝汤、牛肉锅贴 |
    | **盐水鸭** | 章云板鸭 | 片皮盐水鸭 |
    | **小笼包** | 鸡鸣汤包 | 赤豆元宵、蟹黄汤包 |
    | **面食** | 狮王府（狮子桥） | 皮肚面、如意三宝 |
    | **小吃街** | 科巷/夫子庙 | 梅花糕、赤豆酒酿圆子 |
    
    ---
    
    ## 四、重要贴士
    1. **预约提醒**：南京博物院、中山陵、总统府均需实名预约，旺季务必提前抢票。
    2. **交通**：主要景点间地铁可直达，避开早晚高峰打车更优。
    3. **防坑**：夫子庙景区内餐饮选择慎选“游客专供”，推荐去周边居民区就餐。
    4. **气候**：南京夏季炎热，冬季湿冷，春秋最佳；随身备伞以防阵雨。
    
    当前步骤完成如下：# 🇨🇳 南京两日深度游攻略（最终定稿）
    
    ## 📅 行程总览
    *   **路线设计逻辑**：第一天聚焦市中心人文与秦淮风情；第二天深入紫金山历史遗址。
    *   **适用人群**：文化爱好者、家庭出游、自由行游客。
    *   **预算预估**：人均 800-1500 元（含食宿）。
    
    ---
    
    ## 🚩 第一日：民国记忆 & 秦淮灯火
    | 时间段 | 景点/活动 | 开放时间 | 门票参考 | 备注 |
    | :--- | :--- | :--- | :--- | :--- |
    | **09:00-11:30** | **总统府** | 周二至周日 08:30-18:00 | 35 元 | 周一闭馆，需提前预约 |
    | **12:00-13:30** | **午餐·新街口** | - | - | 推荐“李记清真馆”牛杂汤 |
    | **14:00-16:00** | **江宁织造博物馆** | 周二至周日 09:00-17:00 | 免费 | 需预约，红楼梦主题 |
    | **16:30-18:30** | **夫子庙景区** | 全天开放 | 免费 | 核心街区逛古建 |
    | **19:00-20:30** | **秦淮河夜游船** | 18:30-21:30 | 约 100 元 | 必体验夜景 |
    | **21:00** | **返程住宿** | - | - | 夫子庙周边或新街口 |
    
    ## 🚩 第二日：钟山风雨 & 古都怀古
    | 时间段 | 景点/活动 | 开放时间 | 门票参考 | 备注 |
    | :--- | :--- | :--- | :--- | :--- |
    | **08:30-11:00** | **中山陵** | 周二至周日 08:30-17:00 | 免费 | 周一闭馆，需预约登阶 |
    | **11:30-12:30** | **美龄宫** | 周二至周日 08:30-17:30 | 30 元 | 最美项链景观 |
    | **13:00-14:30** | **午餐·明孝陵周边** | - | - | 尝试金陵菜馆 |
    | **15:00-17:00** | **明孝陵/石象路** | 周二至周日 06:30-18:30 | 70 元 | 秋景最佳，漫步神道 |
    | **17:30-18:30** | **鸡鸣寺** | 全天开放 | 10 元 | 祈福求姻缘，看日落 |
    | **19:00** | **晚餐·玄武门** | - | - | 附近湘云小馆等 |
    
    ---
    
    ## 🍜 地道美食及店铺推荐
    | 类别 | 推荐菜品 | 推荐店铺 | 区域 |
    | :--- | :--- | :--- | :--- |
    | **早餐** | 皮肚面、牛肉锅贴 | 鸭血粉丝汤老店、莲湖糕团 | 评事街 |
    | **正餐** | 盐水鸭、红烧狮子头 | 南京大牌档、江南灶 | 新街口/科巷 |
    | **小吃** | 梅花糕、赤豆元宵 | 芳婆糕点、什锦豆腐涝 | 夫子庙 |
    | **饮品** | 状元豆、雨花茶 | 随遇而安茶馆 | 颐和路 |
    
    > **注意**：节假日期间热门餐厅建议提前排队或预订。
    
    ---
    
    ## 🏨 住宿区域建议
    | 区域 | 推荐理由 | 适合人群 | 参考价位 |
    | :--- | :--- | :--- | :--- |
    | **新街口** | 地铁枢纽，购物方便，美食集中 | 第一次来，追求交通便利 | 300-600 元 |
    | **夫子庙** | 风景绝佳，夜生活丰富 | 喜欢热闹，想体验秦淮夜景 | 400-800 元 |
    | **玄武湖/珠江路** | 环境清幽，近图书馆 | 文艺青年，喜安静 | 300-500 元 |
    
    ---
    
    ## ⚠️ 复核与出行贴士
    1.  **证件准备**：身份证必带，学生证可优惠部分景点。
    2.  **预约机制**：钟山风景区、总统府、博物院均为**实名制分时段预约**，建议提前 1-3 天在官方公众号预订。
    3.  **交通建议**：首选地铁（支付宝领电子卡），避开周末早晚高峰拥堵路段。
    4.  **天气预警**：关注近期降水，雨天建议调整户外行程为室内博物馆。
    5.  **防坑指南**：夫子庙路边低价导游团慎入；买特产去正规超市而非景区路边摊。
    
    ---
    *版本更新：2023-10-V2 (已根据最新开园政策及用户反馈优化)*
    
    # 🇨🇳 南京两日深度游全攻略
    
    ## 📍 一、住宿推荐
    | 区域 | 推荐理由 | 适合人群 | 参考价位 |
    | :--- | :--- | :--- | :--- |
    | **新街口商圈** | 地铁枢纽（1/2 号线），餐饮购物最集中，往返景点便利。 | 首次游客，追求效率 | 300-600 元 |
    | **夫子庙/老门东** | 紧邻秦淮河，夜景绝佳，文化氛围浓。 | 喜欢热闹，赏夜景 | 400-800 元 |
    
    ## 🗺️ 二、两日行程安排
    > **⚠️ 重要提示：** 周一多数景点闭馆（总统府、中山陵、南博等），预约请提前 3-7 天关注官方公众号。
    
    ### 📅 第一天：民国风云与秦淮夜韵（市中心线）
    | 时间 | 行程 | 备注/门票 |
    | :--- | :--- | :--- |
    | **09:00** | **总统府** | 需预约（35 元），参观近代历史建筑核心。 |
    | **12:00** | **午餐·新街口/科巷** | 附近品尝地道小吃（见美食篇）。 |
    | **14:30** | **江宁织造博物馆** | 免费（需预约），红楼梦主题，环境清幽。 |
    | **17:30** | **夫子庙 & 老门东** | 逛明清建筑群，晚餐在老门东解决。 |
    | **19:30** | **秦淮河夜游** | 乘画舫赏灯景（约 100-120 元），行程高潮。 |
    
    ### 📅 第二天：钟山风雨与古都怀古（城东线）
    | 时间 | 行程 | 备注/门票 |
    | :--- | :--- | :--- |
    | **09:00** | **中山陵景区** | 免费（需预约），登台阶俯瞰全城。 |
    | **11:30** | **美龄宫 & 明孝陵** | 美龄宫 30 元；明孝陵 70 元（联票更优），看神道石象。 |
    | **14:30** | **鸡鸣寺** | 10 元，祈福求姻缘，登顶可远眺紫峰大厦。 |
    | **16:30** | **玄武湖公园** | 免费，环湖散步，从解放门进入最佳。 |
    | **18:30** | **返程/结束** | 周边享用晚餐后返程。 |
    
    ## 🥢 三、必吃美食清单
    | 类别 | 必点菜品 | 推荐店铺 | 推荐区域 |
    | :--- | :--- | :--- | :--- |
    | **鸭子类** | 盐水鸭、金陵烤鸭 | 章云板鸭、韩复兴 | 随处可见老字号 |
    | **汤面类** | 鸭血粉丝汤、皮肚面 | 小潘记、同来轩 | 科巷、评事街 |
    | **面点类** | 牛肉锅贴、梅花糕 | 李记清真馆、陆氏梅花糕 | 水西门、夫子庙旁 |
    | **特色菜** | 红烧狮子头、活珠子 | 南京大牌档 | 新街口/夫子庙 |
    
    ## ⚠️ 四、出行贴士
    1.  **预约第一**：南京博物院极难抢票（建议提前 7 天），若约不到可用“侵华日军南京大屠杀遇难同胞纪念馆”替代或调整行程。
    2.  **交通方式**：首选地铁（支付宝领卡），避开早晚高峰打车，景区间步行可达。
    3.  **避坑指南**：夫子庙核心区用餐慎选大排档，去周边居民区更实惠；路边低价导游团勿信。
    4.  **气候准备**：春秋最佳，夏季炎热多雨，带好雨具及防晒用品。
    

# 3. RAG
RAG 系统包含三个主要组件：
- 检索器（Retriever）：负责从知识库中找到相关信息。
- 向量数据库（Vector Store）：存储文档的向量表示，支持高效相似度搜索。
- 生成器（Generator）：基于检索结果和原始问题生成最终回答。

流程：
1. 索引阶段。将文档切分为 chunks（文本块），向量化后存入向量数据库。
2. 检索阶段。用户查询到来时，将查询向量化，在向量数据库中进行相似度搜索。
3. 增强阶段。将检索到的相关文档与原始查询一起发送给生成模型。
4. 生成阶段。生成模型基于增强的上下文生成最终回答。

## 3.1 基础 RAG


```python

```

## 3.2 Advanced RAG


```python

```

## 3.3 混合检索


```python

```

## 3.4 GraphRAG
