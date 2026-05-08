# 1 介绍
智能体，本质是自动执行任务的程序，核心在于让模型不只回答问题，而是按步骤完成动作。  

Agent = LLM (大脑) + Planning (规划) + Tool use (执行) + Memory (记忆)。

# 2 核心组件与工作原理

![image.png](../images/Agent3.png)

# 3 大语言模型

## 3.1 Transfomer 架构

## 3.2 API调用


```python
from openai import OpenAI
import os

client = OpenAI(
    api_key='',
    base_url='',
)

response = client.responses.create(
    model='',
    instructions='You are a coding assistant that talks like a pirate.',
    input='How do I check if a Python object is an instance of a class?'
)

print(response.output_text)
```


```python
# 国内支持openai，如阿里云。更多调用https://bailian.console.aliyun.com/cn-beijing/?spm=5176.29619931.J_SEsSjsNv72yRuRFS2VknO.2.2a5610d7c1Gxp0&tab=api#/api/?type=model&url=2833609
client = OpenAI( 
        # api_key=os.getenv("DASHSCOPE_API_KEY"),
        api_key="sk-xxx",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)
completion = client.chat.completions.create(
    model="qwen-plus",  
    messages=[{'role': 'system', 'content': 'You are a helpful assistant.'},
              {'role': 'user', 'content': '你是谁？'}],
    stream=True,  # 流式调用
    stream_options={"include_usage": True} # 流式调用
)
# print(completion.model_dump_json())
# print(completion.choices[0].message.content)

for chunk in completion:
    # chunk 里可能没有 choices 或 delta
    if hasattr(chunk, "choices") and len(chunk.choices) > 0:
        choice = chunk.choices[0]
        if hasattr(choice, "delta") and hasattr(choice.delta, "content"):
            print(choice.delta.content, end='', flush=True)
```

# 4 提示词与token
参考[prompt.ipynb](../Agent/prompt.ipynb)

# 5 推理与规划

## 5.1 思维链 CoT（Chain of Thought）
传统 LLM 生成答案时往往是直觉式的一步到位。

CoT 核心思想是：强制要求模型在输出最终答案前，先显式地输出中间的推理步骤。这种做法能显著激活模型在复杂数学、逻辑推理和常识问答中的潜力。

CoT 不仅让模型有了更多的计算时间（token 数量代表计算量），还让后续的生成能建立在前面正确的逻辑基础上。

>```txt
># 通过提供包含推理过程的示例，引导模型进行 CoT 推理
>prompt = """
>问题：罗杰有5个网球。他又买了2罐网球。每罐有3个网球。他现在共有多少个网球？
>解答：罗杰一开始有5个网球。2罐网球，每罐3个，共计 2 * 3 = 6 个网球。5 + 6 = 11。答案是11。
>
>问题：食堂有23个苹果。如果他们用掉20个做午餐，又买了6个，现在有多少个苹果？
>解答：食堂本来有23个苹果。用掉20个后剩下 23 - 20 = 3 个。又买了6个，现在有 3 + 6 = 9 个。答案是9。
>
>问题：{user_question}
>解答："""
>```

## 5.2 ReAct（Reasoning + Acting）
Agent 遵循 Thought（思考） -> Action（行动） -> Observation（观察） 的循环，直到得出最终结论。

>```mermaid
>flowchart LR
>    subgraph ROAM[ ]
>        direction LR
>        A[思考<br/>Reason<br/>LLM 推理]:::blue
>        B[行动<br/>Action<br/>调用工具]:::green
>        C[观察<br/>Observe<br/>获取结果]:::orange
>        D[记忆<br/>Memory<br/>存储上下文]:::purple
>        E((用户<br/>User)):::dark
>    end
>
>    A -- 1.生成计划 --> B
>    B -- 2.执行动作 --> C
>    C -- 3.接收反馈 --> D
>    D -- 4.更新记忆，继续推理 --> A
>
>    classDef blue fill:#3498db,stroke:#2980b9,stroke-width:2px,color:white
>    classDef green fill:#2ecc71,stroke:#27ae60,stroke-width:2px,color:white
>    classDef orange fill:#e67e22,stroke:#d35400,stroke-width:2px,color:white
>    classDef purple fill:#9b59b6,stroke:#8e44ad,stroke-width:2px,color:white
>    classDef dark fill:#34495e,stroke:#2c3e50,stroke-width:2px,color:white
>```

