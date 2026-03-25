import numpy as np
import datetime
from matplotlib import pyplot as plt


# dt64=np.datetime64('2020-05-12 12:00:02')
# dt=dt64.astype(datetime.datetime)
# print(dt,type(dt))

# dates = np.arange('2020-02-01', '2020-02-10', dtype=np.datetime64)
# print(dates)

# today=np.datetime64('today')
# yestoday=today-np.timedelta64(1,'D')
# print(yestoday)

# a=np.arange(10)
# a=np.array([0,1,2,3])
# print(a)

# a=np.full((3,3),True)
# print(a)
# b=np.ones((3,3,3))
# print(b)

# a=np.zeros(10)
# a[4]=1
# print(a)

# a=np.arange(10,50)
# print(a)

# a=np.empty((3,3,3))
# print(a)

# a=np.ones((5,5))
# a[1:-1,1:-1]=0
# print(a)

# a=np.arange(5,35,3)
# print(a)

# from PIL import Image
# img=Image.open(r"")
# a=np.array(img)
# print(a.shape,a.dtype)

# a=np.array([[1,2],
#             [3,4],
#             [5,6]])
# b=a[0:1,0:1]
# print(b)
# b[0,0]=2
# print(a)


# arr = np.arange(9).reshape(3, 3)
# print(arr)
# x=arr[:,::-1]
# print(x)

# import numpy as np
# import matplotlib.pyplot as plt

# x = np.array([[1, 4, 9, 16, 25]])
# print(x.shape)  # (1, 5)
# plt.plot(x)
# plt.show()


# x = np.array([[1, 4, 9, 16, 25]])
# x = np.squeeze(x)
# print(x.shape)  # (5, )
# plt.plot(x)
# plt.show()

# a = np.arange(10)
# print(a)
# a.shape=[2,5]
# print(a)

# b=a.flatten()
# print(b)

# c=np.ravel(a)
# print(c)

# d=np.reshape(a,[2,5])
# print(d)

# a = np.arange(10).reshape([2, -1])
# b = np.repeat(1, 10).reshape([2, -1])
# print(a)
# print(b)

# print(np.concatenate((a,b)))
# print(np.vstack((a,b)))
# print(np.concatenate((a,b),axis=1))
# print(np.hstack((a,b)))

# arr = np.array([[16, 17, 18, 19, 20],[11, 12, 13, 14, 15],[21, 22, 23, 24, 25],[31, 32, 33, 34, 35],[26, 27, 28, 29, 30]])
# print(np.hsplit(arr,5))
# print(arr.flatten(order='F'))

# x=np.arange(5)
# print(x)

# print(np.logical_and([True,False],[True,False]))

# x = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# y = x > 2
# print(y)

# a = np.random.uniform(1, 50, 20)
# print(a)
# a=np.clip(a,10,30)
# print(a)

# a = np.array([1, 3, 7, 1, 2, 6, 0, 1])
# b1=np.diff(a)
# print(b1)
# # [ 2  4 -6  1  4 -6  1]
# for i in range(1,6):
#     if a[i]>a[i+1] and a[i]>a[i-1]:
#         print(f'index:{i}')

# a=np.array([8,8,3,7,7,0,4,2,5,2])
# b=np.cumsum(a)
# print(b) # [ 8 16 19 26 33 33 37 39 44 46]
# for i in range(2,10):# 2 3 4 5 6 7 8 9
#     c=0
#     if i>2:
#         c=b[i-3]
#     print(np.around((b[i]-c)/3,2))

# Z = np.random.random((5,5))
# # (提示: (x - min) / (max - min))
# for i in Z:
#     i=((i - Z.min())/(Z.max() - Z.min()))
#     print(Z)

# Z = np.random.uniform(0,10,10)
# print(np.around(Z))
# print(np.floor(Z))
# print(np.ceil(Z)-1)
# print(Z-Z%1)
# print(np.trunc(Z))
# print(Z.astype(int))

# x = np.arange(0, 3*np.pi, 0.1)
# y1=np.sin(x)
# y2=np.cos(x)
# plt.plot(y1)
# plt.plot(y2)
# plt.show()

