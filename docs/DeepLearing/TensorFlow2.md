# 目录


---
# 简介与概念
TensorFlow 是一个数学计算的工具箱，专门为机器学习任务而设计  
TensorFlow 是由 Google 开发的开源机器学习框架，用于构建和训练各种机器学习和深度学习模型  
TensorFlow 名字来源于其核心概念：`Tensor（张量）` 和 `Flow（流动）`，表示数据以张量的形式在计算图中流动  

- 张量(Tensor): 多维数组，是 TensorFlow 中的基本数据单位
- 计算图(Computational Graph): 描述数据(Tensor)流动(Flow)的有向图
- 会话(Session): 执行计算图的运行时环境

## 张量（Tensor）
张量是 TensorFlow 中最基本的数据结构，可以理解为多维数组的泛化概念  
从数学角度来说，张量是一个可以用来表示在一些矢量、标量和其他张量之间的线性关系的多线性函数  
简单类比：  
- 标量（0维张量）：一个数字，如 5
- 向量（1维张量）：一列数字，如 [1, 2, 3, 4]
- 矩阵（2维张量）：数字的表格，如 [[1, 2], [3, 4]]
- 3维张量：数字的立方体，如彩色图像（高×宽×颜色通道）
- 更高维张量：例如视频数据（时间×高×宽×颜色通道）

数据表示：  
- 输入数据：图像、文本、音频都可以表示为张量
- 模型参数：权重和偏置都是张量
- 中间结果：计算过程中的所有数据都是张量
- 输出结果：预测结果、损失值等

实际例子：  
- 图像分类：输入张量形状 (batch_size, height, width, channels)
- 文本处理：输入张量形状 (batch_size, sequence_length)
- 时间序列：输入张量形状 (batch_size, time_steps, features)


```python
# 示例张量
import tensorflow as tf

# 创建一个 2x3 的矩阵张量
tensor = tf.constant([[1, 2, 3], [4, 5, 6]])

print(f"形状 (Shape): {tensor.shape}")        # (2, 3)
print(f"数据类型 (Dtype): {tensor.dtype}")    # int32
print(f"维度 (Rank): {tf.rank(tensor)}")      # 2 
print(f"设备 (Device): {tensor.device}")      # /job:localhost/replica:0/task:0/device:CPU:0  张量存储的设备位置
```

## 计算图（Computational Graph）
计算图是一种用节点和边来表示数学运算的图结构：   
- 节点（Node）：代表数学运算（加法、乘法、激活函数等）
- 边（Edge）：代表数据流动的路径（张量）


```python
# TensorFlow 2.x 风格（动态图，推荐）
import tensorflow as tf

# 直接执行运算
x = tf.constant([[1.0, 2.0, 3.0]])
W = tf.Variable(tf.random.normal([3, 2]))
b = tf.Variable(tf.zeros([2]))
y = tf.matmul(x, W) + b # 执行矩阵乘法 x @ W（形状从 [1,3] x [3,2] 得到 [1,2]）

print(y)  # 立即得到结果
```

## 会话（Session）与即时执行（Eager Execution）

即时执行模式（默认，适合开发调试）：
- 运算立即执行
- 易于调试和理解
- 性能略低
  
图模式（适合生产部署）：
- 预先构建完整计算图
- 更好的优化机会
- 更高的执行效率


```python
# TensorFlow 2.x - 即时执行
import tensorflow as tf

a = tf.constant(2.0)
b = tf.constant(3.0)
c = a + b
print(f"结果: {c}")  # 结果: 5.0

# 可以直接访问值
print(f"c 的 numpy 值: {c.numpy()}")  # c 的 numpy 值: 5.0
```


```python
# 切换到图模式
@tf.function
def compute_function(x, y):
    return x * y + x

# 这个函数会被编译成图
result = compute_function(tf.constant(2.0), tf.constant(3.0))
```

## 变量（Variable）和常量（Constant）
常量是`不可变`的张量，一旦创建就不能修改  
变量是`可变`的张量，通常用来存储模型参数  


```python
# 创建常量
scalar_const = tf.constant(3.14)
vector_const = tf.constant([1, 2, 3, 4])
matrix_const = tf.constant([[1, 2], [3, 4]])

# 常量的值不能改变
print(scalar_const)  # tf.Tensor(3.14, shape=(), dtype=float32)
```


```python
# 创建变量
weight = tf.Variable(tf.random.normal([2, 3]))
bias = tf.Variable(tf.zeros([3]))

print(f"初始权重:\n{weight}")

# 修改变量的值
weight.assign(tf.ones([2, 3]))
print(f"修改后权重:\n{weight}")

# 部分更新
weight[0, 0].assign(5.0)
print(f"部分更新后:\n{weight}")
```

## 数据流动和自动微分
前向传播  
数据在计算图中从输入节点流向输出节点的过程  

自动微分（Automatic Differentiation）  
TensorFlow 使用 GradientTape 来记录运算并自动计算梯度  
1. 记录运算：tape 记录所有在其上下文中的运算
2. 构建反向图：创建用于梯度计算的反向计算图
3. 计算梯度：使用链式法则计算梯度

训练循环中的概念整合


```python
# 简单的前向传播示例
import tensorflow as tf

# 输入数据
x = tf.constant([[1.0, 2.0]]) # 1 个样本，每个样本 2 个特征

# 模型参数
W1 = tf.Variable(tf.random.normal([2, 3]))  # 权重矩阵，形状 [输入维度=2, 隐层维度=3]
b1 = tf.Variable(tf.zeros([3]))  # 偏置向量，形状 [隐层维度=3]
W2 = tf.Variable(tf.random.normal([3, 1]))  # tf.random.normal 用正态分布随机初始化权重，避免对称性问题
b2 = tf.Variable(tf.zeros([1]))  # 偏置通常初始化为 0

# 前向传播
hidden = tf.nn.relu(tf.matmul(x, W1) + b1)  # 隐层    
# 线性变换：tf.matmul(x, W1) + b1   x（形状 [1, 2]）与 W1（形状 [2, 3]）相乘，得到形状 [1, 3]   加上偏置 b1（广播机制自动扩展为 [1, 3]）
# 激活函数：tf.nn.relu   对线性变换结果应用 ReLU 激活函数（max(0, x)），引入非线性
output = tf.matmul(hidden, W2) + b2         # 输出层
# 隐层输出 hidden（形状 [1, 3]）与 W2（形状 [3, 1]）相乘，得到形状 [1, 1]   加上偏置 b2（广播机制自动扩展为 [1, 1]）
# output 是最终预测值，形状 [1, 1]（标量值）
print(f"最终输出: {output}")
```


```python
# 自动微分示例
x = tf.Variable(3.0)

# 使用 GradientTape 记录运算
with tf.GradientTape() as tape:
    y = x**2 + 2*x + 1  # y = x² + 2x + 1

# 计算 dy/dx
gradient = tape.gradient(y, x)
print(f"当 x=3 时,dy/dx = {gradient}")  # 应该是 2x + 2 = 8
```


```python
# 完整的训练步骤示例
import tensorflow as tf

# 模型和数据
model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu'), # 隐层：10个神经元，ReLU激活
    tf.keras.layers.Dense(1)                      # 输出层：1个神经元（无激活函数）
])

x_train = tf.random.normal([100, 5]) # 100个样本，每个样本5个特征
y_train = tf.random.normal([100, 1]) # 100个标签，每个标签1个值

optimizer = tf.keras.optimizers.Adam(0.01)
# Adam 优化器：
# 自适应调整学习率，结合了动量（Momentum）和 RMSProp 的优点
# 学习率设为 0.01，控制参数更新步长

# 训练步骤
@tf.function # 将 Python 函数编译为 TensorFlow 计算图，提升执行速度
def train_step(x, y):
    with tf.GradientTape() as tape:
        predictions = model(x)  # 前向传播
        loss = tf.keras.losses.mse(y, predictions)  # 计算MSE损失
    
    gradients = tape.gradient(loss, model.trainable_variables)  # 自动微分
    optimizer.apply_gradients(zip(gradients, model.trainable_variables))  # 更新参数,将梯度应用到参数（model.trainable_variables）
    return loss

# 执行训练
for epoch in range(10):  # 迭代 10 个 epoch（完整遍历数据集 10 次）
    loss = train_step(x_train, y_train)  # 每次调用 train_step 执行一次参数更新
    print(f"Epoch {epoch}: Loss = {loss.numpy():.4f}")  # 打印当前 epoch 的损失值（随着训练，损失应逐渐下降）
```

# 环境搭建
- 隔离依赖：避免不同项目间的包版本冲突
- 干净环境：保持系统 Python 环境整洁
- 易于管理：可以轻松删除和重建环境
- 可复现性：便于在不同机器上复现环境
  
## 使用 venv 创建虚拟环境
VS Code:  
1. 命令面板创建  
f1打开命令面板，输入Creat Environment，选择Venv    
会生成一个.venv文件，并激活虚拟环境  
按 Ctrl + ~ 进入终端，查看是否运行虚拟环境，如果是，文件名前会有 (.venv) 的标识  
如果没有运行，将终端power shell选择为cmd（Windows 的安全机制，默认情况下禁止运行未签名的脚本）  
输入"D:\VS Code python program\.venv\Scripts\activate.bat"   

2. 终端创建  
按 Ctrl + ~ 进入终端，将终端power shell选择为cmd（Windows 的安全机制，默认情况下禁止运行未签名的脚本）  
输入 python -m venv .venv   
与方法1不同的是，需要手动激活虚拟环境，继续输入.venv\Scripts\activate.bat   

此环境是在 VS Code python program 文件夹下的，除此之外，可以对每个项目（对应的文件夹）创建单独的环境

如何在 Jupyter Notebook 中使用虚拟环境   
激活环境后安装 ipykernel  
--name 后填写你想在 Jupyter 中显示的内核名称，建议与虚拟环境名一致，方便识别  
>```
>pip install ipykernel  
>python -m ipykernel install --user --name=venv 
>```
然后在 Jupyter 中选择该内核即可   
  
删除虚拟环境   
venv：直接删除环境文件夹（如 rm -rf 文件名） 或 手动直接删除.venv文件夹   

## 相关终端命令
pip list  
pip install   
.venv\Scripts\activate.bat 激活环境  
deactivate 取消激活  
注意取消激活后，可能还在虚拟环境中，将右下角的python解释器换回全局就可以了  
cls 清理界面  
pip freeze > requirements.txt 创建环境库和对应的版本号文档 requirements.txt  
rmdir /s .venv 删除环境文件夹  
pip install -r requirements.txt 参考requirements.txt下载对应版本库  
  
注意，不要把其他文件放到.venv文件夹下，防止删除环境时误删  
  


```python
#!/usr/bin/env python3
"""
TensorFlow 安装验证脚本
"""

import sys
print("Python version:", sys.version)
print("-" * 50)

# 检查 TensorFlow
try:
    import tensorflow as tf
    print(f"✓ TensorFlow version: {tf.__version__}")
    print(f"✓ Keras version: {tf.keras.__version__}")
    
    # 检查 GPU 支持
    physical_devices = tf.config.list_physical_devices('GPU')
    if physical_devices:
        print(f"✓ GPU devices found: {len(physical_devices)}")
        for i, device in enumerate(physical_devices):
            print(f"  - GPU {i}: {device}")
        print(f"✓ CUDA built: {tf.test.is_built_with_cuda()}")
    else:
        print("&#x26a0; No GPU devices found (CPU only)")
    
    # 简单计算测试
    a = tf.constant([1, 2, 3])
    b = tf.constant([4, 5, 6])
    c = tf.add(a, b)
    print(f"✓ Basic computation test: {a.numpy()} + {b.numpy()} = {c.numpy()}")
    
except ImportError as e:
    print(f"✗ TensorFlow import failed: {e}")

print("-" * 50)

# 检查其他重要包
packages = ['numpy', 'pandas', 'matplotlib', 'sklearn', 'jupyter']
for package in packages:
    try:
        module = __import__(package)
        version = getattr(module, '__version__', 'unknown')
        print(f"✓ {package}: {version}")
    except ImportError:
        print(f"✗ {package}: not installed")

print("-" * 50)

# 内存和设备信息
print("System Information:")
if tf.config.list_physical_devices('GPU'):
    for gpu in tf.config.list_physical_devices('GPU'):
        try:
            tf.config.experimental.set_memory_growth(gpu, True)
            print(f"✓ GPU memory growth enabled for {gpu}")
        except:
            print(f"&#x26a0; Could not set memory growth for {gpu}")

print("Installation verification complete!")
```


```python
"""
性能基准测试
"""
import tensorflow as tf
import time

print("TensorFlow Performance Test")
print("-" * 30)

# 矩阵乘法测试
def benchmark_matmul(device_name, size=1000):
    with tf.device(device_name):
        a = tf.random.normal([size, size])
        b = tf.random.normal([size, size])
        
        # 预热
        for _ in range(5):
            c = tf.matmul(a, b)
        
        # 计时
        start_time = time.time()
        for _ in range(10):
            c = tf.matmul(a, b)
        end_time = time.time()
        
        avg_time = (end_time - start_time) / 10
        return avg_time

# CPU 测试
cpu_time = benchmark_matmul('/CPU:0')
print(f"CPU ({1000}x{1000} matmul): {cpu_time:.4f} seconds")

# GPU 测试（如果可用）
if tf.config.list_physical_devices('GPU'):
    gpu_time = benchmark_matmul('/GPU:0')
    print(f"GPU ({1000}x{1000} matmul): {gpu_time:.4f} seconds")
    print(f"GPU speedup: {cpu_time/gpu_time:.2f}x")
else:
    print("No GPU available for testing")
```

## 安装GPU版本
TensorFlow GPU 版本依赖 NVIDIA 的三个核心组件，必须按顺序安装，且版本需匹配：  
1. NVIDIA 显卡驱动   
2. CUDA Toolkit  
3. cuDNN  
  
TensorFlow 与 CUDA、cuDNN 版本存在严格兼容性，需先确定对应关系  
- 查看 TensorFlow 官方文档 中的版本兼容表（例如：TensorFlow 2.10 对应 CUDA 11.2 + cuDNN 8.1）  
  
安装 CUDA Toolkit  
- 下载对应版本的 CUDA Toolkit：访问 CUDA 历史版本下载页，选择版本和系统，下载安装包  
- 安装路径默认即可（如 C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8），会自动添加环境变量
- nvcc --version  成功安装：会显示 CUDA 编译器（nvcc）的版本信息
  
安装 cuDNN  
- 下载与 CUDA 版本匹配的 cuDNN: 访问 cuDNN 下载页（需注册 NVIDIA 账号），选择对应版本
- 解压下载的 cuDNN 压缩包，得到 bin、include、lib 三个文件夹。将这三个文件夹复制到 CUDA 安装目录下，与现有文件夹合并
  
