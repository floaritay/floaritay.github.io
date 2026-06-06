# 简介
一个用于构建 API 的现代、快速（高性能）的 web 框架，专为在 Python 中构建 RESTful API 而设计，支持前后端分离的Web应用。

FastAPI 使用 Python 3.8+ 并基于标准的 Python 类型提示。

FastAPI 建立在 Starlette 和 Pydantic 之上，利用类型提示进行数据处理，并自动生成API文档。

FastAPI 支持异步编程，可在生产环境中运行。

# 安装
需要Python 3.8 及更高版本
>```bash
>python --version
>
>pip install fastapi
>```
也可以使用以下命令直接安装 FastAPI 及所有可选依赖:
>```bash
>pip install "fastapi[all]"
>```
这会安装：
- fastapi - FastAPI 框架
- uvicorn[standard] - ASGI 服务器
- python-multipart - 表单和文件上传支持
- jinja2 - 模板引擎
- python-jose - JWT 令牌支持
- passlib - 密码哈希
- bcrypt - 密码加密
- python-dotenv - 环境变量支持

另外我们还需要一个 ASGI 服务器，生产环境可以使用 Uvicorn 或者 Hypercorn：
>```bash
>pip install "uvicorn[standard]"
>```

## 简单实例


```python
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
def read_root():
    return {'message' : 'Hello FastAPI'}
```

在命令行中运行以下命令以启动应用（文件名main.py）：
>```bash
>uvicorn main:app --reload
>```
打开浏览器并访问 http://127.0.0.1:8000，你应该能够看到 FastAPI 自动生成的交互式文档，并在根路径 ("/") 返回的 JSON 响应。

如果默认端口已经被占用：

- 停止调试器
- 打开命令面板（⇧⌘P），搜索并选择 Debug: Add Configuration
- 选择 Python Debugger，然后选择 FastAPI
- 这将会在 .vscode/launch.json 中创建一个自定义配置文件
- 在 "args":[] 中添加如下内容以设置自定义端口："args": ["--port=5000"]

## 项目结构建议
>```
>my_fastapi_project/
>├── app/
>│   ├── __init__.py
>│   ├── main.py         # 应用入口
>│   ├── api/            # API路由
>│   │   ├── __init__.py
>│   │   ├── items.py
>│   │   └── users.py
>│   ├── models/         # 数据模型
>│   │   ├── __init__.py
>│   │   └── user.py
>│   ├── schemas/        # Pydantic模型
>│   │   ├── __init__.py
>│   │   └── user.py
>│   └── db/             # 数据库相关
>│       ├── __init__.py
>│       └── session.py
>├── tests/              # 测试代码
>│   ├── __init__.py
>│   └── test_api.py
>├── requirements.txt    # 依赖列表
>└── .env                # 环境变量

## 调试 FastAPI
在 VS Code 中：

1. 设置断点
2. 按 F5 启动调试
3. 在浏览器中访问 API 端点

单元测试
使用 pytest：


```python
# test_main.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'message' : 'Hello FastAPI'}
```

运行测试：
>```bash
>pytest

## 部署准备
生产服务器推荐使用：
- Uvicorn + Gunicorn
- Hypercorn
- Daphne

Docker 部署

创建 Dockerfile：
>```Dockerfile
>FROM python:3.9
>
>WORKDIR /app
>
>COPY requirements.txt .
>RUN pip install --no-cache-dir -r requirements.txt
>
>COPY . .
>
>CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
>```
构建并运行：
>```bash
>docker build -t fastapi-app .
>docker run -d -p 80:80 fastapi-app
>```

# Fast API应用
以下的 FastAPI 应用，在简单实例的基础上加入了一个新的路由操作（/items/{item_id}）


```python
from fastapi import FastAPI
from typing import Union # 用于支持多种数据类型的参数注解

app = FastAPI() # 创建 FastAPI 实例

# 使用了 @app.get("/") 装饰器，定义一个 GET 请求的路由，路径为根路径 "/"
# 表示当用户通过 HTTP GET 请求访问根路径时，将执行 read_root 函数
# 函数返回一个包含 {"Hello": "World"} 的字典，这个字典会被 FastAPI 自动转换为 JSON 格式并返回给用户。    
@app.get('/') 
def read_root():
    return {'message' : 'Hello FastAPI'}

# 函数接受两个参数：
# item_id  是路径参数，指定为整数类型。
# q        是查询参数，指定为字符串类型或空（None）。允许在请求中不提供 q 参数。
@app.get('/items/{item_id}')
def read_item(item_id: int, q: Union[str, None] = None):
    return {'item_id': item_id, 'q': q}
```