局限性： ReAct 在短期的、步骤清晰的任务中表现优异。  
但由于整个思维和动作历史都积压在同一个上下文窗口中，当任务链条过长时，极易陷入死循环或因为上下文超载而遗忘初始目标。

## 5.3 Plan-and-Execute（规划先行执行模式）
>```txt
>复杂目标 --> Plan规划(1. 抓取网页 2. 提取数据 3. 生成报告) --> Executor执行(逐个处理子任务，每次独立上下文) --> 最终交付
>```

## 5.4 ToT (Tree of Thoughts) 与树状多路径探索
**树状多路径探索**

无论是 CoT 还是 Plan-and-Execute，本质上都是线性的路径探索。但在写代码、解数学题或创意写作时，人类往往会设想多种方案，评估后选择最佳的，甚至在发现错误时回溯。

**ToT（思维树）**

将推理过程建模为一棵树：节点是当前的思维状态。  
模型会在每一个分支点生成多个候选 Thought，然后通过内部的 Evaluator（评估器）对这些节点进行打分（如：可行、可能有风险、不可行）。  
结合 BFS（广度优先搜索） 或 DFS（深度优先搜索） 算法，决定是继续深入还是回溯重试。  

## 5.5 任务规划 & MCTS (蒙特卡洛树搜索)

在涉及战略游戏或极高难度的推理任务（如前沿的数学验证、复杂的代码仓库重构）时，简单的 ToT 仍不够高效。

业界开始将 LLM 与传统的强化学习搜索算法 MCTS（Monte Carlo Tree Search） 结合（类似 AlphaGo 的核心逻辑）。

LLM 作为策略网络（Policy Network）：提供启发式的下一步行动建议，减少无意义的分支扩展。

LLM/代码环境作为价值网络（Value Network）：通过仿真执行（Rollout）预判某个行动序列的最终胜率或成功率。

优势：在庞大的解空间中，能够找到最具有全局最优潜力的规划路径。

## 5.6 Reflexion：自我反思与纠错

Reflexion 框架赋予了 Agent 自我反思与纠错的能力。

在 Reflexion 闭环中，当 Agent 的输出被判定为失败（例如：测试用例未通过、API 报错）时，会触发一个 Reviewer 机制。

LLM 被要求根据"历史动作"和"失败的反馈"写一段口语化的反思（Reflection），例如："我刚才使用了错误的 API 参数格式，下一次我应该查阅文档后再传递 JSON"。

这段反思会被存入情景记忆（Episodic Memory）中，作为下一次尝试的上下文提示，从而大幅提升 Agent 的自愈合能力。

>```txt
>reflection_prompt = """
>你是一个正在尝试编写 Python 爬虫的 AI 助手。
>这是你刚才执行的代码：{previous_code}
>这是运行环境返回的错误信息：{error_traceback}
>
>请深刻反思：
>1. 错误发生的根本原因是什么？
>2. 在下一次尝试中，你具体的修改策略是什么？
>
>请将反思记录下来，以指导后续的行动。
>"""
>```

## 5.7 任务分解策略与工程化实践
在实际生产级的 AI 智能体开发中，纯靠 LLM "零样本"进行复杂规划是不稳定的。常用的混合干预策略包括：

| 干预策略          | 核心做法                 | 适用场景                           |
|-------------------|------------------------|-------------------------------------|
| 子任务模板化 (SOP) | 不让 LLM 自由规划，而是预先定义好标准操作程序（SOP），让 LLM 在固定的状态机（State Machine）中流转。         | 客服系统、标准化的数据清洗流水线。   |
| HITL (Human-in-the-Loop) | 在 Planner 生成任务列表后，中断执行，要求人类用户进行确认、修改或审批（Approve），然后再交由 Executor 执行。   | 高风险操作：如删除数据库记录、发送群发邮件、大额资金转账。    |
| RLHF 引导规划     | 利用强化学习和人类偏好反馈，专门微调大模型的规划能力，使其更倾向于生成安全、高效的步骤组合。    | 底层大语言模型基座的训练阶段（如 OpenAI 的 o1 模型训练）。   |


# 6 RAG
检索增强生成:让 LLM 在回答问题时，先从外部知识库中检索相关内容，再基于检索结果生成回答

解决了 LLM 的两个核心痛点：知识截止日期（模型不知道训练后发生的事）和幻觉问题（模型在不确定时会编造答案）。

![image.png](../images/Agent4.png)

## 6.1 文档切分
**文档解析**

在切分时往往面临着格式解析的挑战。特别是 PDF、Word 或扫描件中的表格、图片和多栏排版，普通的文本提取极易造成语义错乱。

