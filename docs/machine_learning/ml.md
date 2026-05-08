```python
#在 Jupyter Notebook 中，使用以下代码来打印当前工作目录：
import os
print(os.getcwd())
```

# 基本函数

# 数据集划分与基本信息

## 留出法

### sklearn.model_selection.train_test_split

sklearn.model_selection.train_test_split(*arrays, test_size=None, train_size=None, random_state=None, shuffle=True, stratify=None)  
参数说明：  
  
arrays：可以是列表、numpy数组、scipy稀疏矩阵或pandas的数据框  
test_size：可以为浮点、整数或None，默认为None  
- 若为浮点时，表示测试集占总样本的百分比  
- 若为整数时，表示测试样本样本数  
- 若为None时，test size自动设置成0.25  
random_state：可以为整数、RandomState实例或None，默认为None  
- 若为None时，每次生成的数据都是随机，可能不一样  
- 若为整数时，每次生成的数据都相同  
stratify：可以为类似数组或None  
- 若为None时，划分出来的测试集或训练集中，其类标签的比例也是随机的  
- 若不为None时，划分出来的测试集或训练集中，其类标签的比例同输入的数组中类标签的比例相同，可以用于处理不均衡的数据集  



```python
# import pandas as pd
# from sklearn.model_selection import train_test_split

# # 导入三个CSV文件
# file1 = r'd:\VS Code python program\machine_learing\wine_data.csv'
# file2 = r'd:\VS Code python program\machine_learing\breast_cancer.csv'
# file3 = r'd:\VS Code python program\machine_learing\prices.csv'

# data1 = pd.read_csv(file1)
# data2 = pd.read_csv(file2)
# data3 = pd.read_csv(file3)

# #划分训练集和测试集
# # 划分特征X和目标变量y
# # 最后一列是目标变量，其他列是特征
# X = data1.iloc[:,:-1]  # 所有行，除了最后一列
# y = data1.iloc[:,-1]   # 所有行，最后一列
# data.iloc[:, :-1]选择了所有行和除了最后一列以外的所有列(:-1表示从第一列到倒数第二列)。而data.iloc[:, -1]选择了所有行的最后一列。

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# # 显示数据集的基本信息

# print(data1.info())

# print(data1.describe())

# # 打印出一部分数据
# print("\nData1 Head:")
# print(data1.head())
```


```python
# 参考课程资料中的“03-机器学习库Scikit-learn.zip”，读取附件中的三个训练数据集，并参考教材P25-26页内容，
# 用一种方法划分出训练集S和测试集T，显示出数据集的基本信息，并打印出一部分数据。


import pandas as pd
from sklearn.model_selection import train_test_split


# 修复列名并读取文件
column_names = [
    'Alcohol', 'Malic_acid', 'Ash', 'Alcalinity', 'Magnesium',
    'Phenols', 'Flavanoids', 'Nonflavanoid_phenols', 'Proanthocyanins',
    'Color_intensity', 'Hue', 'OD280_OD315', 'Proline', 'Class'
]

# 读取CSV文件
file1 = r"d:\VS Code python program\machine_learing\wine_data.csv"
file2 = r'd:\VS Code python program\machine_learing\breast_cancer.csv'
file3 = r'd:\VS Code python program\machine_learing\prices.csv'
data = pd.read_csv(
    file1, 
    header=None,          # 忽略原文件标题行
    names=column_names,   # 使用自定义列名
    skiprows=1            # 跳过原文件第一行
)

# 划分训练集和测试集
# 特征列
X = data.drop('Class', axis=1)# 从data数据框中删除名为Class的列，axis=1表示操作是在列上进行的(axis=0表示在行上进行操作)
# 目标列
y = data['Class']             # 选取了名为Class的列

# 划分数据集
X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.2,  # 80%训练集,20%测试集
    random_state=42,
    stratify=y  # 保持类别比例
)

# 显示数据集信息
print("="*50)
print("数据集基本信息：")
print(data.info()) # 显示数据类型和内存使用

print("\n" + "="*50)
print("数据集统计信息：") 
print(data.describe()) # 显示统计信息,均值、标准差等

print("\n" + "="*50)
print("数据集前5行: ")
print(data.head())

print("\n" + "="*50)
print("类别分布：")
print(y.value_counts()) # 显示类别分布

print("\n" + "="*50)
print("训练集大小：", X_train.shape)
print("测试集大小：", X_test.shape)


```

### stratify参数

# 错误率与精度&查准率、查全率与F1

>```py
># 真实标签/目标标签
>y_true = np.array([1, 0, 1, 1, 0, 1, 1, 0, 1, 0])
>
># 预测标签   
>y_pred = np.array([1, 1, 1, 1, 0, 1, 1, 1, 1, 0])  
>TP = sum((y_pred==1)==(y_pred==y_true))
>FP = sum((y_pred==1)==(y_pred!=y_true))
>FN = sum((y_pred==0)==(y_pred!=y_true))
>TN = sum((y_pred==0)==(y_pred==y_true))
># 精度/准确率(accuracy)  
>accuracy = sum(y_true==y_pred)/len(y_true)
># 查准率(precision)  
>precision = TP / (TP + FP)
># 查全率/召回率(recall)  
>recall = TP / (TP + FN)
># F1  
>f1_score = 2 * precision * recall / (precision + recall)
>
># 也可使用sklearn库计算精度、查准率、查全率与F1:
># 精度/准确率(accuracy)  
>sklearn.metrics.accuracy_score(y_true, y_pred, *, normalize=True, sample_weight=None)
># 查准率(precision)  
>sklearn.metrics.precision_score(y_true, y_pred, *, labels=None, pos_label=1, average='binary', sample_weight=None, zero_division='warn')
># 查全率/召回率(recall)  
>sklearn.metrics.recall_score(y_true, y_pred, *, labels=None, pos_label=1, average='binary', sample_weight=None, zero_division='warn')
># F1  
>sklearn.metrics.f1_score(y_true, y_pred, *, labels=None, pos_label=1, average='binary', sample_weight=None, zero_division='warn')
># 参数含义请参考：https://scikit-learn.org


```python
import numpy as np


ndarray = np.ndarray


