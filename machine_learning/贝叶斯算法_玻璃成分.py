import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.decomposition import PCA

# 加载 glass.csv 数据集
data = pd.read_csv(r'D:\VSCodepythonprogram\machine_learing\glass.csv') 

# 查看数据集的基本信息
print(data.head())
print(data.info())

# 分离特征和标签
X = data.iloc[:, :-1].values  # 假设最后一列是标签
y = data.iloc[:, -1].values   # 标签列

# 拆分数据集为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 配置高斯朴素贝叶斯模型
model = GaussianNB()

# 训练模型
model.fit(X_train, y_train)

# 计算训练集和测试集的准确度
train_accuracy = accuracy_score(y_train, model.predict(X_train))
test_accuracy = accuracy_score(y_test, model.predict(X_test))
print(f"训练集准确度: {train_accuracy}")
print(f"测试集准确度: {test_accuracy}")

# 使用PCA将数据降至两个主成分
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)

# 可视化原始数据集在二维空间中的降维可视化展示
plt.figure(figsize=(8, 6))
for i in range(len(np.unique(y))):
    plt.scatter(X_reduced[y == i, 0], X_reduced[y == i, 1], label=f'Class {i}')
plt.title('Original Data Visualization')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.legend()
plt.show()

# 可视化分类结果
plt.figure(figsize=(8, 6))
for i in range(len(np.unique(y))):
    plt.scatter(X_reduced[y == i, 0], X_reduced[y == i, 1], label=f'Class {i}')
    plt.scatter(X_reduced[model.predict(X) == i, 0], X_reduced[model.predict(X) == i, 1],
                label=f'Class {i} Predicted', marker='x', alpha=0.6)
plt.title('Glass Classification Visualization')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.legend()
plt.show()