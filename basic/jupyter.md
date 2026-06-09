# 目录

- [1 Jupyter Notebook](#1-jupyter-notebook)
  - [1.1 .ipynb文件](#11-ipynb文件)

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


# jupyter-Book

## 安装
>```bash
>pip install jupyter-book
>
>jupyter-book create my-learning-notes
>```
执行后，你会看到自动生成的几样东西：
- _config.yml：网站的“总开关”，配置标题、作者等全局信息。
- _toc.yml：“目录大纲”，决定了笔记的章节顺序。
- intro.md等示例文件：可直接删除。

## 管理文件与目录 (_toc.yml)：

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

## 基本配置 (_config.yml)：
>```yaml
>title: 我的学习笔记       # 网站标题
>author: 你的名字
>logo: images/logo.png    # 可选，Logo路径
># 控制笔记本是否执行: auto, force, or off
>execute:
>  execute_notebooks: auto
>```
这里选择执行模式时需稍加留意：设为 auto 时 Jupyter Book 会用缓存结果，force 会强制执行（当笔记代码较多时，构建时间会比较长）。

## 本地构建与预览
在 my-learning-notes 文件夹下运行构建命令：

>```bash
>jupyter-book build .
>```
终端显示 "build finished successfully" 即表示成功。生成的静态网页都在 _build/html/ 文件夹中。  
你可以在浏览器里打开 _build/html/index.html 来预览。

## 设置 GitHub Actions 自动部署（推荐）：

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