安装 TensorFlow GPU 版本  
- 建议在虚拟环境中安装 
- pip install tensorflow


```python
import tensorflow as tf

# 检查是否识别到 GPU
print("GPU 可用：", tf.test.is_gpu_available())
# 查看 GPU 设备信息
print("GPU 设备列表：", tf.config.list_physical_devices('GPU'))

# 若输出 GPU 可用：True 且显示 GPU 设备信息，说明安装成功
```

# 张量操作
张量是TensorFlow 中的核心数据结构，可以理解为多维数组的扩展概念  
  
在机器学习中，几乎所有数据最终都会被表示为张量形式进行处理  
  
- 数据类型(dtype)：每个张量都有特定的数据类型，如tf.float32、tf.int64等
- 形状(shape)：表示张量每个维度的大小，如(2,3)表示2行3列的矩阵
- 设备位置(device)：指示张量存储在CPU还是GPU上

## 创建张量
从Python列表/NumPy数组创建张量  
创建特殊值张量  
创建随机张量


```python
import tensorflow as tf
import numpy as np

# 从Python列表创建
tensor_from_list = tf.constant([[1, 2], [3, 4]])

# 从NumPy数组创建
numpy_array = np.array([[5, 6], [7, 8]])
tensor_from_numpy = tf.constant(numpy_array)
```


```python
# 全零张量
zeros = tf.zeros((2, 3))  # 2行3列的全0矩阵

# 全一张量
ones = tf.ones((3, 2))    # 3行2列的全1矩阵

# 单位矩阵
eye = tf.eye(3)           # 3×3的单位矩阵

# 填充特定值
filled = tf.fill((2, 2), 7)  # 2×2矩阵，所有元素为7
```


```python
# 均匀分布随机数
uniform = tf.random.uniform((2, 2), minval=0, maxval=1)

# 正态分布随机数
normal = tf.random.normal((3, 3), mean=0, stddev=1)

# 随机排列
shuffled = tf.random.shuffle(tf.constant([1, 2, 3, 4, 5]))
```

## 基本操作
数学运算  
形状操作  
索引与切片


```python
a = tf.constant([[1, 2], [3, 4]])
b = tf.constant([[5, 6], [7, 8]])

# 逐元素加法
add = tf.add(a, b)        # 或使用运算符重载 a + b

# 逐元素乘法
mul = tf.multiply(a, b)   # 或 a * b

# 矩阵乘法
matmul = tf.matmul(a, b)  # 或 a @ b

# 其他数学运算
sqrt = tf.sqrt(tf.cast(a, tf.float32))  # 平方根(需要转换为浮点型)
```


```python
tensor = tf.constant([[1, 2, 3], [4, 5, 6]])

# 获取形状
shape = tensor.shape  # 返回 (2, 3)

# 改变形状(reshape)
reshaped = tf.reshape(tensor, (3, 2))  # 变为3行2列

# 转置(transpose)
transposed = tf.transpose(tensor)  # 变为3行2列

# 扩展维度(expand_dims)
expanded = tf.expand_dims(tensor, axis=0)  # 形状从(2,3)变为(1,2,3)
```


```python
tensor = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# 获取单个元素
elem = tensor[1, 2]  # 获取第2行第3列的元素(值为6)

# 切片操作
row = tensor[1, :]    # 获取第2行所有元素 [4,5,6]
col = tensor[:, 1]    # 获取第2列所有元素 [2,5,8]
sub = tensor[0:2, 1:] # 获取第1-2行，第2-3列 [[2,3],[5,6]]  前闭后开
```

## 广播机制
自动扩展较小的张量以匹配较大张量的形状  
  
广播规则  
- 从最后一个维度开始向前比较
- 两个维度要么相等，要么其中一个为1，要么其中一个不存在
- 在缺失或为1的维度上进行复制扩展  


```python
# 向量(3,)与标量()相加
a = tf.constant([1, 2, 3])
b = tf.constant(2)
c = a + b  # 结果为[3,4,5]，b被广播为[2,2,2]

# 矩阵(3,1)与向量(3,)相加
d = tf.constant([[1], [2], [3]])
e = tf.constant([10, 20, 30])
f = d + e  # d被广播为[[1,1,1],[2,2,2],[3,3,3]]
           # 结果为[[11,21,31],[12,22,32],[13,23,33]]
```

## 聚合操作


```python
tensor = tf.constant([[1, 2, 3], [4, 5, 6]])

# 求和
sum_all = tf.reduce_sum(tensor)        # 所有元素求和 → 21
sum_axis0 = tf.reduce_sum(tensor, 0)  # 沿第0维(行)求和 → [5,7,9]
sum_axis1 = tf.reduce_sum(tensor, 1)  # 沿第1维(列)求和 → [6,15]

# 求均值
mean_all = tf.reduce_mean(tensor)      # 所有元素均值 → 3.5  对整数张量计算均值时会执行整数除法,实际为3

# 最大值/最小值
max_val = tf.reduce_max(tensor)        # 最大值 → 6
min_val = tf.reduce_min(tensor)       # 最小值 → 1

# 逻辑运算
any_true = tf.reduce_any(tensor > 4)   # 是否有元素>4 → True
all_true = tf.reduce_all(tensor > 0)   # 是否所有元素>0 → True
```

## 练习


```python
# 1. 创建一个3×3的随机矩阵，元素值在0-10之间
random_matrix = tf.random.uniform((3, 3), minval=0, maxval=10, dtype=tf.int32)

# 2. 计算该矩阵的转置
transposed_matrix = tf.transpose(random_matrix)

# 3. 计算矩阵与转置矩阵的乘积
product = tf.matmul(random_matrix, transposed_matrix)

# 4. 计算乘积矩阵的对角线元素之和
diag_sum = tf.reduce_sum(tf.linalg.diag_part(product))
```


```python
# 1. 创建一个4×1的矩阵和一个1×4的向量
matrix = tf.constant([[1], [2], [3], [4]]) #(4,1)
vector = tf.constant([10, 20, 30, 40])     #(4,)--视为(1,4),由缺失值对齐1

# 2. 利用广播机制计算它们的和
broadcast_sum = matrix + vector

# 3. 验证结果的形状和值
print("形状:", broadcast_sum.shape)  # 应为(4,4)
print("结果:", broadcast_sum.numpy())
```

# Keras
Keras 是一个用 Python 编写的高级神经网络 API，它能够以 TensorFlow, CNTK 或 Theano 作为后端运行。Keras 的设计理念是用户友好、模块化和易扩展  
## 核心概念
模型 (Model)  
Keras 的核心数据结构是模型，模型是组织神经网络层的方式。Keras 提供了两种主要的模型：  
- Sequential 模型：层的线性堆叠
- Functional API：构建复杂模型的有向无环图
  
层 (Layer)  
层是 Keras 的基本构建块，每个层接收输入数据，进行某种计算后输出结果。Keras 提供了多种预定义层：  
- 核心层：Dense, Activation, Dropout 等
- 卷积层：Conv2D, MaxPooling2D 等
- 循环层：LSTM, GRU 等
- 其他：Embedding, BatchNormalization 等
  
激活函数 (Activation Function)  
激活函数决定神经元的输出，常用的有：  
- ReLU (Rectified Linear Unit)
- Sigmoid
- Tanh
- Softmax (多分类问题)  

## 基本工作流程
>``` python
>## 定义模型
>from tensorflow.keras.models import Sequential
>from tensorflow.keras.layers import Dense, Input
>
>model = Sequential([
>    Input(shape=(784,)),  # 显式定义输入形状（784维向量，如28x28图像展平）
>    Dense(64, activation='relu'), # 第一隐藏层：64个神经元，ReLU激活
>    Dense(64, activation='relu'), # 第二隐藏层：64个神经元，ReLU激活
>    Dense(10, activation='softmax')# 输出层：10个神经元（多分类），Softmax激活
>])
>
>## 编译模型
>model.compile(optimizer='adam', # 使用Adam优化器（自适应学习率）
>              loss='categorical_crossentropy', # 多分类交叉熵损失
>              metrics=['accuracy']) # 监控准确率
>
>## 训练模型
>model.fit(x_train, y_train, 
>          epochs=5, 
>          batch_size=32) # 每批32个样本（梯度更新的粒度）
>
>## 评估模型
>loss_and_metrics = model.evaluate(x_test, y_test, batch_size=128) # 评估时按128个样本一批计算（可调整以优化性能）
>
>## 进行预测
>classes = model.predict(x_test, batch_size=128)
>``` 

## 模型保存与加载
  
1. 保存整个模型  
``model.save('my_model.h5')  # 保存架构、权重和训练配置``  
   
2. 仅保存架构  
``json_string = model.to_json()  # 保存为JSON``  
``yaml_string = model.to_yaml()  # 保存为YAML``  
    
3. 仅保存权重    
``model.save_weights('my_model_weights.h5')``  
  
4. 加载模型  
``from tensorflow.keras.models import load_model``  
``model = load_model('my_model.h5')  # 加载完整模型``  

## 回调函数
回调函数是在训练过程中特定时间点被调用的函数，用于：  
- 模型检查点
- 提前停止
- 学习率调整
- 日志记录等
  
常用回调函数
>```python 
>from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
># ModelCheckpoint：在训练过程中定期保存模型（例如，保存验证损失最低的模型）
># EarlyStopping：当监控的指标（如验证损失）不再改善时，提前终止训练（防止过拟合）
>
>callbacks = [
>    ModelCheckpoint(
>        filepath='best_model.h5', # 保存的文件名
>        monitor='val_loss',       # 监控的指标（这里是验证损失）
>        save_best_only=True       # 只保存监控指标最优的模型（最小val_loss）
>        ),
>    EarlyStopping(
>        monitor='val_loss',       # 监控的指标
>        patience=3                # 当连续n个epoch内监控指标不再改善后停止
>        )
>]
>
>model.fit(x_train, y_train,
>          epochs=10,
>          callbacks=callbacks,
>          validation_data=(x_val, y_val)) # 验证集（用于监控val_loss）
>``` 

## 示例：MNIST 手写数字识别
构建 卷积神经网络（CNN） 来识别 MNIST 手写数字（0-9）  


```python
from tensorflow import keras
from keras import Input
from keras.datasets import mnist                 # 加载 MNIST 数据集（手写数字图片）
from keras.models import Sequential              # Keras 的顺序模型，用于堆叠神经网络层
from keras.layers import Dense, Dropout, Flatten # 全连接层、Dropout 层、展平层
from keras.layers import Conv2D, MaxPooling2D    # 卷积层和池化层（用于 CNN）
from keras.utils import to_categorical           # 将标签转换为 one-hot 编码

# 加载数据
(x_train, y_train), (x_test, y_val) = mnist.load_data()    # 60,000 张 28x28 的灰度训练图像，10,000 张 28x28 的灰度测试图像

# 数据预处理
x_train = x_train.reshape(60000, 28, 28, 1).astype('float32') / 255  
x_test = x_test.reshape(10000, 28, 28, 1).astype('float32') / 255    
# 将图像从 (60000, 28, 28) 调整为 (60000, 28, 28, 1)，增加通道维度(灰度图通道=1),归一化像素值到 [0, 1]（加速训练）
y_train = to_categorical(y_train, 10)
y_val = to_categorical(y_val, 10)
# 将标签转换为 one-hot 编码（10 个类别）

# 构建模型
model = Sequential([
    Input(shape=(28, 28, 1)),                           # 输入层
    Conv2D(32, kernel_size=(3, 3), activation='relu'),  # 卷积层1 32 个 3x3 卷积核，激活函数为 ReLU
    Conv2D(64, (3, 3), activation='relu'),              # 卷积层2 64 个 3x3 卷积核，激活函数为 ReLU
    MaxPooling2D(pool_size=(2, 2)),                     # 池化层，池化窗口大小为 2x2
    Dropout(0.25),                                      # Dropout 层，随机丢弃 25% 的神经元，防止过拟合
    Flatten(),                                          # 展平层，将 3D 特征图展平为 1D 向量（供全连接层使用）    
    Dense(128, activation='relu'),                      # 全连接层 128 个神经元，学习全局特征组合
    Dropout(0.5),                                       # Dropout 层，随机丢弃 50% 的神经元，防止过拟合 
    Dense(10, activation='softmax')                     # 输出层，10 个神经元，（对应 0-9），softmax 输出概率分布
])  

# 编译模型
model.compile(loss='categorical_crossentropy',  # 多分类交叉熵损失（适用于 one-hot 标签）
              optimizer='adam',                 # Adam 优化器
              metrics=['accuracy'])             # 监控训练和测试的准确率        

# 训练模型
model.fit(x_train, y_train,
          batch_size=128,                        # 每批次的样本数
          epochs=12,
          verbose=1,                             # 显示进度条和日志
          validation_data=(x_test, y_val))      # 用测试集作为验证集（监控泛化性能）

# 评估模型
score = model.evaluate(x_test, y_val, verbose=0)# 计算测试集的损失和准确率
print('Test loss:', score[0])
print('Test accuracy:', score[1])
```

## 进阶技巧


```python
# 自定义层
# 定义了一个 自定义 Keras 层（MyLayer），继承自 tensorflow.keras.layers.Layer。该层实现了一个简单的 全连接（Dense）操作（即 y = x @ W，其中 @ 表示矩阵乘法）
from keras import backend as K
from keras.layers import Layer

class MyLayer(Layer):
    def __init__(self, output_dim, **kwargs):   # 初始化方法
        self.output_dim = output_dim            # 输出维度（神经元数量）
        super(MyLayer, self).__init__(**kwargs) # 调用父类初始化
    
    def build(self, input_shape):               # 构建权重
        self.kernel = self.add_weight(name='kernel',                            # 权重名称
                                     shape=(input_shape[1], self.output_dim),   # 权重形状(输入特征数, 输出维度)
                                     initializer='uniform',                     # 权重初始化方法（均匀分布）
                                     trainable=True)                            # 是否可训练
        super(MyLayer, self).build(input_shape)                                 # 调用父类标记层构建方法
    
    def call(self, x):                          # 前向传播
        return K.dot(x, self.kernel)            # 矩阵乘法: y = x @ W
    
    def compute_output_shape(self, input_shape):# 输出形状
        return (input_shape[0], self.output_dim)# 输出形状为 (样本数, 输出维度)
```


```python
# 自定义损失函数
from keras import backend as K

def custom_loss(y_true, y_pred):        
    return K.mean(K.square(y_pred - y_true), axis=-1)   # 均方误差

model.compile(optimizer='adam', loss=custom_loss)
```


```python
# 学习率调度
# 在训练过程中动态调整优化器的学习率（lr）。具体来说，它使用 LearningRateScheduler 回调函数，根据训练轮次（epoch）调整学习率
from keras.callbacks import LearningRateScheduler

def scheduler(epoch, lr):
    if epoch < 10:
        return lr               # 前 10 轮保持学习率不变
    else:
        return lr * K.exp(-0.1) # 之后每轮乘以 exp(-0.1) ≈ 0.9048

callback = LearningRateScheduler(scheduler)
model.fit(x_train, y_train, epochs=15, callbacks=[callback])
```

