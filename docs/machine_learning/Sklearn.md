# 简介
Sklearn（全称 scikit-learn）是一个开源的机器学习库  
在 Sklearn 中，机器学习的流程遵循一定的模式：数据加载、数据预处理、训练模型、评估模型 和 调优模型  

- **数据加载**：使用 Sklearn 或其他库加载数据集，例如通过 datasets.load_iris() 加载经典的鸢尾花数据集，或使用 train_test_split() 分割数据  
  
- **数据预处理**：根据数据的类型，可能需要进行标准化、去噪、缺失值填充等操作  
  
- **选择算法和训练模型**：选择适合的算法（如逻辑回归、支持向量机等），使用 .fit() 方法对模型进行训练  
  
- **模型评估**：使用交叉验证或单一训练/测试集来评估模型的准确性、召回率、F1分数等性能指标  
  
- **模型优化**：使用网格搜索（GridSearchCV）或随机搜索（RandomizedSearchCV）对模型进行超参数优化，提高模型性能    
  
Sklearn 提供了大量经典的机器学习算法    
- **分类算法**：如逻辑回归、支持向量机（SVM）、K近邻（KNN）、随机森林等  
  
- **回归算法**：如线性回归、岭回归、Lasso回归等  
  
- **聚类算法**：如 K均值、层次聚类、DBSCAN 等  
  
- **降维算法**：如主成分分析（PCA）、t-SNE 等  
  
- **模型选择与评估**：交叉验证、网格搜索、模型评估指标等  
  
Sklearn 可以很好地与 NumPy、SciPy、Pandas 等 Python 数据处理库兼容，支持多种数据格式（如 NumPy 数组、Pandas DataFrame）进行输入和输出  

## 常见的模块和类
- 分类（Classification）    
  - sklearn.linear_model.LogisticRegression：逻辑回归  
  - sklearn.svm.SVC：支持向量机分类  
  - sklearn.neighbors.KNeighborsClassifier：K近邻分类  
  - sklearn.ensemble.RandomForestClassifier：随机森林分类  
- 回归（Regression）
  - sklearn.linear_model.LinearRegression：线性回归
  - sklearn.linear_model.Ridge：岭回归
  - sklearn.ensemble.RandomForestRegressor：随机森林回归
- 聚类（Clustering）
  - sklearn.cluster.KMeans：K均值聚类
  - sklearn.cluster.DBSCAN：基于密度的空间聚类
- 降维（Dimensionality Reduction）
  - sklearn.decomposition.PCA：主成分分析（PCA）
  - sklearn.decomposition.NMF：非负矩阵分解
- 模型选择（Model Selection）
  - sklearn.model_selection.train_test_split：将数据集划分为训练集和测试集
  - sklearn.model_selection.GridSearchCV：网格搜索，寻找最佳超参数
- 数据预处理（Preprocessing）
  - sklearn.preprocessing.StandardScaler：标准化
  - sklearn.preprocessing.MinMaxScaler：最小-最大标准化
  - sklearn.preprocessing.OneHotEncoder：独热编码

---

# 基础
5大方面：数据表示、模型类型、预处理方法、评估指标、模型调优

**数据表示：数据集和特征**  
- 数据集（Dataset）  
  在 scikit-learn 中，数据通常通过两个主要的对象来表示： 特征矩阵 和 目标向量
  - 特征矩阵（Feature Matrix）：每一行代表一个数据样本，每一列代表一个特征。它是一个二维的数组或矩阵，通常使用 NumPy 数组或 pandas DataFrame 来存储
  - 目标向量（Target Vector）：它表示每个样本的目标（即输出标签），通常是一个一维数组

>```python
>import numpy as np
>X = np.array([[1.0, 2.0], [2.0, 3.0], [3.0, 4.0]]) #3 个样本，每个样本有 2 个特征
>```  
>
>- 特征和标签
>  - 特征（Features）：是数据集中用于训练模型的输入变量。在上面的例子中，X 是特征矩阵，包含了所有的输入变量  
>  - 标签（Labels）：是机器学习模型的目标输出。在监督学习中，标签是我们希望模型预测的结果。在上面的例子中，y 是标签或目标向量，包含了每个样本的类别  
>
>- 数据集分割  
>  在实际应用中，通常需要将数据集分割成训练集和测试集
>  - train_test_split() 
>```python
>from sklearn.model_selection import train_test_split
>X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
>```
  
**模型与算法**  
- 监督学习（Supervised Learning）：在监督学习中，模型在训练时会利用带标签的数据进行学习，这些标签是我们希望模型预测的结果  
  常见的监督学习任务包括分类和回归。
  - 分类（Classification）：将数据点分配到预定的类别中。例如，判断邮件是垃圾邮件还是非垃圾邮件  
  - 回归（Regression）：预测连续值输出。例如，预测房价、气温等  
- 无监督学习（Unsupervised Learning）：无监督学习是指没有标签数据，模型仅通过输入数据本身的特征进行学习  
  常见的无监督学习任务包括聚类和降维。
  - 聚类（Clustering）：将数据分组，使得同一组中的数据具有相似性。常见的聚类算法包括 K-Means、DBSCAN 等
  - 降维（Dimensionality Reduction）：减少数据中的特征数量，通常用于数据压缩或可视化。常见的降维方法有 PCA（主成分分析）和 t-SNE（t-分布随机邻域嵌入）等
- 预处理与特征工程
  - 标准化（Standardization）：特征的尺度统一，使得每个特征都具有零均值和单位方差
  - 归一化（Normalization）：将特征的值缩放到一个固定范围（通常是 0 到 1）  
  - 类别变量编码：将类别型数据转换为数值型数据（如 one-hot 编码）  
>```python
>from sklearn.preprocessing import StandardScaler
>scaler = StandardScaler()
>X_scaled = scaler.fit_transform(X)
>
>from sklearn.preprocessing import MinMaxScaler
>scaler = MinMaxScaler()
>X_normalized =   scaler.fit_transform(X)
>```
  