目前行业主流方案是引入 文档解析引擎（如 LlamaParse、Unstructured）或多模态大模型，将复杂图文转换为结构化的 Markdown，为后续高质量切分打下基础。

**切分策略**

| 切分策略              | 适用场景          | 优点                     | 缺点                |
|-----------------------|-------------------|--------------------------|---------------------------------|
| 固定大小切分          | 通用文本          | 实现简单，速度快   | 可能切断语义完整的句子                   |
| 递归字符切分          | 结构化文本（Markdown、代码） | 优先按段落、句子等语义边界切分   | 实现略复杂，需设定合理的分隔符列表     |
| 语义切分 (Semantic)   | 长文档、书籍      | 利用 Embedding 计算相邻句子的相似度，自动寻找语义转折点切分  | 计算成本高，预处理速度慢  |
| 父子文档检索 (Small-to-Big) | 全面覆盖场景   | 用"小块"进行高精度向量检索，命中后返回对应的"大块"（父文档）给 LLM，兼顾了检索精度和上下文完整性 | 数据库设计和维护成本翻倍 |

实践中常在切分时加入 重叠（overlap），即相邻块之间共享若干字符，防止重要信息在边界处被截断。典型配置：块大小 512 tokens，重叠 50~100 tokens。

>```py
>from langchain.text_splitter import RecursiveCharacterTextSplitter
>
>splitter = RecursiveCharacterTextSplitter(
>    chunk_size=512,        # 每块最大 token 数
>    chunk_overlap=50,      # 相邻块的重叠 token 数，防止信息在边界处丢失
>    separators=["\n\n", "\n", "。", ".", " ", ""]  # 优先按段落、句子切分
>)
>
>chunks = splitter.split_text(document_text)
>print(f"切分为 {len(chunks)} 个文档块")
>```

## 6.2 向量检索
**Embedding模型**

Embedding 模型负责将文本转换为稠密向量（通常是 768 或 1536 维的浮点数数组）。语义相近的文本在向量空间中距离更近，这正是相似度检索的数学基础。

**距离度量**

检索的核心是度量距离。最常用的是余弦相似度（Cosine Similarity），它计算两个向量的夹角余弦值，值域 [-1, 1]，越接近 1 越相似。

此外还有点积（Dot Product）和欧氏距离（L2 Distance）。

**检索算法**

为了在百万级向量中实现毫秒级检索，数据库通常采用近似最近邻（ANN）算法（如 HNSW、IVF）。

HNSW 是目前最主流的算法，它通过构建多层跳跃图网络，牺牲极少的精度换取了数量级的搜索速度提升。

## 6.3 Advanced RAG
基础架构（Naive RAG）常面临检索不准确、冗余信息多导致"上下文淹没"等问题。Advanced RAG 通过 `预检索优化 → 检索融合 → 后检索优化` 的三段式架构予以解决。

1、预检索：查询优化

用户的原始问题往往表达不够精确：
- 查询改写（Query Rewriting）：用 LLM 将口语化提问改写为规范化的检索词。
- HyDE（Hypothetical Document Embedding）：让 LLM 先"盲猜"一个假设性答案，由于生成的答案通常比原问题包含更多行业术语，用这个假设答案的向量去检索，往往能召回更高质量的文档。

2、混合检索（Hybrid Search）

将向量检索（懂语义，容错率高）与关键词检索（BM25，匹配度高）的结果按权重融合。  
这在遇到专有名词、产品型号、代码片段时尤为重要，因为传统的向量检索容易在特定的专有名词上"翻车"。

3、后检索优化：重排序（Reranking）

这是一个 `粗排 → 精排` 的两阶段设计。向量检索虽然快，但打分不够精确。  
重排序（Reranking）会引入 Cross-Encoder 模型（如 `bge-reranker`），将"问题"和"文档"成对输入模型进行联合推理打分。  
它的运算量大，只负责精选 Top-20 到 Top-5。

>```py
># 伪代码
>from sentence_transformers import CrossEncoder
>
>reranker = CrossEncoder("BAAI/bge-reranker-v2-m3") 
>
># 1. 粗排：向量检索极速召回 Top-50
>candidates = vector_store.similarity_search(query, k=50)
>
># 2. 精排：构建 [问题, 文档] 对进行精确打分
>pairs = [[query, doc.page_content] for doc in candidates]
>scores = reranker.predict(pairs)
>
># 3. 筛选最终传入 LLM 的 Top-5
>ranked_docs = sorted(zip(scores, candidates), reverse=True)
>final_docs = [doc for _, doc in ranked_docs[:5]]
>```