# a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
# b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
# mask=np.equal(a,b) 
# print(np.where(mask)) # np.where(mask) 返回一个元组，其中包含 mask 中值为 True 的索引

# a = np.array([2, 6, 1, 9, 10, 3, 27])
# mask=np.logical_and(np.less_equal(a,10),np.greater_equal(a,5))
# print(np.where(mask)) #对应的索引
# x = np.where(mask)
# print(a[x])  # [ 6  9 10]

# A = np.random.randint(0,2,5) 
# B = np.random.randint(0,2,5)
# print(np.isclose(A,B))
# print(np.allclose(A,B))

# Z = np.array([0.2,1.15])
# print(Z)
# # Z=np.logical_not(Z)
# # print(Z)
# Z=np.negative(Z)
# print(Z)

# # 前5个最大值的位置
# np.random.seed(100)
# a = np.random.randint(1, 50, 20)
# # [ 9 25  4 40 24 16 49 11 31 35  3 35 15 35 49 25 16 37 44 17]
# b=np.argsort(a)
# print(b[-5:])

# c=np.sort(a)
# d=np.where(a>c[-6])
# print(d)

# e=np.argpartition(a,kth=-5)
# print(e[-5:])

# # 删除一维numpy数组中所有NaN值
# a = np.array([1, 2, 3, np.nan, 5, 6, 7, np.nan])
# b = np.isnan(a)
# c=np.where(b == False)
# print(a[c])

# # 获取给定数组a中比7大的数有多少
# np.random.seed(100)
# a = np.random.randint(1, 50, 20)
# # [ 9 25  4 40 24 16 49 11 31 35  3 35 15 35 49 25 16 37 44 17]
# a.sort()
# # [ 3  4  9 11 15 16 16 17 24 25 25 31 35 35 35 37 40 44 49 49]
# print(a)
# print(np.searchsorted(a,7))
# # 2
# print(len(a)-np.searchsorted(a,7))
# # 18

# # 获取数组a和数组b之间的公共项
# a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
# b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
# print(np.intersect1d(a,b))

# # 从数组a中删除数组b中的所有项
# a = np.array([1, 2, 3, 4, 5])
# b = np.array([5, 6, 7, 8, 9])
# print(np.setdiff1d(a,b))

# # 如何在numpy数组中只打印小数点后三位
# np.set_printoptions(precision=3)
# a=np.array([1.25358,2.546686,5.68463561])
# print(a)

# # 将numpy数组a中打印的项数限制为最多6个元素
# np.set_printoptions(threshold=6)
# a=np.array([1,5,6,3,2,4,9,8,7,0])
# print(a)
# # 打印完整的numpy数组a而不中断
# np.set_printoptions(threshold=9999)
# print(a)

# # 创建一个形为5×3的二维数组，以包含5到10之间的随机数
# a=np.random.randint(5,10,[5,3])
# b=np.random.uniform(5,10,[5,3])
# print(a)
# print(b)

# # 计算给定数组中每行的最大值
# np.random.seed(100)
# a = np.random.randint(1, 10, [5, 3])
# print(a)
# # [[9 9 4]
# #  [8 8 1]
# #  [5 3 6]
# #  [3 3 3]
# #  [2 1 9]]
# print(np.amax(a,axis=1))
# # [9 8 6 3 9]

# # 计算两个数组a和数组b之间的欧氏距离
# a = np.array([1, 2, 3, 4, 5])
# b = np.array([4, 5, 6, 7, 8])
# print(np.linalg.norm(a-b))
# print(np.sqrt(np.sum((a-b)**2)))

# # 计算矩阵的行列式和矩阵的逆
# a=np.diag([5,5,5,5,5])
# print(np.linalg.det(a))
# print(np.linalg.inv(a))

# from sklearn import datasets
# iris=datasets.load_iris()
# # 求出鸢尾属植物萼片长度的平均值、中位数和标准差（第1列，sepallength）
# sepal=iris.data[:,0] # 第1列 萼片长度
# print(f'平均值:{np.mean(sepal):.2f}')
# print(f'中位数:{np.median(sepal)}')
# print(f'标准差:{np.std(sepal)}')