# FastAPI 交互式 API 文档
FastAPI 提供了内置的交互式 API 文档。

这个文档是自动生成的，基于 OpenAPI 规范，支持 Swagger UI 和 ReDoc 两种交互式界面。

在运行 FastAPI 应用时，Uvicorn 同时启动了交互式 API 文档服务。

1. 默认情况下，你可以通过访问 http://127.0.0.1:8000/docs 来打开 Swagger UI 风格的文档（注意是http）：

    Swagger UI 提供了一个直观的用户界面，用于浏览 API 的各个端点、查看请求和响应的结构，并支持直接在文档中进行 API 请求测试。

    通过 Swagger UI，你可以轻松理解每个路由操作的输入参数、输出格式和请求示例。

2. 或者通过 http://127.0.0.1:8000/redoc 来打开 ReDoc 风格的文档。

    ReDoc 是另一种交互式文档界面，具有清晰简洁的外观。它使得开发者能够以可读性强的方式查看 API 的描述、请求和响应。

    与 Swagger UI 不同，ReDoc 的设计强调文档的可视化和用户体验。

- 实时更新： 交互式文档会实时更新，反映出应用代码的最新更改。
- 自动验证： 输入参数的类型和格式会得到自动验证，降低了错误的可能性。
- 便于测试： 可以直接在文档中进行 API 请求测试，避免使用其他工具。

接下来我们修改 main.py 文件来从 PUT 请求中接收请求体。

我们借助 Pydantic 来使用标准的 Python 类型声明请求体。

修改完代码后，我们不需要重启服务器，因为服务器将会自动重载，因为在前面的章节中 uvicorn 命令添加了 --reload 选项。


```python
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
```

访问 http://127.0.0.1:8000/docs

点击「Try it out」按钮，之后你可以填写参数并直接调用 API

然后点击「Execute」按钮，用户界面将会和 API 进行通信，发送参数，获取结果并在屏幕上展示

访问 http://127.0.0.1:8000/redoc 同理

# FastAPI 基本路由
? 和 & 是 查询字符串（Query String） 的分隔符，用于传递 GET 请求的参数。

`?` 标记查询字符串的开始  
- 格式：路径?参数1=值1&参数2=值2...

`&` 用于分隔多个参数

`=`	键值对分隔
- 例如：?q=foo&q=bar

|部分	     |说明                    |
|---        |---                     |
|http://	|协议（HTTP）             |
|127.0.0.1	|服务器地址（本地）        |
|:8000	    |端口号（FastAPI 默认端口）|
|/items/	|路径（路由）              |
|?	        |查询字符串开始            |
|skip=1	    |参数1（跳过1条数据）      |
|&	        |参数分隔符                |
|limit=5	|参数2（限制返回5条数据）   |

- 参数顺序不重要
- 如果未指定类型（如 skip: int），则参数值会被解析为字符串
- 如果参数有默认值（如 skip: int = 0），则该参数是可选的
- 参数可以是列表或复杂类型

## 查询参数路由
>```python
>@app.get("/items/")
>def read_item(skip: int = 0, limit: int = 10):
>    return {"skip": skip, "limit": limit}
>```
URL 结构：http://127.0.0.1:8000/items/?skip=1&limit=5  
参数位置：在 ? 之后，以 key=value 形式传递。

## 路径参数路由
>```python
>@app.get("/items/{item_id}") # 注意{item_id}
>def read_item(item_id: int, q: str = None):
>    return {"item_id": item_id, "q": q}
>```
URL 结构：http://127.0.0.1:8000/items/123?q=search  
参数位置：  
item_id：在路径中（/items/123）。  
q：在查询字符串中（?q=search）。 

# FastAPI 请求和响应

## 请求体
接下来创建一个 /items/ 路由，使用 @app.post 装饰器表示这是一个处理 POST 请求的路由。


```python
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None 

app = FastAPI()

@app.post('/items/')
def create_item(item:Item):
    return item
```