**模型评估与验证**
- 交叉验证（Cross-validation）   
  交叉验证是一种常见的模型评估方法，尤其是在数据量有限的情况下  
  通过将数据分成多个子集，每次使用一个子集作为验证集，其余作为训练集，重复多次训练和评估模型，最终计算模型的平均性能  
>```python
>from sklearn.model_selection import cross_val_score
>scores = cross_val_score(clf, X, y, cv=5)  # 5-fold cross-validation 5折交叉验证
>print("Cross-validation scores:", scores)
>```
- 常见评估指标
  - 分类任务的评估指标
    - 准确率（Accuracy）：预测正确的样本占所有样本的比例
    - 精确率（Precision）：正类预测中，实际正类的比例
    - 召回率（Recall）：实际正类中，正确预测的比例
    - F1 分数：精确率和召回率的调和平均数
  - 回归任务的评估指标：
    - 均方误差（MSE）：预测值与真实值的平方差的平均值。
    - 决定系数（R²）：衡量模型对数据变异的解释能力
>```python
>from sklearn.metrics import accuracy_score, classification_report
>print("Accuracy:", accuracy_score(y_test, y_pred))
>print("Classification Report:\n", classification_report(y_test, y_pred))
>
>from sklearn.metrics import mean_squared_error, r2_score
>print("MSE:", mean_squared_error(y_test, y_pred))
>print("R²:", r2_score(y_test, y_pred))
>```

**模型选择与调优**
- 网格搜索（Grid Search）  
  网格搜索是一种常用的超参数调优方法，它通过遍历所有可能的参数组合来寻找最佳的超参数组合  
>```python
>from sklearn.model_selection import GridSearchCV
>
>param_grid = {'max_depth': [3, 5, 7], 'min_samples_split': [2, 5, 10]}
>grid_search = GridSearchCV(DecisionTreeClassifier(), param_grid, cv=5)
>grid_search.fit(X_train, y_train)
>print("Best parameters:", grid_search.best_params_)
>```  
>- 随机搜索（Random Search）  
>  随机搜索是一种通过随机选择超参数的组合来搜索最优超参数的方法，它比网格搜索效率高    
>```python
>from sklearn.model_selection import RandomizedSearchCV
>from scipy.stats import randint
>
>param_dist = {'max_depth': [3, 5, 7], 'min_samples_split': randint(2, 10)}
>random_search = RandomizedSearchCV(DecisionTreeClassifier(), param_dist, n_iter=10, cv=5)
>random_search.fit(X_train, y_train)
>print("Best parameters:", random_search.best_params_)
>```

---

# 数据预处理
## 缺失值
- 检查缺失值
- 填充缺失值 
  - 填充均值（Mean）：适用于数值型数据。
  - 填充中位数（Median）：对于含有离群值的数据集，使用中位数可能更有效。
  - 填充最频繁值（Mode）：适用于类别型数据。


```python
import pandas as pd
from sklearn.impute import SimpleImputer

data={
    'name':['Amy','Jhon'],
    'age': [15,18]
}
df = pd.DataFrame(data)
print(df.isnull().sum()) # 查看每一列缺失值的数量
df_cleaned = df.dropna()  # 删除包含缺失值的行

# 对于数值型数据，使用均值填充
imputer = SimpleImputer(strategy='mean')  # 可选：'mean', 'median', 'most_frequent'
df_imputed = imputer.fit_transform(df)  # 填充缺失值
# df_imputed = SimpleImputer(strategy='mean').fit_transfrom(df)
```

## 数据缩放
- 标准化（Standardization）：将数据转换为均值为0、标准差为1的分布。适用于大多数机器学习算法  
- 归一化（Normalization）：将数据缩放到指定范围(通常是 [0, 1])  
  
为什么需要标准化和归一化？  
标准化：对于距离度量（如 K 最近邻、支持向量机等）非常重要，因为特征的尺度不一致可能导致某些特征对模型的影响过大。标准化能确保每个特征对模型有相同的贡献  
归一化：有些算法（如神经网络、梯度下降优化算法等）对输入数据的范围非常敏感，归一化有助于加速收敛 


## 类别变量编码   
机器学习模型通常无法直接处理字符串类型的类别变量，因此需要将类别变量转化为数值型数据  
- 标签编码  
  标签编码将每个类别映射到一个唯一的整数  
  适用于类别之间有顺序关系的情况（例如，低、中、高）  
>```python
>from sklearn.preprocessing import LabelEncoder
># 或者OrdinalEncoder
># 假设我们有一个类别变量 y
>label_encoder = LabelEncoder()
>y_encoded = label_encoder.fit_transform(y)  # 将类别变量转换为整数
>``` 
>- 独热编码  
>  独热编码将每个类别转换为一个二进制的向量，适用于类别之间没有顺序关系的情况（例如，颜色、国家等）  
>  OneHotEncoder 可以将类别变量转化为独热编码  
>```python
>from sklearn.preprocessing import OneHotEncoder
># 假设我们有一个类别变量 X
>encoder = OneHotEncoder(sparse=False)  # sparse=False 返回一个密集矩阵
>X_encoded = encoder.fit_transform(X)  # 将类别变量转换为独热编码
>
># 在 pandas 中，也可以使用 get_dummies() 函数进行独热编码：
>X_encoded = pd.get_dummies(X)
>```

## 特征选择  
  通过选择最重要的特征来提高模型的性能，并减少计算成本  
- 基于模型的特征选择
  使用一些机器学习模型（如决策树或随机森林）来评估特征的重要性，从而进行特征选择  
>```python
>from sklearn.ensemble import RandomForestClassifier
>
># 训练一个随机森林模型
>clf = RandomForestClassifier()
>clf.fit(X_train, y_train)
>
># 获取特征重要性
>importances = clf.feature_importances_
>print(importances)
>```
- 递归特征消除（Recursive Feature Elimination，RFE）  
  RFE 是一种通过递归的方式，逐步删除最不重要的特征，从而选择最优特征的方法   
  RFE 可以帮助我们自动选择重要特征   
>```python
>from sklearn.feature_selection import RFE
>
># 使用线性模型进行递归特征消除
>rfe = RFE(clf, n_features_to_select=3)  # 保留 3 个最重要的特征
>X_rfe = rfe.fit_transform(X_train, y_train)
>```