def task(y_true: ndarray, y_pred: ndarray):
    
    '''
    二分类任务,正标签为1,负标签为0
    y_true: 数组1*n, 真实标签
    y_pred: 数组1*n, 预测标签
    '''

    TP = sum((y_pred==1)==(y_pred==y_true))
    FP = sum((y_pred==1)==(y_pred!=y_true))
    FN = sum((y_pred==0)==(y_pred!=y_true))
    TN = sum((y_pred==0)==(y_pred==y_true))
    
    precision = TP / (TP + FP)
    
    '''
    任务描述：根据公式实现查全率(recall)和F1
    '''
    ########## Begin ##########
    recall = TP / (TP + FN)
    f1_score = 2 * precision * recall / (precision + recall)

    ########## End ##########
    
    return precision, recall, f1_score

```

# 线性回归

## LinearRegression()

LinearRegression的构造函数中有两个常用的参数可以设置：  
fit_intercept：是否有截据，如果没有则直线过原点，默认为Ture。  
normalize：    是否将数据归一化,默认为False。  

LinearRegression类中的fit函数用于训练模型，fit函数有两个向量输入：  
X：大小为`样本数量*特征数量`的ndarray，存放训练样本  
Y：值为整型，大小为`样本数量`的ndarray，存放训练样本的标签值(目标)  

LinearRegression类中的predict函数用于预测，返回预测值，predict函数有一个向量输入：  
X：大小为`样本数量*特征数量`的ndarray，存放预测样本  

LinearRegression的使用代码如下：  
lr = LinearRegression()  
lr.fit(X_train, Y_train)  
predict = lr.predict(X_test)  


```python
import pandas as pd
from sklearn.linear_model import LinearRegression

# 获取已经划分好的训练数据和标签
train_data = pd.read_csv('./step3/train_data.csv')
train_label = pd.read_csv('./step3/train_label.csv')['target']

# 获取已经划分好的测试数据
test_data = pd.read_csv('./step3/test_data.csv')

# 初始化线性回归模型
lr = LinearRegression(fit_intercept=True, normalize=False)  

# 训练模型
lr.fit(train_data, train_label)

# 对测试集进行预测
predict = lr.predict(test_data)

# 将预测结果保存到 CSV 文件中
result = pd.DataFrame(predict, columns=['result'])
result.to_csv('./step3/result.csv', index=False)
# pd.DataFrame() 是Pandas库中用于创建DataFrame对象的函数。DataFrame是Pandas中的一种数据结构，它以表格形式存储数据，类似于Excel中的工作表或SQL数据库中的表。
# columns=['result'] 是一个参数，用于指定DataFrame中列的名称
# to_csv() 是DataFrame对象的一个方法，用于将DataFrame的内容保存到一个CSV文件中
# index=False 是一个参数，用于指定是否将DataFrame的索引（行标签）保存到CSV文件中。index=False，意味着不保存


```

# 逻辑回归

逻辑回归是通过回归的思想来解决二分类问题的算法。

sigmoid函数的公式为：
σ(t)=1/(1+e^−t)

numpy.exp()函数可以实现 e 的幂运算


```python
import numpy as np
def sigmoid(t):
    '''
    完成sigmoid函数计算
    t: 负无穷到正无穷的实数
    return: 转换后的概率值
    可以考虑使用np.exp()函数
    '''
    #********** Begin **********#
    t=1/(1+np.exp(-t))
    return t
    #********** End **********#
```

## LogisticRegression()

LogisticRegression可以实现多分类。LogisticRegression的构造函数中有三个常用的参数可以设置：  
solver：{'newton-cg' ,  'lbfgs',  'liblinear',  'sag',  'saga'}， 分别为几种优化算法。默认为liblinear；  
C：正则化系数的倒数，默认为 1.0 ，越小代表正则化越强；  
max_iter：最大训练轮数，默认为 100 。  

和sklearn中其他分类器一样，LogisticRegression类中的fit函数用于训练模型，fit函数有两个向量输入：  
X：大小为 `样本数量*特征数量` 的ndarray，存放训练样本；  
Y：值为整型，大小为 `样本数量` 的ndarray，存放训练样本的分类标签。  

LogisticRegression类中的predict函数用于预测，返回预测标签，predict函数有一个向量输入：  
X：大小为`样本数量*特征数量`的ndarray，存放预测样本。  

LogisticRegression的使用代码如下：  
logreg = LogisticRegression(solver='lbfgs',max_iter =10,C=10)  
logreg.fit(X_train, Y_train)  
result = logreg.predict(X_test)  

## 参数选择

Solver 选择：
liblinear：适用于小数据集，特别是当特征是稀疏的（即大部分特征值为零）时。它也支持 L1 正则化。
lbfgs、newton-cg 和 sag：这些求解器适用于大数据集，并且支持 L2 正则化。
lbfgs 是一个优秀的通用求解器，特别是对于 L2 惩罚和小数据集。
newton-cg 是基于牛顿法的求解器，适用于大数据集，但可能需要更多的内存。
sag 和 saga 是基于随机平均梯度的求解器，适用于大数据集和在线学习场景。

C 参数调整：
C 是正则化强度的倒数。较小的 C 值指定了更强的正则化。
如果模型过拟合（即在训练数据上表现良好，但在测试数据上表现不佳），尝试减小 C 值以增加正则化强度。
如果模型欠拟合（即在训练数据和测试数据上表现都不佳），尝试增加 C 值以减少正则化强度。
可以通过交叉验证来找到最佳的 C 值。

max_iter 参数调整：
max_iter 是求解器的最大迭代次数。
如果模型在达到最大迭代次数之前还没有收敛，可以尝试增加 max_iter 的值。
一般来说，对于大数据集和复杂的模型，可能需要更多的迭代次数来确保收敛。
但是，增加迭代次数会增加计算成本和时间。

## 手写图像识别


```python
from sklearn.linear_model import LogisticRegression

