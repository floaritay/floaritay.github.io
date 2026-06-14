# 目录

- [1 介绍](#1-介绍)
  - [1.1 核心原则](#11-核心原则)
- [2 概念](#2-概念)
  - [2.1 API](#21-api)
  - [2.2 REST](#22-rest)
- [3 HTTP](#3-http)
- [4 URL 设计规范](#4-url-设计规范)
  - [4.1 资源导向](#41-资源导向)
  - [4.2 命名规范](#42-命名规范)
  - [4.3 嵌套资源](#43-嵌套资源)
  - [4.4 查询参数](#44-查询参数)
  - [4.5 版本控制](#45-版本控制)
- [5 请求和响应格式](#5-请求和响应格式)
  - [5.1 请求格式](#51-请求格式)
  - [5.2 响应结构设计](#52-响应结构设计)
- [6 实际应用](#6-实际应用)
  - [6.1 完整流程](#61-完整流程)
  - [6.2 错误处理](#62-错误处理)
- [7 实践](#7-实践)
  - [7.1 身份验证和授权](#71-身份验证和授权)
  - [7.2 HTTPS 和数据加密](#72-https-和数据加密)
  - [7.3 性能优化实践](#73-性能优化实践)
  - [7.4 错误处理最佳实践](#74-错误处理最佳实践)
  - [7.5 API 文档化](#75-api-文档化)
  - [7.6 版本控制策略](#76-版本控制策略)
- [8 调试](#8-调试)
  - [8.1 Postman](#81-postman)
  - [8.2 curl 命令行测试](#82-curl-命令行测试)
  - [8.3 浏览器开发者工具](#83-浏览器开发者工具)
  - [8.4 其他问题](#84-其他问题)
  - [8.5 自动化测试](#85-自动化测试)
- [9 curl](#9-curl)
  - [9.1 选项](#91-选项)
  - [9.2 Query 参数](#92-query-参数)
- [10 进阶](#10-进阶)

---
# 1 介绍
在现代 Web 开发中，RESTful API 已成为应用程序之间通信的标准方式。

REST（Representational State Transfer，表述性状态转移）是一种软件架构风格

REST 定义了一组约束条件和原则，用于创建可扩展、松耦合的 Web 服务。

RESTful API 是遵循 REST 架构风格设计的 API。它使用HTTP协议的特性，通过 URL 定位资源，用 HTTP 方法（GET、POST等）描述操作，实现客户端与服务器之间的交互。

- 无状态：每个请求包含处理所需的所有信息
- 统一接口：使用标准 HTTP 方法进行操作
- 资源导向：所有内容都被抽象为资源
- 可缓存：响应应明确是否可缓存

## 1.1 核心原则
所有事物都被抽象为资源，每个资源有唯一的标识符（URI）。
- 使用名词而非动词表示资源
- 使用复数形式命名集合
- 使用小写字母和连字符(-)
- 避免文件扩展名

例如
```md
/users          # 用户集合
/users/123      # ID为123的用户
/users/123/orders  # 用户123的订单集合
```

充分利用HTTP方法的语义

| HTTP方法 | 描述 | 幂等性 | 安全性 |
| --- | --- | --- | --- |
| GET | 获取资源 | 是 | 是 |
| POST | 创建资源 | 否 | 否 |
| PUT | 完整更新资源 | 是 | 否 |
| PATCH | 部分更新资源 | 否 | 否 |
| DELETE | 删除资源 | 是 | 否 |

* 安全性：指该操作是否会对服务器上的资源状态产生修改
* 幂等性：指执行一次和执行多次产生的效果完全相同。

无状态性
- 每个请求必须包含处理所需的所有信息，服务器不保存客户端状态。这使得API易于扩展和负载均衡。

表述形式
- 资源可以有多种表述形式（如JSON、XML），客户端通过Accept头指定需要的格式。

# 2 概念
一种基于HTTP协议的软件架构风格，用于构建网络应用程序接口。

![image.png](RESTFulAPI_files/image.png)

## 2.1 API
API（Application Programming Interface，应用程序编程接口）就像是不同软件之间的"翻译官"。

在编程世界中，API 让不同的软件系统能够相互交流和协作。

![image.png](RESTFulAPI_files/image.png)

API 的主要作用包括：
- 数据交换：让不同系统之间能够传递信息
- 功能复用：避免重复造轮子，使用现成的服务
- 系统解耦：让前端和后端可以独立开发
- 安全控制：控制谁可以访问什么数据

## 2.2 REST
REST（Representational State Transfer，表述性状态转移）一套设计 Web API 的规则和约定。

1. 客户端-服务器架构  
前端（客户端）和后端（服务器）完全分离

2. 无状态性  
每次请求都是独立的，服务器不会记住之前的请求。就像每次去银行办业务，都需要重新出示身份证一样。

3. 可缓存性  
响应数据可以被缓存，提高性能。就像浏览器会缓存网页图片一样。

4. 统一接口  
所有 API 都遵循相同的规则和格式，就像所有餐厅的菜单都有类似的结构。

5. 分层系统  
系统可以有多层，比如：客户端 → 负载均衡器 → API 服务器 → 数据库

6. 按需代码（可选）  
服务器可以向客户端发送可执行代码，比如 JavaScript。

# 3 HTTP

参考[FastAPI.ipynb 中 HTTP 部分](FastAPI.ipynb#HTTP-相关)

# 4 URL 设计规范

## 4.1 资源导向
RESTful API 的 URL 应该表示"资源"而不是"动作"。

例如
```md
GET /api/users          # 获取所有用户
GET /api/users/123      # 获取 ID 为 123 的用户
POST /api/users         # 创建新用户
PUT /api/users/123      # 更新用户 123
DELETE /api/users/123   # 删除用户 123
```


## 4.2 命名规范
```md
使用名词而非动词
GET /api/books

使用复数形式
GET /api/users

使用小写字母
GET /api/user-orders

使用连字符分隔单词
GET /api/user-profiles
```

## 4.3 嵌套资源
当资源之间有从属关系时，可以使用嵌套 URL：
```md
// 获取用户 123 的所有订单
GET /api/users/123/orders

// 获取用户 123 的订单 456
GET /api/users/123/orders/456

// 为用户 123 创建新订单
POST /api/users/123/orders
```

## 4.4 查询参数
```md
javascript// 分页
GET /api/users?page=1&limit=10

// 过滤
GET /api/users?status=active&city=beijing

// 排序
GET /api/users?sort=created_at&order=desc

// 搜索
GET /api/users?search=张三
```

## 4.5 版本控制
URL 路径版本控制
```md
GET /api/v1/users
GET /api/v2/users
```

请求头版本控制
```md
GET /api/users
Accept: application/vnd.api+json;version=1
```

# 5 请求和响应格式
现代 RESTful API 主要使用 JSON（JavaScript Object Notation）格式来传输数据。

## 5.1 请求格式
```javascript
// 请求
GET /api/users/123
Accept: application/json

// 响应
{
  "id": 123,
  "name": "张三",
  "email": "zhangsan@example.com",
  "createdAt": "2024-01-15T08:30:00Z"
}

// 请求
POST /api/users
Content-Type: application/json

{
  "name": "李四",
  "email": "lisi@example.com",
  "password": "securePassword123"
}

// 响应
{
  "id": 124,
  "name": "李四",
  "email": "lisi@example.com",
  "createdAt": "2024-01-15T09:00:00Z",
  "message": "用户创建成功"
}
```

## 5.2 响应结构设计
```javascript
// 统一的响应格式
{
  "success": true,
  "data": {
    "id": 123,
    "name": "张三"
  },
  "message": "操作成功",
  "timestamp": "2024-01-15T08:30:00Z"
}

//错误响应格式
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "输入数据验证失败",
    "details": [
      {
        "field": "email",
        "message": "邮箱格式不正确"
      }
    ]
  },
  "timestamp": "2024-01-15T08:30:00Z"
}

//分页响应
{
  "success": true,
  "data": [
    {
      "id": 1,
      "name": "用户1"
    },
    {
      "id": 2,
      "name": "用户2"
    }
  ],
  "pagination": {
    "currentPage": 1,
    "totalPages": 10,
    "totalItems": 100,
    "itemsPerPage": 10
  }
}
```
请求头常用字段

| 字段名 | 作用 | 示例 |
| --- | --- | --- |
| Content-Type | 请求体数据格式 | application/json |
| Accept | 期望的响应格式 | application/json |
| Authorization | 身份验证信息 | Bearer token123 |
| User-Agent | 客户端信息 | MyApp/1.0 |

# 6 实际应用
设计一个完整的用户管理系统 API

## 6.1 完整流程
API 端点设计
```javascript
// 用户相关操作
GET    /api/users           # 获取用户列表
GET    /api/users/{id}      # 获取特定用户
POST   /api/users           # 创建新用户
PUT    /api/users/{id}      # 更新用户信息
DELETE /api/users/{id}      # 删除用户

// 用户订单相关操作
GET    /api/users/{id}/orders     # 获取用户的订单列表
POST   /api/users/{id}/orders     # 为用户创建订单
GET    /api/orders/{orderId}      # 获取特定订单详情
```

创建用户
```javascript
// 请求
POST /api/users
Content-Type: application/json

{
  "name": "王五",
  "email": "wangwu@example.com",
  "phone": "13800000000",
  "address": {
    "city": "上海",
    "street": "南京路100号"
  }
}

// 成功响应（状态码：201 Created）
{
  "success": true,
  "data": {
    "id": 125,
    "name": "王五",
    "email": "wangwu@example.com",
    "phone": "13800000000",
    "address": {
      "city": "上海", 
      "street": "南京路100号"
    },
    "createdAt": "2024-01-15T10:00:00Z",
    "updatedAt": "2024-01-15T10:00:00Z"
  },
  "message": "用户创建成功"
}
```

读取用户
```javascript
// 获取用户列表
GET /api/users?page=1&limit=5&sort=createdAt&order=desc

// 响应（状态码：200 OK）
{
  "success": true,
  "data": [
    {
      "id": 125,
      "name": "王五",
      "email": "wangwu@example.com",
      "createdAt": "2024-01-15T10:00:00Z"
    },
    {
      "id": 124,
      "name": "李四",
      "email": "lisi@example.com", 
      "createdAt": "2024-01-15T09:00:00Z"
    }
  ],
  "pagination": {
    "currentPage": 1,
    "totalPages": 3,
    "totalItems": 15,
    "itemsPerPage": 5
  }
}

// 获取特定用户
GET /api/users/125

// 响应
{
  "success": true,
  "data": {
    "id": 125,
    "name": "王五",
    "email": "wangwu@example.com",
    "phone": "13800000000",
    "address": {
      "city": "上海",
      "street": "南京路100号"
    },
    "createdAt": "2024-01-15T10:00:00Z",
    "updatedAt": "2024-01-15T10:00:00Z"
  }
}
```

更新用户
```javascript
// 请求
PUT /api/users/125
Content-Type: application/json

{
  "name": "王五",
  "email": "wangwu.new@example.com",
  "phone": "13900000000",
  "address": {
    "city": "深圳",
    "street": "科技园路200号"
  }
}

// 响应（状态码：200 OK）
{
  "success": true,
  "data": {
    "id": 125,
    "name": "王五",
    "email": "wangwu.new@example.com",
    "phone": "13900000000",
    "address": {
      "city": "深圳",
      "street": "科技园路200号"
    },
    "createdAt": "2024-01-15T10:00:00Z",
    "updatedAt": "2024-01-15T11:30:00Z"
  },
  "message": "用户信息更新成功"
}
```

删除用户
```javascript
// 请求
DELETE /api/users/125

// 响应（状态码：200 OK）
{
  "success": true,
  "message": "用户删除成功"
}

// 如果用户不存在（状态码：404 Not Found）
{
  "success": false,
  "error": {
    "code": "USER_NOT_FOUND", 
    "message": "用户不存在"
  }
}
```

## 6.2 错误处理
数据验证错误
```javascript
// 请求（邮箱格式错误）
POST /api/users
{
  "name": "",
  "email": "invalid-email",
  "phone": "123"
}

// 响应（状态码：400 Bad Request）
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "数据验证失败",
    "details": [
      {
        "field": "name",
        "message": "姓名不能为空"
      },
      {
        "field": "email", 
        "message": "邮箱格式不正确"
      },
      {
        "field": "phone",
        "message": "手机号格式不正确"
      }
    ]
  }
}
```

资源不存在错误
```javascript
// 请求
GET /api/users/999

// 响应（状态码：404 Not Found）
{
  "success": false,
  "error": {
    "code": "USER_NOT_FOUND",
    "message": "用户不存在"
  }
}
```

# 7 实践

## 7.1 身份验证和授权
```md
// 使用 JWT Token 进行身份验证
GET /api/users/profile
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

// API 响应包含用户权限检查
{
  "success": true,
  "data": {
    "id": 123,
    "name": "张三",
    "role": "user"
  }
}
```

输入验证
```md
// 服务器端验证示例
POST /api/users
{
  "email": "test@example.com",
  "password": "123"  // 密码太短
}

// 验证失败响应
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "密码长度至少为8位"
  }
}
```

## 7.2 HTTPS 和数据加密
使用https如 https://api.example.com/users

## 7.3 性能优化实践
```md
// 1. 数据分页
// 避免一次返回大量数据
GET /api/users?page=1&limit=20

{
  "success": true,
  "data": [...], // 只返回20条记录
  "pagination": {
    "currentPage": 1,
    "totalPages": 50,
    "totalItems": 1000
  }
}
// 2. 字段过滤
// 只返回需要的字段
GET /api/users?fields=id,name,email

{
  "success": true,
  "data": [
    {
      "id": 1,
      "name": "张三",
      "email": "zhangsan@example.com"
      // 不返回其他不需要的字段
    }
  ]
}
// 3. 缓存策略
// 使用缓存头
GET /api/users/123
Cache-Control: max-age=3600  // 缓存1小时

// 条件请求
GET /api/users/123
If-None-Match: "etag-value"

// 304 Not Modified (数据未变化)
```

## 7.4 错误处理最佳实践
```md
// 统一错误格式
{
  "success": false,
  "error": {
    "code": "SPECIFIC_ERROR_CODE",    // 机器可读的错误码
    "message": "用户友好的错误信息",      // 人类可读的错误信息
    "details": {...},                // 详细错误信息（可选）
    "timestamp": "2024-01-15T10:00:00Z"
  }
}
// 常见错误码设计
const ERROR_CODES = {
  // 4xx 客户端错误
  'VALIDATION_ERROR': 400,        // 数据验证失败
  'UNAUTHORIZED': 401,            // 未授权
  'FORBIDDEN': 403,              // 禁止访问
  'NOT_FOUND': 404,              // 资源不存在
  'METHOD_NOT_ALLOWED': 405,     // 方法不允许
  'CONFLICT': 409,               // 资源冲突
  
  // 5xx 服务器错误
  'INTERNAL_ERROR': 500,         // 内部服务器错误
  'SERVICE_UNAVAILABLE': 503     // 服务不可用
}
```

## 7.5 API 文档化
```md
// 使用标准化文档格式
// 推荐使用 OpenAPI (Swagger) 规范：

# swagger.yaml 示例
openapi: 3.0.0
info:
  title: 用户管理 API
  version: 1.0.0
  description: 提供用户的增删改查功能

paths:
  /api/users:
    get:
      summary: 获取用户列表
      parameters:
        - name: page
          in: query
          description: 页码
          schema:
            type: integer
            default: 1
      responses:
        '200':
          description: 成功
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                  data:
                    type: array
                    items:
                      $ref: '#/components/schemas/User'
```

## 7.6 版本控制策略
```javascript
URL 版本控制（推荐）
// 版本1
GET /api/v1/users

// 版本2（新增字段，保持向后兼容）
GET /api/v2/users
{
  "id": 1,
  "name": "张三",
  "email": "zhangsan@example.com",
  "avatar": "https://example.com/avatar.jpg"  // 新增字段
}
```

兼容性处理
```md
// 保持向后兼容的策略
{
  "deprecationWarning": "该 API 版本将在2024年6月1日后停止支持，请升级到 v2",
  "data": {...}
}
```

# 8 调试


## 8.1 Postman
Postman 是最流行的 API 测试工具 https://www.postman.com/。

基本测试步骤：

- 创建新请求
- 设置 HTTP 方法（GET、POST 等）
- 输入 API 地址
- 添加请求头和请求体
- 发送请求查看响应

示例：
```js
{
  "info": {
    "name": "用户管理 API 测试",
    "description": "测试用户相关的所有 API 端点"
  },
  "item": [
    {
      "name": "获取用户列表",
      "request": {
        "method": "GET",
        "header": [],
        "url": {
          "raw": "{{baseUrl}}/api/users?page=1&limit=10",
          "host": ["{{baseUrl}}"],
          "path": ["api", "users"],
          "query": [
            {"key": "page", "value": "1"},
            {"key": "limit", "value": "10"}
          ]
        }
      }
    }
  ]
}
```

## 8.2 curl 命令行测试
```bash
# 获取用户列表
curl -X GET "https://api.example.com/users" \
     -H "Content-Type: application/json"

# 创建新用户
curl -X POST "https://api.example.com/users" \
     -H "Content-Type: application/json" \
     -d '{
       "name": "张三",
       "email": "zhangsan@example.com"
     }'

# 更新用户信息
curl -X PUT "https://api.example.com/users/123" \
     -H "Content-Type: application/json" \
     -d '{
       "name": "李四",
       "email": "lisi@example.com"
     }'

# 删除用户
curl -X DELETE "https://api.example.com/users/123" \
     -H "Content-Type: application/json"
```

## 8.3 浏览器开发者工具
```JavaScript
// 在浏览器控制台中测试
fetch('/api/users', {
  method: 'GET',
  headers: {
    'Content-Type': 'application/json'
  }
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error('Error:', error));
```

## 8.4 其他问题

1. CORS 跨域问题  
    报错信息：  
    Access to fetch at 'https://api.example.com/users' from origin 'http://localhost:3000'   
    has been blocked by CORS policy  

    解决方案：  
    ```JavaScript
    // 服务器端需要设置 CORS 头  
    app.use((req, res, next) => {
    res.header('Access-Control-Allow-Origin', '*');
    res.header('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE');
    res.header('Access-Control-Allow-Headers', 'Content-Type, Authorization');
    next();
    });
    ```

2. 状态码错误  


3. 数据格式问题
    ```JavaScript
    // 错误的请求格式
    {
    name: "张三",  // &#x274c; 缺少引号
    'email': "test@example.com",  // &#x274c; 单引号
    age: "25"  // &#x274c; 数字用了字符串
    }

    // 正确的请求格式
    {
    "name": "张三",  // &#x2705; 双引号
    "email": "test@example.com",  // &#x2705; 双引号
    "age": 25  // &#x2705; 数字类型
    }
    ```

## 8.5 自动化测试
```JavaScript
// 使用 Jest 测试框架
describe('用户 API 测试', () => {
  test('应该能够获取用户列表', async () => {
    const response = await fetch('/api/users');
    const data = await response.json();
    
    expect(response.status).toBe(200);
    expect(data.success).toBe(true);
    expect(Array.isArray(data.data)).toBe(true);
  });
  
  test('应该能够创建新用户', async () => {
    const newUser = {
      name: "测试用户",
      email: "test@example.com"
    };
    
    const response = await fetch('/api/users', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(newUser)
    });
    
    const data = await response.json();
    
    expect(response.status).toBe(201);
    expect(data.success).toBe(true);
    expect(data.data.name).toBe(newUser.name);
  });
});
```

# 9 curl

基本格式 `curl [选项] [URL]`

## 9.1 选项
-X：指定 HTTP 方法
```bash
curl -X GET "http://localhost:3000/api/books" # -X GET 可以省略
curl -X POST "http://localhost:3000/api/books"
```

-H：添加请求头
- 告诉服务器我发送的数据是什么格式：Content-Type: application/json
- 告诉服务器我是哪个用户：Authorization: Bearer <token>
```bash
# -H 后面跟的就是 "键: 值" 对
curl -X POST "http://localhost:3000/api/books" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer xxx.xxx.xxx"
```

-d：携带请求体数据
```bash
# -d 后面的 JSON 字符串，外层必须用单引号 ' 包裹，内部的字符串用双引号 "
curl -X POST "http://localhost:3000/api/books" \
  -H "Content-Type: application/json" \
  -d '{"title": "新书", "author": "张三", "price": 59.0}'
```

-i 或 -v：查看响应头
- -i (Include)：在输出中包含 HTTP 响应头和状态码。
- -v (Verbose)：不仅得到响应头，连 curl 怎么建立连接、发送了什么请求头都给你打印出来。
```bash
curl -i -X DELETE "http://localhost:3000/api/books/1"
curl -v -X GET "http://localhost:3000/api/books"
```

## 9.2 Query 参数
GET 请求的问号后面。只能传递扁平的键值对。
Query 参数是完全暴露的，不要传密码、Token 等敏感信息。
最常绑定在 GET 和 DELETE 请求上。很多服务器、网关、缓存代理会直接丢弃 GET 请求的 Body，不要在 GET 请求中使用请求体。


```bash
curl -X GET "http://localhost:3000/api/books?page=1&pageSize=10&keyword=API"
```

# 10 进阶