## 特征工程
通过对现有特征进行处理、组合或构造新的特征，以提高模型的表现  
特征工程的常见方式包括：  
- 特征组合：将两个或更多的特征组合成一个新特征  
- 特征转换：对特征进行对数变换、平方根变换等，以解决数据的非线性问题  
- 特征创建：根据现有数据创建新的特征，例如从时间戳中提取出日期、月份、星期等  

## 特征提取
旨在从原始特征中提取出新的、更具表达力的特征  
常见的特征提取方法包括: 主成分分析（PCA） 和 线性判别分析（LDA）  
- 主成分分析（PCA）  
  PCA 是一种常用的降维技术，它通过线性变换将数据从高维空间映射到低维空间，使得新特征（主成分）尽可能保留数据的方差  
  PCA 特别适用于特征数量过多的情况，可以有效降低计算复杂度  
  PCA 主要用于两种场景：  
  降维：当特征过多时，使用 PCA 降维可以减少计算成本，同时保留数据的主要信息  
  可视化：将高维数据映射到 2D 或 3D 空间，帮助我们可视化数据结构  
>```python
>from sklearn.decomposition import PCA
>
># 假设 X 是特征矩阵
>pca = PCA(n_components=2)  # 降维到 2 个主成分
>X_pca = pca.fit_transform(X)
>```
- 线性判别分析（LDA）  
  LDA 是一种监督学习的降维方法，它旨在找到一个线性组合，使得不同类别之间的距离最大化，类别内的距离最小化  
  LDA 通常用于分类任务中  
>```python
>from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
>
># 假设 X 是特征矩阵，y 是目标变量
>lda = LinearDiscriminantAnalysis(n_components=2)  # 降维到 2 个线性判别组件
>X_lda = lda.fit_transform(X, y)
>``` 

## 处理不平衡数据
在分类问题中，如果数据集的各类别样本数量差异较大，可能会导致模型偏向预测多数类，从而影响模型的性能  
常见的处理方法包括：  
- 上采样（Over-sampling）  
通过增加少数类样本的数量，使得数据集更加平衡   
常见的方法是使用 SMOTE（Synthetic Minority Over-sampling Technique） 算法   
>```python
>from imblearn.over_sampling import SMOTE
>
>smote = SMOTE()
>X_resampled, y_resampled = smote.fit_resample(X_train, y_train)
>```
- 下采样（Under-sampling）  
通过减少多数类样本的数量，使得数据集更加平衡  
>```python
>from imblearn.under_sampling import RandomUnderSampler
>
>undersampler = RandomUnderSampler()
>X_resampled, y_resampled = undersampler.fit_resample(X_train, y_train)
>```
---

# 模型
## 分类模型
### 逻辑回归（Logistic Regression）
逻辑回归是一种经典的线性分类模型。它通过将线性回归的输出通过逻辑函数（sigmoid）映射到 0 和 1 之间，从而预测事件的概率  


```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression 

iris=load_iris()
X=pd.DataFrame(iris.data,columns=iris.feature_names)
y=pd.Series(iris.target)
print(X.head()) # 查看前五行

# 假设 X 是特征矩阵，y 是标签
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

# 预测
y_pred = model.predict(X_test)
```

### K-近邻（K-Nearest Neighbors, KNN）
K-近邻（KNN）是一种基于实例的学习方法，预测时通过计算待预测样本与训练集中所有样本的距离，选取距离最近的 K 个邻居，并根据邻居的标签进行预测  
主要参数:  
- K：选择的邻居数量  
- 距离度量：常用欧氏距离，也可以使用曼哈顿距离、闵可夫斯基距离等  


```python
from sklearn.neighbors import KNeighborsClassifier

# 假设 X 是特征矩阵，y 是标签
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

# 预测
y_pred = model.predict(X_test)
```

### 支持向量机（Support Vector Machine, SVM）
支持向量机是一种强大的分类模型，尤其适用于高维数据  
SVM 的基本思想是找到一个超平面，使得不同类别的样本点之间的间隔最大化  
对于非线性可分的数据，SVM 通过核技巧将数据映射到高维空间，找到一个分隔超平面  

核函数:  
- 线性核：适用于线性可分的数据
- 高斯径向基核（RBF）：适用于非线性数据
- 多项式核：适用于具有多项式关系的数据


```python
from sklearn.svm import SVC

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42)

model=SVC(kernel='linear')
model.fit(X_train,y_train)

y_pred=model.predict(X_test)
```

### 决策树与随机森林（Decision Tree & Random Forest）
决策树是一种树形结构的分类模型，通过对数据进行分裂，最终将数据划分到不同的类别  
随机森林则是通过构建多棵决策树，并通过投票或平均来决定最终的预测结果  
决策树通过选择最优的特征进行数据划分，选择准则通常是 `信息增益` 或 `基尼系数`  
随机森林通过多棵决策树的集成来减少过拟合，并提高模型的准确性。它通过引入随机性（如随机选择特征、随机选择数据子集）来增加模型的多样性  


```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

# 假设 X 是特征矩阵，y 是标签
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 决策树
dt_model = DecisionTreeClassifier()
dt_model.fit(X_train, y_train)

# 随机森林
rf_model = RandomForestClassifier(n_estimators=100)
rf_model.fit(X_train, y_train)

# 预测
dt_pred = dt_model.predict(X_test)
rf_pred = rf_model.predict(X_test)
```

## 回归模型
### 线性回归（Linear Regression）
线性回归通过拟合一条直线来预测目标变量。其核心假设是特征与目标变量之间存在线性关系


```python
from sklearn.linear_model import LinearRegression

# 假设 X 是特征矩阵，y 是目标变量
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

# 预测
y_pred = model.predict(X_test)
```

### 岭回归（Ridge Regression）
岭回归是线性回归的一个变种，使用 `L2 正则化` 来约束模型的复杂度，避免过拟合  
通过惩罚回归系数的大小，岭回归能更好地处理多重共线性问题  


