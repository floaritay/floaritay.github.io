# 目录


---
# Scrapy 介绍
Scrapy是一个基于Python的爬虫框架，用于爬取网页数据。

## Scrapy 架构
![image.png](https://i-blog.csdnimg.cn/blog_migrate/862934dd2e1cd4dee93162db356f808a.png)

- **Engine（引擎）**： 框架的核心，处理系统的数据流和事件。

- **Item**： 它是一个抽象的数据结构，所以在图中没有体现出来，它定义了爬取结果的数据结构，爬取的数据会被赋值成 Item 对象。  
每个 Item 就是一个类，类里面定义了爬取结果的数据字段，可以理解为它用来规定爬取数据的存储格式。

- **Scheduler（调度器）**： 接受 Engine 发过来的 Request 并将其加入队列中，同时也可以将 Request 发回给 Engine 供 Downloader 执行，它主要维护 Request 的调度。

- **Spiders（蜘蛛）**： 每个 Spider 里面定义了站点的爬取逻辑和页面的解析规则，它主要负责解析响应并生成 Item 和新的请求然后发给 Engine 进行处理。

- **Downloader（下载器）**： 完成向服务器发送请求，然后拿到响应的过程，得到的响应会再发送给 Engine 处理。

- **Item Pipelines（项目管道）**： 主要负责处理由 Spider 从页面中抽取的 Item，做一些数据清洗、验证和存储等工作，比如将 Item 的某些字段进行规整，将 Item 存储到数据库等操作都可以由 Item Pipeline 来完成。

- **Downloader Middlewares（下载器中间件）**： 位于 Engine 和 Downloader 之间的 Hook 框架，负责实现 Downloader 和 Engine 之间的请求和响应的处理过程。

- **Spider Middlewares（蜘蛛中间件）**： 位于 Engine 和 Spiders 之间的 Hook 框架，负责实现 Spiders 和 Engine 之间的 Item，请求和响应的处理过程。

## Scrapy 数据流
在整个爬虫运行的过程中，Engine 负责了整个数据流的分配和处理，数据流主要包括 Item、Request、Response 这三大部分，那它们又是怎么被 Engine 控制和流转的呢？

1. 启动爬虫项目时，Engine 根据要爬取的目标站点找到处理该站点的 Spider，Spider 会生成最初需要爬取的页面对应的一个或多个 Request，然后发给 Engine。

2. Engine 从 Spider 中获取这些 Request，然后把它们交给 Scheduler 等待被调度。

3. Engine 向 Scheduler 索取下一个要处理的 Request，这时候 Scheduler 根据其调度逻辑选择合适的 Request 发送给 Engine

4. Engine 将 Scheduler 发来的 Request 转发给 Downloader 进行下载执行，将 Request 发送给 Downloader 的过程会经由许多定义好的 Downloader Middlewares 的处理。

5. Downloader 将 Request 发送给目标服务器，得到对应的 Response，然后将其返回给 Engine。将 Response 返回 Engine 的过程同样会经由许多定义好的 Downloader Middlewares 的处理。

6. Engine 从 Downloader 处接收到的 Response 里包含了爬取的目标站点的内容，Engine 会将此 Response 发送给对应的 Spider 进行处理，将 Response 发送给 Spider 的过程中会经由定义好的 Spider Middlewares 的处理

7. Spider 处理 Response，解析 Response 的内容，这时候 Spider 会产生一个或多个爬取结果 Item 或者后续要爬取的目标页面对应的一个或多个 Request，然后再将这些 Item 或 Request 发送给 Engine 进行处理，将 Item 或 Request 发送给 Engine 的过程会经由定义好的 Spider Middlewares 的处理

8. Engine 将 Spider 发回的一个或多个 Item 转发给定义好的 Item Pipelines 进行数据处理或存储的一系列操作，将 Spider 发回的一个或多个 Request 转发给 Scheduler 等待下一次被调度。

重复第2步到第8步，直到 Scheduler 中没有更多的 Request，这时候 Engine 会关闭 Spider，整个爬取过程结束。 

从整体上来看，各个组件都只专注于一个功能，组件和组件之间的耦合度非常低，也非常容易扩展。

再由 Engine 将各个组件组合起来，使得各个组件各司其职，互相配合，共同完成爬取工作。

另外加上 Scrapy 对异步处理的支持，Scrapy 还可以最大限度地利用网络带宽，提高数据爬取和处理的效率。

# Scrapy 安装
安装成功之后，在命令行输入 scrapy 可以看到帮助信息。

# Scrapy 创建项目
首先，使用命令行创建项目  

`scrapy startproject 项目名字`  
例如：scrapy startproject doubantop250_spider

执行完毕之后，当前运行目录下便会出现一个名为 doubantop250_spider 的文件夹，该文件夹就对应一个 Scrapy 爬虫项目。

接着进入文件夹，我们可以再利用命令行创建一个 Spider 用来专门爬取豆瓣的网页内容：

`scrapy genspider 爬虫名字 爬虫域名`  
例如：scrapy genspider douban_top250 movie.douban.com

项目结构如下：
>```
>doubantop250_spider/
>├── doubantop250_spider/          # 项目核心目录
>│   ├── __init__.py
>│   ├── items.py           # 定义Item字段
>│   ├── middlewares.py     # 中间件（请求/响应拦截）
>│   ├── pipelines.py       # 数据处理管道
>│   ├── settings.py        # 配置文件
>│   └── spiders/           # 存放爬虫脚本
>│       └── __init__.py
>|       └── douban_top250.py
>└── scrapy.cfg             # 项目部署配置
>```
- scrapy.cfg: Scrapy项目的配置文件，定义了项目的配置文件路径、部署信息等

- items.py: 定义了Item数据结构

- pipelines.py: 定义了Item Pipeline的实现

- settings.py: 定义了项目的全局配置

- middlewares.py: 定义了Downloader Middlewares和Spider Middlewares的实现

- spiders: 里面包含了一个个 Spider 的实现，每个 Spider 都对应一个 Python 文件。


# Scrapy 入门
