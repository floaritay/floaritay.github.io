# 参考课程资料中的“03-机器学习库Scikit-learn.zip”，读取附件中的三个训练数据集，并参考教材P25-26页内容，
# 用一种方法划分出训练集S和测试集T，显示出数据集的基本信息，并打印出一部分数据。


# import pandas as pd
# from sklearn.model_selection import train_test_split

# # 导入三个CSV文件
# file1 = r'machine_learing\wine_data.csv'
# file2 = r'machine_learing\breast_cancer.csv'
# file3 = r'machine_learing\prices.csv'

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

import pandas as pd
from sklearn.model_selection import train_test_split


# 修复列名并读取文件
column_names = [
    'Alcohol', 'Malic_acid', 'Ash', 'Alcalinity', 'Magnesium',
    'Phenols', 'Flavanoids', 'Nonflavanoid_phenols', 'Proanthocyanins',
    'Color_intensity', 'Hue', 'OD280_OD315', 'Proline', 'Class'
]

# 读取CSV文件
file1 = "machine_learing\\wine_data.csv"
file2 = 'machine_learing\\breast_cancer.csv'
file3 = 'machine_learing\\prices.csv'
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
print("数据集前5行:")
print(data.head())

print("\n" + "="*50)
print("类别分布：")
print(y.value_counts()) # 显示类别分布

print("\n" + "="*50)
print("训练集大小：", X_train.shape)
print("测试集大小：", X_test.shape)