```python
from sklearn.linear_model import Ridge

model = Ridge(alpha=1.0) # alpha 是正则化参数
model.fit(X_train, y_train)

# 预测
y_pred = model.predict(X_test)
```

### Lasso 回归（Lasso Regression）
Lasso 回归也是线性回归的一种形式，它使用 `L1 正则化` 来对回归系数进行惩罚  
与岭回归不同，Lasso 会将一些回归系数压缩到零，从而实现特征选择  


```python
from sklearn.linear_model import Lasso

model = Lasso(alpha=0.1) # alpha 是正则化参数
model.fit(X_train, y_train)

# 预测
y_pred = model.predict(X_test)
```

## 聚类模型
### K-均值（K-Means）
K-均值是一种常见的聚类算法，目标是将数据分为 K 个簇，通过最小化每个数据点与其簇中心的距离来优化簇划分  


```python
from sklearn.cluster import KMeans

model = KMeans(n_clusters=3)
model.fit(X)

# 获取聚类标签
labels = model.predict(X)
```

### DBSCAN（密度聚类）
DBSCAN（Density-Based Spatial Clustering of Applications with Noise）是一种基于密度的聚类算法，它通过寻找密度相对较高的区域来进行聚类，不需要事先指定簇的数量  


```python
from sklearn.cluster import DBSCAN

model=DBSCAN(eps=0.5,min_samples=5)
model.fit(X)

# 获取聚类标签
labels = model.labels_
```

### 层次聚类（Hierarchical Clustering）
层次聚类是一种通过递归地合并或分割簇的方式进行聚类的方法  
常用的层次聚类方法有 凝聚型聚类（Agglomerative）和 分裂型聚类（Divisive）  


```python
from sklearn.cluster import AgglomerativeClustering

model=AgglomerativeClustering(n_clusters=3)
labels=model.fit_predict(X)
```

# 模型评估与调优
## 精度、召回率、F1 分数
对于分类模型  
我们通常使用精度、召回率、F1 分数等指标来评估模型性能  


```python
from sklearn.metrics import accuracy_score, recall_score, f1_score

accuracy = accuracy_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print(f"Accuracy: {accuracy}")
print(f"Recall: {recall}")
print(f"F1 Score: {f1}")
```

`classification_report`  提供了精度、召回率、F1 分数和支持度（每个类别的样本数）等信息  
`confusion_matrix`  混淆矩阵用于显示分类模型在各个类别上的表现，特别是如何将正类预测为负类，反之亦然  
`roc_auc_score`  ROC AUC（接收者操作特征曲线下面积）是评估分类模型性能的指标，尤其适用于不平衡数据集。AUC 值越高，模型性能越好  


```python
from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))
#               precision    recall  f1-score   support(样本数)

#            0       1.00      1.00      1.00        19
#            1       1.00      1.00      1.00        13
#            2       1.00      1.00      1.00        13

#     accuracy(准确率)                        1.00        45
#    macro avg(宏平均)    1.00      1.00      1.00        45
# weighted avg(加权平均)  1.00      1.00      1.00        45

from sklearn.metrics import confusion_matrix

print(confusion_matrix(y_test, y_pred))
# [[19  0  0]
#  [ 0 13  0]
#  [ 0  0 13]]  
# n*n的混淆矩阵，n个类别
# 行表示 真实类别
# 列表示 预测类别
# 对角线上的数字表示 预测正确 的样本数
# 非对角线上的数字表示 预测错误 的样本数

from sklearn.metrics import roc_auc_score

# y_test 是真实标签，y_pred_proba 是模型预测的概率值!!
# print(f"ROC AUC Score: {roc_auc_score(y_test, y_pred_proba)}")
```

## 均方误差（MSE） 和 决定系数（R²）
对于回归问题  
`mean_squared_error`  均方误差是回归模型的常见评估标准，计算预测值与真实值之间的平方误差的均值  
`r2_score`  决定系数 R² 用于衡量模型对数据的拟合程度，值越接近 1，表示模型拟合得越好


```python
from sklearn.metrics import mean_squared_error,r2_score

print(f"Mean Squared Error: {mean_squared_error(y_test, y_pred)}")

print(f"R² Score: {r2_score(y_test, y_pred)}")
```

## 交叉验证（cross_val_score）
将数据集分成多个子集（折叠），并多次训练和测试模型来获得更稳定、可靠的评估结果  

- K折交叉验证：将数据分成 K 个折叠，依次选择其中一个折叠作为测试集，其他 K-1 个折叠作为训练集，重复 K 次，最后计算 K 次的结果平均值    
- 留一法交（Leave-One-Out Cross-Validation, LOOCV）：每次只保留一个数据点作为测试集，剩余的作为训练集。这种方法非常耗时，但可以用于小数据集    
- 分层K折交叉验证：在 K-fold 中，确保每个折叠中的类别分布与整个数据集相似，适用于类别不平衡的情况  


```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

# 进行 5 折交叉验证
scores = cross_val_score(model, X, y, cv=5)
print(f"Cross-validation scores: {scores}") # 返回每一折的评分
```

## 网格搜索（GridSearchCV）
- param_grid：待调优的超参数网格，通常是一个字典，键是参数名，值是参数的候选值
- cv：交叉验证的折数，通常设置为 5 或 10


```python
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC

# 定义参数网格
parameters = {'kernel': ['linear', 'rbf'], 'C': [1, 10, 100]}
# 指定需要调优的超参数及其候选值:  
# kernel：   SVM的核函数类型，测试线性核（'linear'）和高斯核（'rbf'）。
# C：        正则化参数，测试值为 1、10 和 100（控制模型的复杂度与训练误差的权衡）
model = SVC()

# 网格搜索
grid_search = GridSearchCV(model, parameters, cv=5) # 5折交叉验证
grid_search.fit(X, y)

# 输出最佳参数
print(f"Best parameters: {grid_search.best_params_}") # 返回网格搜索中表现最好的超参数组合
print(f"Best score: {grid_search.best_score_}") # 返回最佳参数组合下的交叉验证得分
```

