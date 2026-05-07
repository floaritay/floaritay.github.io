# floaritay 个人博客与学习笔记

> **floaritay** 的个人技术博客，集成了学习笔记、项目实践和技能展示。支持模块化导航与高效检索，内容涵盖编程、机器学习、深度学习、计算机视觉、机器人等多个技术领域。

## 项目概述

这是一个基于 Jupyter Notebook 和 HTML 的个人知识管理系统，通过自动化构建流程将学习笔记转换为美观的网页，并部署到 GitHub Pages。所有技术内容以中文编写，适合技术学习和知识分享。

## 页面结构与功能

- **模块化导航**：页面顶部可切换
- **项目展示**：精选个人重要项目，配有简介与直达 GitHub 仓库按钮
- **技能与工具**：以卡片形式分组展示编程语言、开发工具、机器学习、深度学习、计算机视觉、机器人、数据分析等技能
- **学习笔记索引**：自动收录 docs 目录下所有 HTML 笔记，支持分类筛选与关键词搜索
- **回到顶部按钮**：页面右下角悬浮，便于快速返回顶部

## 技术栈分类

### 基础工具
- **开发环境**：Conda, CUDA, Docker, Git, Linux, VS Code, Ollama
- **文档与协作**：Markdown, Git 工作流

### Python 编程
- **核心编程**：高级语法、面向对象、装饰器、生成器
- **GUI 开发**：tkinter, PyQt
- **正则表达式**：re 模块深入应用

### 数据分析与可视化
- **数据处理**：Numpy, Pandas, 数据清洗与转换
- **数据可视化**：Matplotlib, Seaborn
- **实战案例**：学生成绩分析、电影评分系统、股票数据分析

### 机器学习
- **传统算法**：决策树、SVM、贝叶斯分类、聚类算法
- **模型评估**：交叉验证、超参数调优、模型选择
- **Scikit-learn**：完整机器学习工作流

### 深度学习
- **框架应用**：PyTorch, TensorFlow/Keras
- **计算机视觉**：CNN, YOLO, OpenCV, 图像分类与检测
- **模型架构**：ResNet, Transformer, GAN

### 自然语言处理
- **文本处理**：分词、词性标注、情感分析
- **语言模型**：BERT, GPT 应用
- **NLP 工具**：jieba, NLTK, spaCy

### 机器人与仿真
- **ROS/ROS2**：机器人操作系统、节点通信、TF变换
- **机器人仿真**：Gazebo, URDF建模、MoveIt
- **传感器处理**：激光雷达、摄像头数据处理

### 智能系统
- **智能代理**：Agent 架构、LangChain
- **决策规划**：VRP优化算法、路径规划
- **Web API**：FastAPI, RESTful接口设计

### 数据库与爬虫
- **数据库**：SQL基础、SQLite、MySQL
- **网络爬虫**：requests, BeautifulSoup, Scrapy框架
- **数据采集**：API调用、数据解析与存储

## 快速开始

### 本地访问
1. 克隆仓库：`git clone https://github.com/yourusername/floaritay.git`
2. 打开 `docs/index.html` 即可本地访问博客主页
3. 支持离线浏览，无需服务器环境

### 在线访问
- 直接访问部署在 GitHub Pages 的博客链接
- 响应式设计，支持桌面和移动设备

### 功能使用
1. 打开 `docs/index.html` 即可访问主页，支持本地或 GitHub Pages 部署
2. 顶部切换栏可浏览"介绍"、"项目"、"笔记"三大模块
3. 项目区点击"查看仓库"按钮直达 GitHub
4. 笔记区支持分类筛选与关键词搜索，便于快速定位内容
5. 右下角"回到顶部"按钮提升浏览体验

## 开发与维护

### 内容构建流程

1. **编写笔记**：在对应分类目录中创建 Jupyter Notebook (`.ipynb`)
2. **转换为HTML**：使用 nbconvert 将笔记转换为网页格式
   ```bash
   jupyter nbconvert --to html notebook.ipynb --output ../docs/category/notebook.html
   ```
3. **自动部署**：GitHub Actions 自动构建并部署到 GitHub Pages

### 项目结构

```
floaritay/
├── docs/                    # 生成的HTML网站
│   ├── index.html          # 主页
│   └── category/           # 分类笔记HTML文件
├── Agent/                  # 智能代理相关内容
├── CV/                     # 计算机视觉
├── DeepLearing/            # 深度学习
├── machine_learning/       # 机器学习
├── python/                 # Python编程
├── data_analysis/          # 数据分析
├── ROS/                    # 机器人操作系统
├── images/                 # 共享图片资源
└── .github/workflows/      # CI/CD配置
```

### 贡献指南

欢迎通过以下方式参与项目：
- **内容贡献**：提交新的学习笔记或改进现有内容
- **功能建议**：提出页面功能改进或新特性需求
- **问题反馈**：报告页面显示问题或内容错误
- **代码优化**：改进构建脚本或页面性能

### 许可证

本项目采用 MIT License - 详见 [LICENSE](LICENSE) 文件。

### 联系方式

如有问题或建议，请通过 GitHub Issues 联系项目维护者。