def digit_predict(train_image, train_label, test_image):
    '''
    实现功能：训练模型并输出预测结果
    :param train_sample: 包含多条训练样本的样本集,类型为ndarray,shape为[-1, 8, 8]
    :param train_label: 包含多条训练样本标签的标签集,类型为ndarray
    :param test_sample: 包含多条测试样本的测试集,类型为ndarry
    :return: test_sample对应的预测标签
    '''

    #************* Begin ************#
    #LogisticRegression 需要二维特征矩阵作为输入
    train_image_reshaped = train_image.reshape(-1, 64)
    test_image_reshaped = test_image.reshape(-1, 64)
    # 将训练集和测试集的图像数据从三维展平为二维
    # 形状从 [-1, 8, 8] 变为 [-1, 64]
    logreg = LogisticRegression(solver='lbfgs',max_iter =200,C=3)
    logreg.fit(train_image_reshaped, train_label)
    result = logreg.predict(test_image_reshaped)
    return result
    #************* End **************#
```

# 决策树

## DecisionTreeClassifier()
有两个常用的参数可以设置：  
criterion:划分节点时用到的指标。有gini（基尼系数）,entropy(信息增益)。若不设置，默认为gini  
max_depth:决策树的最大深度，如果发现模型已经出现过拟合，可以尝试将该参数调小。若不设置，默认为None  

事件越确定基尼系数越低，越模棱两可基尼系数就越高。所以基尼系数与信息熵类似，不确定性越高，基尼系数越高    

DecisionTreeClassifier类中的fit函数用于训练模型，fit函数有两个向量输入：  
X：大小为`样本数量*特征数量`的ndarray，存放训练样本  
Y：值为整型，大小为`样本数量`的ndarray，存放训练样本的分类标签  

DecisionTreeClassifier类中的predict函数用于预测，返回预测标签，predict函数有一个向量输入：  
X：大小为`样本数量*特征数量`的ndarray，存放预测样本  

DecisionTreeClassifier的使用代码如下：  
clf = tree.DecisionTreeClassifier()  
clf.fit(X_train, Y_train)  
result = clf.predict(X_test)   


```python
from sklearn.tree import DecisionTreeClassifier
from sklearn import datasets

#加载鸢尾花数据集
iris = datasets.load_iris()
#X表示特征,y表示标签
X = iris.data
y = iris.target

def iris_predict(train_sample, train_label, test_sample):
    '''
    实现功能:1.训练模型 2.预测
    :param train_sample: 包含多条训练样本的样本集,类型为ndarray
    :param train_label: 包含多条训练样本标签的标签集,类型为ndarray
    :param test_sample: 包含多条测试样本的测试集,类型为ndarry
    :return: test_sample对应的预测标签
    '''
    
    # ************* Begin ************#
    clf = DecisionTreeClassifier(criterion='entropy', max_depth=3)
    clf.fit(train_sample, train_label)
    result = clf.predict(test_sample)
    return result
    # ************* End **************#
```

## 计算原理


```python
import numpy as np
from sklearn import datasets
from collections import Counter


# 划分函数
def split(x,y,d,value):
    # x: 数据集的特征矩阵
    # y: 数据集的标签向量
    # d: 划分属性的索引，表示根据哪个特征进行划分。
    # 注意这里的索引是从0开始的，x[:,d]表示取所有样本的第d+1个特征
    index_a=(x[:,d]<=value)
    # 生成一个布尔向量，其中每个元素对应于x中的一行（一个样本），如果第d+1个特征的值小于等于value，则对应位置为True，否则为False
    index_b=(x[:,d]>value)
    # 生成另一个布尔向量，与index_a相反，如果第d+1个特征的值大于value，则对应位置为True，否则为False
    return x[index_a],x[index_b],y[index_a],y[index_b]
    # x[index_a]:根据index_a布尔向量，从x中选取满足条件(第d+1个特征的值小于等于value)的样本
    # x[index_b]:根据index_b布尔向量，从x中选取不满足条件（第d+1个特征的值大于value）的样本
    # y[index_a]:根据index_a布尔向量，从y中选取与子集A对应的标签
    # y[index_b]:根据index_b布尔向量，从y中选取与子集B对应的标签



# 信息熵的计算
def entropy(y):
    # 确保输入是numpy数组
    y = np.array(y)
    # 计算每个类别的频率
    unique_y, counts = np.unique(y, return_counts=True)
    #unique_y 包含了 y 数组中的唯一值（即类别标签），而 counts 数组则包含了与 unique_y 中每个标签相对应的计数，即该标签在 y 数组中出现的次数。
    pro = counts / len(y)
    # 计算信息熵
    res = np.sum(-pro * np.log(pro))
    return res



# 计算最优划分属性和值的函数
def try_spit(x,y):
    # x:一个NumPy数组
    # y:：一个一维数组，包含与 x 中每个样本对应的标签或目标值
    best_entropy=float("inf")
    # 初始化 best_entropy 为正无穷大，表示开始时还没有找到任何分割点
    best_d,best_v=-1,-1
    # 初始化 best_d 和 best_v 为 -1，表示还没有确定最佳分割特征和分割值
    for d in range(x.shape[1]):
        sorted_index=np.argsort(x[:,d])
        # 对该特征列的值进行排序，并获取排序后的索引
        for i in range(1,len(x)):
            if x[sorted_index[i-1],d] != x[sorted_index[i],d]:
                v=(x[sorted_index[i-1],d]+x[sorted_index[i],d])/2
                # 遍历排序后的索引，并通过索引访问特征值，尝试在每个不同的特征值之间找到最佳分割点。如果当前位置与前一个位置的特征值不同，则计算这两个值的中点作为候选分割值 v。
                x_l,x_r,y_l,y_r=split(x,y,d,v)
                e=entropy(y_l)+entropy(y_r)
                # 计算分割后的熵 e，即左半部分和右半部分标签的熵之和
                if e<best_entropy:
                    best_entropy,best_d,best_v=e,d,v
                    # 如果当前分割的熵小于 best_entropy，则更新 best_entropy、best_d 和 best_v 为当前分割的熵、特征和分割值。
    return best_entropy,best_d,best_v
    # best_entropy: 分割后的最小熵值。
    # best_d: 最佳分割特征的索引。
    # best_v: 最佳分割点的值