## 常见问题与解决方案
  
1. 过拟合问题  
- 增加 Dropout 层
- 使用 L1/L2 正则化
- 增加训练数据
- 使用数据增强
  
2. 训练速度慢
- 增加批量大小
- 使用更简单的模型
- 尝试不同的优化器
- 使用 GPU 加速
  
3. 梯度消失/爆炸
- 使用 BatchNormalization
- 使用适当的权重初始化
- 使用 ReLU 等非饱和激活函数
- 使用梯度裁剪

# 第一个神经网络


```python
import numpy as np
from tensorflow import keras
from keras import layers

# 1. 加载数据
(x_train,y_train),(x_test,y_val) = keras.datasets.mnist.load_data()

# 2. 预处理
x_train = x_train.reshape(60000,784).astype('float32')/255  # 不能写成(60000,28,28),见下一个注释
x_test = x_test.reshape(10000,784).astype('float32')/255

y_train = keras.utils.to_categorical(y_train,10)
y_val = keras.utils.to_categorical(y_val,10)

# 3. 构建模型
model = keras.Sequential([
    keras.Input(shape=(784,)),              # 逗号是为了明确表示这是一个 1D 张量（向量） 的形状，而不是一个标量值 
    layers.Dense(512,activation='relu'),    # 全连接神经网络 Dense 需要输入是 2D 数组（样本数 × 特征数），因此将 28x28 的图像展平为 784 维向量。
                                            # 如果是卷积神经网络 Conv2D，则不需要展平，直接保留 (height, width, channels) 格式。使用卷积层,对于图像数据更有效
    layers.Dense(10,activation='softmax')
])

# 4. 编译模型
model.compile(
    optimizer='rmsprop',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# 5. 训练模型
history=model.fit(
    x_train,y_train,
    batch_size=128,
    epochs=10,
    validation_split=0.2
)

# 6. 评估模型
test_loss,test_acc=model.evaluate(x_test,y_val)
print(f"测试准确率{test_acc:.4f}")

# 可视化
import matplotlib.pyplot as plt

plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

# # 保存模型
# model.save("mnist_model.h5")

# # 加载模型
# loaded_model = keras.models.load_model("mnist_model.h5")
```

.compile()

|参数|	说明|	常用值|
|---|---|---|
|optimizer|	优化器，用于更新权重	|"rmsprop", "adam", "sgd"|
|loss	|损失函数，衡量模型预测与真实值的差距	|"categorical_crossentropy" (分类), "mse" (回归)|
|metrics	|评估指标，用于监控训练	|["accuracy"]|

.fit()
|参数	|说明	|建议值|
|---|---|---|
|batch_size	|每次梯度更新使用的样本数	|32-256|
|epochs	|训练轮数	|根据数据复杂度调整|
|validation_split	|用作验证集的训练数据比例	|0.1-0.3|
|validation_data	|验证数据集	||
|callbacks	|回调函数列表	||

shape
- 标量（单个数字）：shape=()（空元组，如 5 的形状是 ()）。
- 1D 向量：shape=(n,)（如 [1, 2, 3] 的形状是 (3,)）。
- 2D 矩阵：shape=(m, n)（如 [[1, 2], [3, 4]] 的形状是 (2, 2)）。
- 3D 张量：shape=(a, b, c)（如 MNIST 图像展平后的形状是 (60000, 784)）

# 常用层详解
## Dense 全连接层
>```python
>Dense(units,
>      activation=None,
>      use_bias=True,
>      kernel_initializer='glorot_uniform',
>      bias_initializer='zeros')
>```
- units：正整数，输出空间的维度  
- activation：激活函数  
- use_bias：是否使用偏置向量  
- kernel_initializer：权重矩阵的初始化方法  
- bias_initializer：偏置向量的初始化方法  
  
应用场景：  
- 用于多层感知机(MLP)
- 作为分类器的最后一层
- 特征变换和非线性映射  

## Conv2D 二维卷积层
>```python
>Conv2D(filters,
>       kernel_size,
>       strides=(1, 1),
>       padding='valid',
>       activation=None)
>```
- filters：卷积核的数目  
- kernel_size：卷积核的尺寸  
- strides：卷积步长  
- padding：填充方式 ('valid'不填充 或 'same'填充使输出与输入尺寸相同)    

应用场景：  
- 图像分类
- 目标检测
- 图像分割

## LSTM 长短期记忆网络层
>```python
>LSTM(units,
>     activation='tanh',
>     recurrent_activation='hard_sigmoid',
>     return_sequences=False)
>```
- units：正整数，输出空间的维度  
- activation：激活函数   
- dropout：0到1之间的浮点数，输入线性变换的丢弃率  
- recurrent_dropout：0到1之间的浮点数，循环状态的丢弃率  
- recurrent_activation：循环步的激活函数  
- return_sequences：是否返回完整序列 

应用场景：  
- 自然语言处理
- 时间序列预测
- 语音识别

## Dropout 随机失活层
>```python
>Dropout(
>    rate=0.5)
>```
- rate：0到1之间的浮点数，丢弃比例  
- noise_shape：整数张量，表示将与输入相乘的二进制丢弃掩层的形状  
- seed：随机数种子  

应用场景：
- 防止神经网络过拟合
- 提高模型泛化能力
- 通常在全连接层后使用

## BatchNormalization 批量归一化层
>```python
>BatchNormalization()
># 对前一层的输出进行批量归一化，加速训练并提高模型稳定性
>```

## MaxPooling2D 二维最大池化层
>```python
>MaxPooling2D(pool_size=(2, 2))
># 创建2x2的最大池化层,取窗口内的最大值来下采样特征图
>```


## Flatten 展平层
>```python
>Flatten()
># 将多维输入展平为一维，常用于从卷积层过渡到全连接层

## Embedding 嵌入层
>```python
>Embedding(input_dim=1000, output_dim=64)
># 词汇表大小为1000，输出维度为64
># 将正整数（索引）转换为固定大小的密集向量

## 组合示例


```python
import keras
from keras.layers import Dense, Dropout, Conv2D, MaxPooling2D, Flatten

# 创建一个简单的CNN模型
model = keras.Sequential([
    keras.Input(shape=(28,28,1)),
    Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(64, activation='relu'),
    Dropout(0.5),
    Dense(10, activation='softmax')
])
```

## 选择层的指导原则
输入数据类型：
- 图像数据：Conv2D + 池化层
- 序列数据：LSTM/GRU
- 结构化数据：Dense层

模型深度：
- 深层网络需要配合BatchNormalization和Dropout

任务类型：
- 分类任务：最后一层使用softmax激活
- 回归任务：最后一层不使用激活函数或使用线性激活

计算资源：
- 大尺寸输入考虑使用池化层减少参数
- 资源有限时减少层数和单元数

# 数据处理与管道
  
tf.data API 是 TensorFlow 提供的高效数据输入管道构建工具，专门用于处理大规模数据集   
  
tf.data API 解决了传统数据加载方式中的性能瓶颈问题，使数据预处理和模型训练能够并行进行  

TensorFlow Dataset API 是构建数据管道的核心工具，它提供了多种数据源接口和转换操作    

## tf.data.Dataset
Dataset 是 tf.data API 的核心抽象，表示一系列元素，其中每个元素包含一个或多个张量   


```python
import tensorflow as tf

# 从内存创建Dataset
data = tf.data.Dataset.from_tensor_slices([1, 2, 3]) 
# from_tensor_slices() 会将输入数据沿第一个维度切片。例如：
# 输入 [1, 2, 3]（形状 (3,)）会被切分为 3 个单独的元素：1, 2, 3。
# 如果输入是二维数组（如 [[1, 2], [3, 4]]），则会按行切片
# 快速测试或小规模数据

# 从文本文件创建
text_data = tf.data.TextLineDataset(["file1.txt", "file2.txt"])
# 逐行读取文本文件，每行作为数据集的一个元素
# 处理文本数据（如 CSV、日志、自然语言数据）

# 从TFRecord创建
tfrecord_data = tf.data.TFRecordDataset("data.tfrecord")
# 读取 TensorFlow 的二进制格式文件
# 适合大规模数据

# 从生成器创建
def gen():
    for i in range(10):
        yield i
           
dataset = tf.data.Dataset.from_generator(gen, output_types=tf.int32)
```

## 数据转换

### map
map 是最常用的转换操作，用于对每个元素应用自定义函数  


```python
# 对每个数字进行平方
dataset = dataset.map(lambda x: x**2)
```

### batch
将多个元素组合成一个批次


```python
# 创建32大小的批次
batched_dataset = dataset.batch(32)

# 不等长序列的填充批次
padded_batch = dataset.padded_batch(
    32,                         
    padded_shapes=([None], []), 
#   定义填充后的目标形状，支持动态长度（None 表示自动推断最大长度）
#   假设原始数据是 (sequence, label) 的元组，其中：
#   sequence 是变长向量（如 [1, 2, 3] 或 [4, 5]）
#   label 是标量（如 0 或 1）
#   padded_shapes=([None], []) 表示：
#   对 sequence 填充到当前批次中最长序列的长度（None 动态适配）
#   对 label 不填充（[] 表示保持标量）
    padding_values=(0.0, 0)
#   指定填充值
#   对 sequence 用 0.0 填充
#   对 label 用 0 填充（这里不用填充）
)
```

### shuffle
打乱数据顺序，对训练至关重要  


```python
# 基本用法，从 dataset 中创建一个打乱顺序的新数据集
shuffled = dataset.shuffle(buffer_size=10000) # buffer_size=10000 表示维护一个大小为 10000 的缓冲区，用于随机采样

# 最佳实践：buffer_size应 >= 数据集大小
full_shuffle = dataset.shuffle(buffer_size=len(dataset))
```

## 数据处理


```python
# 1. 数据加载
# 根据数据来源选择适当的加载方式

# 图像数据加载示例
def load_image(path):
    img = tf.io.read_file(path)                     # 读取文件（二进制）
    img = tf.image.decode_jpeg(img, channels=3)     # 解码JPEG，输出RGB图像
    return tf.image.resize(img, [256, 256])         # 调整图像大小为256x256

image_dataset = tf.data.Dataset.list_files("images/*.jpg") # 获取image文件夹下所有JPG文件路径
image_dataset = image_dataset.map(load_image)              # 对每个路径应用load_image

# 2. 数据预处理
# 使用 map() 方法应用预处理函数

def normalize(image):
    return image / 255.0  # 归一化到0-1范围

normalized_dataset = image_dataset.map(normalize)

# 3. 数据增强
# 训练时常用的增强技术

def augment(image):
    image = tf.image.random_flip_left_right(image)           # 随机左右翻转（50%概率）
    image = tf.image.random_brightness(image, max_delta=0.2) # 随机亮度调整（±20%）
    return image

augmented_dataset = normalized_dataset.map(augment)          # 测试集通常不需要增强，只需归一化

# 4. 批次处理
# 配置批次大小和预取

BATCH_SIZE = 32
train_dataset = augmented_dataset.batch(BATCH_SIZE)      # 每32个样本组成一个批次
train_dataset = train_dataset.prefetch(tf.data.AUTOTUNE) # 预取数据，加速训练
```

## 性能优化
    
### 并行化处理
加速数据加载   
``dataset = dataset.map(process_func,num_parallel_calls=tf.data.AUTOTUNE)``  
  
### 预取 (Prefetch) 
让数据加载和模型执行重叠进行,减少等待时间    
``dataset = dataset.prefetch(buffer_size=tf.data.AUTOTUNE)``    
    
### 缓存机制
避免重复计算  
内存缓存    
``dataset = dataset.cache()``  

文件缓存  
``dataset = dataset.cache(filename='/tmp/cache')``  


```python
optimized_dataset = (tf.data.Dataset.list_files("data/*.png")
                    .map(load_image, num_parallel_calls=tf.data.AUTOTUNE) # 并行加载图像
                    .cache()                                              # 缓存数据到内存
                    .map(augment, num_parallel_calls=tf.data.AUTOTUNE)    # 并行数据增强
                    .batch(32)                                            # 批次化
                    .prefetch(tf.data.AUTOTUNE))                          # 预取数据
```

## 示例：图像分类管道
管道设计原则
- 将耗时操作放在早期阶段
- 保持预处理操作确定性
- 为验证集禁用数据增强


```python
import os

def build_pipeline(image_dir, batch_size=32, is_training=True):
    '''
    image_dir:图像目录路径(需满足 类别子目录/图片.jpg 的结构)
    batch_size:每批样本数(默认 32)
    is_training:是否为训练模式(决定是否启用数据增强)
    '''
    # 1. 加载数据
    dataset = tf.data.Dataset.list_files(f"{image_dir}/*/*.jpg") # 例如："data/cat/1.jpg"
    
    # 2. 解析和预处理
    def process_path(file_path):
        label = tf.strings.split(file_path, os.sep)[-2] # 提取父目录名作为标签 例如："data/cat/1.jpg" → label = "cat"
        image = load_image(file_path)                   # 加载图像  见‘数据处理’
        return image, label
    
    dataset = dataset.map(process_path, num_parallel_calls=tf.data.AUTOTUNE)
    
    dataset_sta = dataset.apply(tf.data.experimental.bytes_produced_stats())  # 监控
    for data, bytes_produced in dataset_sta:
        print(f"Data: {data.numpy()}, Bytes Produced: {bytes_produced.numpy()}")
    
    # 3. 训练时增强
    if is_training:
        dataset = dataset.map(
            lambda x, y: (augment(x), y),  # 使用 lambda 对 x（image） 应用 augment() 函数, y（label） 保持不变
            num_parallel_calls=tf.data.AUTOTUNE
        )
    
    # 4. 优化配置
    dataset = dataset.batch(batch_size)
    dataset = dataset.prefetch(tf.data.AUTOTUNE)
    
    return dataset
```


```python
def build_image_pipeline(file_pattern, batch_size=32, is_training=True):

    dataset = tf.data.Dataset.list_files(file_pattern)
    
    if is_training:
        dataset = dataset.shuffle(10000)
    
    dataset = dataset.map(load_and_preprocess_image,num_parallel_calls=tf.data.experimental.AUTOTUNE)
    
    dataset = dataset.batch(batch_size)
    
    if is_training:
        dataset = dataset.repeat()
    
    return dataset.prefetch(buffer_size=tf.data.experimental.AUTOTUNE)

def load_and_preprocess_image(path):
    image = tf.io.read_file(path)
    image = tf.image.decode_jpeg(image, channels=3)
    image = tf.image.resize(image, [224, 224])
    image = tf.cast(image, tf.float32) / 255.0  # 归一化
    return image
```