## 随机搜索（RandomizedSearchCV）
一种更高效的超参数调优方法，它通过从超参数空间中随机选择一定数量的组合进行评估，从而加速调优过程  
适用于超参数空间较大时，可以节省计算时间  
- param_distributions：待调优的超参数分布，通常是一个字典，值可以是分布对象（如 scipy.stats 中的分布）或者离散的值列表。
- n_iter：随机搜索的迭代次数，即随机选择的超参数组合数量


```python
from sklearn.model_selection import RandomizedSearchCV
from sklearn.svm import SVC
from scipy.stats import uniform

# 加载数据
data = load_iris()
X, y = data.data, data.target

# 创建模型
model = SVC()

# 定义超参数分布
param_distributions = {'C': uniform(0, 10), 'kernel': ['linear', 'rbf']}

# 执行随机搜索
random_search = RandomizedSearchCV(model, param_distributions, n_iter=10, cv=5)
random_search.fit(X, y)

# 输出最佳参数和最佳得分
print(f"Best parameters: {random_search.best_params_}")
print(f"Best score: {random_search.best_score_}")
```

---
# 管道（Pipeline）
在机器学习项目中，数据处理、特征工程、模型训练、评估等步骤往往是互相依赖的，这些步骤的顺序和协调性对于最终模型的性能至关重要   
Pipeline 是 scikit-learn 中用于组织和简化这些步骤的一个重要工具   
通过 Pipeline，我们可以将数据预处理与模型训练整合在一起，从而简化工作流并提高代码的可复用性   

Pipeline 是一个可按顺序执行多个数据处理步骤和模型训练步骤的工具  
Pipeline由多个步骤（step）组成，每个步骤是一个元组，包含一个名称和一个对象  
每个对象通常是一个 转换器（Transformer） 或 估计器（Estimator），其中：  
- `转换器（Transformer）` 是执行数据转换的对象，比如数据预处理（例如归一化、标准化、特征选择等）
- `估计器（Estimator）` 是用于训练模型的对象，例如分类器或回归器  
  
Pipeline 使得将多个步骤整合为一个可重用的工作流变得简单，并且可以确保数据处理过程的一致性，避免因代码重复或手动处理导致的错误  


```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

# 加载数据
data = load_iris()
X, y = data.data, data.target

# 将数据集划分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建 Pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),  # 数据标准化,注意加逗号
    ('svc', SVC())  # 支持向量机分类器
])

# 训练模型
pipeline.fit(X_train, y_train)

# 预测结果
y_pred = pipeline.predict(X_test)

# 打印模型精度
print(f"Model accuracy: {pipeline.score(X_test, y_test)}")

# 首先执行数据预处理步骤（如标准化），然后传递处理后的数据给模型进行训练。
# 这个过程可以通过 pipeline.fit() 一步完成，pipeline.predict() 进行预测时，数据也会按照相同的顺序通过管道中的每个步骤
```


```python
## 是否使用Pipeline对比

# Without Pipeline (需要多次执行预处理)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train) # 防止数据泄露，训练集标准化不能用到测试集
X_test_scaled = scaler.transform(X_test) # 同理，所以要分开计算

model = SVC()
model.fit(X_train_scaled, y_train)
y_pred = model.predict(X_test_scaled)

# With Pipeline (一步完成)
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('svc', SVC())
])

pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)
```

## 调参与优化
当我们使用 Pipeline 时，可以直接进行超参数调优  
通过结合 GridSearchCV 或 RandomizedSearchCV，可以优化管道中的每一个步骤的超参数  


```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.model_selection import GridSearchCV


# 加载数据
data = load_iris()
X, y = data.data, data.target

# 将数据集划分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建 Pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),  # 数据标准化
    ('svc', SVC())  # 支持向量机分类器
])

# 训练模型
pipeline.fit(X_train, y_train)

# 定义超参数网格
param_grid = {
    'svc__C': [0.1, 1, 10],  # 调整 SVC 中的 C 参数
    'svc__kernel': ['linear', 'rbf']  # 调整 kernel 参数
}

# 创建 GridSearchCV 对象
grid_search = GridSearchCV(pipeline, param_grid, cv=5)

# 执行超参数调优
grid_search.fit(X_train, y_train)

# 输出最佳参数和得分
print(f"Best parameters: {grid_search.best_params_}")
print(f"Best score: {grid_search.best_score_}")
```

结合 Pipeline 和交叉验证


```python
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score

data=load_iris()
X,y=data.data,data.target

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42)

pipeline=Pipeline([
    ('scaler',StandardScaler()),
    ('svc',SVC())
])

pipeline.fit(X_train,y_train)

cv_scores = cross_val_score(pipeline,X,y,cv=5)

print(f"Cross-validation scores: {cv_scores}")
print(f"Mean cross-validation score: {cv_scores.mean()}")

```

---
# 自定义模型与功能
除了使用现成的模型和预处理功能外，用户还可以根据自己的需求创建自定义的模型、转换器和功能  
通常涉及继承 scikit-learn 的基类，如 BaseEstimator 和 TransformerMixin，然后实现特定的 fit 和 predict 方法  
## 自定义转换器（Transformer）
转换器是用于对数据进行转换的组件，例如标准化、特征选择等。自定义转换器可以继承 TransformerMixin，并实现 fit 和 transform 方法  
- fit 方法：通常用于学习数据的属性（如均值、方差、特征选择标准等）  
  fit 方法返回转换器本身，以便可以进行链式调用  
- transform 方法：应用已学习的属性，对数据进行转换或处理  


```python
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
# 实现一个自定义的标准化转换器
class CustomScaler(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        """
        计算每个特征的均值和标准差
        """
        self.mean_ = np.mean(X, axis=0)
        self.std_ = np.std(X, axis=0)
        return self  # 返回对象本身

    def transform(self, X):
        """
        标准化数据
        """
        return (X - self.mean_) / self.std_

# 测试自定义转换器
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# 加载数据
data = load_iris()
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建自定义转换器对象
scaler = CustomScaler()

# 使用自定义标准化
scaler.fit(X_train) # 只能fit(X_train)并应用到测试集,避免数据泄露
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("Scaled training data:\n", X_train_scaled)

# fit 方法计算训练数据的均值和标准差，并保存这些值
# transform 方法根据 fit 中计算的均值和标准差来转换数据
```