# 加载数据(鸢尾花)
d=datasets.load_iris()
x=d.data[:,2:] #只选择了数据集中的最后两个特征
y=d.target # 标签
# 计算出最优划分属性和最优值
best_entropy=try_spit(x,y)[0]
best_d=try_spit(x,y)[1]
best_v=try_spit(x,y)[2]
# 使用最优划分属性和值进行划分
x_l,x_r,y_l,y_r=split(x,y,best_d,best_v)
# 打印结果
print("叶子结点的熵值：")
print(entropy(y_l))
print("分支结点的熵值：")
print(entropy(y_r))
```

# Autograd

在训练一个神经网络时，梯度的计算是一个关键的步骤，它为神经网络的优化提供了关键数据  
但是在面临复杂神经网络的时候导数的计算就成为一个难题，要求人们解出复杂、高维的方程是不现实的  
这就是自动微分出现的原因，当前最流行的深度学习框架如 PyTorch、Tensorflow 等都提供了自动微分的支持，让人们只需要很少的工作就能自动计算出复杂函数的梯度  

## Pytorch 中的 Autograd

Tensor(张量) 是 PyTorch 实现多维数组计算和自动微分的关键数据结构  
当设置 .requires_grad = True 之后，在其上进行的各种操作就会被记录下来，用于后续的梯度计算，其内部实现机制被称为动态计算图(dynamic computation graph)   

autograd 机制能够记录作用于 Tensor 上的所有操作，生成一个动态计算图。图的叶子节点是输入的数据，根节点是输出的结果   
当在根节点调用 .backward() 的时候就会从根到叶应用链式法则计算梯度  
默认情况下，只有 .requires_grad 和 is_leaf 两个属性都为 True 的节点才会被计算导数，并存储到 grad 中  

### requires_grad属性

requires_grad 是 PyTorch 中Tensor的一个属性，用于指示是否需要对张量进行梯度计算  
requires_grad 属性默认为 False，默认是不需要求导的  
requires_grad=True：表示需要对这个张量进行梯度计算，且所有依赖它的节点 requires_grad 也会是 True  

### backward函数

backward() 函数是 PyTorch 中用于执行反向传播的关键函数，在需要被求导的节点上调用 backward 函数会计算梯度值到相应的节点上  
backward 需要一个重要的参数 grad_tensor，但如果节点只含有一个标量值，这个参数就可以省略  

backward 函数本身没有返回值，它计算出来的梯度存放在叶子节点的 grad 属性中  
PyTorch 文档中提到，如果 grad 属性不为空，新计算出来的梯度值会直接加到旧值上面  

为什么不直接覆盖旧的结果呢？这是因为有些 Tensor 可能有多个输出，那么就需要调用多个 backward  
叠加的处理方式使得 backward 不需要考虑之前有没有被计算过导数，只需要加上去就行了，这使得设计变得更简单
因此我们用户在反向传播之前，常常需要用 zero_grad 函数对导数手动清零，确保计算出来的是正确的结果

### 示例

>```
>import torch
># 导入了 PyTorch 库，并将 torch.Tensor 赋值给 Tensor
>Tensor = torch.Tensor
># 这样做并不是必需的，可以直接使用 torch.Tensor，但这样写可能在某些情况下使代码更简洁
>
>def task(x: Tensor) -> Tensor:
>    # 定义了一个名为 task 的函数，它接受一个 Tensor 类型的参数 x，并返回一个 Tensor 类型的值。这个函数的目的是计算并返回输入张量 x 的梯度。
>
>    y = 2*x + 6
>
>    z = y * y * 3
>    # 将 y 的平方乘以 3，得到新的张量 z。注意，这里的乘法是逐元素的，不是矩阵乘法
>
>    out = torch.mean(3*z)
>    # 将 z 乘以 3，然后计算结果的均值，得到标量 out。torch.mean 函数会计算张量中所有元素的平均值
>    
>    out.backward() #计算梯度
>    # 自动微分的核心部分。它调用 out 的 .backward() 方法，触发反向传播过程。
>    # 在反向传播过程中，PyTorch 会沿着计算图从 out 开始，逆向计算每个节点的梯度，并将梯度存储在各个张量的 .grad 属性中。
>
>    result = x.grad
>    # 从 x 的 .grad 属性中读取梯度值，并将其存储在 result 中
>    # x.grad 将包含 x 对 out 的梯度，即  ∂x/∂out
>    return result
>```


## 静态图动态图设计

目前神经网络框架分为静态图框架和动态图框架，PyTorch 和 TensorFlow、Caffe 等框架最大的区别就是他们拥有不同的计算图表现形式  
TensorFlow 使用静态图，这意味着我们先定义计算图，然后不断使用它，而在 PyTorch 中，每次都会重新构建一个新的计算图  

动态图比较方便 debug，使用者能够用任何他们喜欢的方式进行 debug，同时非常直观  
而静态图是通过先定义后运行的方式，之后再次运行的时候就不再需要重新构建计算图，所以速度会比动态图更快  

动态图：在计算的时候，就会把计算过程动态图存储起来。每次前向过程都会重新建立一个新图  
静态图：静态图需要预先定义好运算规则流程，然后把运算流程存储下来  

动态图：运算与搭建同时进行；灵活，易调节  
静态图：先搭建图，后运算；高效，不灵活  

∂w/∂y= ∂w/∂a * ∂a/∂y + ∂w/∂b *　∂b/∂y =2×w+x+1=5  
>```
>w = torch.tensor([1.],requires_grad = True)
>x = torch.tensor([2.],requires_grad = True)
>a = w+x
>b = w+1
>y = a*b
>y.backward()
>print(w.grad)
>
>输出：
>tensor([5.])
>```

为了减少内存，在反向传播结束之后，非叶子节点的梯度会被释放掉  
>```
>w = torch.tensor([1.],requires_grad = True)
>x = torch.tensor([2.],requires_grad = True)
>a = w+x
>b = w+1
>y = a*b
>y.backward()
>print(w.is_leaf,x.is_leaf,a.is_leaf,b.is_leaf,y.is_leaf)
>print(w.grad,x.grad,a.grad,b.grad,y.grad)
>
>输出：
>True True False False False
>tensor([5.]) tensor([2.]) None None None
>```
可以看到只有 x 和 w 是叶子节点，然后反向传播计算完梯度后(.backward() 之后)，只有叶子节点的梯度保存下来了  
也可以通过 .retain_grad() 来保留非任意节点的梯度值  

>```
>w = torch.tensor([1.],requires_grad = True)
>x = torch.tensor([2.],requires_grad = True)
>a = w+x
>a.retain_grad()
>b = w+1
>y = a*b
>y.backward()
>print(w.is_leaf,x.is_leaf,a.is_leaf,b.is_leaf,y.is_leaf)
>print(w.grad,x.grad,a.grad,b.grad,y.grad)
>
>输出：
>True True False False False
>tensor([5.]) tensor([2.]) tensor([2.]) None None
>```

torch.tensor 有一个属性 grad_fn,grad_fn 的作用是记录创建该张量时所用的函数，这个属性反向传播的时候会用到  
例如在上面的例子中，y.grad_fn=MulBackward0，表示 y 是通过乘法得到的,所以求导的时候就是用乘法的求导法则  
同样的，a.grad=AddBackward0 表示 a 是通过加法得到的，使用加法的求导法则  
>```
>w = torch.tensor([1.],requires_grad = True)
>x = torch.tensor([2.],requires_grad = True)
>a = w+x
>a.retain_grad()
>b = w+1
>y = a*b
>y.backward()
>print(y.grad_fn)
>print(a.grad_fn)
>print(w.grad_fn)
>
>输出：
><MulBackward0 object at 0x7f95016326d8>
><AddBackward0 object at 0x7f96b832d3c8>
>None
>```

## 正向反向传播

正向传播（forward propagation）是指对神经网络沿着从输入层到输出层的顺序，依次计算并存储模型的中间变量（包括输出）  
反向传播（back-propagation）指的是计算神经网络参数梯度的方法  
总的来说，反向传播依据微积分中的链式法则，沿着从输出层到输入层的顺序，依次计算并存储目标函数有关神经网络各层的中间变量以及参数的梯度  

### 示例

使用神经网络拟合曲线：y=x^2−2x+3，给定 x 的范围为 (0,1)。为了简便起见，该神经网络不加入正则项。

编程示例

数据：
>```
>x_train = np.array([[3.3], [4.4], [5.5], [6.71], [6.93], [4.168],
>                    [9.779], [6.182], [7.59], [2.167], [7.042],
>                    [10.791], [5.313], [7.997], [3.1]], dtype=np.float32)
>y_train = np.array([[1.7], [2.76], [2.09], [3.19], [1.694], [1.573],
>                    [3.366], [2.596], [2.53], [1.221], [2.827],
>                    [3.465], [1.65], [2.904], [1.3]], dtype=np.float32)
>x_train = torch.from_numpy(x_train)
>y_train = torch.from_numpy(y_train)
>```
使用 pytorch 搭建网络结构，代码如下：
>```
># Linear Regression Model
>class LinearRegression(nn.Module):
>    def __init__(self):
>        super(LinearRegression, self).__init__()
>        self.linear = nn.Linear(1, 1)  # input and output is 1 dimension
>    def forward(self, x):
>        out = self.linear(x)
>        return out
>```
训练网络参数，代码如下：
>```
>model = LinearRegression()
># 定义loss和优化函数
>criterion = nn.MSELoss()
>optimizer = optim.SGD(model.parameters(), lr=1e-4)
>num_epochs = 2000
>for epoch in range(num_epochs):
>    inputs = Variable(x_train)
>    target = Variable(y_train)
>    # 正向传播
>    out = model(inputs)
>    loss = criterion(out, target)
>    # 反向传播
>    optimizer.zero_grad()
>    loss.backward()
>    # 更新参数
>    optimizer.step()
>    if (epoch+1) % 20 == 0:
>        print('Epoch[{}/{}], loss: {:.6f}'
>            .format(epoch+1, num_epochs, loss.data))
>```

>```
>import torch
>from torch import nn, optim
>from torch.autograd import Variable
>import numpy as np
>
># 训练数据
>x_train = np.array([[3.3], [4.4], [5.5], [6.71], [6.93], [4.168],
>                    [9.779], [6.182], [7.59], [2.167], [7.042],
>                    [10.791], [5.313], [7.997], [3.1]], dtype=np.float32)
>
>y_train = np.array([[1.7], [2.76], [2.09], [3.19], [1.694], [1.573],
>                    [3.366], [2.596], [2.53], [1.221], [2.827],
>                    [3.465], [1.65], [2.904], [1.3]], dtype=np.float32)
>
># 将numpy数组转换为torch张量
>x_train = torch.from_numpy(x_train)
>y_train = torch.from_numpy(y_train)
>
># Linear Regression Model
>class LinearRegression(nn.Module):
>    """
>    线性回归模型类
>    """
>    def __init__(self):
>        super(LinearRegression, self).__init__()
>        self.linear = nn.Linear(1, 1)  # input and output is 1 dimension
>
>    def forward(self, x):
>        """
>        前向传播函数
>        参数:
>            x: 输入数据
>        返回:
>            out: 线性回归的输出
>        """
>        out = self.linear(x)
>        return out
>
>
>model = LinearRegression()
># 定义loss和优化函数
>criterion = nn.MSELoss()
>optimizer = optim.SGD(model.parameters(), lr=1e-4)
>
>def train():
>    """
>    训练函数
>    """
>    # 开始训练
>    num_epochs = 2000
>    for epoch in range(num_epochs):
>        inputs = Variable(x_train)
>        target = Variable(y_train)
>
>        # 正向传播
>        ########## Begin ##########
>        out = model(inputs)
>        ########## End ##########
>        
>        loss = criterion(out, target)
>        # 反向传播
>        optimizer.zero_grad()
>        ########## Begin ##########
>        loss.backward()
>        ########## End ##########
>
>        optimizer.step()
>
>        if (epoch+1) % 20 == 0:
>            print('Epoch[{}/{}], loss: {:.6f}'
>                .format(epoch+1, num_epochs, loss.data))
>    
>    return loss.data
>```

## 损失函数

一般来说，我们在进行机器学习任务时，使用的每一个算法都有一个目标函数，算法便是对这个目标函数进行优化  
特别是在分类或者回归任务中，便是使用损失函数(Loss Function)作为其目标函数，又称为代价函数(Cost Function)  

### 常见的损失函数
损失函数是用来评价模型的预测值与真实值的不一致程度，它是一个非负实值函数。通常使用 L(Y,f(x)) 来表示，损失函数越小，模型的性能就越好

- Zero-one Loss (0-1 损失)
    如果预测值与目标值不相等，那么为 1，否则为 0  
- Perceptron Loss(感知损失)

- Hinge Loss (铰链损失)
    如在 SVM 中解决几何间隔最大化问题  
- Cross Entropy (交叉熵损失函数)
    使用似然函数最大化时，其形式是进行连乘，但是为了便于处理，一般会套上 log，这样便可以将连乘转化为求和，由于 log 函数是单调递增函数，因此不会改变优化结果  
    因此 log 类型的损失函数也是一种常见的损失函数，如在 LR(Logistic Regression, 逻辑回归)中使用交叉熵(Cross Entropy)作为其损失函数 
- Square Loss (平方误差损失) 
    常用于回归中，若加和再求平均即 MSE

### 示例

>```
>import torch
>y1 = torch.randn(3, 5, requires_grad=True)
>y2 = torch.randn(3, 5)
># 均方差误差（MSELoss）
>loss = torch.nn.MSELoss()
>output = loss(y1, y2)
>print(output)
>输出：
>MSELoss:  tensor(1.8335, grad_fn=<MseLossBackward>)
>```

# 支持向量机

fit() 方法：用于训练 SVM，具体参数已经在定义 SVC对象的时候给出了，这时候只需要给出数据集X和X对应的标签y即可  
predict() 方法: 基于以上的训练，对预测样本T进行类别预测，因此只需要接收一个测试集T，该函数返回一个数组表示个测试样本的类别  


```python
from sklearn import svm # 调用sklearn实现svm算法
from sklearn.datasets import load_iris #加载sklearn库中的数据集
from sklearn.model_selection import train_test_split #划分测试集训练集
# 加载数据集
dataset = load_iris()
data_x = dataset.data #定义数据
data_y = dataset.target #定义标签
# 划分训练集和测试集
x_train,x_test,y_train,y_test = train_test_split(data_x,data_y,test_size=0.3)
#调用svm函数中的SVC核心算法
clf = svm.SVC()
clf = clf.fit(x_train,y_train) #开始训练svm模型
a = clf.predict(x_test) #开始测试
# 准确率
cnt = 0
for i in range(len(y_test)):  
    if a[i] == y_test[i]:
        cnt +=1