## 监控
``dataset = dataset.apply(tf.data.experimental.bytes_produced_stats())``  
统计数据管道中每个元素（或批次）产生的字节数，帮助分析数据加载和预处理的内存开销    
返回一个 Dataset，其元素是原始数据的元组 (original_element, bytes_produced)，其中 bytes_produced 是该元素经过管道处理后占用的字节数      
监控数据是否过大,优化内存使用，避免因数据膨胀导致内存不足   
  
``dataset = dataset.apply(tf.data.experimental.latency_stats())``   
统计数据管道中每个操作的延迟（单位：微秒），帮助识别性能瓶颈  
返回一个 Dataset，其元素是原始数据的元组 (original_element, latency)，其中 latency 是处理该元素所花费的时间   
分析数据管道中哪些操作（如 map、batch、prefetch）耗时最长,优化数据加载速度，减少训练时的 I/O 阻塞   


```python
import tensorflow as tf
import time

# 模拟一个耗时的预处理函数
def slow_preprocess(x):
    time.sleep(0.1)  # 模拟延迟
    return x * 2

# 创建数据集并添加延迟统计
dataset = tf.data.Dataset.range(3)
dataset = dataset.map(slow_preprocess)
dataset = dataset.apply(tf.data.experimental.latency_stats())

# 遍历并打印结果
for data, latency in dataset:
    print(f"Data: {data.numpy()}, Latency (µs): {latency.numpy()}")

# Data: 0, Latency (µs): 100200  # 约 100ms（受 time.sleep 影响）
# Data: 2, Latency (µs): 100150
# Data: 4, Latency (µs): 100180
```


```python
def build_image_pipeline(file_pattern, batch_size=32, is_training=True):
    dataset = tf.data.Dataset.list_files(file_pattern)
    
    if is_training:
        dataset = dataset.shuffle(10000)
    
    dataset = dataset.map(
        lambda x: load_and_preprocess_image(x),
        num_parallel_calls=tf.data.experimental.AUTOTUNE
    )
    
    dataset = dataset.batch(batch_size)
    
    if is_training:
        dataset = dataset.repeat()
    
    return dataset.prefetch(buffer_size=tf.data.experimental.AUTOTUNE)

def load_and_preprocess_image(path):
    image = tf.io.read_file(path)
    image = tf.image.decode_jpeg(image, channels=3)
    image = tf.image.resize(image, [224, 224])
    image = tf.cast(image, tf.float32) / 255.0  # 归一化
    return image
```

## 常见问题与总结
  
处理大型数据集时：  
- 使用 TFRecord 格式存储数据
- 分片处理：dataset.shard(num_shards, index)
- 流式处理：避免 cache() 大文件
  
性能  
1. CPU利用率低
- 增加 num_parallel_calls
- 使用 interleave() 并行化I/O
  
2. GPU利用率低
- 增加 prefetch_buffer_size
- 检查批次大小是否合适
  
如何处理非常大的数据集   
- 使用 tf.data.Dataset.list_files 创建文件数据集
- 使用交错读取 (interleave) 并行处理多个文件
- 考虑使用 TFRecord 格式存储数据
  
为什么我的数据管道速度很慢？
- 检查是否使用了预取 (prefetch)
- 确保 map 操作设置了 num_parallel_calls
- 验证 shuffle 的 buffer_size 是否足够大
- 考虑缓存中间结果
  
最佳实践总结
- 尽早 shuffle：在数据管道的早期应用 shuffle
- 延迟批处理：在应用 map 后再进行批处理
- 利用并行：尽可能使用并行化操作
- 重叠执行：使用 prefetch 实现数据加载和模型执行的重叠
- 合理缓存：对不变的数据进行缓存

# 图像数据处理
在TensorFlow中，图像通常表示为：  
  
灰度图像：[高度, 宽度] 或 [高度, 宽度, 1]  
  
彩色图像：[高度, 宽度, 3]   

为什么需要图像处理  
- 数据标准化：统一图像尺寸和数值范围
  
- 数据增强：通过变换增加训练样本多样性
  
- 特征提取：突出图像中的关键信息
  
- 预处理：为模型输入准备合适的数据格式

## tf.image
TensorFlow提供的专门用于图像处理的API集合  
  
|功能类别	|主要方法示例  tf.image|
|---|---|
|色彩调整	|``adjust_brightness``, ``adjust_contrast``|
|几何变换	|``random_flip_left_right``, ``random_rotation``, ``resize``|
|图像合成	|blend, draw_bounding_boxes|
|格式转换	|``encode_jpeg``, ``decode_image``|
|统计操作	|total_variation, ``per_image_standardization``|

## 标准化处理
将像素值归一化到固定范围（通常是[0,1]或[-1,1]）


```python
def normalize(image):
    """将uint8图像归一化到[0,1]范围"""
    image = tf.cast(image, tf.float32)  # 转换为float32
    return image / 255.0  # 除以最大值

# 使用示例
image = tf.random.uniform([256,256,3], 0, 255, dtype=tf.uint8)
normalized_image = normalize(image)
```

## 数据增强技术
通过随机变换增加数据多样性，对于医学图像，卫星图像等，谨慎使用几何变换，优先考虑色彩空间变换  


```python
from tensorflow import image as tf_image

def augment_image(image, label):
    """应用随机增强的图像处理流水线"""
    # 随机左右翻转
    image = tf_image.random_flip_left_right(image)
    
    # 随机亮度调整
    image = tf_image.random_brightness(image, max_delta=0.2)
    
    # 随机对比度调整
    image = tf_image.random_contrast(image, lower=0.8, upper=1.2)
    
    # 随机旋转（-15°到+15°）
    angle = tf.random.uniform([], -15, 15) * (3.1415/180)
    image = tf_image.rotate(image, angle)
    
    return image, label
```

## 流程
读取图像--加载解码--预处理--数据增强--批次与预取  


```python
def preprocess_dataset(dataset, batch_size=32, is_training=False):
    """构建图像预处理流水线"""
    
    # 定义预处理函数
    def _preprocess(image, label):
        # 解码JPEG图像
        image = tf_image.decode_jpeg(image, channels=3)
        # 调整大小到统一尺寸
        image = tf_image.resize(image, [224, 224])
        # 训练时应用数据增强
        if is_training:
            image = augment_image(image)
        # 标准化处理
        image = normalize(image)
        return image, label
    
    # 应用预处理并创建批次
    dataset = dataset.map(_preprocess, num_parallel_calls=tf.data.AUTOTUNE)
    dataset = dataset.batch(batch_size)
    dataset = dataset.prefetch(tf.data.AUTOTUNE)
    
    return dataset
```

## 高级


```python
from keras import layers
import tensorflow as tf
from tensorflow import keras
## 使用Keras预处理层 
# 创建预处理模型
augmenter = tf.keras.Sequential([
    layers.RandomFlip("horizontal"),  # 以50%概率水平翻转
    layers.RandomRotation(0.1),       # 随机旋转（幅度±0.1弧度）
    layers.RandomZoom(0.1),           # 随机缩放（幅度±0.1）
    layers.Rescaling(1./255)          # 标准化
])

# 在模型中使用
model = tf.keras.Sequential([
    augmenter,  # 数据增强层
    layers.Conv2D(32, 3, activation='relu'),
    # 其他层...
])
```


```python
## 自定义图像处理层
class RandomColorDistortion(tf.keras.layers.Layer):         # 继承自 tf.keras.layers.Layer，表明这是一个自定义的 Keras 层
    def __init__(self, contrast_range=[0.5, 1.5], **kwargs):
        super().__init__(**kwargs)                          # 调用父类（Layer）的初始化方法，确保 Keras 能正确管理该层
        self.contrast_range = contrast_range                # 对比度调整
        
    def call(self, images, training=None):                  # 前向传播方法
        if not training:
            return images
            
        # 随机对比度调整
        contrast_factor = tf.random.uniform(
            [], self.contrast_range[0], self.contrast_range[1])   # [] 表示标量，范围在 [0.5, 1.5] 之间
        images = tf.image.adjust_contrast(images, contrast_factor)
        
        # 随机饱和度调整
        images = tf.image.random_saturation(images, 0.5, 1.5)
        
        return images
```

## 示例


```python
# 定义ImageNet的均值和标准差（RGB通道顺序）
IMAGENET_MEAN = tf.constant([0.485, 0.456, 0.406])
IMAGENET_STD = tf.constant([0.229, 0.224, 0.225])
# 这些值是基于ImageNet训练集中数百万张自然图像的像素值统计计算得出的，用于图像预处理中的标准化 或 归一化，但不适用于医学图像、卫星图像等
mean = IMAGENET_MEAN
std = IMAGENET_STD

# 数据处理管道
def build_pipeline(img_dir,batch_size=32,is_training=True):
    # 获取图像路径
    dataset = tf.data.Dataset.list_files(img_dir)
    # dataset = tf.data.Dataset.list_files(img_dir).interleave(               #或 interleave 以并行加载文件
    # lambda x: tf.data.Dataset.from_tensors(x).map(load_image),
    # num_parallel_calls=tf.data.AUTOTUNE
    # )
    # 加载与解码
    dataset = dataset.map(load_image,num_parallel_calls=tf.data.AUTOTUNE)
    dataset = dataset.cache()                                               # 缓存预处理后的数据,适用于数据集较小或重复训练
    # 预处理（归一化）
    dataset = dataset.map(preprocess,num_parallel_calls=tf.data.AUTOTUNE)
    # 数据增强（测试集通常不需要增强，只需归一化）
    if is_training:
        dataset=dataset.map(augment,num_parallel_calls=tf.data.AUTOTUNE)
    # 批次处理与预取
    dataset = dataset.batch(batch_size)
    dataset = dataset.prefetch(tf.data.AUTOTUNE)

    return dataset

# 图像数据加载与解码
def load_image(path):
    image = tf.io.read_file(path)                     # 读取文件（二进制）
    image = tf.image.decode_jpeg(image, channels=3)   # 解码JPEG，输出RGB图像
    image = tf.image.resize(image, [256, 256])        # 调整图像大小
    assert tf.shape(image)[-1] == 3,                  "图像通道数必须为3(RGB)"
    return image       

# 数据预处理
def preprocess(image):
    # 调整图像大小(已经在load_image处理过了)
    image = tf.image.resize(image,[256,256])
    # 通道转换（如RGB转灰度）（无）
    # 类型转换（如uint8转float32）(在归一化里处理过了)
    image = tf.cast(image,tf.float32)
    # 归一化
    image = tf.cast(image, tf.float32)  # 转换为float32
    return image / 255.0                # 除以最大值
    image = tf.image.convert_image_dtype(image, tf.float32)  # 或 自动归一化到[0,1]
    # 标准化（无）
    image = tf.image.convert_image_dtype(image, tf.float32)  # 先归一化
    image = (image - mean) / std                             # (x - mean) / std 标准化
    return image

# 数据增强
def augment(image):
    image = tf.image.random_flip_left_right(image)               # 随机左右翻转（50%概率）
    image = tf.image.random_brightness(image, max_delta=0.2)     # 随机亮度调整（±20%）
    image = tf.image.random_contrast(image,lower=0.8,upper=1.2)  # 随机对比度调整（±20%） 
    image = tf.image.random_hue(image,max_delta=0.2)             # 随机色调调整（±20%）
    image = tf.image.random_saturation(image,lower=0.5,upper=1.5)# 随机饱和度调整（±50%）
    return image
```


```python
import tensorflow as tf

def build_preprocessing_pipeline(tfrecord_path, batch_size=32, is_training=True):
    """
    构建图像预处理流水线：
    1. 从 TFRecord 加载图像
    2. 解码 JPEG 图像
    3. 随机裁剪到 256x256(训练时)或中心裁剪(推理时)
    4. 随机水平翻转（仅训练时）
    5. 标准化到 [-1, 1] 范围
    6. 创建批次大小为 32 的数据集
    """
    # 1. 从 TFRecord 加载数据
    dataset = tf.data.TFRecordDataset(tfrecord_path)
    
    # 2. 解析 TFRecord（假设存储的是序列化的 tf.train.Example）
    dataset = dataset.map(
        lambda x: parse_tfrecord(x),
        num_parallel_calls=tf.data.AUTOTUNE
    )
    
    # 3. 解码 JPEG 图像并调整大小（如果原始尺寸不是 256x256）
    dataset = dataset.map(
        lambda image, label: decode_and_resize(image, label, target_size=(256, 256)),
        num_parallel_calls=tf.data.AUTOTUNE
    )
    
    # 4. 数据增强（仅训练时）
    if is_training:
        dataset = dataset.map(
            lambda image, label: augment_image(image, label),
            num_parallel_calls=tf.data.AUTOTUNE
        )
    
    # 5. 标准化到 [-1, 1]（假设输入是 [0, 255] 的 uint8 图像）
    dataset = dataset.map(
        lambda image, label: normalize_to_minus1_plus1(image, label),
        num_parallel_calls=tf.data.AUTOTUNE
    )
    
    # 6. 批次处理 & 预取优化
    dataset = dataset.batch(batch_size)
    dataset = dataset.prefetch(tf.data.AUTOTUNE)
    
    return dataset

# --- 辅助函数 ---
def parse_tfrecord(serialized_example):
    """解析 TFRecord 中的 tf.train.Example"""
    feature_description = {
        'image': tf.io.FixedLenFeature([], tf.string),
        'label': tf.io.FixedLenFeature([], tf.int64),
    }
    example = tf.io.parse_single_example(serialized_example, feature_description)
    return example['image'], example['label'] # 假设是 JPEG 编码的二进制字符串

def decode_and_resize(image, label, target_size=(256, 256)):
    """解码 JPEG 图像并调整大小"""
    image = tf.image.decode_jpeg(image, channels=3)  # 解码 JPEG
    image = tf.image.resize(image, target_size)     # 调整到 256x256
    image = tf.cast(image, tf.float32)              # 转为 float32
    return image, label

def augment_image(image, label,):
    """数据增强：随机裁剪 + 水平翻转"""
    # 随机裁剪到 256x256（先放大到 300x300 再随机裁剪）
    image = tf.image.resize_with_crop_or_pad(image, 300, 300)  # 填充到 300x300
    image = tf.image.random_crop(image, size=[256, 256, 3])    # 随机裁剪回 256x256
    
    # 随机水平翻转（50% 概率）
    image = tf.image.random_flip_left_right(image)
    
    return image, label

def normalize_to_minus1_plus1(image, label,):
    """标准化到 [-1, 1] 范围"""
    image = (image / 127.5) - 1.0  # [0, 255] -> [-1, 1]
    return image, label

# --- 使用示例 ---
if __name__ == "__main__":
    # 假设 TFRecord 文件路径
    tfrecord_path = "path/to/your/dataset.tfrecord"
    
    # 构建训练流水线
    train_dataset = build_preprocessing_pipeline(
        tfrecord_path,
        batch_size=32,
        is_training=True
    )
    
    # 构建验证流水线（无数据增强）
    val_dataset = build_preprocessing_pipeline(
        tfrecord_path,
        batch_size=32,
        is_training=False
    )
    
    # 检查输出形状
    for images, labels in train_dataset.take(1):
        print("训练批次形状:", images.shape, labels.shape)  # 应为 (32, 256, 256, 3) 和 (32,)
```