## 6.4 Self-RAG 与 CRAG
加入自我反思机制。  
例如 CRAG（Corrective RAG）在拿到检索结果后，先由 LLM 充当"评委"打分。  
如果本地知识库查无此文或质量极低，系统会自动触发 Web Search（如 Google API）作为补充，大幅降低幻觉。

## 6.5 GraphRAG：知识图谱 + 检索融合
传统 RAG 将知识库当作独立的文本碎片，无法回答诸如"找到所有同时由现任 CEO 创办且市值超千亿的公司"这类需要跨文档、多跳推理的复杂问题。  
GraphRAG 引入知识图谱（Knowledge Graph），将实体和关系显式建模。

![image.png](../images/Agent5.png)

核心步骤
- 知识构建：离线阶段使用 LLM 从文档提取三元组（主体、关系、客体），写入 Neo4j 等图数据库。
- 双路检索：针对提问中的实体，不仅做传统的向量检索，同时在图谱中触发图遍历（Graph Traversal），提取多跳关系链。
- 图文融合生成：将向量检索找回的"片段"与图检索找回的"路径结构"拼装进 Prompt，使得 LLM 既具备全局视野又掌握具体细节。

## 6.6 技术与数据库选型

| 数据库/工具选型 | 类型   | 推荐落地场景 |
|--------------|------|-------------|
| **Pinecone / Zilliz Cloud** | 全托管云服务 | 开箱即用，无需维护基础设施；适合快速商用场景，搭配 **Cohere Rerank + GPT-4o** 可实现高效检索与生成结合。 |
| **Qdrant**| 开源 + 托管  | 基于 Rust 编写，内存管理优秀，性能极高；适合企业级私有化部署，尤其是对检索速度和稳定性要求高的场景。 |
| **Weaviate / Elasticsearch** | 开源 + 托管  | 内置成熟的 **BM25 + 向量混合检索（Hybrid Search）**；适合专有名词较多、需要语义与关键词结合检索的场景（如法律、医疗文档）。|
| **Milvus**| 开源分布式   | 适合十亿至百亿级别的超大规模企业级检索平台；支持高并发、分布式扩展，适合大数据量下的高性能检索需求。 |
| **Chroma / FAISS**    | 本地库/嵌入式 | 极轻量，无需部署独立服务；适合本地开发、个人知识库项目验证，或对资源占用敏感的轻量级应用。|


## 6.7 评估指标
主流使用 RAGAS 框架，从"检索"和"生成"两个维度进行自动化量化测试：

- Context Recall（检索召回率）：标准答案中的信息有多少比例能被检索到。
- Context Precision（检索精确率）：检索到的文档中有多少比例是真正相关的。
- Faithfulness（忠实度/幻觉指标）：生成的答案是否都有检索出的文档支撑。
- Answer Relevance（答案相关性）：生成的答案是否真正回答了用户的问题，避免答非所问。

# 7 Agent架构

## 7.1 单 Agent 循环（Single Agent Loop）
单 Agent 循环直接体现了 ReAct 模式

![image-2.png](../images/Agent6.png)

每次工具调用的结果都会回写到上下文。因此随着任务推进，上下文会不断增长，直到触达 LLM 的上下文窗口限制——这是单 Agent 循环最主要的瓶颈。

- 实现简单
- 无法并行处理多个子任务
- 上下文窗口容易撑满。

>```py
># 单 Agent 循环的简化实现 —— 展示 ReAct 模式的核心逻辑
>
>class SimpleAgent:
>    """单 Agent 循环的基本结构"""
>
>    def __init__(self, model, tools, max_turns=10):
>        self.model = model          # 大语言模型
>        self.tools = tools          # 可用工具列表
>        self.max_turns = max_turns  # 最大循环轮次，防止无限循环
>
>    def run(self, task: str) -> str:
>        """执行任务的主循环"""
>        context = f"用户任务：{task}"
>
>        for turn in range(self.max_turns):
>            # 第一步：思考 —— 让模型决定下一步
>            response = self.model.think(context)
>
>            # 如果模型认为任务完成，返回最终答案
>            if response.is_final():
>                return response.content
>
>            # 第二步：行动 —— 调用模型选择的工具
>            tool_name = response.tool_name
>            tool_args = response.tool_args
>            tool_result = self.tools[tool_name](**tool_args)
>
>            # 第三步：将工具结果反馈给模型，进入下一轮
>            context += f"\n工具 {tool_name} 返回：{tool_result}"
>
>        return "达到最大轮次，任务未完成"
>
># 使用示例
>agent = SimpleAgent(model=llm, tools={
>    "read_file": read_file,
>    "search_code": search_code,
>    "run_test": run_test
>})
>result = agent.run("修复项目中 user.py 的类型错误")
>```