print(cnt/len(a))
# 评估模型
print(clf.score(x_test, y_test)) #它提供了一个缺省的评估法则来评估模型,简要的说,它用你训练好的模型在测试集上进行评分（0~1）1分代表最好
print(clf.support_vectors_)  #输出当前的支持向量
```

svm.SVC()函数中的参数设置详解  

- C: 正则化参数，float参数，默认值为1.0  
平衡分类间隔与误分类样本的容忍度，错误项的惩罚系数  
C越大，即对分错样本的惩罚程度越大，因此在训练样本中准确率越高，但是泛化能力降低，也就是对测试数据的分类准确率降低  
相反，减小C的话，容许训练样本中有一些误分类错误样本，泛化能力强  
对于训练样本带有噪声的情况，一般采用后者，把训练样本集中错误分类的样本作为噪声  

- kernel: 核函数，str参数 默认为 rbf   
可选参数有：  
linear: 线性核函数  
poly：多项式核函数  
rbf：径像核函数/高斯核  
sigmod :sigmod核函数  
precomputed: 核矩阵  
  
- gamma: 核函数系数，float参数 默认为 auto   
核函数系数，只对 rbf, poly, sigmod 有效  
控制核函数的“影响力范围”  
gamma越大：单个样本影响范围小，决策边界复杂（易过拟合）  
gamma越小：单个样本影响范围大，决策边界平滑（易欠拟合）  
如果 gamma 为 auto，代表其值为样本特征数的倒数，即1/n_features  

- coef0: 核函数独立项，float参数 默认为0.0    
核函数中的独立项，只有对 poly 和 sigmod 核函数有用，是指其中的参数c  

- probability：概率估计，bool 参数 默认为 False  
是否启用概率估计。 这必须在调用 fit() 之前启用，并且会 fit() 方法速度变慢。  
启用后可使用predict_proba()输出类别概率  

- cache_size： float参数 默认为200  
指定训练所需要的内存，以 MB 为单位，默认为200MB   

- class_weight：类别权重，字典类型或者 balance 字符串。默认为 None   
给每个类别分别设置不同的惩罚参数 C，如果没有给，则会给所有类别都给C=1，即前面参数指出的参数 C  
如果给定参数 balance，则使用y的值自动调整与输入数据中的类频率成反比的权重  

- verbose ： bool 参数 默认为 False  
是否启用详细输出。 此设置利用 libsvm 中的每个进程运行时设置，如果启用，可能无法在多线程上下文中正常工作。一般情况都设为  False，不用管它  

- max_iter ：最大迭代次数，int 参数 默认为-1  
最大迭代次数，如果为-1，表示不限制  

- random_state： int 型参数 默认为 None  
伪随机数发生器的种子,在混洗数据时用于概率估计  


```python
from sklearn import svm # 加载sklearn库来调用svm算法

