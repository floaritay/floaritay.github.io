# 目录

- [1 Jupyter Notebook](#1-jupyter-notebook)
  - [1.1 .ipynb文件](#11-ipynb文件)
  - [1.2 架构](#12-架构)
  - [1.3 文件转换与可视化](#13-文件转换与可视化)
  - [1.4 生态](#14-生态)
- [2 安装](#2-安装)
- [3 VS Code 中使用 Jupyter Notebook](#3-vs-code-中使用-jupyter-notebook)
  - [3.1 单元格运行与管理](#31-单元格运行与管理)
  - [3.2 导出](#32-导出)
  - [3.3 调试](#33-调试)
  - [3.4 远程连接](#34-远程连接)
  - [3.5 差异比对](#35-差异比对)
- [4 操作模式](#4-操作模式)
- [5 快捷键](#5-快捷键)
  - [5.1 运行 Cell 的快捷键（通用）](#51-运行-cell-的快捷键通用)
  - [5.2 命令模式快捷键（蓝色边框）](#52-命令模式快捷键蓝色边框)
  - [5.3 编辑模式快捷键（绿色边框）](#53-编辑模式快捷键绿色边框)
- [6 魔法命令](#6-魔法命令)
- [7 tqdm](#7-tqdm)
- [8 高级技巧](#8-高级技巧)
- [9 jupyter-Book](#9-jupyter-book)
  - [9.1 安装](#91-安装)
  - [9.2 管理文件与目录 (_toc.yml)：](#92-管理文件与目录-_tocyml)
  - [9.3 基本配置 (_config.yml)：](#93-基本配置-_configyml)
  - [9.4 本地构建与预览](#94-本地构建与预览)
  - [9.5 设置 GitHub Actions 自动部署（推荐）：](#95-设置-github-actions-自动部署推荐)

---
# 1 Jupyter Notebook
一个开源的 Web 应用程序，允许我们创建和分享包含实时代码、数学方程、可视化图表和解释性文本的文档。

Jupyter 的名字来源于它所支持的三种核心语言：Julia、Python 和 R。

Jupyter 是从 IPython Notebook 进化而来的，早期仅支持 Python，后来扩展为多语言工具，但保留了原有的文件格式 .ipynb

特点：
- 交互性：可以尝试不同的代码片段，并立即查看结果。
- 文学化编程：代码、注释、图表和解释可以完美地结合在一起，是制作教程或自学笔记的理想工具。
- 可重复研究：整个分析过程（代码、数据、结果）都被保存在一个文件中，其他人可以完整地复现你的工作。
- 快速原型设计：你可以快速搭建想法，并分段测试代码，无需运行整个脚本。

## 1.1 .ipynb文件
其实是一段结构化的 JSON 文本。意味着它具有极强的可移植性。你可以轻松地在 GitHub 上分享它，或者将其转换成 PDF、HTML。

它需要一个渲染引擎（如 Jupyter Notebook 软件、VS Code 插件或 GitHub 预览器）来将其转化为我们熟悉的交互界面。

## 1.2 架构
核心是一个交互式计算模型。它基于浏览器提供 REPL（读取-求值-输出循环），其底层由以下硬核技术支撑：

- 核心组件： 结合了 IPython（增强型交互式 Python）、ØMQ（高效消息队列）和 Tornado（高性能 Web 服务器）。
- 多语言支持 (Kernels)： 什么是内核？内核是负责执行代码、补全及检查的独立程序。
- 解耦设计： 内核并不依赖于特定的文档，它可以运行在本地，也可以部署在远程服务器上。
- 全能扩展： 目前支持包括 Python、R、Julia、Haskell 在内的 100 多种 编程语言（其名字 Ju-Py-Ter 正是取自 Julia, Python 和 R）。

## 1.3 文件转换与可视化
- nbconvert (导出)： 将 Notebook 转换为 PDF、HTML、Markdown、甚至幻灯片（Reveal.js）和 LaTeX。
- nbviewer (在线预览)： 这是一个基于 Web 的服务，只要你给它一个公开的 Notebook URL，它就能将其动态渲染为精美的网页，无需接收方安装任何软件。

## 1.4 生态
| 阶段/工具 | 定位与特点 | 适用场景 |
| --- | --- | --- |
| Jupyter Notebook | 经典单机版，简单的单元格交互。 | 个人笔记、快速原型、教学演示。 |
| JupyterLab | 下一代 UI。集成了终端、文件浏览器、文本编辑器，支持多窗口布局。 | 生产级开发、多任务数据科学工作流。 |
| JupyterHub | 多用户管理平台。支持生成和管理多个独立的 Notebook 环境。 | 企业团队协作、高校课程实验平台。 |


# 2 安装
前提是你的电脑上已经安装了 Python 和包管理工具 pip

打开你的命令行工具：
```bash
python --version
# 或
python3 --version

pip --version
# 或
pip3 --version

# 安装
pip install jupyter
# 验证
jupyter --version
```
也可以使用conda安装

# 3 VS Code 中使用 Jupyter Notebook

打开 VS Code，点击左侧活动栏的 Extensions（扩展） 图标（快捷键 Ctrl+Shift+X），搜索并安装 "Jupyter" 插件（由 Microsoft 提供），安装此插件会自动安装 Python 扩展。

新建一个以 .ipynb 结尾的文件即可

点击编辑界面右上角的 "Select Kernel"（选择内核）。  

在弹出的列表中，选择你安装好的 Python 版本或 Anaconda 环境（例如 Python 3.x.x 或 base (conda)）。  

如果是第一次运行，VS Code 可能会提示你安装 ipykernel 包，点击"安装"即可。

## 3.1 单元格运行与管理
单块运行：点击单元格左侧的 播放图标 (▶)。

多块运行：使用顶部工具栏的"双箭头"图标 Run All 运行全文；或在特定单元格处选择 Run Above（运行上方所有）或 Run Below（运行下方所有）。

按章节运行：在"大纲 (Outline)"视图中，可以点击章节标题旁的按钮，运行该 Markdown 标题下的整组单元格。

## 3.2 导出
点击工具栏的 ... > Export。支持导出为 .py 脚本、HTML 或 PDF（注：PDF 导出需安装 TeX 环境）。

## 3.3 调试
逐行运行 (Run by Line)：点击单元格工具栏的图标，可不被打扰地单步执行代码。

完全调试：在单元格左侧设置断点，选择 Run 按钮旁的 Debug Cell。

## 3.4 远程连接
若需使用远程服务器的算力：

点击右上角 Kernel Picker（内核选择器）。

选择 Existing Jupyter Server

输入带有 ?token= 的服务器 URL 即可连接。

## 3.5 差异比对
由于 .ipynb 本质是 JSON，VS Code 提供了可视化比对工具。

点击右上角"打开更改"图标

# 4 操作模式

| 模式 | Cell 边框颜色 | 进入方式 | 作用 |
| --- | --- | --- | --- |
| 命令模式 | 蓝色 | 按 Esc 或点击 Cell 左侧空白区 | 对 Cell 进行管理操作（新增、删除、移动等） |
| 编辑模式 | 绿色 | 按 Enter 或双击 Cell 内部 | 在 Cell 内部编写和修改代码或文本 |

# 5 快捷键

## 5.1 运行 Cell 的快捷键（通用）
以下三个快捷键在两种模式下均可使用，是高频操作：

| 快捷键 | 作用 | 适用场景 |
| --- | --- | --- |
| Shift + Enter | 运行当前 Cell，并自动跳转到下一个 Cell | 最常用，依次向下执行代码 |
| Ctrl + Enter | 运行当前 Cell，停留在当前 Cell | 反复测试同一段代码时使用 |
| Alt + Enter | 运行当前 Cell，并在下方插入一个新 Cell | 边运行边向下新增代码块时使用 |


## 5.2 命令模式快捷键（蓝色边框）
按 Esc 进入命令模式后，可使用以下快捷键：

1、Cell 的插入与删除

| 快捷键 | 作用 |
| --- | --- |
| A | 在当前 Cell 上方插入新 Cell（Above） |
| B | 在当前 Cell 下方插入新 Cell（Below） |
| D, D（连按两次 D） | 删除当前 Cell |
| Z | 撤销删除（恢复刚刚删除的 Cell） |
| X | 剪切当前 Cell |
| C | 复制当前 Cell |
| V | 在当前 Cell 下方粘贴 Cell |
| Shift + V | 在当前 Cell 上方粘贴 Cell |

2、Cell 类型切换

Jupyter 中的 Cell 有三种类型，可以随时切换：
| 快捷键 | 切换为 | 用途 |
| --- | --- | --- |
| Y | Code（代码） | 编写并运行 Python 代码 |
| M | Markdown（标记语言） | 编写格式化文档、标题、说明文字 |
| R | Raw（原始文本） | 原样输出文本，不执行也不渲染 |
| 1 ~ 6 | Markdown 标题级别 H1 ~ H6 | 快速将 Cell 设为对应级别的标题（会自动切换到 Markdown 模式） |

3、Cell 的选择与合并

| 快捷键 | 作用 |
| --- | --- |
| ↑ / K | 选中上方的 Cell |
| ↓ / J | 选中下方的 Cell |
| Shift + ↑ / Shift + K | 向上连续选中多个 Cell |
| Shift + ↓ / Shift + J | 向下连续选中多个 Cell |
| Shift + M | 将选中的多个 Cell 合并为一个 |

4、输出与显示控制

| 快捷键 | 作用 |
| --- | --- |
| O | 折叠/展开当前 Cell 的输出结果 |
| Shift + O | 切换当前 Cell 输出区域的滚动模式（输出内容很长时使用） |
| L | 显示/隐藏当前 Cell 的行号 |
| F | 在 Cell 中查找和替换文本 |

5、内核与界面操作
| 快捷键 | 作用 |
| --- | --- |
| I, I（连按两次 I） | 中断当前正在运行的 Cell（相当于 Ctrl+C） |
| 0, 0（连按两次 0） | 重启内核（会清空所有已运行的变量，谨慎使用） |
| H | 打开快捷键帮助面板（显示所有可用快捷键） |
| P | 打开命令面板，可以搜索所有 Jupyter 功能 |
| Space | 向下滚动页面 |
| Shift + Space | 向上滚动页面 |
| S / Ctrl + S | 保存 Notebook |

## 5.3 编辑模式快捷键（绿色边框）
按 Enter 进入编辑模式后，可使用以下快捷键在 Cell 内部操作：

1、代码编辑

| 快捷键 | 作用 |
| --- | --- |
| Tab | 代码自动补全（输入部分函数名/变量名后按 Tab 补全） |
| Shift + Tab | 查看光标所在函数的参数说明（弹出文档提示，按一次显示简要，连按两次显示完整文档） |
| Ctrl + / | 注释/取消注释当前行或选中的多行代码 |
| Ctrl + D | 删除当前整行 |
| Ctrl + Shift + - | 在光标处将当前 Cell 拆分为两个 Cell |
| Ctrl + Z | 撤销（恢复上一步编辑） |
| Ctrl + Y | 重做（取消撤销） |
| Ctrl + A | 全选当前 Cell 内的所有内容 |
| Ctrl + Home | 跳转到 Cell 内容的最开头 |
| Ctrl + End | 跳转到 Cell 内容的最末尾 |
| Ctrl + ← / Ctrl + → | 按单词跳转光标（快速移动到上/下一个单词） |

2、从编辑模式返回命令模式

| 快捷键 | 作用 |
| --- | --- |
| Esc | 退出编辑模式，返回命令模式（Cell 边框变蓝） |
| Ctrl + M | 同 Esc，退出编辑模式 |


# 6 魔法命令
Jupyter 内置的特殊指令，以 %（单行）或 %%（整个 Cell）开头，用于完成计时、调试、文件操作等常用任务


```python
# %timeit：对单行代码进行多次重复计时，取平均值，结果更准确（适合测试简短表达式的性能）
%timeit [x**2 for x in range(1000)]
# 输出示例：98.3 µs ± 1.2 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

# %%time：对整个 Cell 的代码只计时一次（适合测试耗时较长的完整流程）
%%time
import time
data = [x**2 for x in range(100000)]
time.sleep(1)
# 输出示例：
# CPU times: user 45.2 ms, sys: 8.1 ms, total: 53.3 ms
# Wall time: 1.05 s
```


```python
# %matplotlib inline：将图表直接嵌入 Notebook 中显示（最常用，静态图）
# 通常放在 Notebook 的第一个 Cell 中，整个 Notebook 只需执行一次
%matplotlib inline

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 100)
plt.plot(x, np.sin(x))
plt.title('正弦波')
plt.show()

# %matplotlib notebook：启用交互式图表，可以缩放、平移（但不能与 inline 同时使用）
# %matplotlib notebook
```


```python
# %who：列出当前命名空间中所有已定义的变量名
%who
# 输出示例：data  plt  x

# %whos：比 %who 更详细，同时显示变量的类型和值
%whos
# 输出示例：
# Variable   Type    Data/Info
# ----------------------------
# x          ndarray 100: [0. 0.06 ... 6.28]
# data       list    n=100000

# %reset：清空所有变量（会弹出确认提示，适合重新开始计算时使用）
%reset

# %reset -f：强制清空所有变量，不弹出确认提示（-f 表示 force）
%reset -f
```


```python
# %pwd：显示当前工作目录（Print Working Directory）
%pwd
# 输出示例：'/home/user/notebooks'

# %ls：列出当前目录下的所有文件（Windows 用户可能需要用 %ls 或直接用 !dir）
%ls
# 输出示例：data.csv  model.py  notebook.ipynb

# %%writefile：将整个 Cell 的内容写入到指定文件（常用于快速创建脚本文件）
%%writefile hello.py
def greet(name):
    print(f"你好，{name}！")

greet("世界")
# 执行后会在当前目录生成 hello.py 文件，内容就是 Cell 中的代码

# %run：运行一个外部 Python 脚本文件，并将其变量导入当前命名空间
%run hello.py
# 输出：你好，世界！

# %load：将外部脚本文件的内容加载到当前 Cell（不会自动执行，仅加载代码）
%load hello.py
```


```python
# 在命令前加 ! 可以直接执行系统终端命令，无需切换到终端窗口
!pip install pandas          # 安装 Python 包
!pip list                    # 查看已安装的包列表
!python --version            # 查看 Python 版本

# 也可以将命令输出结果保存为 Python 变量
files = !ls -1               # 执行 ls 命令，结果赋值给 files 变量
print(files)                 # files 是一个列表，每个文件名是一个元素
```


```python
# %history：查看本次会话中执行过的所有命令历史
%history
# 加 -n 显示行号，加 -l 5 只显示最近 5 条
%history -n -l 5

# %debug：在代码报错后，在下一个 Cell 执行 %debug 可以进入交互式调试模式
# 可以在调试模式下输入变量名查看值，输入 q 退出调试
# 例如运行了一段报错的代码后：
%debug
```


```python
# %%html：将 Cell 内容作为 HTML 渲染输出（可以嵌入自定义样式和交互元素）
%%html
<h3 style="color: steelblue;">这是一个 HTML 标题</h3>
<p style="font-size: 16px;">可以在 Notebook 中直接渲染 HTML 内容。</p>

# %%latex：将 Cell 内容作为 LaTeX 公式渲染（常用于写数学公式）
%%latex
$$E = mc^2$$
$$\int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}$$
```

# 7 tqdm
常用的进度条库，支持循环、Pandas、多种 Jupyter 场景

```bash
pip install tqdm
```


```python
from tqdm.notebook import tqdm   # 在 Jupyter 中使用 notebook 版本，显示效果更美观
import time

# 基本用法：将可迭代对象包裹在 tqdm() 中即可自动显示进度条
for i in tqdm(range(100)):
    time.sleep(0.05)    # 模拟耗时操作
# 输出：显示进度条、已完成百分比、已用时间、预计剩余时间

# 配合 enumerate 使用
data = list(range(50))
for i, item in enumerate(tqdm(data, desc="处理数据")):
    # desc 参数设置进度条左侧的标签文字
    time.sleep(0.05)

# 手动控制进度（适用于不确定总量的场景）
with tqdm(total=100, desc="下载进度") as pbar:
    for chunk in range(10):
        time.sleep(0.1)
        pbar.update(10)     # 每次更新 10 个单位的进度
        pbar.set_postfix({"chunk": chunk})  # 在进度条右侧显示附加信息
```

# 8 高级技巧
...

# 9 jupyter-Book

## 9.1 安装
>```bash
>pip install jupyter-book
>
>jupyter-book create my-learning-notes
>```
执行后，你会看到自动生成的几样东西：
- _config.yml：网站的“总开关”，配置标题、作者等全局信息。
- _toc.yml：“目录大纲”，决定了笔记的章节顺序。
- intro.md等示例文件：可直接删除。

## 9.2 管理文件与目录 (_toc.yml)：

>```yaml
>format: jb-book
>root: intro   # 指定首页文件（如 intro.md）
>chapters:
>- file: python/01-basic
>- file: python/02-data-structure
>  sections:       # 子章节
>  - file: python/02-list
>- file: data-analysis/01-numpy
>```
然后，您需要把 .ipynb 或 .md 文件放到对应的文件夹里（如 python/01-basic.ipynb）。

## 9.3 基本配置 (_config.yml)：
>```yaml
>title: 我的学习笔记       # 网站标题
>author: 你的名字
>logo: images/logo.png    # 可选，Logo路径
># 控制笔记本是否执行: auto, force, or off
>execute:
>  execute_notebooks: auto
>```
这里选择执行模式时需稍加留意：设为 auto 时 Jupyter Book 会用缓存结果，force 会强制执行（当笔记代码较多时，构建时间会比较长）。

## 9.4 本地构建与预览
在 my-learning-notes 文件夹下运行构建命令：

>```bash
>jupyter-book build .
>```
终端显示 "build finished successfully" 即表示成功。生成的静态网页都在 _build/html/ 文件夹中。  
你可以在浏览器里打开 _build/html/index.html 来预览。

## 9.5 设置 GitHub Actions 自动部署（推荐）：

1. 添加 .nojekyll 文件（必须）：回到本地 my-learning-notes 根目录，创建空的 .nojekyll 文件以关闭 Jekyll 处理。

2. 设置 Pages 源：仓库 Settings -> Pages -> 在 "Build and deployment" 下，将 "Source" 从 "Deploy from a branch" 切换为 "GitHub Actions"-1。

3. 编写自动化脚本：在本地新建 .github/workflows/deploy.yml 文件，粘贴以下配置：
>```yaml
>name: deploy-book
>
>on:
>  push:
>    branches: [ main ]
>
>jobs:
>  deploy-book:
>    runs-on: ubuntu-latest
>    permissions:
>      pages: write
>      id-token: write
>    steps:
>    - uses: actions/checkout@v4
>    - name: Set up Python
>      uses: actions/setup-python@v5
>      with:
>        python-version: '3.11'
>        cache: 'pip'
>    - name: Install dependencies
>      run: pip install -r requirements.txt
>    - name: Build the book
>      run: jupyter-book build .
>    - name: Upload artifact
>      uses: actions/upload-pages-artifact@v3
>      with:
>        path: "_build/html"
>    - name: Deploy to GitHub Pages
>      id: deployment
>      uses: actions/deploy-pages@v4
>```
4. 推送触发部署：推送代码到 GitHub，稍等1-2分钟即可通过 https://你的用户名.github.io/my-learning-notes 访问。
