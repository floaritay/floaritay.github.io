import pandas as pd
from sklearn import svm
import numpy as np

## 6.2分别用线性核和高斯核训练一个SVM，并比较其支持向量的差别

# 提取数据集
data = {
    '密度': [0.697, 0.774, 0.634, 0.608, 0.556, 0.403, 0.481, 0.437, 0.666, 0.243, 0.245, 0.343, 0.639, 0.657, 0.360, 0.593, 0.719],
    '含糖率': [0.460, 0.376, 0.264, 0.318, 0.215, 0.237, 0.149, 0.211, 0.091, 0.267, 0.057, 0.099, 0.161, 0.198, 0.370, 0.042, 0.103],
    '好瓜': [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}

df = pd.DataFrame(data)

# 特征和标签
X = df[['密度', '含糖率']]
y = df['好瓜']
# X=df[:,:-1]
# y=df[:,-1]

# 线性核 SVM 模型
linear_svm = svm.SVC(kernel='linear')
linear_svm.fit(X, y)
linear_support_vectors = linear_svm.support_

# 高斯核 RBF SVM 模型
rbf_svm = svm.SVC(kernel='rbf')
rbf_svm.fit(X, y)
rbf_support_vectors = rbf_svm.support_

print("线性核支持向量索引:", linear_support_vectors)
print("高斯核支持向量索引:", rbf_support_vectors)
# 线性核支持向量索引: [ 8  9 11 12 13 14 15 16  0  1  2  3  4  5  6  7]
# 高斯核支持向量索引: [ 8  9 10 11 12 13 14 15 16  0  1  2  3  4  5  6  7]
# 索引为 10 的样本点 (密度=0.245, 含糖率=0.057, 好瓜=0) 在线性核模型中不是边界上的关键点，因此没有被选为支持向量
# 说明高斯核则能够更好地捕捉数据的复杂模式

# 打印具体的样本点
print("\n线性核支持向量:")
for i in linear_support_vectors:
    print(df.iloc[i])

print("\n高斯核支持向量:")
for i in rbf_support_vectors:
    print(df.iloc[i])



## 6.3(选取了load_iris和load_breast_cancer数据集)分别用线性核和高斯核训练一个SVM，并与BP神经网络和C4.5决策树进行实验比较

# 导入数据集
from sklearn.datasets import load_iris , load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,classification_report
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier

# 鸢尾花数据集
data1=load_iris()
X1=data1.data
y1=data1.target

# 划分数据集
X1_train,X1_test,y1_train,y1_test=train_test_split(X1,y1,test_size=0.2,random_state=42)

# 线性核 SVM 模型
iris_linear_svm=svm.SVC(kernel='linear')
iris_linear_svm.fit(X1_train,y1_train)
y1_pred=iris_linear_svm.predict(X1_test)
accuracy = accuracy_score(y1_test, y1_pred)
print(f"Model: iris_linear_svm")
print(f"Accuracy: {accuracy:.2f}")
print("Classification Report:")
print(classification_report(y1_test, y1_pred))
print("\n")

# 高斯核 RBF SVM 模型
iris_rbf_svm=svm.SVC(kernel='rbf')
iris_rbf_svm.fit(X1_train,y1_train)
y1_pred=iris_rbf_svm.predict(X1_test)
accuracy = accuracy_score(y1_test, y1_pred)
print(f"Model: iris_rbf_svm")
print(f"Accuracy: {accuracy:.2f}")
print("Classification Report:")
print(classification_report(y1_test, y1_pred))
print("\n")

# BP Neural Network 模型
iris_bp_nn = MLPClassifier(hidden_layer_sizes=(50,), max_iter=2000, learning_rate_init=0.001, random_state=42)
iris_bp_nn.fit(X1_train, y1_train)
y1_pred = iris_bp_nn.predict(X1_test)
accuracy = accuracy_score(y1_test, y1_pred)
print(f"Model: iris_bp_nn")
print(f"Accuracy: {accuracy:.2f}")
print("Classification Report:")
print(classification_report(y1_test, y1_pred))
print("\n")

# C4.5 Decision Tree 模型 (使用 CART 算法作为代理)
iris_c45_tree = DecisionTreeClassifier(criterion='entropy', random_state=42)
iris_c45_tree.fit(X1_train, y1_train)
y1_pred = iris_c45_tree.predict(X1_test)
accuracy = accuracy_score(y1_test, y1_pred)
print(f"Model: iris_c45_tree")
print(f"Accuracy: {accuracy:.2f}")
print("Classification Report:")
print(classification_report(y1_test, y1_pred))
print("\n")


# 乳腺癌数据集
data2=load_breast_cancer()
X2=data2.data
y2=data2.target

# 划分数据集
X2_train,X2_test,y2_train,y2_test=train_test_split(X2,y2,test_size=0.2,random_state=42)

# 线性核 SVM 模型
cancer_linear_svm=svm.SVC(kernel='linear')
cancer_linear_svm.fit(X2_train,y2_train)
y2_pred=cancer_linear_svm.predict(X2_test)
accuracy = accuracy_score(y2_test, y2_pred)
print(f"Model: cancer_linear_svm")
print(f"Accuracy: {accuracy:.2f}")
print("Classification Report:")
print(classification_report(y2_test, y2_pred))
print("\n")

# 高斯核 RBF SVM 模型
cancer_rbf_svm=svm.SVC(kernel='rbf')
cancer_rbf_svm.fit(X2_train,y2_train)
y2_pred=cancer_rbf_svm.predict(X2_test)
accuracy = accuracy_score(y2_test, y2_pred)
print(f"Model: cancer_rbf_svm")
print(f"Accuracy: {accuracy:.2f}")
print("Classification Report:")
print(classification_report(y2_test, y2_pred))
print("\n")

# BP Neural Network 模型
cancer_bp_nn = MLPClassifier(hidden_layer_sizes=(50,), max_iter=2000, learning_rate_init=0.001, random_state=42)
cancer_bp_nn.fit(X2_train, y2_train)
y2_pred = cancer_bp_nn.predict(X2_test)
accuracy = accuracy_score(y2_test, y2_pred)
print(f"Model: cancer_bp_nn")
print(f"Accuracy: {accuracy:.2f}")
print("Classification Report:")
print(classification_report(y2_test, y2_pred))
print("\n")

# C4.5 Decision Tree 模型 (使用 CART 算法作为代理)
cancer_c45_tree = DecisionTreeClassifier(criterion='entropy', random_state=42)
cancer_c45_tree.fit(X2_train, y2_train)
y2_pred = cancer_c45_tree.predict(X2_test)
accuracy = accuracy_score(y2_test, y2_pred)
print(f"Model: cancer_c45_tree")
print(f"Accuracy: {accuracy:.2f}")
print("Classification Report:")
print(classification_report(y2_test, y2_pred))
print("\n")