X = [[0, 0], [1, 1]] #输入的数据
y = [0, 1]  #输入数据对应的类别(标签)
# 调用svm函数中的SVC核心算法
clf = svm.SVC();    
# 开始训练
clf = clf.fit(X,y)
# 测试
test_X = [[0.5, 0.5], [1.5, 1.5]] #输入需要预测的数据
print(clf.predict(test_X))       # 调用预测函数进行分类

print(clf.score(X,y)) #它提供了一个缺省的评估法则来评估模型,简要的说,它用你训练好的模型在测试集上进行评分（0~1）1分代表最好
print(clf.support_vectors_)  #输出当前的支持向量
```

# 朴素贝叶斯


```python
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.metrics import classification_report

data_path ='/data/bigfiles/5297379b-7cd5-4239-bcac-e2d361753393'
df = pd.read_csv(data_path, delimiter='\t',header=None)
######Begin ######

# 将label编码，替换为数值形式：ham -> 1, spam -> 0
df[0] = df[0].replace(to_replace=['spam', 'ham'], value=[0, 1])

# 完成数据划分及词向量的转化
X = df[1].values  # 邮件内容
y = df[0].values  # 标签
# 划分训练集和测试集 使用random_state=0确保结果可复现
X_train_raw,X_test_raw,y_train,y_test=train_test_split(X,y,random_state = 0)
# 初始化TfidfVectorizer，用于将文本数据转化为词向量
vectorizer = TfidfVectorizer()
# 对训练集进行fit和transform，学习词汇表并生成词向量
x_train = vectorizer.fit_transform(X_train_raw)
# 对测试集进行transform，仅使用训练集学到的词汇表生成词向量
x_test = vectorizer.transform(X_test_raw)