## 响应体
返回 JSON 数据  
路由处理函数返回一个字典，该字典将被 FastAPI 自动转换为 JSON 格式，并作为响应发送给客户端：


```python
# 例如之前的
@app.get('/items/{item_id}')
def read_item(item_id: int, q: Union[str, None] = None):
    return {'item_id': item_id, 'q': q}
```

返回 Pydantic 模型  
路由处理函数返回一个 Pydantic 模型实例，FastAPI 将自动将其转换为 JSON 格式，并作为响应发送给客户端：


```python
# 例如之前的
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None 

@app.post('/items/')
def create_item(item:Item):
    return item
```

## 请求头和 Cookie


```python
from fastapi import FastAPI
from fastapi import Header,Cookie

app = FastAPI() 
@app.get('/items/')
def read_items(user_agent:str=Header(None),session_token:str=Cookie(None)):
    return {'user_agent': user_agent, 'session_token': session_token}
```

## 重定向和状态码
以下代码在浏览器访问 http://127.0.0.1:8000/redirect/ 会自动跳转到 http://127.0.0.1:8000/items/ 页面：


```python
from fastapi import FastAPI
from fastapi import Header,Cookie
from fastapi.responses import RedirectResponse

app = FastAPI() 
@app.get('/items/')
def read_items(user_agent:str=Header(None),session_token:str=Cookie(None)):
    return {'user_agent': user_agent, 'session_token': session_token}

@app.get('/redirect/')
def redirect():
    return RedirectResponse(url='/items/')    
```

使用 HTTPException 抛出异常，返回自定义的状态码和详细信息。

以下实例在 item_id 为 42 会返回 404 状态码：


```python
from fastapi import FastAPI
from fastapi import HTTPException

app = FastAPI()

@app.get('/items/{item_id}')
def read_item(item_id:int):
  if item_id == 42:
    raise HTTPException(status_code=404,detail='item not found')
  return {'item_id': item_id}
```

## 自定义响应头
使用 JSONResponse 自定义响应头:


```python
from fastapi import FastAPI
from fastapi.reponses import JSONResponse

app = FastAPI()

@app.get('/items/{item_id}')
def read_item(item_id:int):
    headers={'X-Custom-Header':'custom-header-value'}
    content={'item_id':item_id}
    return JSONResponse(header=header,content=content)
```

# FastAPI Pydantic 模型
Pydantic 是一个用于数据验证和序列化的 Python 模型库。

它在 FastAPI 中广泛使用，用于定义请求体、响应体和其他数据模型，提供了强大的类型检查和自动文档生成功能。

使用 Pydantic 定义一个模型非常简单，只需创建一个继承自 pydantic.BaseModel 的类，并在其中定义字段。

字段的类型可以是任何有效的 Python 类型，也可以是 Pydantic 内置的类型。

## 请求体验证

在 FastAPI 中，可以将 Pydantic 模型用作请求体（Request Body），以自动验证和解析客户端发送的数据。

create_item 路由处理函数接受一个名为 item 的参数，其类型是 Item 模型。FastAPI 将自动验证传入的 JSON 数据是否符合模型的定义，并将其转换为 Item 类型的实例。


```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name:str
    price:float
    description:str = None
    tax:float = None 

@app.post('/items/'):
def create_item(item:Item):
    return item

# 请求连接示例：
# curl -X POST "http://127.0.0.1:8000/items/" -H "accept: application/json" -H "Content-Type: application/json" -d '{"name":"Foo","price":35.5,"description":"A very nice Item","tax":3.5}'
```

## 查询参数验证
read_item 路由处理函数接受一个 Item 模型的实例作为查询参数，以及一个名为 q 的字符串查询参数。通过使用 Query 函数，我们还可以为查询参数指定更多的验证规则，如最大长度限制。


```python
from fastapi import Query
 
@app.get('/items/')
def read_item(item:Item,q:str=Query(...,max_length=10)):
    return {'item':item,'q':q}
```

# FastAPI 路径操作依赖项
允许你在路由处理函数执行之前或之后运行一些额外的逻辑。

依赖项就是一个函数，且可以使用与路径操作函数相同的参数。

路径操作依赖项提供了一种灵活的方式来组织代码、验证输入、进行身份验证等。

