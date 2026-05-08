# Docker 简介
Docker 是一个开源的应用容器引擎，基于 Go 语言 并遵从 Apache2.0 协议开源。

Docker 可以让开发者打包他们的应用以及依赖包到一个轻量级、可移植的容器中，然后发布到任何流行的 Linux 机器上，也可以实现虚拟化。

容器是完全使用沙箱机制，相互之间不会有任何接口（类似 iPhone 的 app）,更重要的是容器性能开销极低。

Docker 从 17.03 版本之后分为 CE（Community Edition: 社区版） 和 EE（Enterprise Edition: 企业版），我们用社区版就可以了。

# Docker 概念

## 核心概念

**容器（Container）**：基于镜像创建的轻量化的运行实例，包含应用代码、运行时环境和依赖库。
- 隔离性：每个容器都有自己的文件系统、网络和进程空间，但共享主机操作系统内核（比虚拟机更高效）。
- 临时性：容器可以被创建、启动、停止、删除
- 可写层：容器在镜像基础上添加了一个可写层
- 进程级：容器内通常运行一个主进程

**镜像（Image）**：只读模板，定义了容器的运行环境。
- 分层存储：镜像由多个层组成，进而优化空间和构建速度。每一层代表一次修改。
- 只读性：镜像本身是只读的，不能直接修改。
- 可复用：同一个镜像可以创建多个容器。
- 版本管理：通过标签(tag)进行版本管理。

**Dockerfile**：文本文件，描述如何自动构建镜像（例如指定基础镜像、安装软件、复制文件等）。

**仓库（Registry）**：存储和分发镜像的平台，可以包含一个镜像的多个版本。如 Docker Hub（官方公共仓库）或私有仓库（如 Harbor）。

### 什么是容器化技术？  
容器共享主机内核，轻量、隔离且高效，不像虚拟机需要完整的操作系统。