# 构建模型及训练
model = MultinomialNB()

#对于测试集x_test进行预测
model.fit(x_train,y_train)
# 对测试集进行预测，得到分类标签
x_pre_test=model.predict(x_test)
# 对测试集进行预测，得到每个类别的概率
x_pro_test=model.predict_proba(x_test)
#计算验证集的auc值,参数为预测值和概率估计
auc=roc_auc_score(y_test, x_pro_test[:, 1])

###### End ######

print("auc的值:{}".format(auc))
```

from sklearn.naive_bayes import MultinomialNB  
fit函数实现了朴素贝叶斯分类算法训练模型的功能，predict函数实现了法模型预测的功能   

其中fit函数的参数如下：   
X：大小为[样本数量,特征数量]的ndarry，存放训练样本  
Y：值为整型，大小为[样本数量]的ndarray，存放训练样本的分类标签  

而predict函数有一个向量输入：  
X：大小为[样本数量,特征数量]的ndarry，存放预测样本  

MultinomialNB的使用代码如下：  
clf = MultinomialNB()  
clf.fit(X_train, Y_train)  
result = clf.predict(X_test)  


```python
from sklearn.feature_extraction.text import CountVectorizer  
# 从sklearn.feature_extraction.text里导入文本特征向量化模块
from sklearn.naive_bayes import MultinomialNB


def news_predict(train_sample, train_label, test_sample):
    '''
    训练模型并进行预测,返回预测结果
    :param train_sample:原始训练集中的新闻文本,类型为ndarray
    :param train_label:训练集中新闻文本对应的主题标签,类型为ndarray
    :test_sample:原始测试集中的新闻文本,类型为ndarray
    '''

    #实例化向量化对象
    vec = CountVectorizer()
    #将训练集中的新闻向量化
    train_sample = vec.fit_transform(train_sample)
    #将测试集中的新闻向量化
    test_sample = vec.transform(test_sample)  

    clf = MultinomialNB()
    clf.fit(train_sample, train_label)
    result = clf.predict(test_sample)    
    return result
```

## 算法流程


| 编号 | 颜色 | 声音 | 纹理 | 是否为好瓜 |
| :--: | :--: | :--: | :--: | :--: |
| 1 | 绿 | 清脆 | 清晰 | 是 |
| 2 | 黄 | 浑厚 | 模糊 | 否 |
| 3 | 绿 | 浑厚 | 模糊 | 是 |
| 4 | 绿 | 清脆 | 清晰 | 是 |
| 5 | 黄 | 浑厚 | 模糊 | 是 |
| 6 | 绿 | 清脆 | 清晰 | 否 |

从表中数据可以看出：  
P(是好瓜)=4/6  
P(颜色绿|是好瓜)=3/4  
P(颜色黄|是好瓜)=1/4  
P(声音清脆|是好瓜)=1/2  
P(声音浑厚|是好瓜)=1/2  
P(纹理清晰|是好瓜)=1/2  
P(纹理模糊|是好瓜)=1/2  
P(不是好瓜)=2/6  
P(颜色绿|不是好瓜)=1/2  
P(颜色黄|是好瓜)=1/2  
P(声音清脆|不是好瓜)=1/2  
P(声音浑厚|不是好瓜)=1/2  
P(纹理清晰|不是好瓜)=1/2  
P(纹理模糊|不是好瓜)=1/2  

预测一下这个西瓜是不是好瓜  

| 颜色 | 声音 | 纹理 | 是否为好瓜 |
| :--: | :--: | :--: | :--: |
| 绿 | 清脆 | 清晰 |  ？ |

假设事件A1为好瓜，事件B为绿，事件C为清脆，事件D为清晰。则有：  

P(A1)P(B|A1)P(C|A1)P(D|A1)= 4/6 * 3/4 * 1/2 * 1/2 = 1/8  

假设事件A2为不是好瓜，则有：  

P(A2)P(B|A2)P(C|A2)P(D|A2)= 2/6 * 1/2 * 1/2 * 1/2 = 1/24  

由于 1/8 > 1/24 所以这个西瓜是好瓜。  


```python
import numpy as np