## 依赖项
路由操作函数执行前或后运行的可复用的函数或对象。
- 预处理（Before）依赖项： 在路由操作函数执行前运行，用于预处理输入数据，验证请求等。
- 后处理（After）依赖项： 在路由操作函数执行后运行，用于执行一些后处理逻辑，如日志记录、清理等。

依赖注入是将依赖项注入到路由操作函数中的过程。

在 FastAPI 中，通过在路由操作函数参数中声明依赖项来实现依赖注入。

FastAPI 将负责解析依赖项的参数，并确保在执行路由操作函数之前将其传递给函数。

## 预处理
common_parameters 是一个依赖项函数，它接受查询参数 q、skip 和 limit，并返回一个包含这些参数的字典。

在路由操作函数 read_items 中，通过传入 Depends(common_parameters)，我们使用了这个依赖项函数，实现了在路由执行前预处理输入数据的功能。

FastAPI 将在执行路由操作函数之前运行 common_parameters 函数，并将其返回的结果传递给 read_items 函数。


```python
from fastapi import FastAPI,Depends

app = FastAPI()

def common_parameters(q:str=None,skip:int=0,limit:int=10):
    return {'q':q,'skip':skip,'limit':limit}

@app.get('/items/')
async def read_item(commons:dict=Depends(common_parameters)):
    return commons
```

## 后处理
以下例子中，after_request 是一个后处理函数，用于在路由执行后执行一些逻辑。

在路由操作函数 read_items_after 中，通过传入 Depends(after_request)，我们使用了这个后处理依赖项，实现了在路由执行后进行额外操作的功能。


```python
# -----同上------
from fastapi import FastAPI,Depends

app = FastAPI()

def common_parameters(q:str=None,skip:int=0,limit:int=10):
    return {'q':q,'skip':skip,'limit':limit}

@app.get('/items/')
async def read_item(commons:dict=Depends(common_parameters)):
    return commons

# -----后处理-----
async def after_request():
    # 这里可以执行一些后处理逻辑，比如记录日志
    pass

@app.get("/items/", response_model=dict) # esponse_model=dict 用于指定路由返回的响应数据的模型
async def read_items_after(request: dict = Depends(after_request)):
    return {"message": "Items returned successfully"}
```

## 多个依赖项的组合
common_parameters 和 verify_token 是两个不同的依赖项函数，verify_token 依赖于 common_parameters，

这种组合依赖项的方式允许我们在路由执行前先验证一些参数，然后在进行身份验证。


```python
from fastapi import Depends, FastAPI, HTTPException

app = FastAPI()

# 依赖项函数1
def common_parameters(q: str = None, skip: int = 0, limit: int = 10):
    return {"q": q, "skip": skip, "limit": limit}

# 依赖项函数2
def verify_token(token: str = Depends(common_parameters)):
    if token is None:
        raise HTTPException(status_code=400, detail="Token required")
    return token

# 路由操作函数
@app.get("/items/")
async def read_items(token: dict = Depends(verify_token)):
    return token
```

## 异步依赖项
依赖项函数和后处理函数可以是异步的，允许在它们内部执行异步操作。

以下例子中，get_token 是一个异步的依赖项函数，模拟了一个异步操作。

在路由操作函数 read_items 中，我们使用了这个异步依赖项函数。


```python
from fastapi import Depends, FastAPI, HTTPException
from typing import Optional
import asyncio

app = FastAPI()

# 异步依赖项函数
async def get_token():
    # 模拟异步操作
    await asyncio.sleep(2)
    return "fake-token"

# 异步路由操作函数
@app.get("/items/")
async def read_items(token: Optional[str] = Depends(get_token)):
    return {"token": token}
```

# FastAPI 表单数据
在 FastAPI 中，接收表单数据是一种常见的操作，通常用于处理用户通过 HTML 表单提交的数据。

FastAPI 提供了 Form 类型，可以用于声明和验证表单数据。

接下来我们设计一个接收一个登陆的表单数据，要使用表单，需预先安装 python-multipart：
>```bash
>pip install python-multipart。

## 声明表单数据模型


```python
from fastapi import FastAPI, Form

app = FastAPI()

@app.post("/login/")
async def login(username: str = Form(), password: str = Form()):
    return {"username": username}