![image.png](https://www.runoob.com/wp-content/uploads/2025/05/d7d5638a-d0fe-45a4-8a67-59a21f4318d6.png)

- 上层：多个容器（App A~F），每个容器独立运行一个应用。
- 中间层：Docker，负责管理这些容器。
- 底层：主机操作系统（Host OS）和基础设施，为容器提供硬件和系统支持。

### 传统应用部署的痛点
1. 环境不一致：应用在开发环境运行正常，但在测试或生产环境出现问题
2. 依赖管理复杂：不同应用需要不同版本的运行时、库文件等
3. 资源利用率低：传统虚拟机需要完整的操作系统，占用大量资源
4. 部署复杂：需要手动配置环境、安装依赖，容易出错

### 容器化技术的解决方案
1. 环境标准化：将应用及其依赖打包在一起，确保在任何环境中都能一致运行
2. 轻量级：容器共享宿主机的操作系统内核，比虚拟机更轻量
3. 快速部署：容器可以在几秒内启动，大大提高了部署效率
4. 可移植性：一次构建，到处运行

### 容器化的核心理念
1. 应用和环境被打包成不可变的镜像
2. 每次部署都使用相同的镜像
3. 配置通过环境变量或配置文件注入
4. 问题修复通过重新构建镜像而非修改运行中的容器

## Docker 与 虚拟机
|特性	    |虚拟机	            |Docker容器|
|-----------|--------------------|----------|
|隔离级别	|硬件级别虚拟化	     |操作系统级别虚拟化|
|操作系统	|每个VM需要完整OS	 |共享宿主机OS内核|
|资源占用	|重量级，占用较多资源 |轻量级，资源占用少|
|启动时间	|分钟级别	         |秒级别|
|性能开销	|较大	             |接近原生性能|
|镜像大小	|GB级别	             |MB级别|

![image.png](https://www.runoob.com/wp-content/uploads/2025/05/1_choU2ZN14HZThwbqRFzlHg.png)

虚拟机适用场景：需要完全隔离的环境、运行不同操作系统的应用、需要硬件级别的安全隔离

Docker容器适用场景：微服务架构、CI/CD流水线、应用快速部署和扩展、开发环境标准化

# Docker 架构
Docker 使用客户端-服务器 (C/S) 架构模式，使用远程 API 来管理和创建 Docker 容器。

![image.png](https://www.runoob.com/wp-content/uploads/2025/05/screenshot-2023-01-16-at-110130.png)  

Docker Client（客户端）：用户与Docker交互的主要方式，接收用户命令并发送给Docker Daemon，可以与远程Docker Daemon通信

Docker Daemon（守护进程）：Docker的核心服务进程，管理镜像、容器、网络和存储卷，监听Docker API请求并处理

Docker Engine（引擎）：是Docker的核心组件  
组成：Docker Client + Docker Daemon + REST API

Docker Registry（仓库）：存储和分发Docker镜像，提供镜像的版本管理，支持公有和私有仓库


Docker 架构工作流程：
1. Client发送命令到Daemon
2. Daemon解析并执行命令
3. 与Registry交互（如需要）
4. 管理本地镜像和容器
5. 返回结果给Client

![image.png](https://www.runoob.com/wp-content/uploads/2016/07/docker-architecture.webp)



Docker Compose：一个用于定义和运行多容器 Docker 应用的工具。用户可以使用一个 docker-compose.yml 配置文件定义多个容器（服务），并可以通过一个命令启动这些容器。  
Docker Compose 主要用于开发、测试和部署多容器应用。

创建一个简单的 docker-compose.yml 文件来配置一个包含 Web 服务和数据库服务的应用：  
>```yml
>version: '3'
>services:
>  web:
>    image: nginx
>    ports:
>      - "8080:80"
>  db:
>    image: mysql
>    environment:
>      MYSQL_ROOT_PASSWORD: example
>```      
>启动 Compose 定义的所有服务：
>```bash
>docker-compose up
>```

Docker Swarm: Docker 提供的集群管理和调度工具。允许将多个 Docker 主机（节点）组织成一个集群，并通过 Swarm 集群管理工具来调度和管理容器。  

初始化 Swarm 集群：
>```bash
>docker swarm init
>```

Docker Networks（网络）：允许容器之间相互通信，并与外部世界进行连接。Docker 提供了多种网络模式来满足不同的需求，如 bridge 网络（默认）、host 网络和 overlay 网络等。  

创建一个自定义网络并将容器连接到该网络：  
>```bash
>docker network create my_network
>docker run -d --network my_network ubuntu
>```

Docker Volumes(卷): 一种数据持久化机制，允许数据在容器之间共享。与容器文件系统不同，卷的内容不会随着容器的销毁而丢失，适用于数据库等需要持久存储的应用。  

创建并挂载卷：  
>```bash
>docker volume create my_volume
>docker run -d -v my_volume:/data ubuntu
>```

Docker 的工作流程
1. 构建镜像：使用 Dockerfile 创建镜像。
2. 推送镜像到注册表：将镜像上传到 Docker Hub 或私有注册表中。
3. 拉取镜像：通过 docker pull 从注册表中拉取镜像。
4. 运行容器：使用镜像创建并启动容器。
5. 管理容器：使用 Docker 客户端命令管理正在运行的容器（例如查看日志、停止容器、查看资源使用情况等）。
6. 网络与存储：容器之间通过 Docker 网络连接，数据通过 Docker 卷或绑定挂载进行持久化。

# Docker 安装

## Linux Docker 安装

## Windows Docker 安装
Docker 并非是一个通用的容器工具，它依赖于已存在并运行的 Linux 内核环境。

Docker 实质上是在已经运行的 Linux 下制造了一个隔离的文件环境，因此它执行的效率几乎等同于所部署的 Linux 主机。

因此，Docker 必须部署在 Linux 内核的系统上。如果其他系统想部署 Docker 就必须安装一个虚拟 Linux 环境。

### 虚拟机 安装Linux

### WSL2 安装Linux
https://learn.microsoft.com/zh-cn/windows/wsl/install

### 双系统 安装Linux

## 云服务器 Docker 安装
云服务器(Elastic Compute Service, ECS)是一种简单高效、安全可靠、处理能力可弹性伸缩的计算服务。

云服务器管理方式比物理服务器更简单高效，我们无需提前购买昂贵的硬件，即可迅速创建或删除云服务器，云服务器费用一般在几十到几百不等，可以根据我们的需求配置。

目前市场上的云服务器很多，这里主要介绍以下几家：

- [阿里云](https://www.aliyun.com/minisite/goods?userCode=i5mn5r7m)
- [腾讯云](https://cloud.tencent.com/act/pro/cps_3?fromSource=gwzcw.6688284.6688284.6688284&utm_medium=cps&utm_id=gwzcw.6688284.6688284.6688284&cps_key=822991d9cc1eddb9c45d4c9d51e8cc65&s_refer=https%3A%2F%2Fwww.runoob.com%2F)
- [京东云](https://www.jdcloud.com/cn/pages/yunhuigousale?utm_source=cpscf&type=1&channelReferrer=3368643326214660&channelCode=JD_YTKCPS)
- [华为云](https://activity.huaweicloud.com/1111_promotion/index.html?fromacct=25d108d4-60d1-4baf-b5b1-d6dcb1f9e6f5&utm_source=dGlhbnFpeGlu=&utm_medium=cps&utm_campaign=201905)

注意：很多云服务器给新用户提供的优惠力度是最大，基本上都是 1～2 折，建议新注册的用户购买。

## Docker 镜像源
国内从 DockerHub 拉取镜像有时会遇到困难，此时可以配置镜像加速器。

Docker 官方和国内很多云服务商都提供了国内加速器服务，例如：

<!-- - 科大镜像：https://docker.mirrors.ustc.edu.cn/
- 网易：https://hub-mirror.c.163.com/
- 阿里云：https://<你的ID>.mirror.aliyuncs.com
- 七牛云加速器：https://reg-mirror.qiniu.com 
目前国内 Docker 镜像源出现了一些问题，基本不能用了，后期再更新。-->

当配置某一个加速器地址之后，若发现拉取不到镜像，请切换到另一个加速器地址。

国内各大云服务商均提供了 Docker 镜像加速服务，建议根据运行 Docker 的云平台选择对应的镜像加速服务。

阿里云镜像获取地址：https://cr.console.aliyun.com/cn-hangzhou/instances/mirrors 登陆后，左侧菜单选中镜像加速器就可以看到你的专属地址了：

![image.png](https://www.runoob.com/wp-content/uploads/2019/10/02F3AF04-8203-4E3B-A5AF-96973DBE515F.jpg)

### Windows 10
在系统右下角托盘 Docker 图标内右键菜单选择 Settings，打开配置窗口后左侧导航菜单选择 Daemon。

在 Registrymirrors 一栏中填写加速器地址 https://docker.mirrors.ustc.edu.cn/  ，之后点击 Apply 保存后 Docker 就会重启并应用配置的镜像地址了。

![image.png](https://www.runoob.com/wp-content/uploads/2019/10/38507F68-E30F-4CCA-AE9D-9E9EEF60EC83.jpg)

检查加速器是否生效

效配置加速器之后，如果拉取镜像仍然十分缓慢，请手动检查加速器配置是否生效，在命令行执行 docker info，如果从结果中看到了如下内容，说明配置成功。
>```bash
>$ docker info
>Registry Mirrors:
>    https://reg-mirror.qiniu.com

# Docker 客户端

Docker 客户端是与Docker Daemon交互的命令行工具。

可以直接输入 `docker` 命令来查看到 Docker 客户端的所有命令选项。
>```bash
>$ docker
>```

可以通过命令 `docker command --help` 更深入的了解指定的 Docker 命令使用方法。

例如我们要查看 docker stats 指令的具体使用方法：
>```bash
>$ docker stats --help
>```

## 常用的 Docker 客户端命令:

| 命令 | 功能 | 示例 |
| ---- | ---- | ---- |
| docker run | 启动一个新的容器并运行命令 | docker run -d ubuntu |
| docker ps | 列出当前正在运行的容器 | docker ps |
| docker ps -a | 列出所有容器（包括已停止的容器） | docker ps -a |
| docker build | 使用 Dockerfile 构建镜像 | docker build -t my-image . |
| docker images | 列出本地存储的所有镜像 | docker images |
| docker pull | 从 Docker 仓库拉取镜像 | docker pull ubuntu |
| docker push | 将镜像推送到 Docker 仓库 | docker push my-image |
| docker exec | 在运行的容器中执行命令 | docker exec -it container_name bash |
| docker stop | 停止一个或多个容器 | docker stop container_name |
| docker start | 启动已停止的容器 | docker start container_name |
| docker restart | 重启一个容器 | docker restart container_name |
| docker rm | 删除一个或多个容器 | docker rm container_name |
| docker rmi | 删除一个或多个镜像 | docker rmi my-image |
| docker logs | 查看容器的日志 | docker logs container_name |
| docker inspect | 获取容器或镜像的详细信息 | docker inspect container_name |
| docker exec -it | 进入容器的交互式终端 | docker exec -it container_name /bin/bash |
| docker network ls | 列出所有 Docker 网络 | docker network ls |
| docker volume ls | 列出所有 Docker 卷 | docker volume ls |
| docker-compose up | 启动多容器应用（从 docker-compose.yml 文件） | docker-compose up |
| docker-compose down | 停止并删除由 docker-compose 启动的容器、网络等 | docker-compose down |
| docker info | 显示 Docker 系统的详细信息 | docker info |
| docker version | 显示 Docker 客户端和守护进程的版本信息 | docker version |
| docker stats | 显示容器的实时资源使用情况 | docker stats |
| docker login | 登录 Docker 仓库 | docker login |
| docker logout | 登出 Docker 仓库 | docker logout |

常用选项说明
| 选项 | 说明 | 示例 |
| ---- | ---- | ---- |
| -d | 后台运行容器 | docker run -d ubuntu |
| -it | 以交互式终端运行容器 | docker exec -it container_name bash |
| -t | 为镜像指定标签 | docker build -t my-image . |

# Docker 容器
![image.png](https://www.runoob.com/wp-content/uploads/2016/05/0_Uw0RmvCbgHBkZfi1.png)

## 1. 获取镜像 docker pull 
如果我们本地没有 ubuntu 镜像，我们可以使用 `docker pull` 命令来载入 ubuntu 镜像：  
>```bash
>$ docker pull ubuntu
>```

## 2. 启动容器 docker run
以下命令使用 ubuntu 镜像启动一个容器，参数为以命令行模式进入该容器：  
>```bash
>$ docker run -it ubuntu /bin/bash
># 或
>$ docker run -i -t ubuntu /bin/bash
># 后台运行
>$ docker run -d ubuntu /bin/bash
># 注：加了 -d 参数默认不会进入容器，想要进入容器需要使用指令 docker exec
>```
参数说明：

-i: 交互式操作。  
-t: 终端。  
-d: 后台运行容器。  
ubuntu: ubuntu 镜像。  
/bin/bash：放在镜像名后的是命令，这里我们希望有个交互式 Shell，因此用的是 /bin/bash。  
要退出终端，直接输入 `exit`。  

## 3. 停止容器 docker stop
查看所有的容器：
>```bash
>$ docker ps -a
>```
停止容器：  
>```bash
>$ docker stop 容器id
>```

## 4. 启动已停止的容器 docker start
容器之前通过 docker stop 或正常退出后，需要重新启动  
>```bash
>$ docker start 容器id
>```

## 5. 重启容器 docker restart    
重启一个正在运行或已停止的容器  
>```bash
>$ docker restart 容器id 
>```

## 6. 进入容器 docker attach
在使用 -d 参数时启动容器时，容器会运行在后台，这时如果要进入容器，可以通过以下命令进入：  

- `docker attach`：允许你与容器的标准输入（stdin）、输出（stdout）和标准错误（stderr）进行交互。  

- `docker exec`：推荐大家使用 docker exec 命令，因为此命令会退出容器终端，但不会导致容器的停止。  
>```bash
>$ docker attach 容器id
># 注意： 如果从这个容器退出，会导致容器停止。
>$ docker exec -it 容器id /bin/bash
># 注意： 如果从这个容器退出，容器不会停止。
># 更多参数说明请使用 docker exec --help 命令查看。
>```

## 7. 导出容器 docker export
如果要导出本地某个容器，可以使用 `docker export` 命令。
>```bash
>$ docker export 1e560fca3906 > ubuntu.tar
># 导出容器 1e560fca3906 快照到本地文件 ubuntu.tar
>```

## 8.导入容器快照 docker import
可以使用 `docker import` 从容器快照文件中再导入为镜像，以下实例将快照文件 ubuntu.tar 导入到镜像 test/ubuntu:v1:
>```bash
>$ cat docker/ubuntu.tar | docker import - test/ubuntu:v1
>```
此外，也可以通过指定 URL 或者某个目录来导入，例如：
>```bash
>$ docker import http://example.com/exampleimage.tgz example/imagerepo
>```

## 9. 删除容器 docker rm
删除一个容器，可以使用 `docker rm` 命令。
>```bash
>$ docker rm 容器id
>```
删除已停止的容器，可以使用 `-f` 参数：  
>```bash
>$ docker rm -f 容器id
>```
清理掉所有处于终止状态的容器。
>```bash
>$ docker container prune
>```



## WEB 应用容器
### 创建一个web应用
接下来让我们尝试使用 docker 构建一个 web 应用程序。

我们将在docker容器中运行一个 Python Flask 应用来运行一个web应用。

>```bash
>docker pull training/webapp  # 载入镜像
>docker run -d -P training/webapp python app.py
>```
- python app.py:覆盖镜像的默认启动命令，指定容器启动时运行 python app.py
- -P:将容器内部使用的网络端口随机映射到我们的主机上。

运行成功后，我们可以通过 docker ps 命令查看容器的运行状态。
>```bash
>docker ps
>CONTAINER ID        IMAGE               COMMAND             ...        PORTS                 
>d3d5e39ed9d3        training/webapp     "python app.py"     ...        0.0.0.0:32769->5000/tcp
>```
Docker 开放了 5000 端口（默认 Python Flask 端口）映射到主机端口 32769 上。

我们可以通过浏览器访问WEB应用：
>```bash
>http://localhost:32769
>```
访问成功后，可以看到如下页面：  
![image.png](https://www.runoob.com/wp-content/uploads/2016/05/docker31.png)

也可以通过 -p 参数明确指定端口:
>```bash
>docker run -d -p 5000:5000 training/webapp python app.py
>```

使用 docker port 可以查看指定 （ID 或者名字）容器的某个确定端口映射到宿主机的端口号。
>```bash
>docker port <container_id> 
># 或
>docker port <container_name> 
># 结果
>5000/tcp -> 0.0.0.0:5000
>```

### 查看 WEB 应用程序日志
`docker logs [ID或者名字]`
>```bash
>$ docker logs -f bf08b7f2cd89
> * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
>192.168.239.1 - - [09/May/2016 16:30:37] "GET / HTTP/1.1" 200 -
>192.168.239.1 - - [09/May/2016 16:30:37] "GET /favicon.ico HTTP/1.1" 404 -
>```
从上面，我们可以看到应用程序使用的是 5000 端口并且能够查看到应用程序的访问日志。

### 查看WEB应用程序容器的进程
`docker top [ID或者名字]`
>```bash
>$ docker top bf08b7f2cd89
>UID                 PID                 PPID                C                   STIME               TTY                 TIME                CMD
>root                1580                1535                0                   08:30               ?                   00:00:00            python app.py
>```

### 检查 WEB 应用程序
`docker inspect [ID或者名字]`

### 停止 WEB 容器
`docker stop [ID或者名字]`

### 启动/重启 WEB 容器
`docker start [ID或者名字]`  
`docker restart [ID或者名字]`

### 删除 WEB 容器
`docker rm [ID或者名字]`  
删除容器时，容器必须是停止状态。  
`docker rm -f [ID或者名字]`  
强制删除容器时，容器可以运行。  




# Docker 镜像
当运行容器时，使用的镜像如果在本地中不存在，docker 就会自动从 docker 镜像仓库中下载，默认是从 Docker Hub 公共镜像源下载。

## 列出镜像列表 docker images
>```bash
>$ docker images           
>REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
>ubuntu              14.04               90d5884b1ee0        5 days ago          188 MB
>php                 5.6                 f40e9e0f10c8        9 days ago          444.8 MB
>nginx               latest              6f8d099c3adc        12 days ago         182.7 MB
>mysql               5.6                 f2e8d6c772c0        3 weeks ago         324.6 MB
>httpd               latest              02ef73cf1bc0        3 weeks ago         194.4 MB
>ubuntu              15.10               4e3b13c8a266        4 weeks ago         136.3 MB
>hello-world         latest              690ed74de00f        6 months ago        960 B
>training/webapp     latest              6fae60ef3446        11 months ago       348.8 MB
>```
REPOSITORY：表示镜像的仓库源

同一仓库源可以有多个 TAG，代表这个仓库源的不同个版本，如 ubuntu 仓库源里，有 15.10、14.04 等多个不同的版本，我们使用 REPOSITORY:TAG 来定义不同的镜像。

例如要使用版本为15.10的ubuntu系统镜像来运行容器时，命令如下：
>```bash
>$ docker run -t -i ubuntu:15.10 /bin/bash 
># 只使用 ubuntu，docker 将默认使用 ubuntu:latest 镜像。
>```

## 拉取镜像 docker pull

## 查找镜像 docker search
我们可以从 Docker Hub 网站来搜索镜像，Docker Hub 网址为： https://hub.docker.com/

我们也可以使用 `docker search` 命令来搜索镜像。比如我们需要一个 httpd 的镜像来作为我们的 web 服务
>```bash
>docker search httpd
>```
![image.png](https://www.runoob.com/wp-content/uploads/2016/05/423F2A2C-287A-4B03-855E-6A78E125B346.jpg)

- NAME: 镜像仓库源的名称
- DESCRIPTION: 镜像的描述
- OFFICIAL: 是否 docker 官方发布
- STARS:表示点赞、喜欢的意思。
- AUTOMATED: 自动构建。

## 删除镜像 docker rmi

## 创建镜像 docker commmit
`docker commit`从已经创建的容器中更新镜像，并且提交这个镜像
>```bash
>$ docker commit -m "update" -a "yourname" 5a0c7b4d5a0c myapp:v2
>$ docker images
>REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
>myapp               v2                  5a0c7b4d5a0c        7 minutes ago       348.8 MB
>```
`-m`参数指定镜像的描述，`-a`参数指定镜像的作者。`5a0c7b4d5a0c`是容器的ID，`myapp:v2`是镜像名称和标签。

## 创建镜像 docker build
`docker build` 命令用于创建镜像。为此，我们需要创建一个 Dockerfile 文件，其中包含一组指令来告诉 Docker 如何构建我们的镜像。
- -t：指定镜像的名称和标签。
- -f：指定 Dockerfile 文件的位置。
- .：指定 Dockerfile 文件所在目录。

创建一个 Dockerfile 文件，内容如下：
>```bash
>$ cat Dockerfile
>FROM ubuntu:15.10
>RUN apt-get update
>RUN apt-get install -y nginx
>EXPOSE 80
>CMD ["nginx"]
>```
每一个指令都会在镜像上创建一个新的层，每一个指令的前缀都必须是大写的。

FROM 指定使用哪个镜像源

RUN 指令告诉docker 在镜像内执行命令，安装了什么。

EXPOSE，指定nginx的端口号

CMD，指定nginx的启动命令

然后，我们使用 Dockerfile 文件，通过 docker build 命令来构建一个镜像。
>```bash
>$ docker build -t mynginx .
>```
镜像构建完成后，我们可以使用 `docker images` 命令查看镜像。

## 设置镜像标签 docker tag
>```bash
>$ docker tag mynginx mynginx:v1
>$ docker images
>REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
>mynginx             v1                  5a0c7b4d5a0c        7 minutes ago       348.8 MB
>mynginx             latest              5a0c7b4d5a0c        7 minutes ago       348.8 MB
>```

# Docker 容器连接
前面实现了通过网络端口来访问运行在 docker 容器内的服务。

容器中可以运行一些网络应用，要让外部也可以访问这些应用，可以通过 -P 或 -p 参数来指定端口映射。

>```bash
>$ docker run -d -P training/webapp python app.py
>$ docker ps
>CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS                     NAMES
>fce072cc88ce        training/webapp     "python app.py"     7 seconds ago       Up 6 seconds        0.0.0.0:49153->5000/tcp   naughty_poitras
>```
- -P：是容器内部端口随机映射到主机的端口。
- -p：是容器内部端口绑定到指定的主机端口。
>```bash
>$ docker run -d -p 5000:5000 training/webapp python app.py
>$ docker ps
>CONTAINER ID        IMAGE               COMMAND           ...           PORTS                     NAMES
>33e4523d30aa        training/webapp     "python app.py"   ...   0.0.0.0:5000->5000/tcp    berserk_bartik
>fce072cc88ce        training/webapp     "python app.py"   ...   0.0.0.0:32768->5000/tcp   grave_hopper
>```
可以指定容器绑定的网络地址，比如绑定 127.0.0.1
>```bash
>$ docker run -d -p 127.0.0.1:5001:5000 training/webapp python app.py
>$ docker ps
>CONTAINER ID        IMAGE               COMMAND           ...     PORTS                                NAMES
>95c6ceef88ca        training/webapp     "python app.py"   ...  5000/tcp, 127.0.0.1:5001->5000/tcp   adoring_stonebraker
>33e4523d30aa        training/webapp     "python app.py"   ...  0.0.0.0:5000->5000/tcp               berserk_bartik
>fce072cc88ce        training/webapp     "python app.py"   ...    0.0.0.0:32768->5000/tcp              grave_hopper
>```
默认都是绑定 tcp 端口，如果要绑定 UDP 端口，可以在端口后面加上 /udp
>```bash
>$ docker run -d -p 127.0.0.1:5001:5000/udp training/webapp python app.py
>$ docker ps
>CONTAINER ID        IMAGE               COMMAND           ...     PORTS                                NAMES
>95c6ceef88ca        training/webapp     "python app.py"   ...  5000/tcp, 5000/udp, 127.0.0.1:5001->5000/tcp
>```
## 查看端口 docker port
>```bash
>$ docker port adoring_stonebraker 5000
>127.0.0.1:5001
>```

## Docker 容器互联
端口映射并不是唯一把 docker 连接到另一个容器的方法。

docker 有一个连接系统允许将多个容器连接在一起，共享连接信息。

docker 连接会创建一个父子关系，其中父容器可以看到子容器的信息。


>```bash
># 先创建一个新的 Docker 网络,并列出所有网络：
># -d：参数指定 Docker 网络类型，有 bridge、overlay。
>$ docker network create -d bridge test-net
>$ docker network ls
>
># 运行一个容器并连接到新建的 test-net 网络:
>$ docker run -itd --name test1 --network test-net ubuntu /bin/bash
>
># 打开新的终端，再运行一个容器并加入到 test-net 网络:
>$ docker run -itd --name test2 --network test-net ubuntu /bin/bash
>
>$ docker ps
>CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
>0c0f0c5c0c0f        ubuntu             "/bin/bash"         2 seconds ago       Up 1 second                             test2
>9c0f0c5c0c0f        ubuntu             "/bin/bash"         2 seconds ago       Up 1 second                             test1 
>
># 下面通过 ping 来证明 test1 容器和 test2 容器建立了互联关系。
># 如果 test1、test2 容器内中无 ping 命令，则在容器内执行以下命令安装 ping（可以在一个容器里安装好，提交容器到镜像，在以新的镜像重新运行以上俩个容器）。
>$ apt-get update
>$ apt install iputils-ping
>
>$ docker exec -it test1 /bin/bash
># 在 test1 容器输入以下命令：
>$ ping test2
>```
如果你有多个容器之间需要互相连接，推荐使用 Docker Compose，后面会介绍。

## 配置 DNS
在宿主机的 /etc/docker/daemon.json 文件中增加以下内容来设置全部容器的 DNS：
>```json
>{
>  "dns" : [
>    "114.114.114.114",
>    "8.8.8.8"
>  ]
>}
>```
设置后，启动容器的 DNS 会自动配置为 114.114.114.114 和 8.8.8.8。

配置完，需要重启 docker 才能生效。

查看容器的 DNS 是否生效可以使用以下命令，它会输出容器的 DNS 信息：
>```bash
>$ docker run -it --rm  ubuntu  cat etc/resolv.conf
>nameserver 114.114.114.114
>nameserver 8.8.8.8
>```
如果只想在指定的容器设置 DNS，则可以使用以下命令：
>```bash
>$ docker run -it --rm -h host_ubuntu  --dns=114.114.114.114 --dns-search=test.com ubuntu
># --rm：容器退出时自动清理容器内部的文件系统。
># -h HOSTNAME 或者 --hostname=HOSTNAME： 设定容器的主机名，它会被写到容器内的 /etc/hostname 和 /etc/hosts。
># --dns=IP_ADDRESS： 添加 DNS 服务器到容器的 /etc/resolv.conf 中，让容器用这个服务器来解析所有不在 /etc/hosts 中的主机名。
># --dns-search=DOMAIN： 设定容器的搜索域，当设定搜索域为 .example.com 时，在搜索一个名为 host 的主机时，DNS 不仅搜索 host，还会搜索 host.example.com。
>```
如果在容器启动时没有指定 --dns 和 --dns-search，Docker 会默认用宿主主机上的 /etc/resolv.conf 来配置容器的 DNS。

## 解决windows系统无法对docker容器进行端口映射的问题
在Windows中运行docker，实际上还是在Windows下先安装了一个Linux环境，然后在这个系统中运行的docker。也就是说，服务中使用的localhost指的是这个Linux环境的地址，而不是我们的宿主环境Windows。

通过命令:
>```bash
>docker-machine ip default   
># 其中，default 是docker-machine的name，可以通过docker-machine -ls 查看找到这个Linux的ip地址，
># 一般情况下这个地址是192.168.99.100，然后在Windows的浏览器中，输入这个地址，加上服务的端口即可启用了。
>```
比如，首先运行一个docker 容器：
>```bash
>docker run -it -p 8888:8888 conda:v1
># 其中，conda:v1是我的容器名称。然后在容器中开启jupyter notebook 服务：
>jupyter notebook --no-browser --port=8888 --ip=172.17.0.2 --allow-root
># 其中的ip参数为我的容器的ip地址，可以通过如下命令获得：
>docker inspect container_id
># 最后在windows浏览器中测试结果：
>http://192.168.99.100:8888
>```

# Docker 仓库管理
Docker 官方维护了一个公共仓库 [Docker Hub](https://hub.docker.com/)。

免费注册一个 Docker 账号登录就可以从 docker hub 上拉取自己账号下的全部镜像。
>```bash
>$ docker login
>Username: <username>
>Password: <password>
>Login Succeeded
>
>$ docker search ubuntu # 以 ubuntu 为关键词搜索镜像
>$ docker pull ubuntu
>
>$ docker tag ubuntu:18.04 username/ubuntu:18.04 # username 请替换为你的 Docker 账号用户名
>$ docker image ls
>
>REPOSITORY      TAG        IMAGE ID            CREATED           ...  
>ubuntu          18.04      275d79972a86        6 days ago        ...  
>username/ubuntu 18.04      275d79972a86        6 days ago        ...  
>$ docker push username/ubuntu:18.04 # 推送镜像
>$ docker search username/ubuntu
>
>NAME             DESCRIPTION       STARS         OFFICIAL    AUTOMATED
>username/ubuntu
>
>$ docker logout # 注销
>```

# Docker Dockerfile
Dockerfile 是一个文本文件，包含了构建 Docker 镜像的所有指令

下面以定制一个 nginx 镜像为例（构建好的镜像内会有一个 /usr/share/nginx/html/index.html 文件）

在一个空目录下，新建一个名为 Dockerfile 文件，并在文件内添加以下内容：
>```bash
>$ mkdir Dockerfile
>$ cd Dockerfile/
>$ vim Dockerfile
>$ cat Dockerfile
>FROM nginx
># FROM：定制的镜像都是基于 FROM 的镜像，这里的 nginx 就是定制需要的基础镜像。后续的操作都是基于 nginx。
>RUN echo '这是一个本地构建的nginx镜像' > /usr/share/nginx/html/index.html
># RUN：用于执行后面跟着的命令行命令。有以下俩种格式：1. RUN <命令> 2. RUN [<可执行文件>, <参数1>, <参数2>...]
># 例如：RUN ["./test.php", "dev", "offline"] 等价于 RUN ./test.php dev offline
>```
注意：Dockerfile 的指令每执行一次都会在 docker 上新建一层。所以过多无意义的层，会造成镜像膨胀过大。
例如：
>```bash
>FROM centos
>RUN yum -y install wget
>RUN wget -O redis.tar.gz "http://download.redis.io/releases/redis-5.0.3.tar.gz"
>RUN tar -xvf redis.tar.gz
>```
以上执行会创建 3 层镜像。可简化为以下格式：
>```bash
>FROM centos
>RUN yum -y install wget \
>    && wget -O redis.tar.gz "http://download.redis.io/releases/redis-5.0.3.tar.gz" \
>    && tar -xvf redis.tar.gz
>```
在 Dockerfile 文件的存放目录下，执行构建动作。

以下示例，通过目录下的 Dockerfile 构建一个 nginx:v3（镜像名称:镜像标签）。
>```bash
>$ docker build -t nginx:v3 .
>Sending build context to Docker daemon
>Step 1/3 : FROM nginx
>---> 9e05c5c0c0c1
>Step 2/3 : RUN echo '这是一个本地构建的nginx镜像' > /usr/share/nginx/html/index.html
>---> Running in 0c0d0c0d0c0d
>Removing intermediate container 0c0c0c0c0c0c
>---> 0c0c0c0c0c0c
>Successfully built 0c0c0c0c0c0c
>Successfully tagged nginx:v3
>
># 镜像构建成功后，可以通过 docker images 命令查看镜像列表。
>$ docker images
>REPOSITORY   TAG       IMAGE ID       CREATED         SIZE
>nginx        v3        0c0c0c0c0c0c   2 minutes ago   109MB
>```

指令最后一个` . `是上下文路径的结束符。

上下文路径，是指 docker 在构建镜像，有时候想要使用到本机的文件（比如复制），docker build 命令得知这个路径后，会将路径下的所有内容打包。

解析：

由于 docker 的运行模式是 C/S。我们本机是 C，docker 引擎是 S。

实际的构建过程是在 docker 引擎下完成的，所以这个时候无法用到我们本机的文件。这就需要把我们本机的指定目录下的文件一起打包提供给 docker 引擎使用。

如果未说明最后一个参数，那么默认上下文路径就是 Dockerfile 所在的位置。

注意：上下文路径下不要放无用的文件，因为会一起打包发送给 docker 引擎，如果文件过多会造成过程缓慢。

## 指令详解
|指令|	描述|
|---|---|
|FROM|	指定基础镜像，用于后续的指令构建|
|RUN|	执行命令，并生成镜像|
|CMD|	指定容器启动时运行的命令|
|LABEL|	为镜像添加标签|
|EXPOSE|	指定容器的端口号|
|ADD|	将文件或目录添加到镜像中|
|COPY|	将文件或目录添加到镜像中|
|ENTRYPOINT|	指定容器启动时运行的命令|
|VOLUME|	创建一个挂载点，用于数据卷的挂载|
|WORKDIR|	设置工作目录|
|ENV|	设置环境变量|
|USER|	指定用户|
|ARG|	定义构建参数|
|ONBUILD|	在FROM指令之后，指定当镜像被用作其他镜像的基镜像时，会自动执行的指令|
|STOPSIGNAL|	指定容器停止的信号|
|HEALTHCHECK|	指定容器健康检查的指令|
|SHELL|	指定Shell

# Docker Compose
Compose 是用于定义和运行多容器 Docker 应用程序的工具。

通过 Compose 可以使用 YML 文件来配置应用程序需要的所有服务。

然后，使用一个命令，就可以从 YML 文件配置中创建并启动所有服务。

Compose 使用的三个步骤：
1. 使用 Dockerfile 定义应用程序的环境。
2. 使用 docker-compose.yml 定义构成应用程序的服务，这样它们可以在隔离环境中一起运行。
3. 最后，执行 docker-compose up 命令来启动并运行整个应用程序。

docker-compose.yml
>```yml
># yaml 配置实例
>version: '3'
>services:
>  web:
>    build: .
>    ports:
>    - "5000:5000"
>    volumes:
>    - .:/code
>    - logvolume01:/var/log
>    links:
>    - redis
>  redis:
>    image: redis
>volumes:
>  logvolume01: {}
>```

## Compose 安装

## Compose 使用
...

## yml 配置指令参考
...

# Swarm 集群管理
Docker Swarm 是 Docker 的集群管理工具。它将 Docker 主机池转变为单个虚拟 Docker 主机。

Docker Swarm 提供了标准的 Docker API，所有任何已经与 Docker 守护程序通信的工具都可以使用 Swarm 轻松地扩展到多个主机。

如下图所示，swarm 集群由管理节点（manager）和工作节点（work node）构成。
- swarm mananger：负责整个集群的管理工作包括集群配置、服务管理等所有跟集群有关的工作。
- work node：即图中的 available node，主要负责运行相应的服务来执行任务（task）。
![alt text](https://www.runoob.com/wp-content/uploads/2019/11/services-diagram.png)

## Swarm 使用
...

# Docker 实例
可参考 ROS/

# ...

## Docker run

`docker run -d --name my-redis -p 6379:6379 redis`  
参数解释：    
-d ：后台运行  
--name ：指定容器名称  
-p ：端口映射  
-i ：交互式运行  
-t ：分配一个伪输入终端  


>```bash
>$ docker run -i -t ubuntu:15.10 /bin/bash
>root@0123ce188bd8:/#
>```
docker: Docker 的二进制执行文件。
run: 与前面的 docker 组合来运行一个容器。
ubuntu:15.10 指定要运行的镜像，Docker 首先从本地主机上查找镜像是否存在，如果不存在，Docker 就会从镜像仓库 Docker Hub 下载公共镜像。
/bin/bash: 在启动的容器里执行的命令
第二行 root@0123ce188bd8:/#，此时我们已进入一个 ubuntu15.10 系统的容器

通过运行 exit 命令或者使用 CTRL+D 来退出容器。

root@0123ce188bd8:/#  exit
exit
root@runoob:~#

第三行中 root@runoob:~# 表明我们已经退出了当前的容器，返回到当前的主机中。

启动容器（后台模式）
使用以下命令创建一个以进程方式运行的容器

runoob@runoob:~$ docker run -d ubuntu:15.10 /bin/sh -c "while true; do echo hello world; sleep 1; done"
2b1b7a428627c51ab8810d541d759f072b4fc75487eed05812646b8534a2fe63
在输出中，我们没有看到期望的 "hello world"，而是一串长字符

2b1b7a428627c51ab8810d541d759f072b4fc75487eed05812646b8534a2fe63

这个长字符串叫做容器 ID，对每个容器来说都是唯一的，我们可以通过容器 ID 来查看对应的容器发生了什么。

首先，我们需要确认容器有在运行，可以通过 docker ps 来查看：

runoob@runoob:~$ docker ps
CONTAINER ID        IMAGE                  COMMAND              ...  
5917eac21c36        ubuntu:15.10           "/bin/sh -c 'while t…"    ...
输出详情介绍：

CONTAINER ID: 容器 ID。

IMAGE: 使用的镜像。

COMMAND: 启动容器时运行的命令。

CREATED: 容器的创建时间。

STATUS: 容器状态。

状态有7种：

created（已创建）
restarting（重启中）
running 或 Up（运行中）
removing（迁移中）
paused（暂停）
exited（停止）
dead（死亡）
PORTS: 容器的端口信息和使用的连接类型（tcp\udp）。

NAMES: 自动分配的容器名称。

在宿主主机内使用 docker logs 命令，查看容器内的标准输出：

runoob@runoob:~$ docker logs 2b1b7a428627


runoob@runoob:~$ docker logs amazing_cori


停止容器
我们使用 docker stop 命令来停止容器:



通过 docker ps 查看，容器已经停止工作:

runoob@runoob:~$ docker ps
可以看到容器已经不在了。

也可以用下面的命令来停止:

runoob@runoob:~$ docker stop amazing_cori