# 完成fit与predict函数,分别实现模型的训练与预测。
# 在fit函数中需要将预测时需要的概率保存到self.label_prob和self.condition_prob这两个变量
class NaiveBayesClassifier(object):
    def __init__(self):
        '''
        self.label_prob表示每种类别在数据中出现的概率
        例如,{0:0.333, 1:0.667}表示数据中类别0出现的概率为0.333,类别1的概率为0.667
        '''
        self.label_prob = {}# 用于存储每个类别的先验概率，即每个类别在训练数据中出现的概率
        '''
        self.condition_prob表示每种类别确定的条件下各个特征出现的概率
        例如训练数据集中的特征为 [[2, 1, 1],
                              [1, 2, 2],
                              [2, 2, 2],
                              [2, 1, 2],
                              [1, 2, 3]]
        标签为[1, 0, 1, 0, 1]
        那么当标签为0时第0列的值为1的概率为0.5,值为2的概率为0.5;
        当标签为0时第1列的值为1的概率为0.5,值为2的概率为0.5;
        当标签为0时第2列的值为1的概率为0,值为2的概率为1,值为3的概率为0;
        当标签为1时第0列的值为1的概率为0.333,值为2的概率为0.666;
        当标签为1时第1列的值为1的概率为0.333,值为2的概率为0.666;
        当标签为1时第2列的值为1的概率为0.333,值为2的概率为0.333,值为3的概率为0.333;
        因此self.label_prob的值如下:     
        {
            0:{
                0:{
                    1:0.5
                    2:0.5
                }
                1:{
                    1:0.5
                    2:0.5
                }
                2:{
                    1:0
                    2:1
                    3:0
                }
            }
            1:
            {
                0:{
                    1:0.333
                    2:0.666
                }
                1:{
                    1:0.333
                    2:0.666
                }
                2:{
                    1:0.333
                    2:0.333
                    3:0.333
                }
            }
        }
        '''
        self.condition_prob = {}# 用于存储在给定类别的条件下，每个特征取不同值的条件概率
    def fit(self, feature, label):
        '''
        对模型进行训练,需要将各种概率分别保存在self.label_prob和self.condition_prob中
        :param feature: 训练数据集所有特征组成的ndarray
        :param label:训练数据集中所有标签组成的ndarray
        :return: 无返回
        '''
        #********* Begin *********#
        row_num = len(feature)
        col_num = len(feature[0])
        for c in label:
            if c in self.label_prob:
                self.label_prob[c] += 1
            else:
                self.label_prob[c] = 1
        for key in self.label_prob.keys():
            self.label_prob[key] /= row_num
            self.condition_prob[key] = {}
            for i in range(col_num):
                self.condition_prob[key][i] = {}
                for k in np.unique(feature[:,i], axis=0):
                    self.condition_prob[key][i][k] = 0
        for i in range(len(feature)):
            for j in range(len(feature[i])):
                if feature[i][j] in self.condition_prob[label[i]]:
                    self.condition_prob[label[i]][j][feature[i][j]] += 1
                else:
                    self.condition_prob[label[i]][j][feature[i][j]] = 1
        for label_key in self.condition_prob.keys():
            for k in self.condition_prob[label_key].keys():
                total = 0
                for v in self.condition_prob[label_key][k].values():
                    total += v
                for kk in self.condition_prob[label_key][k].keys():
                    self.condition_prob[label_key][k][kk] /= total
        #********* End *********#


    def predict(self, feature):
        '''
        对数据进行预测,返回预测结果
        :param feature:测试数据集所有特征组成的ndarray,有多条数据
        :return:预测结果,feature中有多少条数据,就需要返回长度为多少的list或者ndarry**
        '''
        # ********* Begin *********#
        result = []
        for i,f in enumerate(feature):
            prob=np.zeros(len(self.label_prob.keys()))
            i1 = 0
            for label,label_prob in self.label_prob.items():
                prob[i1] = label_prob
                for  j  in range(len(feature[0])):
                    prob[i1] *= self.condition_prob[label][j][f[j]]
                i1 += 1
            result.append(list(self.label_prob.keys())[np.argmax(prob)])
        return np.array(result)
        #********* End *********#
```

# 聚类

## 外部指标


```python
# 导入 numpy 科学计算库
import numpy as np

# 令 m=100
m = 100

# lambda_true 表示参考模型给出的簇标记
np.random.seed(0)
lambda_true = np.random.randint(0,5,m)

# lambda_pred 表示通过聚类得到的簇标记
np.random.seed(1)
lambda_pred = np.random.randint(0,5,m)

# 计算 a,b,c,d
a = b = c = d = 0
for j in range(m):
    for i in range(j):
        if lambda_true[i]==lambda_true[j] and lambda_pred[i]==lambda_pred[j]:
            a = a + 1
        elif lambda_true[i]==lambda_true[j] and lambda_pred[i]!=lambda_pred[j]:
            b = b + 1
        elif lambda_true[i]!=lambda_true[j] and lambda_pred[i]==lambda_pred[j]:
            c = c + 1
        else:
            d = d + 1
        

# 计算 Jaccard 系数
JC = a / ( a + b + c)

# 计算 FM 指数

FM = np.sqrt( (a**2) / ( (a+b) * (a+c) ) )

# 计算 Rand 指数

RI = ( 2 * (a+b) ) / ( m * (m-1) )

# 打印结果
print("Jaccard 系数为{},FM 指数为{},Rand 指数为{}".format(JC, FM, RI))
```

## 内部指标
样本内平均距离，最远距离，
样本间最近距离，中心点距离

## K-Means算法
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=2)
.fit(X)
.predict(y)

n_clusters 参数用于指定聚类的数量


```python
# 从 sklearn.cluster 导入 KMeans
from sklearn.cluster import KMeans
import numpy as np

# 加载数据集
X = np.array([[1, 2], [2, 2.2], [3, 1.5], [2, 1.8], [1, 1.4], [1, 2.5], [1, 1], [10, 2], [10, 2.5], [9, 2.3], [10, 2.4], [9.5, 2.1]])

# 1：创建 KMeans 对象，令 n_clusters=2
kmeans = KMeans(n_clusters=2)

# 2：调用 fit 函数执行训练过程
kmeans.fit(X)

# 3：调用 predict 函数进行预测，预测的数据为 [0,0], [8,2], [10,3]
y=np.array(([0,0], [8,2], [10,3]))
y_pred = kmeans.predict(y)

# 打印结果
print(y_pred)
# [0 1 1]
```

## 应用示例


```python
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
import numpy as np

# 加载鸢尾花数据集
iris = load_iris()
x = iris['data']
y = iris['target']

# 将数据集分为训练集和测试集
np.random.seed(0)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1)

# 1：创建 KMeans 对象,令 n_clusters=4
kmeans = KMeans(n_clusters=4)

# 2：调用 fit 函数执行训练过程
kmeans.fit(x_train)

# 3：调用 predict 函数进行预测 
y_pred = kmeans.predict(x_test) 

# 打印结果
print("真实结果：\n", y_test)
print("预测结果：\n", y_pred)

# 计算 a,b,c,d
a = b = c = d = 0
m = 15
for j in range(m):
    for i in range(j):
        if y_test[i]==y_test[j] and y_pred[i]==y_pred[j]:
            a = a + 1
        elif y_test[i]==y_test[j] and y_pred[i]!=y_pred[j]:
            b = b + 1
        elif y_test[i]!=y_test[j] and y_pred[i]==y_pred[j]:
            c = c + 1
        else:
            d = d + 1
        
# 根据公式计算 Jaccard 系数
JC = a / (a + b + c)

# 根据公式计算 FM 指数
FM = np.sqrt(a ** 2 / ((a + b) * (a + c)))

# 根据公式计算 Rand 指数
RI = 2 * (a + b) / (m * (m - 1))

# 打印结果
print("Jaccard 系数为{},FM 指数为{},Rand 指数为{}".format(JC, FM, RI))
```