# 文本数据处理
原始文本数据通常包含许多噪声和不一致性，例如：  
- 大小写不一致
- 标点符号
- 停用词（如"的"、"是"等）
- 特殊字符
- 拼写错误  
  
预处理的目标是将原始文本转换为干净、一致的格式，便于后续的特征提取和模型训练   
  
TensorFlow 提供了多个用于文本处理的模块：  
- tf.strings：基础字符串操作
  
- tf.keras.layers.TextVectorization：文本向量化层
  
- tf.data.TextLineDataset：从文本文件创建数据集
  
- tensorflow_text：高级文本处理库（需单独安装）
  


```python
import tensorflow as tf
from keras.layers import TextVectorization
```

## tf.strings


```python
# 创建字符串张量
text = tf.constant(["TensorFlow 文本处理", "深度学习自然语言处理"])

# 转换为小写
lower_case = tf.strings.lower(text)
# 输出: ['tensorflow 文本处理', '深度学习自然语言处理']

# 分割字符串
words = tf.strings.split(text)
# 输出: [['TensorFlow', '文本处理'], ['深度学习', '自然语言处理']]

# 字符串长度
length = tf.strings.length(text)
# 输出: [10, 11]


import re
import tensorflow as tf
import string
# 移除标点符号
def remove_punctuation(text):
    return tf.strings.regex_replace(text, '[%s]' % re.escape(string.punctuation), '')

text = tf.constant("Hello, World!")
clean_text = remove_punctuation(text)
# 输出: "Hello World"
```

## 文本向量化 
将文本转换为数值表示是文本处理的核心步骤。TensorFlow 提供了 TextVectorization 层来实现这一功能   
  
TextVectorization 层可以：
- 标准化文本（如转小写、去除标点）
  
- 分词（按空格或自定义规则拆分单词）
  
- 将单词映射到整数索引（构建词汇表）
  
- 将文本转换为整数序列或one-hot 编码
  
|参数|	说明|
|---|---|
|max_tokens	|词汇表大小（保留最高频的 max_tokens-1 个词，其余为 [UNK]）|
|output_mode|	"int"（默认，整数序列）、"binary"、"count" 或 "tf-idf"|
|output_sequence_length|	固定序列长度（短则填充 0，长则截断）|
|standardize	|标准化方式："lower"（转小写）、"lower_and_strip_punctuation" 或自定义函数|
|split	|分词方式："whitespace"（默认）或 "character"（按字符分割）|
|ngrams	|是否使用 N-gram（如 ngrams=2 会添加二元组到词汇表）|
  
TextVectorization 层支持多种输出模式：
  
|模式	|描述|	适用场景|
|---|---|---|
|'int'	|输出单词索引|	嵌入层输入|
|'binary'|	多热编码|	小词汇量分类|
|'count'|	词频计数|	词袋模型|
|'tf-idf'|	TF-IDF 权重|	信息检索|


```python
from keras import layers
import keras
# 1.创建向量化层
# 定义文本向量化层
vectorize_layer = layers.TextVectorization(
    max_tokens=10000,        # 最大词汇量（保留前10000个高频词，其余标记为 [UNK]（未知词））
    output_mode='int',       # 输出模式:整数索引（每个词对应一个唯一ID）
    output_sequence_length=50  # 统一序列长度（短则补零，长则截断）
)

# 示例文本数据
text_dataset = tf.data.Dataset.from_tensor_slices([
    "这是第一个句子",
    "这是另一个不同的句子",
    "添加第三个示例句子"
])

# 适配数据并构建词汇表
vectorize_layer.adapt(text_dataset)

# 2.向量化文本
# 向量化单个句子
vectorized_text = vectorize_layer("这是一个示例句子")
print(vectorized_text)
# 输出类似: [ 5, 3, 10, 8, 0, 0, ... ] (输出的是词汇表中词汇的索引，后面补零到长度50)

# 获取词汇表
vocab = vectorize_layer.get_vocabulary()
print(vocab[:10])  # 打印前10个词汇，词汇表前两项固定为 ''（填充符）和 [UNK]

```

## 流程


```python
vectorize_layer = layers.TextVectorization(
    max_tokens=10000,        # 最大词汇量（保留前10000个高频词，其余标记为 [UNK]（未知词））
    output_mode='int',       # 输出模式:整数索引（每个词对应一个唯一ID）
    output_sequence_length=50  # 统一序列长度（短则补零，长则截断）
)

def preprocess_text(text):
    # 转换为小写
    text = tf.strings.lower(text)
    # 移除标点
    text = tf.strings.regex_replace(text, '[^a-zA-Z0-9\u4e00-\u9fa5]', ' ')
    return text

# 创建处理管道
def make_text_pipeline(text, batch_size=32):
    # 预处理
    text = text.map(preprocess_text)
    # 向量化
    text = text.map(vectorize_layer)
    # 批处理
    text = text.batch(batch_size)
    return text

# 使用管道
processed_ds = make_text_pipeline(text_dataset)
```

## 高级文本处理 tf_text
对于更复杂的文本处理需求，可以使用 tensorflow_text 库
>```python
># 安装 tensorflow_text (如果需要)
># !pip install tensorflow-text
>
>import tensorflow_text as tf_text
># 1. 分词器
># 创建分词器
>tokenizer = tf_text.WhitespaceTokenizer()
>
># 分词
>tokens = tokenizer.tokenize(["TensorFlow 文本处理", "深度学习 NLP"])
>print(tokens)
># 输出: [['TensorFlow', '文本处理'], ['深度学习', 'NLP']]
>
># 2. 子词分词
># 使用 BERT 分词器
>bert_tokenizer = tf_text.BertTokenizer(
>    vocab_lookup_table="path/to/vocab.txt",
>    token_out_type=tf.int32
>)
>
>tokens = bert_tokenizer.tokenize(["自然语言处理很有趣"])
>print(tokens)
>```


## 示例


```python
import keras
from keras import layers
import tensorflow as tf
# 1. 加载数据
(train_text, train_labels), (test_text, test_labels) = tf.keras.datasets.imdb.load_data(num_words=80000) # train_text 是已经整数编码的评论,而不是原始字符串

# 已经适配好了
# # 2. 创建向量化层
# vectorize_layer = layers.TextVectorization(
#     max_tokens=80000,
#     output_mode='int',
#     output_sequence_length=250
# )

# # 3. 适配数据 (只使用训练数据构建词汇表)
# text_ds = tf.data.Dataset.from_tensor_slices(train_text).batch(128)
# vectorize_layer.adapt(text_ds)

# 4. 构建模型
model = keras.Sequential([
    # vectorize_layer,
    keras.layers.Embedding(80000, 16),
    keras.layers.GlobalAveragePooling1D(),
    keras.layers.Dropout(0.5),
    keras.layers.Dense(16, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')
])

# 5. 编译和训练模型
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# 需要将数据转为 Tensor 并填充到统一长度
train_text = keras.preprocessing.sequence.pad_sequences(train_text, maxlen=250)
test_text = keras.preprocessing.sequence.pad_sequences(test_text, maxlen=250)
model.fit(train_text, train_labels, epochs=10,
    validation_data=(test_text, test_labels),  # 监控测试集表现
    verbose=1)

# 6. 最终评估
test_loss, test_acc = model.evaluate(test_text, test_labels)
print(f'Test accuracy: {test_acc}')

```

最佳实践  
  
- 词汇表大小：根据数据集大小选择适当的词汇量，通常 10,000-50,000 足够
  
- 序列长度：分析文本长度分布，选择覆盖大多数样本的长度
  
- 预处理一致性：确保训练和推理时使用相同的预处理步骤
  
- 内存优化：对于大型数据集，使用生成器或 tf.data 的缓存功能
  
1. 词汇表外词(OOV)处理：
>```python
>vectorize_layer = TextVectorization(
>    max_tokens=10000,
>    output_mode='int',
>    output_sequence_length=50,
>    pad_to_max_tokens=True  # 确保所有输出长度一致
>)
>```
  
2. 处理多语言文本：  
统一编码为 UTF-8  
考虑语言特定的预处理（如中文分词）  
  
3. 性能优化：  
使用 tf.data 的 prefetch 和 cache  
考虑离线预处理大型数据集    


```python
import tensorflow as tf
from keras import layers, models

# 加载 IMDB 数据集
max_features = 10000  # 词汇表大小
sequence_length = 256  # 每个序列的最大长度

(train_data, train_labels), (test_data, test_labels) = tf.keras.datasets.imdb.load_data(num_words=max_features)

# 将整数序列填充为相同的长度
train_data = tf.keras.preprocessing.sequence.pad_sequences(train_data, maxlen=sequence_length)
test_data = tf.keras.preprocessing.sequence.pad_sequences(test_data, maxlen=sequence_length)

# 构建模型
model = models.Sequential([
    layers.Embedding(input_dim=max_features, output_dim=128),
    layers.GlobalAveragePooling1D(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(1, activation='sigmoid')
])

# 编译模型
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# 训练模型
history = model.fit(
    train_data,
    train_labels,
    epochs=10,
    batch_size=32,
    validation_split=0.2
)

# 评估模型
test_loss, test_acc = model.evaluate(test_data, test_labels)
print(f"Test Loss: {test_loss}")
print(f"Test Accuracy: {test_acc}")

# 绘制训练和验证的准确性曲线
import matplotlib.pyplot as plt

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs_range = range(10)

plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label='Training Accuracy')
plt.plot(epochs_range, val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label='Training Loss')
plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')

plt.show()
```

# 模型训练
.compile()

|参数|	说明|	常用值|
|---|---|---|
|optimizer|	优化器，用于更新权重	|"rmsprop", "adam", "sgd"|
|loss	|损失函数，衡量模型预测与真实值的差距	|"categorical_crossentropy" (分类), "mse" (回归)|
|metrics	|评估指标，用于监控训练	|["accuracy"],['mse']|
  
.fit()
|参数	|说明	|建议值|
|---|---|---|
|batch_size	|每次梯度更新使用的样本数	|32-256|
|epochs	|训练轮数	|根据数据复杂度调整|
|validation_split	|用作验证集的训练数据比例	|0.1-0.3|
|validation_data	|验证数据集	||
|callbacks	|回调函数列表	||


```python
import tensorflow as tf
from keras import datasets,layers, models

# 加载数据集（以MNIST为例）
(train_images, train_labels), (test_images, test_labels) = datasets.mnist.load_data()

# 数据预处理
train_images = train_images.reshape((60000, 28, 28, 1)).astype('float32') / 255
test_images = test_images.reshape((10000, 28, 28, 1)).astype('float32') / 255

# 转换为TensorFlow Dataset
train_dataset = tf.data.Dataset.from_tensor_slices((train_images, train_labels))
train_dataset = train_dataset.shuffle(10000).batch(64)


# 构建Sequential模型
model = models.Sequential([
    keras.Input(shape=(28, 28, 1)),
    layers.Conv2D(32, (3, 3), activation='relu' ),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# 查看模型结构
model.summary()

# 模型编译
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 模型训练
history = model.fit(train_dataset, 
                    epochs=10,
                    validation_data=(test_images, test_labels))

import matplotlib.pyplot as plt

# 绘制训练和验证的准确率曲线
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.show()
```

## 自定义与回调


```python
# 自定义训练循环，而不是使用内置的 model.fit()

# 定义损失函数和优化器
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy() # 使用 SparseCategoricalCrossentropy 损失函数，适用于多分类问题，且标签是整数形式
optimizer = tf.keras.optimizers.Adam()                    # 使用 Adam 优化器，它是一种自适应学习率的优化算法，适用于大多数任务

# 自定义训练步骤
@tf.function                    # 将函数编译为 TensorFlow 计算图，提升执行速度
def train_step(images, labels):
    with tf.GradientTape() as tape: # GradientTape记录前向传播过程中的操作，用于自动微分（计算梯度）
        predictions = model(images) # 前向传播,计算预测值 predictions
        loss = loss_fn(labels, predictions) # 计算损失
    gradients = tape.gradient(loss, model.trainable_variables) # 计算损失对模型可训练参数的梯度
    optimizer.apply_gradients(zip(gradients, model.trainable_variables)) # 将梯度应用到参数上，完成一次参数更新
    return loss

# 自定义训练循环
for epoch in range(10):
    for images, labels in train_dataset:  # 遍历训练数据
        loss = train_step(images, labels) # 执行训练步骤
    print(f'Epoch {epoch}, Loss: {loss.numpy()}')
```


```python
# 回调函数使用

from keras.callbacks import ModelCheckpoint, EarlyStopping

# 创建回调函数
callbacks = [
    ModelCheckpoint('best_model.h5', save_best_only=True),
    EarlyStopping(patience=3, monitor='val_loss')
]

# 使用回调训练
model.fit(train_dataset,
          epochs=20,
          validation_data=(test_images, test_labels),
          callbacks=callbacks)
```

## 常见问题
|问题现象	   |可能原因	    |解决方案|
|---          |---            |---|
|损失不下降	   |学习率过高/过低	|调整学习率|
|准确率波动大  |批量大小不合适	|调整batch_size|
|过拟合	       |模型太复杂	   |添加正则化或Dropout|
|训练速度慢	   |硬件限制	    |使用GPU加速或减小模型|

>```python
># 使用prefetch和cache加速数据加载
>train_dataset = train_dataset.cache().prefetch(buffer_size=tf.data.AUTOTUNE)
>
># 混合精度训练
>policy = tf.keras.mixed_precision.Policy('mixed_float16')
>tf.keras.mixed_precision.set_global_policy(policy)
>
># 分布式训练
>strategy = tf.distribute.MirroredStrategy()
>with strategy.scope():
>    model = create_model()
>    model.compile(...)

## 示例


```python
import tensorflow as tf
# from tensorflow.keras import layers,callbacks,models,datasets
from keras import datasets,callbacks,models,layers

# 加载Fashion MNIST数据集
(train_images,train_labels),(test_images,test_labels) = datasets.fashion_mnist.load_data()

# 预处理（扩展为4D张量,归一化图像数据）
train_images = train_images.reshape((train_images.shape[0],28,28,1)).astype('float32') / 255.0
test_images = test_images.reshape((test_images.shape[0],28,28,1)).astype('float32') / 255.0

# 转换为TensorFlow Dataset
train_dataset = tf.data.Dataset.from_tensor_slices((train_images,train_labels))
train_dataset = train_dataset.shuffle(10000).batch(64)