```

使用 Pydantic 模型来声明表单数据模型。

在模型中，使用 Field 类型声明每个表单字段，并添加必要的验证规则。


```python
from pydantic import BaseModel, Field

class Item(BaseModel):
    name: str = Field(..., title="Item Name", max_length=100)
    description: str = Field(None, title="Item Description", max_length=255)
    price: float = Field(..., title="Item Price", gt=0)
```

## 在路由中接收表单数据
在路由操作函数中，可以使用 Form 类型来接收表单数据。

Form 类型的参数可以与 Pydantic 模型的字段一一对应，以实现表单数据的验证和转换。

create_item 路由操作函数接收了三个表单字段：name、description 和 price，这些字段与 Item 模型的相应字段一致，FastAPI 将自动根据验证规则验证表单数据。


```python
from fastapi import FastAPI, Form

app = FastAPI()

# 路由操作函数
@app.post("/items/")
async def create_item(
    name: str = Form(...),
    description: str = Form(None),
    price: float = Form(..., gt=0),
):
    return {"name": name, "description": description, "price": price}
```

## 处理文件上传
如果表单包含文件上传，可以使用 UploadFile 类型处理。

create_file 路由操作函数接收了一个 UploadFile 类型的文件参数。

FastAPI 将负责处理文件上传，并将文件的相关信息包装在 UploadFile 对象中，可以轻松地获取文件名、内容类型等信息。

通过上述方式，FastAPI 提供了一种简单而强大的方法来接收和处理表单数据，同时保持了代码的清晰性和可维护性。


```python
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

# 路由操作函数
@app.post("/files/")
async def create_file(file: UploadFile = File(...)):
    return {"filename": file.filename}
