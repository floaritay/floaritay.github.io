import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import accuracy_score

# 加载MNIST数据集
digits = load_digits()
X = digits.data / 16.0  # 归一化
y = digits.target

# one-hot编码
encoder = OneHotEncoder(sparse_output=False)
y_onehot = encoder.fit_transform(y.reshape(-1, 1))

# 分割数据集
X_train, X_test, y_train, y_test = train_test_split(X, y_onehot, test_size=0.2, random_state=42)

# 初始化参数
input_size = 64
hidden_size = 128
output_size = 10
learning_rate = 0.1
epochs = 1000

# 随机初始化权重和偏置
W1 = np.random.randn(input_size, hidden_size)
b1 = np.zeros(hidden_size)
W2 = np.random.randn(hidden_size, output_size)
b2 = np.zeros(output_size)

# 定义激活函数和其导数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# 训练神经网络
for epoch in range(epochs):
    # 前向传播
    z1 = np.dot(X_train, W1) + b1
    a1 = sigmoid(z1)
    z2 = np.dot(a1, W2) + b2
    a2 = sigmoid(z2)

    # 计算损失
    loss = np.mean((a2 - y_train) ** 2)

    # 反向传播
    d_z2 = a2 - y_train
    d_W2 = np.dot(a1.T, d_z2)
    d_b2 = np.sum(d_z2, axis=0)
    d_a1 = np.dot(d_z2, W2.T)
    d_z1 = d_a1 * sigmoid_derivative(a1)
    d_W1 = np.dot(X_train.T, d_z1)
    d_b1 = np.sum(d_z1, axis=0)

    # 更新权重和偏置
    W1 -= learning_rate * d_W1
    b1 -= learning_rate * d_b1
    W2 -= learning_rate * d_W2
    b2 -= learning_rate * d_b2

    if epoch % 100 == 0:
        print(f'Epoch {epoch}, Loss: {loss}')

# 测试神经网络
z1 = np.dot(X_test, W1) + b1
a1 = sigmoid(z1)
z2 = np.dot(a1, W2) + b2
a2 = sigmoid(z2)
predictions = np.argmax(a2, axis=1)
true_labels = np.argmax(y_test, axis=1)
accuracy = accuracy_score(true_labels, predictions)
print(f'Accuracy: {accuracy}')

# 可视化部分结果
fig, axes = plt.subplots(1, 4, figsize=(10, 3))
for ax, img, pred, true in zip(axes, X_test, predictions, true_labels):
    ax.set_axis_off()
    ax.imshow(img.reshape(8, 8), cmap=plt.cm.gray_r, interpolation='nearest')
    ax.set_title(f'Pred: {pred}, True: {true}')
plt.show()