## 7.2 规划 + 执行（Plan & Execute）
![image.png](../images/Agent7.png)


|规划|行为|典型场景|特点与代价|
| ---- | ---- | ---- | ---- |
|静态规划|计划一次性生成，按顺序线性执行，不中途调整|流程固定、步骤明确的任务，如数据迁移脚本|实现相对简单，但缺乏灵活性，难以应对任务执行过程中的变化|
|动态规划|每执行一步后重新评估，根据结果调整后续计划|结果不确定的任务，如调试、探索性数据分析|更健壮，能适应任务执行中的变化，但实现复杂度更高，且每步重新规划会消耗额外的 token|

Claude Code 的 Plan Mode 就是这个架构的体现

- 执行前可人工审查计划
- 推理和执行分离
- 增加了推理轮次，对长任务友好，简单任务浪费
- 初始计划可能不够准确
- 两阶段增加了延迟
- 静态版本难以应对意外情况

>```py
># Plan & Execute 架构的简化实现
>
>class PlanExecuteAgent:
>    """先规划、后执行的 Agent"""
>
>    def plan(self, task: str) -> list:
>        """阶段一：生成执行计划"""
>        plan = self.model.generate(f"""
>        请将以下任务拆解为可执行的步骤列表：
>        任务：{task}
>        返回 JSON 格式的步骤列表，每步包含：
>        - step_id: 步骤编号
>        - description: 步骤描述
>        - tool: 需要调用的工具名
>        """)
>        return plan
>
>    def execute(self, plan: list, dynamic: bool = False) -> str:
>        """阶段二：逐步执行计划"""
>        results = []
>        remaining_plan = plan.copy()
>
>        while remaining_plan:
>            step = remaining_plan.pop(0)
>            output = self.tools[step["tool"]](step["description"])
>            results.append({"step": step["step_id"], "output": output})
>
>            if dynamic and remaining_plan:
>                # 动态规划：根据当前结果重新评估后续计划
>                remaining_plan = self.replan(remaining_plan, results)
>
>        return self.summarize(results)
>
># 使用示例
>agent = PlanExecuteAgent()
>plan = agent.plan("为项目添加用户认证功能")
># 人类可以先审查 plan，确认合理后再执行
>result = agent.execute(plan, dynamic=True)
>```

## 7.3 多 Agent 协作（Multi-Agent）
![image.png](../images/Agent8.png)

每个子 Agent 拥有独立的上下文窗口。

子 Agent（Subagent）是短暂的、隔离的——完成一个任务后即销毁。Agent 团队（Agent Teams）则是多个独立 Agent 实例长时间协作、互相发消息，更像一个真实的团队。

- 天然支持并行，速度快
- 子 Agent 各自独立，上下文互不干扰
- 可以专门化每个子 Agent 的角色
- 协调逻辑复杂，调试困难
- 多个 Agent 并行的 Token 成本更高
- Orchestrator 本身可能成为瓶颈
- 多 Agent 协作的主要成本是编排开销。如果子任务非常简单（每个只需 1-2 步），编排开销可能超过实际工作的开销，单 Agent 更合适。

>```py
># 多 Agent 协作的简化实现
>
>class Orchestrator:
>    """编排器：负责任务拆解、分发和结果汇总"""
>
>    def __init__(self):
>        self.subagents = {
>            "code_review": Subagent(
>                name="代码审查",
>                tools=["read_file", "static_analysis"],
>                system_prompt="你是代码审查专家..."
>            ),
>            "security": Subagent(
>                name="安全检测",
>                tools=["scan_vulnerability", "check_deps"],
>                system_prompt="你是安全检测专家..."
>            ),
>            "performance": Subagent(
>                name="性能分析",
>                tools=["profile_code", "analyze_complexity"],
>                system_prompt="你是性能分析专家..."
>            )
>        }
>
>    def handle_task(self, task: str) -> dict:
>        # 第一步：分析任务，决定需要哪些 Subagent
>        needed = self.plan(task)
>
>        # 第二步：并行分发（各 Subagent 同时工作，独立上下文）
>        results = {}
>        for agent_name in needed:
>            sub_task = self.decompose(task, agent_name)
>            results[agent_name] = self.subagents[agent_name].run(sub_task)
>
>        # 第三步：汇总各 Subagent 的结果，综合输出
>        return self.synthesize(task, results)
>
># 使用示例：一次运行，三个维度并行分析
>orch = Orchestrator()
>report = orch.handle_task("审查PR #42")
>```