# 建立模型
model = models.Sequential([
    layers.Input(shape=(28,28,1)),
    layers.Conv2D(32,(3,3),activation='relu'),
    layers.MaxPooling2D((2,2)),
    layers.Conv2D(64,(3,3),activation='relu'),
    layers.MaxPooling2D((2,2)),
    layers.Conv2D(64,(3,3),activation='relu'),
    layers.Flatten(),
    layers.Dense(64,activation='relu'),
    layers.Dense(10,activation='softmax')
])

# 编译模型
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])

# 回调
callbacks = [
    callbacks.EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True),      # 定义EarlyStopping回调
    callbacks.ModelCheckpoint('best_model.h5', monitor='val_accuracy', save_best_only=True), # 定义ModelCheckpoint回调以保存最佳模型
    callbacks.ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=2, min_lr=0.00001) # 定义学习率衰减
]

# 训练模型
history = model.fit(train_dataset,epochs=10,validation_data=(test_images,test_labels),callbacks=callbacks)

# 精确率与损失率
import  matplotlib.pyplot as plt

plt.plot(history.history['accuracy'],label='accuracy')
plt.plot(history.history['val_accuracy'],label='val_accuracy')
plt.xlabel('epoch')
plt.ylabel('accuracy')
plt.ylim([0,1])
plt.legend(loc='lower right')
plt.show()

plt.plot(history.history['loss'],label='loss')
plt.plot(history.history['val_loss'],label='val_loss')
plt.xlabel('epoch')
plt.ylabel('accuracy')
plt.ylim([0,2.5])
plt.legend(loc='upper right')
plt.show()
```

# 模型评估
|指标类型	|适用场景	|常见指标|
|---       |---        |---    |
|分类指标	|分类问题	|准确率、精确率、召回率、F1分数|
|回归指标	|回归问题	|MSE、MAE、R²|
|聚类指标	|无监督学习	|轮廓系数、Davies-Bouldin指数|


```python
import tensorflow as tf

# 常用分类指标
metrics = [
    tf.keras.metrics.BinaryAccuracy(),  # 二分类准确率
    tf.keras.metrics.Precision(),       # 精确率
    tf.keras.metrics.Recall(),          # 召回率 / 灵敏度
    tf.keras.metrics.AUC()              # ROC曲线下面积
]

# 常用回归指标
metrics = [
    tf.keras.metrics.MeanSquaredError(),   # 均方误差，MSE
    tf.keras.metrics.MeanAbsoluteError(),  # 平均绝对误差，MAE
    tf.keras.metrics.RootMeanSquaredError()# 均方根误差，RMSE
]
```

## 评估


```python
# 1.编译模型时指定指标
model.compile(
 optimizer='adam',
 loss='binary_crossentropy',
 metrics=['accuracy', tf.keras.metrics.AUC()]   # accuracy(正确率) != precision
)

# 2.使用 evaluate 方法评估
test_loss, test_acc, test_auc = model.evaluate(
 test_images, test_labels, verbose=2
)                                                # 返回值数量取决于 model.compile() 的 metrics 参数，evaluate() 返回 [loss, accuracy] 和 metrics 的其他参数

# 3.自定义评估函数
import tensorflow as tf

@tf.function
def custom_metric(y_true, y_pred):
    threshold = 0.5
    y_pred = tf.cast(y_pred > threshold, tf.float32)
    # 计算准确率，而不仅仅是正例比例
    correct_predictions = tf.cast(tf.equal(y_true, y_pred), tf.float32)
    return tf.reduce_mean(correct_predictions)

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=[custom_metric, 'accuracy']  # 可以同时保留标准准确率指标作为参考
)
```

## TensorBoard 集成
TensorBoard 是 TensorFlow 的可视化工具，可以实时监控训练过程  
关键指标：损失函数，评估指标，学习率，权重分布，梯度变化  
  
使用流程    
1. 在训练模型时，通过 tf.keras.callbacks.TensorBoard 记录日志  
>```python
>import tensorflow as tf
>import datetime
> 
># 定义模型
>model = tf.keras.Sequential([...])
>model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
>
># 配置 TensorBoard 日志目录
>log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
>tensorboard_callback = tf.keras.callbacks.TensorBoard(
>    log_dir=log_dir,  # 日志保存路径
>    histogram_freq=1, # 每1个epoch记录一次直方图（0表示不记录）
>    write_graph=True, # 记录计算图
>    write_images=True # 记录权重分布图
>)
> 
># 训练模型并记录日志
>model.fit(
>    x_train, y_train,
>    epochs=5,
>    validation_data=(x_val, y_val),
>    callbacks=[tensorboard_callback]  # 添加回调
>)
>```  
>
>2. 启动 TensorBoard：  
>在终端运行以下命令（确保路径与 log_dir 一致）  
>``tensorboard --logdir=./logs``   
>或通过 Python 启动：
>```python
>%load_ext tensorboard  # 在 Jupyter Notebook 中
>%tensorboard --logdir logs/fit
>```

3. 访问 TensorBoard
打开浏览器，访问默认地址：  
http://localhost:6006/  

## 交叉验证 混淆矩阵分析


```python
import numpy as np
from sklearn.model_selection import KFold
from sklearn.datasets import make_classification
from sklearn.preprocessing import StandardScaler
from keras import models,layers
# from tensorflow.keras import models
# from tensorflow.keras import layers

# 生成一个简单的二分类数据集
X, y = make_classification(n_samples=1000, n_features=20, n_informative=2, n_redundant=10, random_state=42)

# 数据标准化
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 定义K折交叉验证
kf = KFold(n_splits=5, shuffle=True, random_state=42)

# 存储每次交叉验证的结果
fold_results = []

for train_index, val_index in kf.split(X_scaled):               # kf.split(train_data)返回的是每个折叠对应的训练集和验证集的索引
    X_train, X_val = X_scaled[train_index], X_scaled[val_index] # 提取每一折的训练集，和对应的标签
    y_train, y_val = y[train_index], y[val_index]               # 提取每一折的验证集，和对应的标签
    
    # 每次折叠都需要一个新的独立模型以避免权重共享带来的偏差
    model = models.Sequential([
        layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
        layers.Dense(32, activation='relu'),
        layers.Dense(1, activation='sigmoid')
    ])
    
    # 编译模型
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    
    # 训练模型
    model.fit(X_train, y_train, epochs=10, batch_size=32, verbose=0)
    
    # 在测试集上评估模型
    loss, accuracy = model.evaluate(X_val, y_val, verbose=0)
    fold_results.append(accuracy)
    
    print(f'Test Accuracy for Fold {len(fold_results)}: {accuracy:.4f}')

# 输出所有折叠的平均准确率
print(f'\nAverage Test Accuracy Across Folds: {np.mean(fold_results):.4f}')

```


```python
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# 获取预测结果
y_pred = model.predict(test_images)
y_pred_classes = np.argmax(y_pred, axis=1)

# 生成混淆矩阵
conf_mat = confusion_matrix(test_labels, y_pred_classes)

# 可视化
plt.figure(figsize=(10, 8))
sns.heatmap(conf_mat, annot=True, fmt='d')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

# 10分类结果，对角线元素：预测正确的样本数，非对角线元素：预测错误的样本数
```

## 示例


```python
import tensorflow as tf
from keras import models,layers,datasets,callbacks
# from tensorflow.keras import layers

# 1. 数据准备
(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()
train_images = train_images.reshape((60000, 28, 28, 1)).astype('float32') / 255
test_images = test_images.reshape((10000, 28, 28, 1)).astype('float32') / 255

# 2. 模型构建
model = tf.keras.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(10, activation='softmax')
])

# 3. 编译模型（添加你选择的指标）
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])

# 4. 训练模型（添加TensorBoard回调）
import os
log_dir = os.path.join("logs", "fit_1")  # 固定目录名
os.makedirs(log_dir, exist_ok=True)     # 确保目录存在
tensorboard = callbacks.TensorBoard(
    log_dir= log_dir,
    histogram_freq= 0,
    write_graph=False,
    write_images=False
    )

history = model.fit(train_images,train_labels,epochs=5,validation_data=(test_images,test_labels),callbacks=[tensorboard]) # callbacks参数是列表

# 5. 评估模型
test_loss, test_acc = model.evaluate(test_images,test_labels,verbose=2)

# 6. 混淆矩阵分析
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# 获取预测结果
y_pred = model.predict(test_images)
y_pred_classes = np.argmax(y_pred, axis=1)

# 生成混淆矩阵
conf_mat = confusion_matrix(test_labels, y_pred_classes)

# 可视化
plt.figure(figsize=(10, 8))
sns.heatmap(conf_mat, annot=True, fmt='d')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

```

# 模型调优
1. 先训练一个简单模型作为基准  
2. 避免同时改变多个参数  
3. 使用TensorBoard或MLflow跟踪实验  
3. 确保验证集代表真实数据分布  
4. 平衡调优效果与资源消耗  
  
## 学习率
>```python
># 使用Keras Tuner进行学习率搜索
>import keras_tuner as kt
>
>def build_model(hp):
>    model = tf.keras.Sequential()
>    model.add(tf.keras.layers.Dense(10))
>    # 设置学习率搜索范围
>    hp_learning_rate = hp.Choice('learning_rate', values=[1e-2, 1e-3, 1e-4])
>    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=hp_learning_rate),
>                  loss='mse')
>    return model
>
>tuner = kt.RandomSearch(build_model, objective='val_loss', max_trials=5)


```python
# 基本学习率设置示例
optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)

# 学习率衰减示例
initial_learning_rate = 0.1
lr_schedule = tf.keras.optimizers.schedules.ExponentialDecay(
    initial_learning_rate,
    decay_steps=10000, # 每 10000 步执行一次衰减
    decay_rate=0.96,   # 衰减率（每次衰减后学习率乘以 0.96）
    staircase=True)    # 如果为 True，学习率会在 decay_steps 的整数倍处阶梯式衰减（离散）；若为 False，则平滑连续衰减

optimizer = tf.keras.optimizers.SGD(learning_rate=lr_schedule)
```

## 批量
|批量大小	    |优点	       |缺点
|---           |---           |---|
|小批量(16-64)	|收敛快，泛化好	|训练不稳定
|中批量(64-256)	|平衡选择	    |需要更多内存
|大批量(256+)	|训练稳定	    |可能陷入局部最优

## 结构优化
宽度调整  
>```python
># 使用Keras Tuner自动搜索最佳层大小
>def build_model(hp):
>    model = tf.keras.Sequential()
>    # 搜索最佳神经元数量
>    hp_units = hp.Int('units', min_value=32, max_value=512, step=32)
>    model.add(tf.keras.layers.Dense(units=hp_units, activation='relu'))
>    model.add(tf.keras.layers.Dense(10))
>    model.compile(optimizer='adam', loss='mse')
>    return model
>```
  
深度调整   
1、从浅层网络开始，逐步增加深度   
2、使用残差连接(ResNet)解决深度网络梯度消失问题  
>```python
># 残差块示例
>def residual_block(x, filters):
>  shortcut = x
>  x = tf.keras.layers.Conv2D(filters, (3,3), padding='same')(x)
>  x = tf.keras.layers.BatchNormalization()(x)
>  x = tf.keras.layers.Activation('relu')(x)
>  x = tf.keras.layers.Conv2D(filters, (3,3), padding='same')(x)
>  x = tf.keras.layers.BatchNormalization()(x)
>  x = tf.keras.layers.Add()([shortcut, x])
>  return tf.keras.layers.Activation('relu')(x)
>```

##  正则化技术


```python
## Dropout
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.5),  # 50%的神经元会被随机丢弃
    tf.keras.layers.Dense(10)
])

## L1/L2正则化
# 添加L2正则化
tf.keras.layers.Dense(64, 
                     activation='relu',
                     kernel_regularizer=tf.keras.regularizers.l2(0.01))

## 早停法(Early Stopping)
early_stopping = tf.keras.callbacks.EarlyStopping(
    monitor='val_loss',
    patience=5,  # 连续5个epoch验证损失没有改善则停止
    restore_best_weights=True)  # 恢复最佳权重

model.fit(x_train, y_train, 
          validation_data=(x_test, y_val),
          epochs=100,
          callbacks=[early_stopping])
```

## 训练过程优化


```python
## 数据增强
# 图像数据增强示例
data_augmentation = tf.keras.Sequential([
    tf.keras.layers.RandomFlip("horizontal"),
    tf.keras.layers.RandomRotation(0.1),
    tf.keras.layers.RandomZoom(0.1),
])
# 使用增强数据训练
model.fit(data_augmentation(x_train), y_train, epochs=10)

## 批归一化(Batch Normalization)
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Activation('relu'),
    tf.keras.layers.Dense(10)
])

## 梯度裁剪
# 梯度裁剪防止梯度爆炸
optimizer = tf.keras.optimizers.Adam(clipvalue=1.0)
model.compile(optimizer=optimizer)
```

## 高级
>```python
>## 自动化超参数调优
># 使用Keras Tuner进行自动化调优
>tuner = kt.Hyperband(
>    build_model,
>    objective='val_accuracy',
>    max_epochs=10,
>    factor=3,
>    directory='my_dir',
>    project_name='intro_to_kt')
>
>tuner.search(x_train, y_train, epochs=10, validation_data=(x_val, y_val))
>best_model = tuner.get_best_models(num_models=1)[0]
>
>## 模型蒸馏
># 教师模型训练
>teacher = tf.keras.models.load_model('teacher_model.h5')
>
># 学生模型定义
>student = tf.keras.Sequential([...])
>
># 蒸馏损失
>def distillation_loss(y_true, y_pred, teacher_pred, temp=5.0):
>    return tf.keras.losses.kl_divergence(
>        tf.nn.softmax(teacher_pred/temp),
>        tf.nn.softmax(y_pred/temp))
>```

# 实例 - 图像分类


```python
# from tensorflow.keras.datasets import cifar10
# from tensorflow.keras import layers, models
import numpy as np
import tensorflow as tf
from keras import datasets,layers,models,callbacks
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体（如黑体）
plt.rcParams['axes.unicode_minus'] = False   # 解决负号显示问题

# 加载数据
(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()

# 类别名称
class_names = ['飞机', '汽车', '鸟', '猫', '鹿', '狗', '青蛙', '马', '船', '卡车']

# 归一化像素值到0-1范围
train_images = train_images / 255.0
test_images = test_images / 255.0

# 查看数据形状
print("训练集图像形状:", train_images.shape) # 训练集图像形状: (50000, 32, 32, 3)
print("训练集标签形状:", train_labels.shape) # 训练集标签形状: (50000, 1)

# 建立模型
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
    layers.MaxPooling2D((2, 2)),
    
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    
    layers.Conv2D(64, (3, 3), activation='relu'),
    
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10)  # 输出层，10个类别
])

# 编译模型
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# 训练模型
history = model.fit(train_images, train_labels, epochs=10, 
                    validation_data=(test_images, test_labels)) # 用测试集作验证集，严格来说应单独划分验证集

# 可视化
plt.plot(history.history['accuracy'], label='训练准确率')
plt.plot(history.history['val_accuracy'], label='验证准确率')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0, 1])
plt.legend(loc='lower right')
plt.show()

plt.plot(history.history['loss'],label='训练损失率')
plt.plot(history.history['val_loss'],label='验证损失率')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.ylim([0,2.5])
plt.legend(loc='upper right')
plt.show()

test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
print(f'\n测试准确率: {test_acc}')

# 直接对原始模型输出应用 softmax ，使输出为概率
predictions = tf.nn.softmax(model.predict(test_images[:5]))
# 对测试集前5张图进行预测
predicted_labels = np.argmax(predictions, axis=1)
# 显示预测结果
for i in range(5):
    print(f"预测: {class_names[predicted_labels[i]]} | 实际: {class_names[test_labels[i][0]]}")
```