# # 创建一种标准化形式的鸢尾属植物萼片长度，其值正好介于0和1之间，这样最小值为0，最大值为1（第1列，sepallength）
# sepal_min=np.min(sepal)
# sepal_max=np.max(sepal)
# normalized_sepal_length = (sepal-sepal_min) / (sepal_max - sepal_min)
# # print(sepal_max)
# # print(sepal_min)
# # print("标准化后的萼片长度:", normalized_sepal_length)

# # 找到鸢尾属植物萼片长度的第5和第95百分位数（第1列，sepallength）
# print(f'第5和第95百分位数:{np.percentile(sepal,5)}和{np.percentile(sepal,95)}')

# # 把iris_data数据集中的20个随机位置修改为np.nan值
# np.random.seed(42)

# # 在iris_data的sepallength中查找缺失值的个数和位置（第1列）
# count=np.isnan(sepal).sum()
# indices=np.where(np.isnan(sepal))[0]
# print(f"缺失值的个数: {count}")
# print(f"缺失值的位置（索引）: {indices}")

# #  筛选具有 sepallength（第1列）< 5.0 并且 petallength（第3列）> 1.5 的 iris_data行
# petal=iris.data[:,2]
# condition=(sepal<5.0)&(petal>1.5)
# print(np.where(condition))
# # np.where 返回一个元组，因此使用 [0] 来获取第一个元素，即满足条件的行的索引
# indices=np.where(condition)[0]
# print(indices)
# print(iris.data[indices])

# #  选择没有任何 nan 值的 iris_data行
# mask = ~np.isnan(iris.data).any(axis=1)
# # np.isnan(iris.data) True 表示对应位置的元素是 np.nan
# # .any(axis=1) 对于每一行，它会检查该行中是否有任何 True
# # ~ 取反
# rows = iris.data[mask]
# print("没有 np.nan 值的行数:", len(rows))
# # print("没有 np.nan 值的行数据:")
# # print(rows)

# # 计算 iris_data 中sepalLength（第1列）和petalLength（第3列）之间的相关系数
# print(f'相关系数:{np.corrcoef(sepal,petal)}')

# # 找出iris_data是否有任何缺失值
# values = np.isnan(iris.data).any() 
# print(values)
# if values:
#     print("数据集中存在缺失值。")
# else:
#     print("数据集中没有缺失值。")

# #  在numpy数组中将所有出现的nan替换为0
# iris.data[np.isnan(iris.data)]=0

# # 将 iris_data 的花瓣长度（第3列）以形成分类变量的形式显示。定义：Less than 3 --> 'small'；3-5 --> 'medium'；'>=5 --> 'large'
# petal_categories = np.where(petal < 3, 'small',np.where((petal >= 3) & (petal < 5), 'medium', 'large'))
# print("花瓣长度分类:")
# print(petal_categories)

# # 根据 sepallength 列对数据集进行排序
# sorted_indices = np.argsort(iris.data[:,0])
# # 特征（数据）和标签（目标）通常需要分别排序
# sorted_data = iris.data[sorted_indices]
# sorted_target = iris.target[sorted_indices]

# # 在鸢尾属植物数据集中找到最常见的花瓣长度值(第3列)
# values, counts = np.unique(iris.data, return_counts=True)
# max_count_index = np.argmax(counts)
# print(f"最常见的花瓣长度值是: {values[max_count_index]} cm")
# print(f"该值出现了 {counts[max_count_index]} 次")

# # 在鸢尾花数据集的 petalwidth（第4列）中查找第一次出现的值大于1.0的位置
# petal_width=iris.data[:,3]
# # 找到第一个大于1.0的值的索引
# first_index = np.where(petal_width > 1.0)[0][0]
# print(f"第一次出现 petal width 大于1.0的位置是索引: {first_index}")
# print(f"对应的 petal width 值是: {petal_width[first_index]}")