## 7.4 反思与修正（Reflection）
![image.png](../images/Agent9.png)

| 方式       | 机制                                                         | 优点                          | 缺点                                      |
|------------|--------------------------------------------------------------|-------------------------------|-------------------------------------------|
| 自我反思   | 同一个模型先执行再评估自己的输出                             | 实现简单，无额外模型成本       | 模型可能对自己的错误"视而不见"            |
| Critic 模型 | 用独立的评判模型评估执行模型的输出                           | 更客观，能发现执行模型盲区     | 增加模型调用成本和延迟                    |

- 显著提升输出质量
- 可以设置明确的质量标准
- 适合有客观评判标准的任务
- 多次迭代增加延迟和成本
- 需要设置最大迭代次数防止死循环
- 评判标准难以形式化时效果有限

>```py
># 反思架构的简化实现
>
>class ReflectiveAgent:
>    """带有自我反思能力的 Agent"""
>
>    def __init__(self, model, tools, max_reflections=3):
>        self.model = model
>        self.tools = tools
>        self.max_reflections = max_reflections  # 最多修正次数，防止死循环
>
>    def run(self, task: str) -> str:
>        # 第一步：正常执行，产生初始输出
>        output = self.model.generate(task)
>
>        for i in range(self.max_reflections):
>            # 第二步：反思 —— 评估输出质量
>            critique = self.model.generate(f"""
>            请严格评估以下输出：
>            原始任务：{task}
>            当前输出：{output}
>            检查：事实错误？逻辑漏洞？遗漏信息？格式问题？
>            如果输出完美无缺，请回复 "PASS"。
>            """)
>
>            if "PASS" in critique:
>                break  # 输出通过审查
>
>            # 第三步：修正 —— 根据批评意见改进
>            output = self.model.generate(f"""
>            原始任务：{task}
>            上次输出：{output}
>            问题反馈：{critique}
>            请根据反馈修正输出。
>            """)
>
>        return output
>
># 使用示例
>agent = ReflectiveAgent(model=llm, tools={})
>code = agent.run("编写一个 Python 函数，实现字符串的 AES 加密")
># Agent 生成代码后自我检查加密实现、密钥处理，
># 发现漏洞后自动修正，确保输出安全可靠
>```

## 7.5 RAG + Agent（检索增强型智能体）
![image.png](../images/Agent10.png)

与一般RAG不同：   
一般 RAG 是用户提问时固定检索一次，将结果塞入 Prompt。  
RAG + Agent 中 Agent 自主判断在推理的哪个环节需要补充知识、需要检索什么，并可以多次查询知识库，直到获得足够的信息来完成任务。

- 突破上下文窗口限制
- 输出有据可查，减少幻觉
- 知识库可独立更新
- 检索质量影响整体效果
- 向量数据库的维护成本
- 检索延迟增加响应时间

>```py
># RAG + Agent 的简化实现
>
>class RAGAgent:
>    """带有动态检索能力的 Agent"""
>
>    def __init__(self, model, vector_db, max_retrievals=5):
>        self.model = model
>        self.vector_db = vector_db  # 向量数据库
>        self.max_retrievals = max_retrievals
>
>    def should_retrieve(self, context: str, question: str) -> bool:
>        """Agent 自己判断是否需要检索更多信息"""
>        decision = self.model.generate(f"""
>        当前已知信息：{context}
>        当前问题：{question}
>        现有信息是否足以回答问题？回答 YES 或 NO。
>        """)
>        return "NO" in decision
>
>    def run(self, task: str) -> str:
>        context = ""
>        retrieval_count = 0
>
>        while retrieval_count < self.max_retrievals:
>            # Agent 自主判断是否需要检索
>            if not self.should_retrieve(context, task):
>                break
>
>            # Agent 自主决定检索什么
>            search_query = self.model.generate(f"""
>            任务：{task}
>            已有信息：{context}
>            为了完成任务，下一步应该检索什么信息？
>            """)
>
>            # 执行检索，结果追加到上下文
>            docs = self.vector_db.search(search_query)
>            context += "\n".join(docs)
>            retrieval_count += 1
>
>        # 综合所有信息生成最终答案
>        return self.model.generate(f"任务：{task}\n参考资料：{context}")
>
># 使用示例
>agent = RAGAgent(model=llm, vector_db=runoob_docs_db)
>answer = agent.run("项目框架中如何配置数据库连接池？")
># Agent 先检索"连接池配置"，发现提到"最大连接数"
># 如果不理解，会再次检索"最大连接数最佳实践"
># 最终综合多轮检索结果给出完整回答
>```