# 实例 - 文本分类


```python
import tensorflow as tf
from keras import layers
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 从TensorFlow数据集加载IMDB数据
imdb = tf.keras.datasets.imdb

# 只保留前10000个最常出现的单词
(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=10000)

print("训练样本数: {}, 测试样本数: {}".format(len(train_data), len(test_data)))
# 输出：训练样本数: 25000, 测试样本数: 25000

# 查看第一条评论和标签
print(train_data[0])
# 输出：[1, 14, 22, 16, 43, 530, 973, 1622, 1385, 65, ...]
print(train_labels[:5])
# 输出：[1, 0, 0, 1, 0]        0 表示负面评论  1 表示正面评论

# 将整数序列转换为多热编码,也可以使用词嵌入(Embedding)代替多热编码
def vectorize_sequences(sequences, dimension=10000):
    """
    将整数序列（文本中的单词索引序列）转换为多热编码
    输入：一个整数序列的列表（例如 [[1, 5, 10], [2, 3]]，每个子列表代表一个样本的单词索引）
    输出：一个多维数组（通常是 NumPy 数组），其中每个样本被转换为一个多热向量
    多热编码：如果序列中包含某个索引，则对应位置设为 1,否则为 0(与独热编码不同,多热编码允许一个样本对应多个 1)
    """
    results = np.zeros((len(sequences), dimension))
    # 初始化一个全零矩阵，形状为 (样本数, 维度)
    for i, sequence in enumerate(sequences):
        # 遍历每个样本（sequence）及其索引（i）
        results[i, sequence] = 1.
        # 将 sequence 中的每个整数索引对应的位置设为 1
    return results

x_train = vectorize_sequences(train_data) # TensorFlow/Keras 的模型通常要求输入数据为 NumPy 数组或张量，而非 Python 列表
x_test = vectorize_sequences(test_data)   # 激活函数需要浮点数输入，同时避免计算的类型冲突，且现代 GPU 对浮点数的计算优化远好于整数

# 将标签转换为浮点数
y_train = np.asarray(train_labels).astype('float32')
y_val = np.asarray(test_labels).astype('float32')

model = tf.keras.Sequential([
    layers.Input(shape=(10000,)),
    layers.Dense(16, activation='relu'),
    layers.Dense(16, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['accuracy'])

history = model.fit(x_train,
                    y_train,
                    epochs=20,
                    batch_size=512,
                    validation_split=0.2,
                    )

# 绘制训练损失和验证损失
plt.plot(history.history['loss'], 'bo', label='Training loss')
plt.plot(history.history['val_loss'], 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

# 绘制训练准确率和验证准确率
plt.plot(history.history['accuracy'], 'bo', label='Training acc')
plt.plot(history.history['val_accuracy'], 'b', label='Validation acc')
plt.title('Training and validation accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

# 评估模型 损失和准确率
results = model.evaluate(x_test, y_val)
print(results)

# 进行预测
predictions = model.predict(x_test)
print(predictions[0])  # 第一条测试样本的预测概率
```

# 实例 - 回归问题


```python
# 波士顿房价预测
import tensorflow as tf
from keras.datasets import boston_housing
from keras import layers,models,callbacks,regularizers
from sklearn.model_selection import KFold

# 加载数据
(train_data, train_targets), (test_data, test_targets) = boston_housing.load_data()

# 数据标准化（重要步骤）
mean = train_data.mean(axis=0)
train_data -= mean
std = train_data.std(axis=0)
train_data /= std

test_data -= mean
test_data /= std

# 建立模型
def build_model():
    model = models.Sequential([
        layers.Input(shape=(train_data.shape[1],)),
        layers.Dense(64, activation='relu', kernel_regularizer=regularizers.l2(0.001)), #加入正则化
        layers.Dense(64, activation='relu', kernel_regularizer=regularizers.l2(0.001)),
        layers.Dense(32, activation='relu', kernel_regularizer=regularizers.l2(0.001)),
        layers.Dense(1)  # 输出层不需要激活函数
    ])
    return model

# 使用k折交叉验证
kf = KFold(n_splits=4, shuffle=True, random_state=42)
all_scores = []

for train_index, val_index in kf.split(train_data):                 # kf.split(train_data)返回的是每个折叠对应的训练集和验证集的索引
    X_train,X_val = train_data[train_index],train_data[val_index]
    y_train,y_val = train_targets[train_index],train_targets[val_index]

    model = build_model()
    model.compile(optimizer='rmsprop',
                  loss='mse',  # 均方误差 对较大误差给予更大惩罚
                  metrics=['mae'])  # 平均绝对误差 预测值与真实值差距的平均值
    
    history = model.fit(X_train, y_train,
                        epochs=100,
                        batch_size=16,
                        validation_data=(X_val, y_val),
                        verbose=0) # 设置verbose=0以减少输出信息
    
    val_mse, val_mae = model.evaluate(X_val, y_val, verbose=0)
    all_scores.append(val_mae)
print(f"各折叠验证MAE: {all_scores}")
print(f"平均验证MAE: {sum(all_scores)/len(all_scores)}")

# model = build_model()
# model.compile(optimizer='rmsprop',
#               loss='mse',  # 均方误差 对较大误差给予更大惩罚
#               metrics=['mae'])  # 平均绝对误差 预测值与真实值差距的平均值


# history = model.fit(train_data, train_targets,
#                     epochs=100,
#                     batch_size=16,
#                     validation_split=0.2) # 默认从训练数据的最后20%样本中划分验证集，若需随机划分，建议手动划分后通过validation_data传入，或在fit()中设置shuffle=True

# 在测试集上评估
test_mse_score, test_mae_score = model.evaluate(test_data, test_targets)
print(f"测试集MAE: {test_mae_score}")

# 对新数据进行预测
sample = test_data[0]  # 取测试集第一个样本
prediction = model.predict(sample.reshape(1, -1))
print(f"预测价格: {prediction[0][0]}, 实际价格: {test_targets[0]}")
```

# 模型保存与加载
TensorFlow 2.x 主要支持三种模型保存格式：
- SavedModel 格式（推荐）
  
- HDF5 格式（.h5 , 更通用）
  
- 旧版 Keras 格式
  
|特性	             |SavedModel	|HDF5      |
|---                 |---           |---       |
|包含自定义对象	      |是	         |需要额外配置|
|包含优化器状态	      |是	         |可选       |
|TensorFlow Serving	 |原生支持	     |不支持     |
|文件大小	          |较大	         |较小       |

## model.save
``model.save()``  
``model.save_weights()``  
  
保存后的目录结构  
my_model/  
├── assets/  
├── variables/  
│   ├── variables.data-00000-of-00001   
│   └── variables.index   
└── saved_model.pb   


```python
import tensorflow as tf

# 创建并训练一个简单模型
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.fit(x_train, y_train, epochs=5)

# 保存为SavedModel格式
model.save('my_model')  # 注意：没有文件扩展名
# 保存为HDF5格式
model.save('my_model.h5') # 注意.h5扩展名
```


```python
# 保存权重
model.save_weights('my_model_weights')

# 保存为HDF5格式的权重
model.save_weights('my_model_weights.h5')
# 对于大模型保存，使用save_weights替代save可以减少保存时间
```


```python
# 训练中断恢复：使用检查点回调定期保存模型
from keras import callbacks
# 创建检查点回调
callback = callbacks.ModelCheckpoint(
    filepath="training_1/cp.ckpt",
    monitor='val_loss',         # 监控指标，保留指标最佳的模型
    mode='min',                 # 指定监控指标的优化方向，确保正确识别最佳模型   'min'表示最小化指标，'max'表示最大化
    save_weights_only=True,     # 只保存权重（默认保存整个模型）
    verbose=1)

# 使用回调训练模型
model.fit(x_train, y_train,
          epochs=10,
          callbacks=[callback]) # 启用检查点保存
```

## models.load_model
``tf.keras.models.load_model()``  
``new_model.load_weights``


```python
# 从SavedModel加载
loaded_model = tf.keras.models.load_model('my_model')

# 从HDF5文件加载
loaded_model = tf.keras.models.load_model('my_model.h5')
```


```python
# 创建相同架构的模型
new_model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])
new_model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

# 加载权重
new_model.load_weights('my_model_weights')

# 或者对于.h5文件
new_model.load_weights('my_model_weights.h5')
```

## 自定义层/模型保存
跨版本兼容性问题  
- 尽量使用相同版本的 TensorFlow 保存和加载模型
  
- 对于生产环境，考虑使用 TensorFlow Serving 来避免版本问题


```python
# 自定义层示例
class CustomLayer(tf.keras.layers.Layer):
    def __init__(self, units=32, **kwargs):
        super().__init__(**kwargs)
        self.units = units
    
    def build(self, input_shape):
        self.w = self.add_weight(
            shape=(input_shape[-1], self.units),
            initializer="random_normal",
            trainable=True)
    
    def call(self, inputs):
        return tf.matmul(inputs, self.w)
    
    def get_config(self):
        config = super().get_config()
        config.update({"units": self.units})
        return config

# 使用自定义层并保存
model = tf.keras.Sequential([CustomLayer(10)])
model.compile(optimizer='adam', loss='mse')
model.save('custom_model')  # 会自动保存自定义层
```

# 模型转换与优化
在机器学习项目开发中，模型转换与优化是部署前的重要步骤  

TensorFlow 提供了多种工具和技术来帮助开发者将训练好的模型转换为适合不同部署环境的格式，并对其进行优化以提高性能

|技术类型	    |主要工具                           |适用场景|
|---|---|---|
|模型格式转换	|tf.saved_model, TFLiteConverter    |跨平台部署
|量化	        |TFLiteConverter                    |减小模型大小，提高推理速度
|剪枝	        |tfmot                              |减少参数数量
|硬件加速	     |TensorRT, Core ML                 |特定硬件优化
  
流程：  
训练好的Keras模型--保存为SaveModel--目标平台  
- 移动/嵌入端--TFlite转换--量化/剪枝--测试性能--部署
- 服务器--TensorRt优化--精度设置--测试性能--部署
- ios--CoreML转换

## TensorFlow Lite 
TensorFlow Lite 是针对移动和嵌入式设备的轻量级解决方案  
  
转换选项  
- optimizations：设置优化级别（默认、大小优化、延迟优化）  
- target_spec：指定目标设备特性  
- representative_dataset：用于量化校准的数据集  


```python
## 转换模型为 TFLite 格式
# 读取模型
converter = tf.lite.TFLiteConverter.from_saved_model('my_model') 
# 如果模型是 Keras 格式（.h5），需改用 from_keras_model()

# 转换模型   
tflite_model = converter.convert()   

# 保存转换后的模型
with open('model.tflite', 'wb') as f:
    f.write(tflite_model)
```

## 量化（Quantization）
量化通过降低数值精度来减小模型大小和提高推理速度。

|量化类型	|权重精度	|激活精度	|大小减少	|精度损失|
|---|---|---|---|---|
|无量化	    |FP32	    |FP32	    |0%	        |无|
|动态范围	|INT8	    |FP32	    |~75%	    |小|
|全整型	    |INT8	    |INT8	    |~75%	    |中等|
|FP16	    |P16	    |FP16	    |~50%	    |很小|


```python
## 优化并转换模型
# 读取模型
converter = tf.lite.TFLiteConverter.from_saved_model('my_model') 

# 优化模型
converter.optimizations = [tf.lite.Optimize.DEFAULT]  # 默认优化 其中包含动态范围量化
# 或量化（需校准数据）
converter.representative_dataset = ...  
converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]

# 转换模型   
tflite_model = converter.convert()   

# 保存转换后的模型
with open('model.tflite', 'wb') as f:
    f.write(tflite_model)
```

## 剪枝（Pruning）
剪枝通过移除不重要的神经元连接来减少模型参数
>```python
>import tensorflow_model_optimization as tfmot
>
># 定义剪枝参数
>prune_params = {
>    'pruning_schedule': tfmot.sparsity.keras.PolynomialDecay(
>        initial_sparsity=0.50,
>        final_sparsity=0.90,
>        begin_step=0,
>        end_step=1000
>    )
>}
>
># 应用剪枝
>model = tf.keras.Sequential([...])  # 你的模型
>model_for_pruning = tfmot.sparsity.keras.prune_low_magnitude(model, **prune_params)
>
># 训练剪枝模型
>model_for_pruning.compile(...)
>model_for_pruning.fit(...)
>
># 去除剪枝包装
>model_for_export = tfmot.sparsity.keras.strip_pruning(model_for_pruning)
>```

## TensorRT 优化（NVIDIA GPU）


```python
# 使用 TF-TRT 转换器
from tensorflow.python.compiler.tensorrt import trt_convert as trt

converter = trt.TrtGraphConverterV2(
    input_saved_model_dir='my_model', # 输入模型的路径
    precision_mode=trt.TrtPrecisionMode.FP16 # 设置优化精度为 FP16
)
converter.convert()
converter.save('trt_optimized_model')
```

## Core ML 转换（Apple 设备）
>```python
>import coremltools as ct
>
># 从 SavedModel 转换
>mlmodel = ct.convert('my_model')
>
># 保存 Core ML 模型
>mlmodel.save('model.mlmodel')
>```

# 分布式训练
分布式策略（Distribution Strategy）
>```python
># 常用分布式策略
>strategy = tf.distribute.MirroredStrategy()  # 单机多卡
>strategy = tf.distribute.MultiWorkerMirroredStrategy()  # 多机多卡
>strategy = tf.distribute.TPUStrategy()  # TPU集群
>strategy = tf.distribute.ParameterServerStrategy()  # 参数服务器架构
>```
  

数据并行:每个设备处理不同数据批次,实现简单，适合大多数场景,需要同步梯度  
模型并行:模型被拆分到不同设备,适合超大模型,实现复杂   

同步更新：所有设备完成计算后统一更新模型  
异步更新：设备独立计算并更新，无需等待  

MirroredStrategy 会自动按 GPU 数量分片批量数据  
MultiWorkerMirroredStrategy 需手动计算全局批量大小（batch_size * num_workers * num_gpus_per_worker）  