## 自定义估计器（Estimator）
估计器是指模型本身，如回归器、分类器等  
自定义估计器需要继承 BaseEstimator 类，并实现 fit 和 predict 方法  
- fit 方法：用于训练模型，计算需要的参数（如权重、偏置等）
- predict 方法：基于训练好的参数对输入数据进行预测


```python
from sklearn.base import  BaseEstimator
import numpy as np

class SimpleClassifier(BaseEstimator):
    def fit(self,X,y):
        """
        训练模型：计算每个特征的均值
        """
        self.mean_=np.mean(X,axis=0)
        return self
    def predict(self,X):
        """
        基于均值进行分类：如果特征值大于均值,则预测为 1,否则为 0
        """
        return (X>self.mean_).astype(int)

# 测试自定义分类器
X_train = np.array([[1.5, 2.5], [2.0, 3.0], [3.5, 4.5], [4.0, 5.0]])
y_train = np.array([0, 0, 1, 1])

# 创建自定义分类器对象
classifier = SimpleClassifier()

# 训练模型
classifier.fit(X_train, y_train)

# 进行预测
X_test = np.array([[2.5, 3.5], [1.0, 2.0]])
y_pred = classifier.predict(X_test)

print("Predictions:", y_pred)    
# fit 方法计算训练数据的均值并将其存储在 self.mean_ 中
# predict 方法通过比较测试数据与均值的大小，做出分类预测
```

## 使用管道
scikit-learn 允许将自定义转换器和估计器作为管道的步骤  
这使得可以将数据预处理和模型训练过程整合成一个工作流  
自定义模型和功能可以像内建的转换器和估计器一样，与管道一起工作  


```python
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline

# 利用前面俩个例子的自定义转换器和估计器

# 测试自定义分类器
X_train = np.array([[1.5, 2.5], [2.0, 3.0], [3.5, 4.5], [4.0, 5.0]])
y_train = np.array([0, 0, 1, 1])

# 创建管道，包含自定义的标准化和分类器
pipeline = Pipeline([
    ('scaler', CustomScaler()),  # 自定义标准化
    ('classifier', SimpleClassifier())  # 自定义分类器
])

# 训练管道
pipeline.fit(X_train, y_train)

X_test = np.array([[2.5, 3.5], [1.0, 2.0]])
# 预测
y_pred = pipeline.predict(X_test)
print("Predictions:", y_pred)
```

- BaseEstimator：是所有 scikit-learn 估计器的基类  
  它提供了 get_params() 和 set_params() 方法，这使得自定义估计器能够与 GridSearchCV 等工具配合工作  
- TransformerMixin：是所有 scikit-learn 转换器的基类  
  它提供了 fit_transform() 方法，使得转换器能够与 Pipeline 一起使用  
  
通过继承这两个基类，我们可以非常方便地创建自己的自定义模型和功能，并且可以利用 scikit-learn 的工具（如 GridSearchCV 和 Pipeline）进行调优和评估。


```python
from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

class CustomEstimator(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        # 模拟一个简单的"模型"：计算每个特征的均值
        self.mean_ = np.mean(X, axis=0)
        return self

    def transform(self, X):
        # 基于均值将数据标准化
        return X - self.mean_

    def predict(self, X):
        # 简单的预测方法：如果特征值大于均值，则预测为 1，否则为 0
        return (X > self.mean_).astype(int)

# 使用自定义估计器和转换器
# 加载数据
data = load_iris()
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建管道
pipeline = Pipeline([
    ('custom', CustomEstimator())
])

# 训练模型
pipeline.fit(X_train, y_train)
# 没有标准化
# 预测
y_pred = pipeline.predict(X_test)
print("Predictions:", y_pred)
```

---

# 模型保存与加载
在机器学习中，模型的训练过程通常是耗时的，为了避免每次重新训练模型，我们可以将训练好的模型保存下来，便于以后进行加载和预测  
scikit-learn 提供了两种常用的方式来保存和加载模型：joblib 和 pickl  
## joblib
joblib 是一个高效的 Python 序列化工具，特别适合用于保存包含大量数值数组（如 numpy 数组、scikit-learn 模型等）的对象  
相较于 pickle，joblib 在处理大规模数据时更高效  
joblib 提供了一个简单的 API 来保存和加载对象  
我们可以使用 joblib.dump() 方法将模型保存到文件中  
``joblib.dump()``  
``joblib.load()``


```python
import joblib
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

data = load_iris()
X, y = data.data, data.target

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建并训练模型
model = SVC(kernel='linear')
model.fit(X_train, y_train)

## 保存
# 保存模型到文件
joblib.dump(model, 'svm_model.joblib')

##加载
# 加载保存的模型
model = joblib.load('svm_model.joblib')

# 使用加载的模型进行预测
y_pred = model.predict(X_test)

# 打印预测结果
print("Predictions:", y_pred)
```

## pickle
pickle 是 Python 内置的模块，允许将 Python 对象序列化和反序列化  
虽然 joblib 更适用于处理大量数据，但 pickle 也是常用的保存和加载模型的工具，适用于一般情况  



```python
import pickle
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

data = load_iris()
X, y = data.data, data.target

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建并训练模型
model = SVC(kernel='linear')
model.fit(X_train, y_train)

## 保存
# 使用 pickle 保存模型
with open('svm_model.pkl', 'wb') as f:
    pickle.dump(model, f)


## 加载
with open('svm_model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

# 使用加载的模型进行预测
y_pred = loaded_model.predict(X_test)

# 打印预测结果
print("Predictions:", y_pred)    
```

## 保存和加载管道


```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
import joblib

# 创建一个管道
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('svc', SVC(kernel='linear'))
])

# 训练管道
pipeline.fit(X_train, y_train)

## 保存
# 保存管道到文件
joblib.dump(pipeline, 'pipeline_model.joblib')

## 加载
# 加载管道
loaded_pipeline = joblib.load('pipeline_model.joblib')

# 使用加载的管道进行预测
y_pred = loaded_pipeline.predict(X_test)

# 打印预测结果
print("Predictions:", y_pred)
```

