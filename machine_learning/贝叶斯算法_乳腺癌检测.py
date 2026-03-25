# from sklearn.naive_bayes import MultinomialNB
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# 加载数据集
data = load_breast_cancer()
X, y = data.data, data.target  # 特征和标签

# 划分训练集和测试集（80%训练，20%测试）
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 构建高斯朴素贝叶斯模型
model = GaussianNB()

# 训练模型
model.fit(X_train, y_train)

# 模型评分
train_score = model.score(X_train, y_train)  # 训练集评分
test_score = model.score(X_test, y_test)    # 测试集评分

# 打印结果
print(f"训练集评分: {train_score:.4f}")
print(f"测试集评分: {test_score:.4f}")

# 选取某一样本进行预测
sample_index = 0  # 选择第一个样本
sample = X_test[sample_index].reshape(1, -1)  # 重塑为二维数组
predicted = model.predict(sample)
print(f"样本 {sample_index} 的预测结果: {'恶性' if predicted[0] == 1 else '良性'}")
print(f"实际标签: {'恶性' if y_test[sample_index] == 1 else '良性'}")
sample_index = 100  # 选择第100个样本
sample = X_test[sample_index].reshape(1, -1)  
predicted = model.predict(sample)
print(f"样本 {sample_index} 的预测结果: {'恶性' if predicted[0] == 1 else '良性'}")
print(f"实际标签: {'恶性' if y_test[sample_index] == 1 else '良性'}")