多 worker 训练时，仅主节点（task_id=0） 应保存模型，避免冲突  

单机单卡测试：设置
>```python
>os.environ['TF_CONFIG'] = '{"cluster": {"worker": ["localhost:2222"]}, "task": {"type": "worker", "index": 0}}' 
>```
模拟多 worker


```python
import tensorflow as tf
from keras import layers,models
# 1.设置分布式环境
# 初始化分布式策略
strategy = tf.distribute.MirroredStrategy()

# 查看可用设备数量
print(f"Number of devices: {strategy.num_replicas_in_sync}")

# 2.在策略范围内构建模型
with strategy.scope():
    # 在此范围内定义的所有变量将被镜像到所有设备
    model = models.Sequential([
        layers.Dense(128, activation='relu'),
        layers.Dense(10)
    ])
    
    model.compile(
        optimizer='adam',
        loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
        metrics=['accuracy']
    )

# 3.准备分布式数据集
# 加载数据集
def load_data():
    (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
    x_train = x_train.astype('float32') / 255.0  # 归一化
    x_test = x_test.astype('float32') / 255.0
    train_dataset = tf.data.Dataset.from_tensor_slices((x_train, y_train))
    test_dataset = tf.data.Dataset.from_tensor_slices((x_test, y_test))
    # 批量大小会自动按 GPU 数量分片
    train_dataset = train_dataset.shuffle(1000).batch(64 * strategy.num_replicas_in_sync)
    test_dataset = test_dataset.batch(64 * strategy.num_replicas_in_sync)
    return train_dataset, test_dataset

train_data, test_data = load_data()

# 4.训练模型
model.fit(train_data, epochs=5, validation_data=test_data)
```


```python
import tensorflow as tf

# 1. 配置 TPU
resolver = tf.distribute.cluster_resolver.TPUClusterResolver(tpu='grpc://your-tpu-address')
tf.config.experimental_connect_to_cluster(resolver)
tf.tpu.experimental.initialize_tpu_system(resolver)
strategy = tf.distribute.TPUStrategy(resolver)

# 2. 定义模型（同上，但在 strategy.scope() 内）
with strategy.scope():
    model = tf.keras.Sequential([...])
    model.compile(...)

# 3. 训练（需使用 tf.data.Dataset）
model.fit(train_dataset, epochs=5)
```

多机配置
>```python
># 在每个worker节点上设置TF_CONFIG环境变量
>import json
>import os
># 设置 TF_CONFIG 环境变量
>os.environ['TF_CONFIG'] = json.dumps({
>    'cluster': {
>        'worker': ["worker1.example.com:12345", "worker2.example.com:23456"] # 定义集群中的所有 Worker 节点及其网络地址（主机名:端口）
>    },
>    'task': {'type': 'worker', 'index': 0}  # 定义节点的角色和编号,每个worker的index不同
>})
>```

自定义训练循环
>```python
>@tf.function
>def train_step(inputs):
>    x, y = inputs
>    
>    with tf.GradientTape() as tape:
>        predictions = model(x, training=True)
>        loss = loss_object(y, predictions)
>    
>    gradients = tape.gradient(loss, model.trainable_variables)
>    optimizer.apply_gradients(zip(gradients, model.trainable_variables))
>    return loss
>
># 分布式训练步骤
>@tf.function
>def distributed_train_step(dataset_inputs):
>    per_replica_losses = strategy.run(train_step, args=(dataset_inputs,))
>    return strategy.reduce(tf.distribute.ReduceOp.SUM, per_replica_losses, axis=None)
>```

混合精度优化
>```python
>import tensorflow as tf
>
># 1. 启用混合精度
>policy = tf.keras.mixed_precision.Policy('mixed_float16')
># float16：用于加速计算（如矩阵乘法、卷积），减少显存占用
># float32：用于关键计算（如梯度更新、损失计算），避免数值不稳定
>tf.keras.mixed_precision.set_global_policy(policy)
>
># 2. 构建模型（自动应用混合精度）
>model = tf.keras.Sequential([
>    tf.keras.layers.Dense(128, activation='relu', input_shape=(784,)),
>    tf.keras.layers.Dense(10, activation='softmax')
>])
>
># 3. 编译模型（优化器也会自动处理混合精度）
>model.compile(
>    optimizer='adam',
>    loss='sparse_categorical_crossentropy',
>    metrics=['accuracy']
>)
>
># 4. 训练（输入数据建议转换为 float16）
>(x_train, y_train), _ = tf.keras.datasets.mnist.load_data()
>x_train = x_train.astype('float16') / 255.0  # 手动转换输入数据
>model.fit(x_train, y_train, batch_size=64, epochs=5)
>```

内存动态增长
>```python
>gpus = tf.config.experimental.list_physical_devices('GPU') # 检测当前系统中可用的 GPU 设备
>for gpu in gpus:
>    tf.config.experimental.set_memory_growth(gpu, True) # 对每个 GPU 设备设置内存分配策略为 “按需增长”（而非默认的“预先全部占用”）
>```

# 生产环境
部署架构
|部署方式	|延迟	|吞吐量	|资源使用	|适用场景|
|---|---|---|---|---|
|TensorFlow Serving	|中	|高	|中	|云服务、高并发|
|TFLite	|低	|中	|低	|移动/IoT设备|
|ONNX Runtime	|中	|高	|中	|多框架统一部署|
|自定义gRPC服务	|可调	|可调	|可调	|特殊需求场景|

>```python
># 使用Flask构建的简单模型服务
>from flask import Flask, request
>import tensorflow as tf
>
>app = Flask(__name__)
>model = tf.keras.models.load_model('path/to/model')
>
>@app.route('/predict', methods=['POST'])
>def predict():
>    data = request.json['data']
>    prediction = model.predict(data)
>    return {'prediction': prediction.tolist()}
>```
容器化：推荐使用Docker打包模型和环境  
服务发现：结合Kubernetes实现自动扩缩容  
监控集成：Prometheus + Grafana监控体系  

硬件加速
GPU优化技巧：
使用tf.config.optimizer.set_jit(True)启用XLA编译  
批量处理输入数据（典型批量大小32-256）  
使用混合精度训练(tf.keras.mixed_precision)  

TPU配置：
>```python
>resolver = tf.distribute.cluster_resolver.TPUClusterResolver()
>tf.config.experimental_connect_to_cluster(resolver)
>tf.tpu.experimental.initialize_tpu_system(resolver)
>strategy = tf.distribute.TPUStrategy(resolver)
>```

图优化
>```python
># 会话配置优化
>config = tf.compat.v1.ConfigProto()
>config.graph_options.optimizer_options.global_jit_level = tf.compat.v1.OptimizerOptions.ON_1
>config.gpu_options.allow_growth = True
>session = tf.compat.v1.Session(config=config)
>```



ML Pipeline设计
>```python
># 使用TFX构建的简单pipeline
>from tfx.components import Trainer
>from tfx.proto import trainer_pb2
>
>trainer = Trainer(
>    module_file=module_file,
>    transformed_examples=transform.outputs['transformed_examples'],
>    schema=infer_schema.outputs['schema'],
>    train_args=trainer_pb2.TrainArgs(num_steps=10000),
>    eval_args=trainer_pb2.EvalArgs(num_steps=5000))

# 生态系统
``TensorFlow Core``  
TensorFlow 的核心框架，提供基础的张量计算和自动微分功能，基础模型开发  
  
``TensorFlow.js``  
允许在浏览器和 Node.js 环境中运行机器学习模型的 JavaScript 库，浏览器端ML  
>```python
>// 在浏览器中加载预训练模型
>async function loadModel() {
>    const model = await tf.loadLayersModel('model.json');
>    return model;
>}
>```
  
``TensorFlow Lite``  
专为移动和嵌入式设备优化的轻量级解决方案  

``TensorFlow Extended (TFX)``  
端到端的机器学习平台，用于生产环境中的 ML 流水线  
>```python
># 定义 TFX 流水线组件
>example_gen = CsvExampleGen(input_base=path_to_csv)
>statistics_gen = StatisticsGen(examples=example_gen.outputs['examples'])
>```

``TensorFlow Hub``  
预训练模型库，可以轻松重用已有模型  
>```python
># 使用 TF Hub 中的预训练模型
>embed = hub.load("https://tfhub.dev/google/nnlm-en-dim128/1")
>embeddings = embed(["TensorFlow is great"])
>```

TensorFlow Serving
高性能服务系统，用于部署训练好的模型
>```python
># 启动 TensorFlow Serving 服务
>tensorflow_model_server --port=8500 --rest_api_port=8501 \
>    --model_name=my_model --model_base_path=/models/my_model
>```


# 自定义组件
- 自定义层(Custom Layers) - 实现新的神经网络层结构
- 自定义损失函数(Loss Functions) - 设计特定任务的优化目标
- 自定义评估指标(Metrics) - 定义独特的性能衡量标准
- 自定义训练循环(Training Loops) - 实现特殊训练逻辑


```python
# 简单自定义层示例
class SimpleDense(tf.keras.layers.Layer):
    def __init__(self, units=32):   # 初始化层的配置:指定该层的输出维度（神经元数量），默认为 32
        super().__init__()  # 初始化父类
        self.units = units  # 将 units 保存为实例变量，供后续方法使用

    def build(self, input_shape):   # 在第一次调用该层时（或显式调用 build() 时），根据输入形状动态创建权重参数
        self.w = self.add_weight(shape=(input_shape[-1], self.units))
        self.b = self.add_weight(shape=(self.units,))
        # 权重 w：形状为 (input_dim, units) 的矩阵，表示输入维度到输出维度的线性变换
        # 偏置 b：形状为 (units,) 的向量，表示每个输出神经元的偏置项
        # 通过 add_weight 方法添加可训练参数（TensorFlow 会自动跟踪这些参数）
        
    def call(self, inputs):  # 定义层的前向计算逻辑
        return tf.matmul(inputs, self.w) + self.b   #输入与权重矩阵相乘（线性变换） 加上偏置向量（广播机制会自动处理维度）
```

为什么需要自定义组件
- 解决特定领域问题
  - 计算机视觉中的特殊卷积操作
  - NLP 中的注意力机制变体
  - 推荐系统中的特征交叉方法
- 性能优化需求
  - 针对硬件优化的计算内核
  - 混合精度训练的特殊处理
- 研究创新
  - 实现论文中的新型网络结构
  - 实验自定义的正则化方法

自定义层开发详解
1. 基础结构  
每个自定义层需要继承 tf.keras.layers.Layer 并实现：  

- __init__() - 初始化配置参数
- build() - 创建权重变量(推荐)
- call() - 定义前向计算逻辑
- get_config() - 支持序列化(可选)

权重管理最佳实践

|方法	        |说明	        |使用场景|
|---|---|---|
|add_weight()	|自动管理权重	|大多数情况|
|直接创建变量	|更灵活控制	    |需要特殊初始化时|
|重用现有权重	|共享参数	    |注意力机制等|


```python
class CustomLayer(tf.keras.layers.Layer):
    def __init__(self, units=32, **kwargs):
        super().__init__(**kwargs)
        self.units = units
    
    def build(self, input_shape):
        self.kernel = self.add_weight(
            name="kernel",
            shape=(input_shape[-1], self.units),
            initializer="glorot_uniform"
        )
        self.bias = self.add_weight(
            name="bias",
            shape=(self.units,),
            initializer="zeros"
        )
    
    def call(self, inputs):
        return tf.matmul(inputs, self.kernel) + self.bias
    
    def get_config(self):
        return {"units": self.units}
```

2. 自定义损失函数开发
两种实现方式  

方式1：函数形式
>```python
>def custom_mse(y_true, y_pred):
>    squared_diff = tf.square(y_true - y_pred)
>    return tf.reduce_mean(squared_diff, axis=-1)
>```

方式2：类形式(继承Loss类)
>```python
>class CustomLoss(tf.keras.losses.Loss):
>    def __init__(self, regularization_factor=0.1):
>        super().__init__()
>        self.reg_factor = regularization_factor
>   
>    def call(self, y_true, y_pred):
>        mse = tf.reduce_mean(tf.square(y_true - y_pred))
>        reg = tf.reduce_sum(self.reg_factor * tf.abs(y_pred))
>        return mse + reg
>```

常见注意事项
- 确保计算过程可微分
- 处理不同形状的输入(如batch处理)
- 考虑数值稳定性(如添加小epsilon)

3. 自定义训练循环集成
>```python
>model = tf.keras.Sequential([...])
>optimizer = tf.keras.optimizers.Adam()
>loss_fn = CustomLoss()
>
>@tf.function  # 提升执行效率
>def train_step(x, y):
>    with tf.GradientTape() as tape:
>        preds = model(x)
>        loss = loss_fn(y, preds)
>    grads = tape.gradient(loss, model.trainable_weights)
>    optimizer.apply_gradients(zip(grads, model.trainable_weights))
>    return loss
>
>for epoch in range(epochs):
>    for x_batch, y_batch in train_dataset:
>        loss = train_step(x_batch, y_batch)
>    print(f"Epoch {epoch}, Loss: {loss.numpy()}")
>```

关键组件说明
- GradientTape - 自动微分记录器
- apply_gradients - 权重更新方法
- @tf.function - 图执行装饰器


```python
## 示例：图像超分辨率增强（PixelShuffle层） 通过亚像素卷积实现高效上采样，避免传统转置卷积的棋盘效应，提升图像细节恢复质量
class PixelShuffle(tf.keras.layers.Layer):
    def __init__(self, upscale_factor):
        super().__init__()
        self.upscale_factor = upscale_factor

    def call(self, inputs):
        return tf.nn.depth_to_space(inputs, self.upscale_factor)

# 应用场景：超分辨率模型（如ESRGAN）
model = Sequential([
    layers.Conv2D(64, 3, padding='same'),
    PixelShuffle(upscale_factor=2),  # 将低分辨率特征图上采样为高分辨率
    layers.Conv2D(3, 3, padding='same', activation='sigmoid')
])


## 示例：时间序列预测的分位数损失（QuantileLoss） 同时预测多个分位数（10%、50%、90%），提供预测区间而不仅是点估计，增强模型对不确定性的建模能力
class QuantileLoss(tf.keras.losses.Loss):
    def __init__(self, quantiles=[0.1, 0.5, 0.9]):
        super().__init__()
        self.quantiles = quantiles

    def call(self, y_true, y_pred):
        losses = []
        for i, q in enumerate(self.quantiles):
            error = y_true - y_pred[:, i]
            losses.append(tf.maximum(q * error, (q - 1) * error))
        return tf.reduce_mean(tf.add_n(losses))

# 应用场景：多步时间序列预测（如电力负荷预测）
model.compile(optimizer='adam', loss=QuantileLoss(quantiles=[0.1, 0.5, 0.9]))
```