## 版本管理
每次训练模型并保存时，最好为模型文件命名加上时间戳或版本号，以便区分不同版本的模型  


```python
import time

# 创建时间戳
timestamp = time.strftime("%Y%m%d-%H%M%S")

# 保存带时间戳的模型
joblib.dump(model, f'svm_model_{timestamp}.joblib')
```

## 更多
可以将保存的模型与 Web 服务、批处理作业或其他应用程序集成  
假设我们正在使用 Flask 创建一个简单的 Web 服务，通过 API 接口提供模型预测服务  
>```python
>from flask import Flask, request, jsonify
>import joblib
>import numpy as np
>
>app = Flask(__name__)
>
># 加载模型
>model = joblib.load('svm_model.joblib')
>
>@app.route('/predict', methods=['POST'])
>def predict():
>    data = request.get_json()  # 获取输入数据
>    features = np.array(data['features']).reshape(1, -1)  # 转换成适合预测的格式
>    prediction = model.predict(features)  # 使用加载的模型进行预测
>    return jsonify({'prediction': prediction.tolist()})  # 返回预测结果
>
>if __name__ == '__main__':
>    app.run(debug=True)
>```

# 示例
## 数据加载与可视化


```python
from sklearn.datasets import load_iris
import pandas as pd

# 加载鸢尾花数据集
data = load_iris()

# 转换为 DataFrame 方便查看
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target # 添加目标列 target（0, 1, 2 分别代表三种鸢尾花）
df['species'] = df['target'].apply(lambda x: data.target_names[x]) # 添加物种名称列 species，通过映射 target_names 将数字标签转换为字符串名称

# 查看前5行数据
print(df.head())
```


```python
from sklearn.datasets import load_iris
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 加载鸢尾花数据集
data = load_iris()

# 转换为 DataFrame 方便查看
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target
df['species'] = df['target'].apply(lambda x: data.target_names[x])

# 绘制特征之间的关系
sns.pairplot(df, hue="species") #绘制所有特征两两之间的散点图矩阵,hue="species" 表示用不同颜色区分不同物种
plt.show()
```


```python
from sklearn.datasets import load_iris
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 加载鸢尾花数据集
data = load_iris()

# 转换为 DataFrame 方便查看
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target
df['species'] = df['target'].apply(lambda x: data.target_names[x])

# 绘制特征之间的关系
correlation_matrix = df.drop(columns=['target', 'species']).corr()
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f") # 热力图查看特征之间的相关性
plt.title("Correlation Heatmap")
plt.show()
```

## 特征选择与数据预处理


```python
from sklearn.preprocessing import StandardScaler

# 提取特征和标签
X = df.drop(columns=['target', 'species'])
y = df['target']
# 对于鸢尾花数据集，特征值已经是数值型数据，不需要太多的预处理。但是，我们可以对数据进行标准化，以提高模型的训练效果
# 标准化特征
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```


```python
from sklearn.feature_selection import SelectKBest, f_classif

# 使用卡方检验选择 2 个最相关的特征
selector = SelectKBest(f_classif, k=2)
X_new = selector.fit_transform(X_scaled, y)

# 打印选择的特征
selected_features = selector.get_support(indices=True)
print("Selected features:", X.columns[selected_features])
```

## 建立分类模型


```python
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# 划分数据集
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 初始化决策树分类器
model_dt = DecisionTreeClassifier(random_state=42)

# 训练模型
model_dt.fit(X_train, y_train)

# 预测
y_pred_dt = model_dt.predict(X_test)

# 评估模型
accuracy_dt = accuracy_score(y_test, y_pred_dt)
print(f"Decision Tree Accuracy: {accuracy_dt:.4f}")
```


```python
from sklearn.svm import SVC

# 初始化 SVM 分类器
model_svm = SVC(kernel='linear', random_state=42)

# 训练模型
model_svm.fit(X_train, y_train)

# 预测
y_pred_svm = model_svm.predict(X_test)

# 评估模型
accuracy_svm = accuracy_score(y_test, y_pred_svm)
print(f"SVM Accuracy: {accuracy_svm:.4f}")
```

## 评估模型并优化


```python
from sklearn.metrics import classification_report, confusion_matrix

# 混淆矩阵
cm = confusion_matrix(y_test, y_pred_dt)
print("Confusion Matrix (Decision Tree):")
print(cm)

# 精度、召回率、F1 分数
report = classification_report(y_test, y_pred_dt)
print("Classification Report (Decision Tree):")
print(report)
```


```python
from sklearn.model_selection import GridSearchCV

# 定义决策树的参数网格
param_grid = {
    'max_depth': [3, 5, 10, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

# 初始化 GridSearchCV
grid_search = GridSearchCV(estimator=DecisionTreeClassifier(random_state=42), param_grid=param_grid, cv=5)

# 训练网格搜索
grid_search.fit(X_train, y_train)

# 获取最佳参数和最佳模型
print("Best Parameters:", grid_search.best_params_)
best_model = grid_search.best_estimator_

# 预测和评估
y_pred_optimized = best_model.predict(X_test)
accuracy_optimized = accuracy_score(y_test, y_pred_optimized)
print(f"Optimized Decision Tree Accuracy: {accuracy_optimized:.4f}")
```


```python
from sklearn.model_selection import cross_val_score

# 进行 5 折交叉验证
cross_val_scores = cross_val_score(best_model, X_scaled, y, cv=5)
print(f"Cross-validation Scores: {cross_val_scores}")
print(f"Mean CV Accuracy: {cross_val_scores.mean():.4f}")
```

## 完整代码