## 7.6 工作流编排（Workflow / DAG 有向无环图）
把 Agent 行为固化为一张有向无环图（DAG），每个节点是一个 LLM 调用或工具调用，边表示数据依赖关系，由框架驱动执行。

这是最接近传统软件工程的一种 Agent 架构。与前面几种架构的最大区别在于：`Agent 的自主决策空间被限制在单个节点内部，节点之间的流转是预先定义好的，不可更改。`

![image.png](../images/Agent11.png)

- 可预测、可审计、可重试
- 支持并行加速
- 工程化程度高，运维友好
- 流程需要预先设计，灵活性低
- 难以应对未预期的情况
- 需要学习编排框架

>```py
># DAG 工作流的简化定义（类似 LangGraph 风格）
>
>from langgraph import StateGraph
>
># 定义工作流状态 —— 节点间传递的数据对象
>class PipelineState:
>    raw_data: str = ""         # 原始输入数据
>    cleaned_data: str = ""     # 清洗后的数据
>    analysis_result: dict = {} # 分析结果
>    final_report: str = ""     # 最终报告
>
># 定义 DAG 节点 —— 每个节点是独立的处理单元
>def extract_data(state: PipelineState) -> PipelineState:
>    """节点1：从 runoob 数据库中提取原始数据"""
>    state.raw_data = query_database("SELECT * FROM logs")
>    return state
>
>def clean_data(state: PipelineState) -> PipelineState:
>    """节点2：清洗数据（去重、标准化格式）"""
>    state.cleaned_data = preprocess(state.raw_data)
>    return state
>
>def analyze_data(state: PipelineState) -> PipelineState:
>    """节点3：统计分析"""
>    state.analysis_result = statistical_analysis(state.cleaned_data)
>    return state
>
>def generate_report(state: PipelineState) -> PipelineState:
>    """节点4：使用 LLM 生成报告"""
>    state.final_report = llm.generate(
>        f"基于以下分析结果生成报告：{state.analysis_result}"
>    )
>    return state
>
># 构建 DAG：定义节点和边（数据流向）
>workflow = StateGraph(PipelineState)
>workflow.add_node("extract", extract_data)
>workflow.add_node("clean", clean_data)
>workflow.add_node("analyze", analyze_data)
>workflow.add_node("report", generate_report)
>
># 定义边：extract → clean → analyze → report
>workflow.add_edge("extract", "clean")
>workflow.add_edge("clean", "analyze")
>workflow.add_edge("analyze", "report")
>workflow.set_entry_point("extract")
>workflow.set_finish_point("report")
>
># 编译并运行
>app = workflow.compile()
>result = app.invoke(PipelineState())
>print(result.final_report)
>```

# 8 AI Agent 简单实现