```

# FastAPI 核心概念

# HTTP 相关

HTTP（超文本传输协议）是一种用于从网络传输超文本到本地浏览器的传输协议。它定义了客户端与服务器之间请求和响应的格式。HTTP 工作在 TCP/IP 模型之上，通常使用端口 80。

HTTPS（超文本传输安全协议）是 HTTP 的安全版本，它在 HTTP 下增加了 SSL/TLS 协议，提供了数据加密、完整性校验和身份验证。HTTPS 通常使用端口 443。

主要的HTTP方法有：
- GET：请求从服务器获取指定资源。这是最常用的方法，用于访问页面。
- POST：请求服务器接受并处理请求体中的数据，通常用于表单提交。
- PUT：请求服务器存储一个资源，并用请求体中的内容替换目标资源的所有内容。
- DELETE：请求服务器删除指定的资源。
- HEAD：与 GET 类似，但不获取资源的内容，只获取响应头信息。

状态码分为五类：
- 1xx（信息性状态码）：表示接收的请求正在处理。
- 2xx（成功状态码）：表示请求正常处理完毕。
- 3xx（重定向状态码）：需要后续操作才能完成这一请求。
- 4xx（客户端错误状态码）：表示请求包含语法错误或无法完成。
- 5xx（服务器错误状态码）：服务器在处理请求的过程中发生了错误。

版本
- HTTP/1.1：支持持久连接，允许多个请求/响应通过同一个 TCP 连接传输，减少了建立和关闭连接的消耗。
- HTTP/2：基于二进制分帧，支持多路复用，允许同时通过单一的 HTTP/2 连接发起多重的、独立的、双向的交流。
- HTTP/3：基于 QUIC 协议，旨在减少网络延迟，提高传输速度和安全性。

Web 服务器有：Nginx 服务器，Apache 服务器，IIS 服务器（Internet Information Services）等。

## 消息结构
请求消息结构

- 请求行（Request Line）：
  - 方法：如 GET、POST、PUT、DELETE等，指定要执行的操作。
  - 请求 URI（统一资源标识符）：请求的资源路径，通常包括主机名、端口号（如果非默认）、路径和查询字符串。
  - HTTP 版本：如 HTTP/1.1 或 HTTP/2。
  - 请求行的格式示例：GET /index.html HTTP/1.1

- 请求头（Request Headers）：
  - 包含了客户端环境信息、请求体的大小（如果有）、客户端支持的压缩类型等。
  - 常见的请求头包括Host、User-Agent、Accept、Accept-Encoding、Content-Length等。

- 空行：
  - 请求头和请求体之间的分隔符，表示请求头的结束。

- 请求体（可选）：
  - 在某些类型的HTTP请求（如 POST 和 PUT）中，请求体包含要发送给服务器的数据。

响应消息结构
- 状态行（Status Line）：
  - HTTP 版本：与请求消息中的版本相匹配。
  - 状态码：三位数，表示请求的处理结果，如 200 表示成功，404 表示未找到资源。
  - 状态信息：状态码的简短描述。
  - 状态行的格式示例：HTTP/1.1 200 OK

- 响应头（Response Headers）：
  - 包含了服务器环境信息、响应体的大小、服务器支持的压缩类型等。
  - 常见的响应头包括Content-Type、Content-Length、Server、Set-Cookie等。

- 空行：
  - 响应头和响应体之间的分隔符，表示响应头的结束。
  
- 响应体（可选）：
  - 包含服务器返回的数据，如请求的网页内容、图片、JSON数据等。

## 响应头
| 响应头信息（英文） | 响应头信息（中文） | 描述 |
| ---- | ---- | ---- |
| Date | 日期 | 响应生成的日期和时间。例如：Wed, 18 Apr 2024 12:00:00 GMT |
| Server | 服务器 | 服务器软件的名称和版本。例如：Apache/2.4.1 (Unix) |
| Content-Type | 内容类型 | 响应体的媒体类型（MIME类型），如text/html; charset=UTF-8, application/json等。 |
| Content-Length | 内容长度 | 响应体的大小，单位是字节。例如：3145 |
| Content-Encoding | 内容编码 | 响应体的压缩编码，如 gzip, deflate等。 |
| Content-Language | 内容语言 | 响应体的语言。例如：zh-CN |
| Content-Location | 内容位置 | 响应体的 URI。例如：/index.html |
| Content-Range | 内容范围 | 响应体的字节范围，用于分块传输。例如：bytes 0-999/8000 |
| Cache-Control | 缓存控制 | 控制响应的缓存行为, 如 no-cache 表示必须重新请求。 |
| Connection | 连接 | 管理连接的选项，如keep-alive或close，keep-alive 表示连接不会在传输后关闭。 |
| Set-Cookie | 设置 Cookie | 设置客户端的 cookie。例如：sessionId=abc123; Path=/; Secure |
| Expires | 过期时间 | 响应体的过期日期和时间。例如：Thu, 18 Apr 2024 12:00:00 GMT |
| Last-Modified | 最后修改时间 | 资源最后被修改的日期和时间。例如：Wed, 18 Apr 2024 11:00:00 GMT |
| ETag | 实体标签 | 资源的特定版本的标识符。例如："33a64df551425fcc55e6" |
| Location | 位置 | 用于重定向的 URI。例如：/newresource |
| Pragma | 实现特定的指令 | 包含实现特定的指令，如 no-cache。 |
| WWW-Authenticate | 认证信息 | 认证信息，通常用于HTTP认证。例如：Basic realm="Access to the site" |
| Accept-Ranges | 接受范围 | 指定可接受的请求范围类型。例如：bytes |
| Age | 经过时间 | 响应生成后经过的秒数，从原始服务器生成到代理服务器。例如：24 |
| Allow | 允许方法 | 列出资源允许的 HTTP 方法 。例如：GET, POST，HEAD等 |
| Vary | 变化 | 告诉下游代理如何使用响应头信息来确定响应是否可以从缓存中获取。例如：Accept |
| Strict-Transport-Security | 严格传输安全 | 指示浏览器仅通过 HTTPS 与服务器通信。例如：max-age=31536000; includeSubDomains |
| X-Frame-Options | 框架选项 | 控制页面是否允许在框架中显示，防止点击劫持攻击。例如：SAMEORIGIN |
| X-Content-Type-Options | 内容类型选项 | 指示浏览器不要尝试猜测资源的 MIME 类型。例如：nosniff |
| X-XSS-Protection | XSS保护 | 控制浏览器的 XSS 过滤和阻断。例如：1; mode=block |
| Public-Key-Pins | 公钥固定 | HTTP 头信息，用于HTTP公共密钥固定（HPKP），一种安全机制，用于防止中间人攻击。例如：pin-sha256="base64+primarykey"; pin-sha256="base64+backupkey"; max-age=expireTime |