```python
# 导入必要的库
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# 1. 数据加载
# 加载鸢尾花数据集
data = load_iris()

# 转换为 DataFrame 方便查看
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target
df['species'] = df['target'].apply(lambda x: data.target_names[x])

# 查看前几行数据
print("数据预览：")
print(df.head())

# 2. 数据可视化
# 绘制特征之间的关系
sns.pairplot(df, hue="species")
plt.show()

# 绘制热力图查看特征之间的相关性
correlation_matrix = df.drop(columns=['target', 'species']).corr()
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

# 3. 特征选择与数据预处理
# 提取特征和标签
X = df.drop(columns=['target', 'species'])
y = df['target']

# 数据标准化
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. 建立分类模型
# 划分数据集
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 使用决策树分类器
model_dt = DecisionTreeClassifier(random_state=42)
model_dt.fit(X_train, y_train)

# 预测
y_pred_dt = model_dt.predict(X_test)

# 输出决策树的准确率
accuracy_dt = accuracy_score(y_test, y_pred_dt)
print(f"Decision Tree Accuracy: {accuracy_dt:.4f}")

# 使用支持向量机（SVM）分类器
model_svm = SVC(kernel='linear', random_state=42)
model_svm.fit(X_train, y_train)

# 预测
y_pred_svm = model_svm.predict(X_test)

# 输出SVM的准确率
accuracy_svm = accuracy_score(y_test, y_pred_svm)
print(f"SVM Accuracy: {accuracy_svm:.4f}")

# 5. 模型评估
# 决策树模型评估
print("\nDecision Tree Classification Report:")
print(classification_report(y_test, y_pred_dt))

print("\nDecision Tree Confusion Matrix:")
print(confusion_matrix(y_test, y_pred_dt))

# SVM模型评估
print("\nSVM Classification Report:")
print(classification_report(y_test, y_pred_svm))

print("\nSVM Confusion Matrix:")
print(confusion_matrix(y_test, y_pred_svm))

# 6. 网格搜索调优
# 定义决策树的参数网格
param_grid = {
    'max_depth': [3, 5, 10, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

# 初始化 GridSearchCV
grid_search = GridSearchCV(estimator=DecisionTreeClassifier(random_state=42), param_grid=param_grid, cv=5)
grid_search.fit(X_train, y_train)

# 获取最佳参数和最佳模型
print("\nBest Parameters from GridSearchCV (Decision Tree):")
print(grid_search.best_params_)

# 使用最佳模型进行预测
best_model = grid_search.best_estimator_
y_pred_optimized = best_model.predict(X_test)

# 输出优化后的决策树准确率
accuracy_optimized = accuracy_score(y_test, y_pred_optimized)
print(f"Optimized Decision Tree Accuracy: {accuracy_optimized:.4f}")

# 7. 交叉验证
# 进行 5 折交叉验证
cross_val_scores = cross_val_score(best_model, X_scaled, y, cv=5)
print("\nCross-validation Scores (Optimized Decision Tree):")
print(cross_val_scores)
print(f"Mean CV Accuracy: {cross_val_scores.mean():.4f}")
```

# 房价预测


```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 模拟数据：包含房屋的面积、房间数、楼层、建造年份、位置（类别变量），以及房价（目标变量）
data = {
    'area': [70, 85, 100, 120, 60, 150, 200, 80, 95, 110],
    'rooms': [2, 3, 3, 4, 2, 5, 6, 3, 3, 4],
    'floor': [5, 2, 8, 10, 3, 15, 18, 7, 9, 11],
    'year_built': [2005, 2010, 2012, 2015, 2000, 2018, 2020, 2008, 2011, 2016],
    'location': ['Chaoyang', 'Haidian', 'Chaoyang', 'Dongcheng', 'Fengtai', 'Haidian', 'Chaoyang', 'Fengtai', 'Dongcheng', 'Haidian'],
    'price': [5000000, 6000000, 6500000, 7000000, 4500000, 10000000, 12000000, 5500000, 6200000, 7500000]  # 房价（目标变量）
}

# 创建 DataFrame
df = pd.DataFrame(data)

# 查看数据
print("数据预览：")
print(df.head())

# 特征选择
X = df[['area', 'rooms', 'floor', 'year_built', 'location']]  # 特征数据
y = df['price']  # 目标变量

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 数据预处理：数值特征标准化、类别特征 One-Hot 编码
numeric_features = ['area', 'rooms', 'floor', 'year_built']
categorical_features = ['location']

# 数值特征预处理：标准化
numeric_transformer = Pipeline(steps=[
    ('scaler', StandardScaler())
])

# 类别特征预处理：One-Hot 编码，设置 handle_unknown='ignore'
categorical_transformer = Pipeline(steps=[
    ('onehot', OneHotEncoder(handle_unknown='ignore'))  
    # handle_unknown='ignore'：如果测试集出现训练集中未见的类别，不会报错，而是将该样本的所有独热编码列设为0（避免预处理失败）
])

# 合并数值和类别特征的处理步骤
preprocessor = ColumnTransformer(
    transformers=[ #transformers：定义列名和对应的预处理管道。格式：(名称, 转换器, 列名列表)
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ]
)

# 3. 建立模型
# 使用线性回归模型，结合数据预处理步骤
model_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

# 训练模型
model_pipeline.fit(X_train, y_train)

# 进行预测
y_pred = model_pipeline.predict(X_test)

# 输出预测结果
print("\n预测结果：")
print(y_pred)

# 4. 模型评估：计算均方误差（MSE）和 R² 决定系数
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n模型评估：")
print(f"均方误差 (MSE): {mse:.2f}")
print(f"决定系数 (R²): {r2:.2f}")

# 5. 模型优化：使用网格搜索调整超参数
# 对线性回归的超参数进行调优（仅调整 'fit_intercept'）
param_grid = {
    'regressor__fit_intercept': [True, False],  # 是否拟合截距
}

grid_search = GridSearchCV(model_pipeline, param_grid, cv=5, scoring='neg_mean_squared_error', verbose=1)
grid_search.fit(X_train, y_train)

# 输出最佳参数和结果
print("\n最佳参数：")
print(grid_search.best_params_)

# 使用最佳模型进行预测
best_model = grid_search.best_estimator_
y_pred_optimized = best_model.predict(X_test)

# 输出优化后的评估结果
mse_opt = mean_squared_error(y_test, y_pred_optimized)
r2_opt = r2_score(y_test, y_pred_optimized)

print("\n优化后的模型评估：")
print(f"均方误差 (MSE): {mse_opt:.2f}")
print(f"决定系数 (R²): {r2_opt:.2f}")
```