```python
from typing import Any, Dict, List, Callable
import time

# -----------------------------
# Memory（非常轻量）
# -----------------------------
class Memory:
    def __init__(self):
        self.short = {}   # 当前会话上下文
        self.long = {}    # 长期偏好/联系人等

    def get_short(self, k, default=None):
        return self.short.get(k, default)

    def set_short(self, k, v):
        self.short[k] = v

    def get_long(self, k, default=None):
        return self.long.get(k, default)

    def set_long(self, k, v):
        self.long[k] = v

# -----------------------------
# LLM 抽象（替换点）
# -----------------------------
class LLMInterface:
    def generate(self, prompt: str) -> str:
        """
        这里给出一个非常简单的规则式模拟回答器。
        真实使用时：替换为 OpenAI/其它模型的调用代码，返回 model 文本。
        """
        # 极简解析示例：识别是否需要判断"下雨"
        if "是否下雨" in prompt or "下雨" in prompt:
            return "请先查询天气；如果有雨，请生成提醒并发送给目标联系人。"
        if "生成提醒" in prompt:
            return "请提醒小王：明天北京有雨，请带伞。"
        return "我理解了。"

# -----------------------------
# 工具注册与模拟工具
# -----------------------------
class ToolRegistry:
    def __init__(self):
        self.tools: Dict[str, Callable[..., Any]] = {}

    def register(self, name: str, fn: Callable[..., Any]):
        self.tools[name] = fn

    def call(self, name: str, *args, **kwargs):
        if name not in self.tools:
            raise ValueError(f"工具未注册: {name}")
        return self.tools[name](*args, **kwargs)

# 模拟工具：天气查询（真实情况会调用天气 API）
def mock_weather_api(city: str, date: str) -> Dict[str, Any]:
    # 简单规则：如果 city 包含 "北京" 且 date 包含 "明天"，返回下雨示例
    if "北京" in city and "明天" in date:
        return {"city": city, "date": date, "cond": "雨", "precip_mm": 5}
    return {"city": city, "date": date, "cond": "晴", "precip_mm": 0}

# 模拟工具：发送消息（真实情况会调用短信/邮件/企业微信等）
def mock_send_message(contact: str, message: str) -> bool:
    print(f"[发送消息] to={contact} message={message}")
    return True

# 模拟工具：简单搜索（示意）
def mock_search(query: str) -> str:
    return f"模拟搜索结果：关于 `{query}` 的信息摘要。"

# -----------------------------
# Planner / Executor
# -----------------------------
class SimplePlanner:
    def plan(self, goal: str) -> List[Dict[str, Any]]:
        """
        将目标拆解为步骤列表（非常简化的实现）
        每一步包含：action(工具名或内部动作)、params
        """
        steps = []
        # 例：若提示包含"天气"，生成两个步骤：查天气、判断并可能发提醒
        if "天气" in goal or "下雨" in goal:
            steps.append({"action": "query_weather", "params": {"city": "北京", "date": "明天"}})
            steps.append({"action": "decide_and_notify", "params": {"contact_name": "小王"}})
        else:
            steps.append({"action": "search", "params": {"query": goal}})
        return steps

class Executor:
    def __init__(self, tools: ToolRegistry, memory: Memory, llm: LLMInterface):
        self.tools = tools
        self.memory = memory
        self.llm = llm

    def run_step(self, step: Dict[str, Any]):
        action = step["action"]
        params = step.get("params", {})
        if action == "query_weather":
            res = self.tools.call("weather", params["city"], params["date"])
            self.memory.set_short("last_weather", res)
            return res
        if action == "decide_and_notify":
            weather = self.memory.get_short("last_weather", {})
            # 简单规则决策
            if weather.get("cond") == "雨":
                # 让 LLM 生成提醒文本（示例）
                prompt = f"基于天气信息：{weather}，生成一条发给{params['contact_name']}的提醒。"
                reminder = self.llm.generate(prompt)
                # 从长期记忆中获取联系方式
                contact = self.memory.get_long(params["contact_name"]) or "13800000000"
                ok = self.tools.call("send_message", contact, reminder)
                return {"notified": ok, "message": reminder}
            else:
                return {"notified": False, "reason": "天气晴朗"}
        if action == "search":
            return self.tools.call("search", params["query"])
        raise ValueError(f"未知动作: {action}")

# -----------------------------
# Agent 本体
# -----------------------------
class SimpleAgent:
    def __init__(self):
        self.memory = Memory()
        self.tools = ToolRegistry()
        self.llm = LLMInterface()
        self.planner = SimplePlanner()
        self.executor = Executor(self.tools, self.memory, self.llm)
        # 注册默认工具
        self.tools.register("weather", mock_weather_api)
        self.tools.register("send_message", mock_send_message)
        self.tools.register("search", mock_search)
        # 假设长期记忆里存了小王的联系方式
        self.memory.set_long("小王", "13911112222")

    def handle(self, user_prompt: str):
        # 1) 大脑解析（用 LLM 抽象）
        intent = self.llm.generate(user_prompt)
        # 2) 规划
        steps = self.planner.plan(user_prompt)
        # 3) 逐步执行
        results = []
        for step in steps:
            r = self.executor.run_step(step)
            results.append({"step": step, "result": r})
        # 4) 输出合并
        return {"intent": intent, "steps": results}

# -----------------------------
# 运行示例
# -----------------------------
if __name__ == "__main__":
    agent = SimpleAgent()
    task = "查一下明天北京的天气，如果下雨，帮我写个提醒并发给小王。"
    out = agent.handle(task)
    import json
    print(json.dumps(out, ensure_ascii=False, indent=2))
```
