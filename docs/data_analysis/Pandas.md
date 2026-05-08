# 数据结构
Pandas 的主要数据结构是 Series （一维数据）与 DataFrame（二维数据）  
- Series 是一种类似于一维数组的对象，它由一组数据（各种 Numpy 数据类型）以及一组索引组成     
Series 可以看作是 DataFrame 中的一列，也可以是单独存在的一维数据结构 
- DataFrame 是一个表格型的数据结构，它含有一组有序的列，每列可以是不同的值类型（数值、字符串、布尔型值）  
DataFrame 既有行索引也有列索引，它可以被看做由 Series 组成的字典（共同用一个索引）  
  
    
DataFrame 由 Index、Key、Value 组成


```python
import pandas as pd

# 创建一个简单的 DataFrame
data = {'Name': ['Google', 'Runoob', 'Taobao'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)

# 查看 DataFrame
print(df)

#      Name  Age
# 0  Google   25
# 1  Runoob   30
# 2  Taobao   35
```


```python
import pandas as pd

# 创建两个Series对象
series_apples = pd.Series([1, 3, 7, 4])
series_bananas = pd.Series([2, 6, 3, 5])

# 将两个Series对象相加，得到DataFrame，并指定列名
df = pd.DataFrame({ 'Apples': series_apples, 'Bananas': series_bananas })

# 显示DataFrame
print(df)
```

# Series
类似于一个一维的数组，具有数据和索引


```python
import pandas as pd

# 创建一个Series对象，指定名称为'A'，值分别为1, 2, 3, 4
# 默认索引为0, 1, 2, 3
series = pd.Series([1, 2, 3, 4], name='A')

# 显示Series对象
print(series)

# 如果你想要显式地设置索引，可以这样做：
custom_index = [1, 2, 3, 4]  # 自定义索引
series_with_index = pd.Series([1, 2, 3, 4], index=custom_index, name='A')

# 显示带有自定义索引的Series对象
print(series_with_index)

# 0    1
# 1    2
# 2    3
# 3    4
# Name: A, dtype: int64
# 1    1
# 2    2
# 3    3
# 4    4
# Name: A, dtype: int64
```

## pd.Series()
``pandas.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)``  
创建一个 Series 对象，传递一个数据数组（可以是列表、NumPy 数组等）和一个可选的索引数组  
  
- data：Series 的数据部分，可以是列表、数组、字典、标量值等。如果不提供此参数，则创建一个空的 Series。
- index：Series 的索引部分，用于对数据进行标记。可以是列表、数组、索引对象等。如果不提供此参数，则创建一个默认的整数索引。
- dtype：指定 Series 的数据类型。可以是 NumPy 的数据类型，例如 np.int64、np.float64 等。如果不提供此参数，则根据数据自动推断数据类型。
- name：Series 的名称，用于标识 Series 对象。如果提供了此参数，则创建的 Series 对象将具有指定的名称。
- copy：是否复制数据。默认为 False，表示不复制数据。如果设置为 True，则复制输入的数据。
- fastpath：是否启用快速路径。默认为 False。启用快速路径可能会在某些情况下提高性能。




```python
import pandas as pd

a = ["Google", "Runoob", "Wiki"]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar["y"])

# 也可以使用 key/value 对象，类似字典来创建 Series

sites = {1: "Google", 2: "Runoob", 3: "Wiki"}

myvar = pd.Series(sites)

print(myvar)

# 如果我们只需要字典中的一部分数据，只需要指定需要数据的索引即可

sites = {1: "Google", 2: "Runoob", 3: "Wiki"}

myvar = pd.Series(sites, index = [1, 2])

print(myvar)
```

## Series方法
| 方法名称       | 功能描述                                                                 |
|----------------|--------------------------------------------------------------------------|
| index          | 获取 Series 的索引                                                       |
| values         | 获取 Series 的数据部分（返回 NumPy 数组）                                 |
| head(n)        | 返回 Series 的前 n 行（默认为 5）                                        |
| tail(n)        | 返回 Series 的后 n 行（默认为 5）                                        |
| dtype          | 返回 Series 中数据的类型                                                 |
| shape          | 返回 Series 的形状（行数）                                               |
| describe()      | 返回 Series 的统计描述（如均值、标准差、最小值等）                        |
| isnull()       | 返回一个布尔 Series，表示每个元素是否为 NaN                               |
| notnull()      | 返回一个布尔 Series，表示每个元素是否不是 NaN                             |
| unique()       | 返回 Series 中的唯一值（去重）                                           |
| value_counts() | 返回 Series 中每个唯一值的出现次数                                       |
| map(func)      | 将指定函数应用于 Series 中的每个元素                                       |
| apply(func)    | 将指定函数应用于 Series 中的每个元素，常用于自定义操作                     |
| astype(dtype)  | 将 Series 转换为指定的类型                                               |
| sort_values()  | 对 Series 中的元素进行排序（按值排序）                                   |
| sort_index()   | 对 Series 的索引进行排序                                                 |
| dropna()       | 删除 Series 中的缺失值（NaN）                                           |
| fillna(value)  | 填充 Series 中的缺失值（NaN）                                           |
| replace(to_replace, value) | 替换 Series 中指定的值                                              |
| cumsum()       | 返回 Series 的累计求和                                                   |
| cumprod()      | 返回 Series 的累计乘积                                                   |
| shift(periods) | 将 Series 中的元素按指定的步数进行位移                                     |
| rank()         | 返回 Series 中元素的排名                                                 |
| corr(other)    | 计算 Series 与另一个 Series 的相关性（皮尔逊相关系数）                     |
| cov(other)     | 计算 Series 与另一个 Series 的协方差                                       |
| to_list()      | 将 Series 转换为 Python 列表                                             |
| to_frame()     | 将 Series 转换为 DataFrame                                               |
| iloc[]         | 通过位置索引来选择数据                                                   |
| loc[]          | 通过标签索引来选择数据                                                   |


```python
import pandas as pd

# 创建 Series
data = [1, 2, 3, 4, 5, 6]
index = ['a', 'b', 'c', 'd', 'e', 'f']
s = pd.Series(data, index=index)

# 查看基本信息
print("索引:", s.index)
print("数据:", s.values)
print("数据类型:", s.dtype)
print("前两行数据:", s.head(2))

# 使用 map 函数将每个元素加倍
s_doubled = s.map(lambda x: x * 2)
print("元素加倍后:", s_doubled)

# 计算累计和
cumsum_s = s.cumsum()
print("累计求和:", cumsum_s)

# 查找缺失值（这里没有缺失值，所以返回的全是 False）
print("缺失值判断:", s.isnull())

# 排序
sorted_s = s.sort_values()
print("排序后的 Series:", sorted_s)

print(s.sum())  # 输出 Series 的总和
print(s.mean())  # 输出 Series 的平均值
print(s.max())  # 输出 Series 的最大值
print(s.min())  # 输出 Series 的最小值
print(s.std())  # 输出 Series 的标准差

# 获取描述统计信息
print(s.describe())

# 获取最大值和最小值的索引
print(s.idxmax())
print(s.idxmin())

# 将 Series 中的所有元素转换为 float64 类型
s = s.astype('float64')  
# 输出 Series 的数据类型
print(s.dtype)
```

## 更多


```python
## 创建方法
import numpy as np
# 使用列表创建 Series
s = pd.Series([1, 2, 3, 4])

# 使用 NumPy 数组创建 Series
s = pd.Series(np.array([1, 2, 3, 4]))

# 使用字典创建 Series
s = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4})
```


```python
## 基本操作
# 指定索引创建 Series
s = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])

# 获取值
print(s['a'])  # 返回索引标签 'a' 对应的元素
# 1
# 使用切片语法来访问 Series 的一部分
print(s['b':'c'])  # 返回索引标签 'b' 到 'c' 之间的元素
print(s[1:3])  # 返回第一到第二个元素
# b    2
# c    3
# dtype: int64

# .item()
for index, value in s.items():
    print(f"Index: {index}, Value: {value}")
# Index: a, Value: 1
# Index: b, Value: 2
# Index: c, Value: 3
# Index: d, Value: 4


# 为特定的索引标签赋值
s['a'] = 10  # 将索引标签 'a' 对应的元素修改为 10

# 通过赋值给新的索引标签来添加元素
s['e'] = 5  # 在 Series 中添加一个新的元素，索引标签为 'e'

# 使用 del 删除指定索引标签的元素。
del s['a']  # 删除索引标签 'a' 对应的元素

# 使用 drop 方法删除一个或多个索引标签，并返回一个新的 Series。
s_dropped = s.drop(['b'])  # 返回一个删除了索引标签 'b' 的新 Series
print(s_dropped)
# c    3
# d    4
# e    5
# dtype: int64
```


```python
# 算术运算
result = series * 2  # 所有元素乘以2

# 过滤
filtered_series = series[series > 2]  # 选择大于2的元素

# 数学函数
import numpy as np
result = np.sqrt(series)  # 对每个元素取平方根

print(s > 2)  # 返回一个布尔 Series，其中的元素值大于 2
```

---
# DataFrame

## pd.DataFrame()
``pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)``
  
- data：DataFrame 的数据部分，可以是字典、二维数组、Series、DataFrame 或其他可转换为 DataFrame 的对象。如果不提供此参数，则创建一个空的 DataFrame。
  
- index：DataFrame 的行索引，用于标识每行数据。可以是列表、数组、索引对象等。如果不提供此参数，则创建一个默认的整数索引
  
- columns：DataFrame 的列索引，用于标识每列数据。可以是列表、数组、索引对象等。如果不提供此参数，则创建一个默认的整数索引。
  
- dtype：指定 DataFrame 的数据类型。可以是 NumPy 的数据类型，例如 np.int64、np.float64 等。如果不提供此参数，则根据数据自动推断数据类型。
  
- copy：是否复制数据。默认为 False，表示不复制数据。如果设置为 True，则复制输入的数据。


```python
import pandas as pd
## 1.使用列表
data = [['Google', 10], ['Runoob', 12], ['Wiki', 13]]

df = pd.DataFrame(data, columns=['Site', 'Age'])

# 使用astype方法设置每列的数据类型
df['Site'] = df['Site'].astype(str)
df['Age'] = df['Age'].astype(float)

print(df)

## 2.使用字典
data = {'Site':['Google', 'Runoob', 'Wiki'], 'Age':[10, 12, 13]}
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]

df = pd.DataFrame(data)

print (df)

## 3.使用Series 
s1 = pd.Series(['Alice', 'Bob', 'Charlie'])
s2 = pd.Series([25, 30, 35])
s3 = pd.Series(['New York', 'Los Angeles', 'Chicago'])
df = pd.DataFrame({'Name': s1, 'Age': s2, 'City': s3})

# 以下实例使用 ndarrays 创建,ndarray 的长度必须相同,
# 如果传递了 index,则索引的长度应等于数组的长度,
# 如果没有传递索引，则默认情况下，索引将是range(n)，其中n是数组长度

## 4.使用 ndarrays 
import numpy as np
ndarray_data = np.array([
    ['Google', 10],
    ['Runoob', 12],
    ['Wiki', 13]
])

df = pd.DataFrame(ndarray_data, columns=['Site', 'Age'])

print(df)
```


```python
import pandas as pd

data = {
  "A": [420, 380, 390],
  "B": [50, 40, 45]
}

df = pd.DataFrame(data)

## 1.返回指定行和列

# 返回第一行
print(df.loc[0])
# A    420
# B     50
# Name: 0, dtype: int64
# 返回结果其实就是一个 Pandas Series 数据

# 返回第一列
print(df.loc[:,'A'])
# 0    420
# 1    380
# 2    390
# Name: A, dtype: int64

## 2.返回多行多列

# 返回第一行和第二行
print(df.loc[[0, 1]])
#    A  B
# 0       420        50
# 1       380        40
# 返回结果其实就是一个 Pandas DataFrame 数据

# 返回第一 和 第三行，'A' 和 'B'列的数据
print(df.loc[[0,2],['A','B']])      #使用列表
# 返回第一 到 第三行，'A' 到 'B'列的数据  注意与上一行的区别
print(df.iloc[0:3,0:2])             #使用切片，切片不包含结束索引

## 3.提取列（Series 或值）

column_a = df['A']           # 返回列'A'的Series
values = df['A'].values             # 返回 NumPy 数组
values = df['A'].to_numpy()         # 推荐方式
subset = df[['A', 'B']]      # 返回包含列'A'和'B'的DataFrame

## 4.条件筛选

# 选择列'A'值大于1的行
filtered = df[df['A'] > 1]
# 多条件筛选（用 & 或 |）
filtered = df[(df['A'] > 1) & (df['B'] == 'z')]
```


```python
import pandas as pd

data = {
  "A": [420, 380, 390],
  "B": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
# 指定索引
print(df.loc["day2"])
# A    380
# B     40
# Name: day2, dtype: int64
```

## DataFrame 方法
| 方法名称               | 功能描述                                                                 |
|------------------------|--------------------------------------------------------------------------|
| `head(n)`              | 返回 DataFrame 的前 n 行数据（默认前 5 行）                               |
| `tail(n)`              | 返回 DataFrame 的后 n 行数据（默认后 5 行）                               |
| `info()`               | 显示 DataFrame 的简要信息（列名、数据类型、非空值数量等）                 |
| `describe()`           | 返回数值列的统计信息（均值、标准差、最小值等）                            |
| `shape`                | 返回行数和列数（格式：`(行数, 列数)`）                                   |
| `columns`              | 返回所有列名（Index 对象）                                               |
| `index`                | 返回行索引（Index 对象）                                                 |
| `dtypes`               | 返回每列的数据类型（Series 对象）                                        |
| `sort_values(by)`      | 按指定列排序（可指定升序/降序）                                          |
| `sort_index()`          | 按行索引排序                                                            |
| `dropna()`             | 删除含缺失值（NaN）的行或列（可指定参数控制）                             |
| `fillna(value)`        | 用指定值填充缺失值                                                      |
| `isnull()`             | 返回布尔值 DataFrame（标记缺失值位置）                                    |
| `notnull()`            | 返回布尔值 DataFrame（标记非缺失值位置）                                  |
| `loc[]`                | 按[行索引,列名]选择数据（支持切片和布尔索引）                                  |
| `iloc[]`               | 按位置[行，列]选择数据（支持切片，切片不包含结束索引）                                          |
| `at[]`                 | 快速访问单个元素（比 `loc[]` 更高效）                                     |
| `iat[]`                | 快速按位置访问单个元素（比 `iloc[]` 更高效）                              |
| `apply(func)`          | 对行/列应用函数（返回 Series 或 DataFrame）                               |
| `applymap(func)`       | 对每个元素应用函数（仅限 DataFrame）                                      |
| `groupby(by)`          | 按列分组（支持聚合操作，如 `mean()`、`sum()`）                            |
| `pivot_table()`        | 创建透视表（支持多级索引和聚合函数）                                      |
| `merge()`              | 合并 DataFrame（类似 SQL JOIN，支持 `inner`/`outer`/`left`/`right`）       |
| `concat()`             | 按行或列拼接多个 DataFrame（支持 `axis=0` 或 `axis=1`）                   |
| `to_csv()`             | 导出为 CSV 文件（可指定分隔符、编码等）                                   |
| `to_excel()`           | 导出为 Excel 文件（需安装 `openpyxl` 或 `xlsxwriter`）                    |
| `to_json()`            | 导出为 JSON 格式                                                         |
| `to_sql()`             | 导出到 SQL 数据库（需配置数据库连接）                                     |
| `query()`              | 使用字符串表达式查询数据（如 `df.query("age > 30")`）                    |
| `duplicated()`         | 返回布尔 Series（标记重复行）                                             |
| `drop_duplicates()`    | 删除重复行（可保留第一个/最后一个）                                      |
| `set_index()`          | 将某列设置为索引（可多列）                                                |
| `reset_index()`        | 重置索引（生成默认整数索引，原索引变为列）                                |
| `transpose()`          | 转置 DataFrame（行列互换，等价于 `df.T`）                                 |


```python
import pandas as pd

# 创建 DataFrame
data = {
   'Name': ['Alice', 'Bob', 'Charlie', 'David'],
   'Age': [25, 30, 35, 40],
   'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data)

# 查看前两行数据
print(df.head(2))

# 查看 DataFrame 的基本信息
print(df.info())

# 获取描述统计信息
print(df.describe())

# 按年龄排序
df_sorted = df.sort_values(by='Age', ascending=False)
print(df_sorted)

# 选择指定列
print(df[['Name', 'Age']])

# 按索引选择行
print(df.iloc[1:3])  # 选择第二到第三行（按位置）

# 按标签选择行
print(df.loc[1:2])  # 选择第二到第三行（按标签）

# 计算分组统计（按城市分组，计算平均年龄）
print(df.groupby('City')['Age'].mean())

# 处理缺失值（填充缺失值）
df['Age'] = df['Age'].fillna(30)

# 导出为 CSV 文件
# df.to_csv('output.csv', index=False)
```

## 更多

### .loc[]    .iloc[]


```python
## 访问
data = {
   'Name': ['Alice', 'Bob', 'Charlie', 'David'],
   'Age': [25, 30, 35, 40],
   'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data)
# 通过列名访问
print(df['Name'])

# 通过属性访问
print(df.Name) 

# 通过 .loc[] 访问
print(df.loc[:, 'Name'])

# 通过 .iloc[] 访问
print(df.iloc[:, 0]) # 'Name' 是第一列

# 访问单个元素
print(df['Name'][0])  # 'Name' 列的第一个元素

# 通过行标签访问
print(df.loc[0, 'Name'])  # 第一行的 'Name' 列的值
```


```python
## 修改 DataFrame
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data)

# 修改列数据：直接对列进行赋值
df['duration'] = [10, 11, 12]

#添加新列：给新列赋值。
df['NewColumn'] = [100, 200, 300]

#添加新行：使用 loc 或 concat 方法
# 使用 loc 为特定索引添加新行,直接赋值
df.loc[3] = [400,13,150]

# # 使用concat添加新行
new_row = pd.DataFrame([[410, 7,170]], columns=['calories', 'duration','NewColumn']) # 创建一个只包含新行的DataFrame
df = pd.concat([df, new_row], ignore_index=True) # 将新行添加到原始DataFrame

print(df)
```

### .drop()
``df.drop(labels=None, axis=0, index=None, columns=None, inplace=False, errors='raise')``


```python
## 删除 DataFrame 元素
data = {
  "c1": [1, 2, 3],
  "c2": [4, 5, 6]
}
df = pd.DataFrame(data,index=['r1','r2','r3'])

# 删除行：同样使用 drop 方法
df_dropped = df.drop('r1')  # 删除索引为 r1 的行
df_dropped = df.drop('r1', axis=0)  # 等价于 df.drop('r1')    axis=0（默认）
df_dropped = df.drop(index='r1')  
df_dropped = df.drop(['r1','r2'])  # 删除索引为 r1,r2 的行  对象有多个时必须加[]
print(df_dropped)

# 删除列：使用 drop 方法
df_dropped = df.drop('c1',axis=1)
df_dropped = df.drop(columns='c1')  # 更直观的写法
# 删除多个列时同理
print(df_dropped)

# 默认情况下，.drop() 返回新对象，原数据不变。若想直接修改原数据：
df.drop('r1', inplace=True)  # 直接删除原 DataFrame 中的 'row1'
print(df)  # 原数据已改变
```


```python
## DataFrame 的统计分析
df.describe()
#计算统计数据：使用聚合函数如 .sum()、.mean()、.max() 等。
df['Column1'].sum()
df.mean()
```


```python
## DataFrame 的索引操作
# 重置索引：.reset_index()
df_reset = df.reset_index(drop=True)

# 设置索引：.set_index()
df_set = df.set_index('Column1')

# DataFrame 的布尔索引
# 使用布尔表达式：根据条件过滤 DataFrame
df[df['Column1'] > 2]

## DataFrame 的数据类型
# 查看数据类型： dtypes 属性
df.dtypes

# 转换数据类型： astype 方法
df['Column1'] = df['Column1'].astype('float64')
```

### .concat()
沿轴拼接（连接）多个 DataFrame 或 Series  
将多个数据结构按行（垂直）或列（水平）方向合并，类似于 SQL 中的 UNION 或 Excel 中的合并表格  
``pd.concat(objs , axis=0 , join='outer' , ignore_index=False , keys=None , verify_integrity=False )``

- 要拼接的 DataFrame 或 Series 列表 (如 [df1, df2])
- 拼接方向：0/'index'（垂直，默认）或 1/'columns'（水平）
- 合并方式：'outer'（默认，保留所有列）或 'inner'（只保留共有的列）
- 是否忽略原索引，生成新索引（0, 1, 2...）
- 为每个数据源添加多级索引标签（用于区分来源）
- 检查索引是否重复（合并后索引冲突会报错）


```python
## DataFrame 的合并
## 纵向合并
data1 = {
  "c1": [1, 2, 3],
  "c2": [4, 5, 6]
}
data2 = {
  "c1": ['a','b','c'],
  "c2": ['d','d','f']
}
df1 = pd.DataFrame(data1,index=['r1','r2','r3'])
df2 = pd.DataFrame(data2,index=['r1','r2','r3'])

df=pd.concat([df1, df2], ignore_index=True) # 忽略行标签
#   c1 c2
# 0  1  4
# 1  2  5
# 2  3  6
# 3  a  d
# 4  b  d
# 5  c  f
```

### .merge()
``pd.merge(left , right , how='inner', on=None , left_on=None , right_on=None , suffixes=('_x', '_y') , indicator=False)``
- 左侧 DataFrame
- 右侧 DataFrame
- 合并方式：'left', 'right', 'outer', 'inner'（默认）
- 用于合并的列名（双方必须存在）
- 左侧 DataFrame 的列名（用于合并）
- 右侧 DataFrame 的列名（用于合并）
- 重复列名的后缀
- 是否显示合并来源（'left_only', 'right_only', 'both'）


```python
## DataFrame 的合并
# 横向合并
df1 = pd.DataFrame({
    'id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie']
})
 
df2 = pd.DataFrame({
    'id': [1, 2, 4],
    'score': [90, 85, 88]
})

result = pd.merge(df1, df2, on='id', how='inner')
#    id   name  score
# 0   1  Alice     90
# 1   2    Bob     8
```

### .pivot()
``df.pivot(index=None,columns=None,values=None)``
- 用于行索引的列名
- 用于列索引的列名
- 用于填充数据的列名
  
类似于 Excel 中的数据透视表


```python
# DataFrame 的分割
# 长格式转宽格式
data = {
    'Date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02'],
    'Category': ['A', 'B', 'A', 'B'],
    'Value': [10, 20, 30, 40]
}
df = pd.DataFrame(data)

result = df.pivot(index='Date', columns='Category', values='Value')
# Category     A   B
# Date              
# 2023-01-01  10  20
# 2023-01-02  30  40

# 存在重复的 (index, columns) 组合，pivot() 会报错,需用 pivot_table
df_dup = pd.DataFrame({
    'Date': ['2023-01-01', '2023-01-01', '2023-01-01'],
    'Category': ['A', 'A', 'B'],
    'Value': [10, 15, 20]
})
result = df_dup.pivot_table(
    index='Date', 
    columns='Category', 
    values='Value', 
    aggfunc='mean'  # 对重复值取平均
)
print(df_dup)
# Category      A   B
# Date              
# 2023-01-01  12.5  20
```

### .melt()
``df.melt(id_vars=None , value_vars=None , var_name=None , value_name='value' , col_level=None) ``
- 保持不变的列（作为标识符）
- 需要“融化”的列（默认所有非 id_vars 的列）  
- 融化后新列的名称（默认 'variable'）
- 融化后值的列名（默认 'value'）
- 多级索引时的列级别 
   
与 pivot() 的作用相反。melt() 特别适用于将多个列“融合”为键值对（key-value pairs），便于数据分析和可视化  
将多列合并为两列（一列存储原列名，一列存储值）  


```python
# DataFrame 的分割
# 宽格式转长格式
import pandas as pd

data = {
    'Date': ['2023-01-01', '2023-01-02'],
    'A': [10, 30],
    'B': [20, 40]
}
df = pd.DataFrame(data)
#          Date   A   B
# 0  2023-01-01  10  20
# 1  2023-01-02  30  40

melted = df.melt(id_vars='Date', value_vars=['A', 'B'])
print(melted)
#          Date variable  value
# 0  2023-01-01        A     10
# 1  2023-01-02        A     30
# 2  2023-01-01        B     20
# 3  2023-01-02        B     4

```


```python
## 索引和切片
print(df[['Name', 'Age']]) # 提取多列
print(df[1:3]) # 切片行
print(df.loc[:, 'Name'])# 提取单列
print(df.loc[1:2, ['Name', 'Age']]) # 标签索引提取指定行列
print(df.iloc[:, 1:])# 位置索引提取指定列
```

### .replace()
>```python
>df.replace(
>    to_replace='old_value',  # 需要替换的值（支持标量、列表、字典、正则表达式）
>    value='new_value',       # 替换后的新值（可选，若省略则直接返回匹配结果）
>    inplace=False,           # 是否原地修改 DataFrame（默认为 False，返回新对象）
>    limit=None,              # 最大替换次数（默认全部替换）
>    regex=False,             # 是否将 to_replace 视为正则表达式
>    method=None              # 填充方法（如 'pad'、'ffill' 等，用于缺失值填充）
>)


```python
import pandas as pd
df = pd.DataFrame({'A': ['apple', 'orange', 'banana'], 'B': [1, 2, 3]})

df.replace('apple', 'pear')  # 将 'apple' 替换为 'pear'
df.replace(['apple', 'orange'], ['pear', 'grape'])  # 同时替换多个值
df.replace({'A': 'apple', 'B': 1}, {'A': 'pear', 'B': 100})  # 分别替换列 A 和 B 的值
df.replace(r'^[a-z]', 'fruit_', regex=True)  # 在字符串开头添加 'fruit_'
df.replace('apple', 'pear', inplace=True)  # 直接修改原 DataFrame
```

---
# CSV
## pd.read_csv()
``df = pd.read_csv(filepath_or_buffer, sep=',', header=0, names=None, index_col=None, ...)`` 

| 参数 | 说明 | 示例 |
|------|------|------|
| `filepath_or_buffer` | 文件路径、URL 或类文件对象 | `'data.csv'`, `'https://example.com/data.csv'` |
| `sep`  | 分隔符，默认为 `','` | `sep='\t'`（制表符分隔） |
| `header` | 指定表头行（列名），默认为 `0`（第一行） | `header=None`（无表头） |
| `names` | 自定义列名列表 | `names=['col1', 'col2', 'col3']` |
| `index_col` | 将某列设为索引 | `index_col=0`（第一列）或 `index_col='id'` |
| `dtype` | 指定列的数据类型 | `dtype={'列名': str, '数值列': 'int32'}` |
| `usecols` | 选择读取的列 | `usecols=[0, 2]` 或 `usecols=['列A', '列C']` |
| `parse_dates` | 尝试解析日期列 | `parse_dates=['日期列']` |
| `na_values` | 指定缺失值标识符 | `na_values=['NA', 'NULL', 'missing']` |
| `encoding` | 文件编码 | `encoding='utf-8'` 或 `encoding='gbk'` |
| `nrows` | 仅读取前 `n` 行 | `nrows=100` |
| `skiprows` | 跳过指定行 | `skiprows=2`（跳过前两行）或 `skiprows=[0, 2]` |
| `skipfooter` | 跳过文件结尾的指定行数 |  |
| `chunksize` | 分块读取大小（大文件处理） | `chunksize=1000` |

>```python
>
>
># 示例1：基本读取
>df = pd.read_csv('data.csv')
>
># 示例2：自定义分隔符和列名
>df = pd.read_csv('data.tsv', sep='\t', names=['A', 'B', 'C'], header=0)
>
># 示例3：处理无表头文件
>df = pd.read_csv('data.csv', header=None, names=['col1', 'col2', 'col3'])
>
># 示例4：读取特定列并设置索引
>df = pd.read_csv('data.csv', usecols=['id', 'value'], index_col='id')
>
># 示例5：处理日期和缺失值
>df = pd.read_csv('data.csv', parse_dates=['date'], na_values=['NA', 'missing'])
>
># 示例6：从URL读取
>url = 'https://example.com/data.csv'
>df = pd.read_csv(url)
>
># 示例7：大文件分块读取
>for chunk in pd.read_csv('large_file.csv', chunksize=10000):
>    process(chunk)  # 逐块处理
>```

>```python
>#读取数据
>df = pd.read_csv('nba.csv')
>
>print(df.to_string())
>
># to_string() 用于返回 DataFrame 类型的数据，如果不使用该函数，则输出结果为数据的前面 5 行和末尾 5 行，中间部分以 ... 代替。
>```
---

## df.to_csv()
>```python
>DataFrame.to_csv(
>    path_or_buf=None,       
>    sep=',',                
>    na_rep='',              
>    float_format=None,      
>    columns=None,           # 指定保存的列
>    header=True,            # 是否保存列名
>    index=True,             # 是否保存索引
>    index_label=None,       # 索引列的列名
>    encoding=None,          # 文件编码（如 'utf-8'）
>    mode='w',               # 写入模式（'w' 覆盖，'a' 追加）
>    quoting=None,           # 引号控制（如 csv.QUOTE_ALL）
>    escapechar=None,        # 转义字符
>    date_format=None,       # 日期格式（如 '%Y-%m-%d'）
>    decimal='.'             # 小数点符号（如欧洲数据用 ','）
>)
>```
| 参数 | 默认值 | 说明 | 示例 |
|------|--------|------|------|
| `path_or_buf` | `None` | 文件路径或类文件对象（如 `StringIO`） | `'output.csv'` 或 `StringIO()` |
| `sep` | `','` | 字段分隔符 | `sep='\t'`（制表符分隔） |
| `na_rep` | `''` | 缺失值（`NaN`）的替换文本 | `na_rep='NULL'` |
| `float_format` | `None` | 浮点数格式（如 `'%.2f'`） | `float_format='%.3f'`（保留3位小数） |
| `columns` | `None` | 指定要写入的列名列表 | `columns=['col1', 'col3']` |
| `header` | `True` | 是否写入列名（或指定列名） | `header=False`（不写入列名） |
| `index` | `True` | 是否写入行索引 | `index=False`（不写入索引） |
| `index_label` | `None` | 索引列的列名 | `index_label='ID'` |
| `encoding` | `None` | 文件编码（如 `'utf-8'`） | `encoding='utf-8-sig'`（支持中文BOM） |
| `mode` | `'w'` | 写入模式（`'w'` 覆盖，`'a'` 追加） | `mode='a'`（追加写入） |
| `quoting` | `None` | 引号控制（需导入 `csv` 模块） | `quoting=csv.QUOTE_ALL` |
| `escapechar` | `None` | 转义字符 | `escapechar='\\'` |
| `date_format` | `None` | 日期格式（如 `'%Y-%m-%d'`） | `date_format='%Y%m%d'` |
| `decimal` | `'.'` | 小数点符号（如欧洲数据用 `','`） | `decimal=','` |
| `line_terminator` | `\n` | 定义行结束符 |  |
| `quotechar` | `"` | 设置用于引用的字符 |  |
| `doublequote` | `True` | 如果为 True，则在写入时会将包含引号的文本使用双引号括起来 |  |


>```python
>import pandas as pd
>
># 示例1：基本保存
>df.to_csv('output.csv')  # 保存为 CSV 文件（默认含索引和列名）
>
># 示例2：自定义分隔符和缺失值
>df.to_csv('output.tsv', sep='\t', na_rep='NULL')  # 制表符分隔，缺失值用 NULL 表示
>
># 示例3：控制索引和列名
>df.to_csv('output.csv', index=False, header=False)  # 不保存索引和列名
>
># 示例4：选择特定列并命名索引
>df.to_csv('output.csv', columns=['col1', 'col3'], index_label='RowID')  # 仅保存 col1 和 col3，索引列命名为 RowID
>
># 示例5：处理浮点数和日期
>df.to_csv('output.csv', float_format='%.2f', date_format='%Y-%m-%d')  # 浮点数保留2位小数，日期格式化为 YYYY-MM-DD
>
># 示例6：追加模式和大文件分块保存
>with open('large_output.csv', 'w') as f:
>    for chunk in pd.read_csv('large_input.csv', chunksize=10000):
>        processed_chunk = process(chunk)  # 假设的处理函数
>        processed_chunk.to_csv(f, mode='a', header=f.tell() == 0)  # 仅首次写入表头
>
># 示例7：欧洲数据格式（逗号作为小数点）
>df.to_csv('output_europe.csv', sep=';', decimal=',')  # 分号分隔，逗号作为小数点
>```

常见问题
1. **中文乱码**  
   使用 `encoding='utf-8-sig'`（带 BOM 头）或 `encoding='gbk'`。

2. **避免保存索引**  
   设置 `index=False`，否则会多出一列无名称的索引。

3. **科学计数法转普通数字**  
   用 `float_format='%.f'` 或 `float_format='%.2f'` 控制格式。

4. **追加数据时重复表头**  
   在追加模式（`mode='a'`）下，首次写入需 `header=True`，后续设为 `header=False`。
---

# Excel
## `pd.read_excel()`


| 参数 | 默认值 | 说明 | 示例 |
|------|--------|------|------|
| `io` | `None` | Excel 文件路径或类文件对象 | `'data.xlsx'` 或 `BytesIO(excel_bytes)` |
| `sheet_name` | `0` | 指定读取的工作表（名称或索引，`None` 读取所有） | `sheet_name='Sheet1'` 或 `sheet_name=[0,1]` |
| `header` | `0` | 指定列名行索引（`None` 表示无列名） | `header=1`（第二行为列名） |
| `names` | `None` | 自定义列名列表，如果提供，将覆盖文件中的列名 | `names=['col1', 'col2']` |
| `index_col` | `None` | 指定行索引列（单列名、索引或列表） | `index_col='ID'` 或 `index_col=[0,1]` |
| `usecols` | `None` | 选择读取的列（列名、索引或函数） | `usecols=['A', 'C']` 或 `usecols=lambda x: x in ['col1', 'col2']` |
| `dtype` | `None` | 指定列数据类型（字典形式） | `dtype={'col1': str, 'col2': float}` |
| `skiprows` | `None` | 跳过指定行（列表或整数） | `skiprows=[0,2]`（跳过第1、3行） |
| `nrows` | `None` | 仅读取前 N 行 | `nrows=100` |
| `na_values` | `None` | 自定义缺失值标记 | `na_values=['NA', 'NULL']` |
| `parse_dates` | `False` | 尝试解析日期列（列表或字典） | `parse_dates=['date_column']` |
| `thousands` | `None` | 千位分隔符（如 `','`） | `thousands=','` |
| `decimal` | `'.'` | 小数点符号（如欧洲数据用 `','`） | `decimal=','` |
| `engine` | `None` | 指定解析引擎（`'openpyxl'`、`'xlrd'` 等） | `engine='openpyxl'` |


>```python
># 示例
>import pandas as pd
>from io import BytesIO
>
># 示例1：读取单个工作表
>df = pd.read_excel('data.xlsx', sheet_name='Sheet1')
>
># 示例2：读取所有工作表（返回字典）
>all_sheets = pd.read_excel('data.xlsx', sheet_name=None)
>
># 示例3：自定义列名和索引
>df = pd.read_excel('data.xlsx', 
>                  names=['ID', 'Value'], 
>                  index_col='ID',
>                  header=0)
>
># 示例4：选择特定列和跳过行
>df = pd.read_excel('data.xlsx', 
>                  usecols=['A', 'C'], 
>                  skiprows=1,
>                  nrows=1000)
>
># 示例5：处理欧洲格式数据（逗号小数点）
>df = pd.read_excel('data_europe.xlsx', decimal=',')
>
># 示例6：从内存字节流读取
>with open('data.xlsx', 'rb') as f:
>    excel_bytes = f.read()
>df = pd.read_excel(BytesIO(excel_bytes))

## df.to_excel()


| 参数 | 默认值 | 说明 | 示例 |
|------|--------|------|------|
| `excel_writer` | `None` | 文件路径或 `ExcelWriter` 对象 | `'output.xlsx'` 或 `pd.ExcelWriter('output.xlsx')` |
| `sheet_name` | `'Sheet1'` | 指定工作表名称 | `sheet_name='Data'` |
| `na_rep` | `''` | 缺失值（`NaN`）的替换文本 | `na_rep='NULL'` |
| `float_format` | `None` | 浮点数格式（如 `'%.2f'`） | `float_format='%.3f'`（保留3位小数） |
| `columns` | `None` | 指定要写入的列名列表 | `columns=['col1', 'col3']` |
| `header` | `True` | 是否写入列名（或自定义列名） | `header=['ID', 'Value']`（覆盖原列名） |
| `index` | `True` | 是否写入行索引 | `index=False`（不写入索引） |
| `index_label` | `None` | 索引列的列名 | `index_label='RowID'` |
| `startrow` | `0` | 数据写入的起始行索引（从0开始） | `startrow=2`（从第3行开始） |
| `startcol` | `0` | 数据写入的起始列索引（从0开始） | `startcol=1`（从第2列开始） |
| `engine` | `None` | 指定写入引擎（`'openpyxl'`、`'xlsxwriter'` 等） | `engine='xlsxwriter'` |
| `merge_cells` | `True` | 是否合并相同内容的单元格 | `merge_cells=False`（禁用合并） |
| `encoding` | `None` | 文件编码（如 `'utf-8'`） | `encoding='utf-8-sig'`（支持中文BOM） |
| `if_sheet_exists` | `'error'` | 工作表已存在时的处理方式（`'replace'`、`'overlay'`） | `if_sheet_exists='replace'` |


>```python
>import pandas as pd
>
># 示例1：基本保存（默认含索引和列名）
>df.to_excel('output.xlsx')
>
># 示例2：自定义工作表名、不写入索引
>df.to_excel('output.xlsx', sheet_name='Sheet1', index=False)
>
># 示例3：指定列和缺失值替换
>df.to_excel('output.xlsx', 
>           columns=['A', 'B'], 
>           na_rep='NA',
>           sheet_name='Filtered')
>
># 示例4：控制浮点数格式和起始位置
>df.to_excel('output.xlsx', 
>           float_format='%.2f',
>           startrow=1,
>           startcol=1)
>
># 示例5：多工作表写入（需使用 ExcelWriter）
>with pd.ExcelWriter('output_multi.xlsx') as writer:
>    df1.to_excel(writer, sheet_name='Sheet1', index=False)
>    df2.to_excel(writer, sheet_name='Sheet2', index=False)
>
># 示例6：覆盖已存在的工作表
>with pd.ExcelWriter('output.xlsx', mode='a', if_sheet_exists='replace') as writer:
>    df.to_excel(writer, sheet_name='Sheet1')
>
># 示例7：使用 xlsxwriter 引擎添加格式
>with pd.ExcelWriter('output_styled.xlsx', engine='xlsxwriter') as writer:
>    df.to_excel(writer, sheet_name='Data')
>    workbook = writer.book
>    worksheet = writer.sheets['Data']
>    format1 = workbook.add_format({'num_format': '0.00%'})  # 百分比格式
>    worksheet.set_column('B:B', None, format1)  # 应用到B列

## pd.ExcelFile()
|参数|默认值|说明|示例|
|---|---|---|---|
|io|None|Excel 文件路径或类文件对象（如 BytesIO）|'data.xlsx' 或 BytesIO(excel_bytes)|
|engine|None|指定解析引擎（'openpyxl'、'xlrd' 等）|engine='openpyxl'|

>```python
>import pandas as pd
>from io import BytesIO
>
># 示例1：读取Excel文件对象
>with pd.ExcelFile('data.xlsx') as excel:
>    df_sheet1 = pd.read_excel(excel, sheet_name='Sheet1')
>    df_sheet2 = pd.read_excel(excel, sheet_name='Sheet2')
>
># 示例2：从内存字节流读取
>with open('data.xlsx', 'rb') as f:
>    excel_bytes = f.read()
>with pd.ExcelFile(BytesIO(excel_bytes)) as excel:
>    df = pd.read_excel(excel, sheet_name=None)  # 读取所有工作表
>
># 示例3：显式指定引擎
>with pd.ExcelFile('old_data.xls', engine='xlrd') as excel:
>    df = pd.read_excel(excel)
>
># 示例4：获取工作表名称列表
>with pd.ExcelFile('data.xlsx') as excel:
>    print(excel.sheet_names)  # 输出: ['Sheet1', 'Sheet2']
>```

## pd.ExcelWriter()
|参数	|默认值	|说明	|示例|
|---|---|---|---|
|path	|None	|输出文件路径或类文件对象	|'output.xlsx' 或 BytesIO()|
|engine	|None	|指定写入引擎（'openpyxl'、'xlsxwriter' 等）	|engine='xlsxwriter'|
|datetime_format	|None	|日期时间格式（如 'YYYY-MM-DD'）	|datetime_format='YYYY-MM-DD'|
|mode	|'w'	|'w'（覆盖）或 'a'（追加）	|mode='a'（需引擎支持）|
|if_sheet_exists	|'error'	|工作表存在时的处理方式（'replace'、'overlay'）	|if_sheet_exists='replace'|

>```python
>import pandas as pd
>from io import BytesIO
>
># 示例1：基本用法（覆盖模式）
>with pd.ExcelWriter('output.xlsx') as writer:
>    df1.to_excel(writer, sheet_name='Sheet1')
>    df2.to_excel(writer, sheet_name='Sheet2')
>
># 示例2：追加模式（需引擎支持）
>with pd.ExcelWriter('output.xlsx', mode='a', engine='openpyxl') as writer:
>    df_new.to_excel(writer, sheet_name='Sheet3')
>
># 示例3：替换已存在的工作表
>with pd.ExcelWriter('output.xlsx', mode='a', if_sheet_exists='replace') as writer:
>    df_updated.to_excel(writer, sheet_name='Sheet1')
>
># 示例4：使用 xlsxwriter 引擎设置格式
>with pd.ExcelWriter('styled.xlsx', engine='xlsxwriter') as writer:
>    df.to_excel(writer, sheet_name='Data')
>    workbook = writer.book
>    worksheet = writer.sheets['Data']
>    format1 = workbook.add_format({'bold': True, 'bg_color': 'yellow'})
>    worksheet.set_column('A:A', 20, format1)
>
># 示例5：内存中生成Excel文件
>output = BytesIO()
>with pd.ExcelWriter(output) as writer:
>    df.to_excel(writer, sheet_name='Sheet1')
>excel_bytes = output.getvalue()
>```

---
# JSON
## pd.read_json()
>```python
>import pandas as pd
> 
>df = pd.read_json(
>    path_or_buf,
>    orient=None,
>    typ='frame',
>    dtype=True,
>    convert_dates=True,
>    lines=False,
>    encoding=None,
>    **kwargs
>)
>```


| 参数名          |  默认值  | 说明                                                                 |
|-----------------|---------------|----------------------------------------------------------------------|
| **`path_or_buf`** |  必需    | JSON 数据来源（文件路径、URL 或文件对象），也可直接传入 JSON 字符串（Pandas 1.3+） |
| **`orient`**     | `'columns'` | 指定 JSON 结构格式，可选值：<br> - `'columns'`：列名作为键（默认）<br> - `'records'`：每行一个字典的列表<br> - `'index'`：行索引作为外层键<br> - `'split'`：分离索引/列/数据<br> - `'values'`：纯值数组（无行列名） |
| **`typ`**        |  `'frame'` | 返回类型：<br> - `'frame'`：DataFrame（默认）<br> - `'series'`：一维数据时返回 Series |
| **`dtype`**      |  `True`  | 强制指定列数据类型（如 `{'col1': 'int32'}`），`True` 时自动推断。          |
| **`lines`**      |  `False` | 若为 `True`，按行解析 JSON（适用于 JSON Lines 格式，`.jsonl` 文件）。       |
| **`encoding`**   |  `None`  | 文件编码（如 `'utf-8'`、`'gbk'`），处理中文文件时常用。                   |
| **`convert_dates`** | `True`  | 是否尝试将符合日期格式的字符串转换为 `datetime` 类型。                    |
| **`nrows`**      |  `None`  | 仅读取前 `n` 行数据（适用于大文件快速预览）。                              |

## df.to_json()
>```python
>df.to_json(
>    path_or_buf=None,
>    orient=None,
>    indent=None,
>    compression='infer',
>    index=True,
>    default_handler=None,
>    lines=False,
>    **kwargs
>)
>```

|参数名		|默认值	|说明|
|---|---|---|
|path_or_buf|		|None	|文件路径或文件对象。若为 None，返回 JSON 字符串；否则写入文件|
|orient		|'columns'	|指定 JSON 输出格式，可选值：<br> - `'columns'`：列名作为键（默认）<br> - `'records'`：每行一个字典的列表<br> - `'index'`：行索引作为外层键<br> -` 'split'`：分离索引/列/数据<br> - `'values'`：纯值数组（无行列名）<br> - `'table'`：符合 JSON Table Schema 标准|
|indent		|None	|缩进空格数（美化输出）。若为 None，输出紧凑格式|
|index		|True	|是否包含行索引|
|lines		|False	|若为 True，每行输出一个 JSON 对象（需配合 orient='records'）|
|compression		|'infer'	|压缩格式（如 'gzip'、'zip'），仅在写入文件时生效|
|default_handler		|None	|处理无法序列化的对象（如自定义类）的函数|

## orient参数
|参数值|	输出示例|	适用场景|
|---|---|---|
|'columns'	|{"col1": [1, 2], "col2": ["a", "b"]}	|默认，列名作为键|
|'records'	|[{"col1": 1, "col2": "a"}, {...}]	|每行一个字典的列表|
|'index'	|{"idx1": {"col1": 1}, "idx2": {...}}	|行索引作为外层键|
|'split'	|{"index": ["idx1"], "columns": ["col1"], "data": [[1]]}	|显式分离索引/列/数据|
|'values'	|[[1, "a"], [2, "b"]]	|纯值数组（无行列名）|
|'table'	|{"schema": {...}, "data": [...]}	|符合 JSON Table Schema 标准|

JSON 对象与 Python 字典具有相同的格式


```python

# 字典格式的 JSON                                                                                              
s = {
    "col1":{"row1":1,"row2":2,"row3":3},
    "col2":{"row1":"x","row2":"y","row3":"z"}
}

# 读取 JSON 转为 DataFrame                                                                                          
df = pd.DataFrame(s)
print(df)

#       col1 col2
# row1     1    x
# row2     2    y
# row3     3    z
```

## json_normalize()
处理内嵌的 JSON 数据文件
>```json
>{
>    "school_name": "ABC primary school",
>    "class": "Year 1",
>    "students": [
>    {
>        "id": "A001",
>        "name": "Tom",
>        "math": 60,
>        "physics": 66,
>        "chemistry": 61
>    },
>    {
>        "id": "A002",
>        "name": "James",
>        "math": 89,
>        "physics": 76,
>        "chemistry": 51
>    },
>    {
>        "id": "A003",
>        "name": "Jenny",
>        "math": 79,
>        "physics": 90,
>        "chemistry": 78
>    }]
>}
>```

>```python
># 直接处理
>import pandas as pd
>
>df = pd.read_json('nested_list.json')
>
>print(df)
>#           school_name   class                                           students
># 0  ABC primary school  Year 1  {'id': 'A001', 'name': 'Tom', 'math': 60, 'phy...
># 1  ABC primary school  Year 1  {'id': 'A002', 'name': 'James', 'math': 89, 'p...
># 2  ABC primary school  Year 1  {'id': 'A003', 'name': 'Jenny', 'math': 79, 'p...
>
># 使用json_normalize()
>import pandas as pd
>import json
>
># 使用 Python JSON 模块载入数据
>with open('nested_list.json','r') as f:
>    data = json.loads(f.read())
>
># 展平数据
>df_nested_list = pd.json_normalize(data, record_path =['students'])
>print(df_nested_list)
>#      id   name  math  physics  chemistry
># 0  A001    Tom    60       66         61
># 1  A002  James    89       76         51
># 2  A003  Jenny    79       90         78
>```

读取更复杂的 JSON 数据，该数据嵌套了列表和字典
>```json
>{
>    "school_name": "local primary school",
>    "class": "Year 1",
>    "info": {
>      "president": "John Kasich",
>      "address": "ABC road, London, UK",
>      "contacts": {
>        "email": "admin@e.com",
>        "tel": "123456789"
>      }
>    },
>    "students": [
>    {
>        "id": "A001",
>        "name": "Tom",
>        "math": 60,
>        "physics": 66,
>        "chemistry": 61
>    },
>    {
>        "id": "A002",
>        "name": "James",
>        "math": 89,
>        "physics": 76,
>        "chemistry": 51
>    },
>    {
>        "id": "A003",
>        "name": "Jenny",
>        "math": 79,
>        "physics": 90,
>        "chemistry": 78
>    }]
>}
>```
>```python
>import pandas as pd
>import json
>
># 使用 Python JSON 模块载入数据
>with open('nested_mix.json','r') as f:
>    data = json.loads(f.read())
>    
>df = pd.json_normalize(
>    data, 
>    record_path =['students'], 
>    meta=[
>        'class',
>        ['info', 'president'], 
>        ['info', 'contacts', 'tel']
>    ]
>)
>
>print(df)
>#      id   name  math  physics  chemistry   class info.president info.contacts.tel
># 0  A001    Tom    60       66         61  Year 1    John Kasich         123456789
># 1  A002  James    89       76         51  Year 1    John Kasich         123456789
># 2  A003  Jenny    79       90         78  Year 1    John Kasich         123456789
>
>```

>```python
>{
>    "school_name": "local primary school",
>    "class": "Year 1",
>    "students": [
>    {
>        "id": "A001",
>        "name": "Tom",
>        "grade": {
>            "math": 60,
>            "physics": 66,
>            "chemistry": 61
>        }
>  
>    },
>    {
>        "id": "A002",
>        "name": "James",
>        "grade": {
>            "math": 89,
>            "physics": 76,
>            "chemistry": 51
>        }
>        
>    },
>    {
>        "id": "A003",
>        "name": "Jenny",
>        "grade": {
>            "math": 79,
>            "physics": 90,
>            "chemistry": 78
>        }
>    }]
>}
># 使用glom访问其中的math字段
># glom 模块允许我们使用 . 来访问内嵌对象的属性
>import pandas as pd
>from glom import glom
>
>df = pd.read_json('nested_deep.json')
>
>data = df['students'].apply(lambda row: glom(row, 'grade.math'))
>print(data)
># 0    60
># 1    89
># 2    79
># Name: students, dtype: int64
>```

# 数据清洗
1.缺失值处理：识别并填补缺失值，或删除含缺失值的行/列。

2.重复数据处理：检查并删除重复数据，确保每条数据唯一。

3.异常值处理：识别并处理异常值，如极端值、错误值。

4.数据格式转换：转换数据类型或进行单位转换，如日期格式转换。

5.标准化与归一化：对数值型数据进行标准化（如 Z-score）或归一化（如 Min-Max）。

6.类别数据编码：将类别变量转换为数值形式，常见方法包括 One-Hot 编码和标签编码。

7.文本处理：对文本数据进行清洗，如去除停用词、词干化、分词等。

8.数据抽样：从数据集中抽取样本，或通过过采样/欠采样处理类别不平衡。

9.特征工程：创建新特征、删除不相关特征、选择重要特征等。

## 删除空值 .dropna()
``DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)``
  
- axis：默认为 0，表示逢空值剔除整行，如果设置参数 axis＝1 表示逢空值去掉整列
  
- how：默认为 'any' 如果一行（或一列）里任何一个数据有出现 NA 就去掉整行，如果设置 how='all' 一行（或列）都是 NA 才去掉这整行
  
- thresh：设置需要多少非空值的数据才可以保留下来的
  
- subset：设置想要检查的列。如果是多个列，可以使用列名的 list 作为参数  
  
- inplace：如果设置 True，将计算得到的值直接覆盖之前的值并返回 None，修改的是源数  

>```python
># 可以通过 isnull() 判断各个单元格是否为空。
>import pandas as pd
>
>df = pd.read_csv('property-data.csv')
>
>print (df['NUM_BEDROOMS']) # 打印NUM_BEDROOMS列
>print (df['NUM_BEDROOMS'].isnull())
>
># Pandas 把 n/a 和 NA 当作空数据，na 不是空数据，不符合我们要求，我们可以指定空数据类型
>missing_values = ["n/a", "na", "--"] #指定空数据
>df = pd.read_csv('property-data.csv', na_values = missing_values)
>
>print (df['NUM_BEDROOMS'])
>print (df['NUM_BEDROOMS'].isnull())
>
># 删除空数据行
>new_df = df.dropna()
>
>print(new_df.to_string())
># 注意：默认情况下，dropna() 方法返回一个新的 DataFrame，不会修改源数据
># 如果你要修改源数据 DataFrame, 可以使用 inplace = True 参数
>
>df.dropna(subset=['ST_NUM'], inplace = True) # 检查ST_NUM列的空值
>
>```

## 填充空值 .fillna()
>```python
>df.fillna(
>    value=None,           # 用于填充缺失值的标量、字典或 DataFrame
>    method=None,          # 填充方法：'ffill'（前向填充）或 'bfill'（后向填充）
>    axis=None,            # 按列 或 行填充：0/'index'（默认）或 1/'columns'
>    inplace=False,        # 是否原地修改 DataFrame
>    limit=None,           # 最大连续填充次数
>    downcast=None         # 向下转换填充后的数据类型（如 'int64' → 'int32'）
>)
># 'ffill'：用前一个有效值填充
># 'bfill'：用后一个有效值填充
>
># 示例
>df.fillna(0)  # 所有缺失值填充为 0
>df['A'].fillna(1, inplace = True)# 将A列的空值替换为1
>df.fillna({'A': 100, 'B': 'unknown'})  # 列 A 填充 100，列 B 填充 'unknown'
>
>import numpy as np
>df = pd.DataFrame([[np.nan, 1], [2, np.nan]])
>df.fillna(method='ffill', axis=1)  # 用左侧有效值填充右侧缺失值
>#      0    1
># 0  NaN  1.0
># 1  2.0  2.0
>```
替换空单元格的常用方法是计算列的均值mean()、中位数值median()或众数mode()。  
>```python
>import pandas as pd
>df = pd.read_csv('property-data.csv')
>x = df["ST_NUM"].mean()
>
>df["ST_NUM"].fillna(x, inplace = True)
>
>print(df.to_string())
>
># 结合 groupby 分组填充
>df['A'] = df.groupby('group_col')['A'].transform(lambda x: x.fillna(x.mean())) #对列 'A' 的缺失值，按 'group_col' 分组后，用当前组内的均值填充
>
># 时间序列填充
>df.resample('D').ffill()  # 按天重采样并前向填充
>```


```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'group_col': ['A', 'A', 'B', 'B', 'B'],
    'A': [1, np.nan, 3, np.nan, 5]
})

# 按组填充均值
df['A'] = df.groupby('group_col')['A'].transform(lambda x: x.fillna(x.mean()))
# df.groupby('group_col')['A']：按 'group_col' 分组，并选中列 'A'。
# .transform(...)：对每个分组应用函数，并返回与原 DataFrame 相同形状的结果。
# lambda x: x.fillna(x.mean())：
# 对每个分组的数据 x，计算其均值x.mean()，然后用 fillna() 填充组内缺失值
print(df)
#   group_col    A
# 0         A  1.0   组 A 的均值是 1 / 1 → 1（实际计算会忽略 NaN）
# 1         A  1.0
# 2         B  3.0
# 3         B  4.0   组 B 均值是 (3+5)/2=4.0
# 4         B  5.0
```

## 清洗格式错误数据


```python
import pandas as pd

# 第三个日期格式错误
data = {
  "Date": ['2020/12/01', '2020/12/02' , '20201226'],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
# 通过包含空单元格的行，或者将列中的所有单元格转换为相同格式的数据
df['Date'] = pd.to_datetime(df['Date'], format='mixed')

print(df.to_string())
```

## 清洗错误数据


```python
import pandas as pd

person = {
  "name": ['Google', 'Runoob' , 'Taobao'],
  "age": [50, 40, 12345]    # 12345 年龄数据是错误的
}

df = pd.DataFrame(person)

df.loc[2, 'age'] = 30 # 将第3行，age列的数据修改为30
# 或者将 age 大于 120 的设置为 120
for x in df.index:
  if df.loc[x, "age"] > 120:
    df.loc[x, "age"] = 120
# 或者删除这一行
for x in df.index:
  if df.loc[x, "age"] > 120:
    df.drop(x, inplace = True)

print(df.to_string())
```

## 清洗重复数据 duplicated()  drop_duplicates()
  
如果我们要清洗重复数据，可以使用**duplicated()** 和 **drop_duplicates()** 方法  
如果对应的数据是重复的，duplicated() 会返回 True，否则返回 False  
删除重复数据，可以直接使用drop_duplicates() 方法  


```python
import pandas as pd

person = {
  "name": ['Google', 'Runoob', 'Runoob', 'Taobao'],
  "age": [50, 40, 40, 23]  
}
df = pd.DataFrame(person)
print(df.duplicated())

df.drop_duplicates(inplace = True)
print(df)
```

## 独热编码 .get_dummies()
将分类变量转换为虚拟/指示变量的函数，常用于机器学习中的特征工程，如独热编码
>```python
>pandas.get_dummies(
>    data,                # 输入数据（DataFrame、Series或数组）
>    prefix=None,         # 列名前缀
>    prefix_sep='_',      # 前缀与原始列名的分隔符
>    dummy_na=False,      # 是否为NaN值生成虚拟列
>    columns=None,        # 指定要编码的列（默认自动选择）
>    drop_first=False,    # 是否删除第一列以避免多重共线性
>    dtype=None,          # 输出数据类型（默认np.uint8）
>    sparse=False,        # 是否返回稀疏矩阵
>    drop_columns=None    # 要删除的列
>)


```python
data = {'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}

df = pd.DataFrame(data)

# 对 "City" 列进行 One-Hot 编码
df_encoded = pd.get_dummies(df, columns=['City'])

#         City_Chicago  City_Houston  City_Los Angeles  City_New York
# 0             0             0                 0              1
# 1             0             0                 1              0
# 2             1             0                 0              0
# 3             0             1                 0              0
```

## 标准化


```python
from sklearn.preprocessing import StandardScaler
import pandas as pd
# Z-score 标准化，将数据转换为均值为 0、标准差为 1 的分布
data = {'Age': [25, 30, 35, 40, 45],
        'Salary': [50000, 60000, 70000, 80000, 90000]}

df = pd.DataFrame(data)

# 标准化数据
scaler = StandardScaler() # 初始化标准化器
df_scaled = scaler.fit_transform(df) # fit(): 计算每列的均值和标准差 transform(): 对每个值应用标准化公式

print(df_scaled) # 输入可以是 DataFrame 或 NumPy 数组，但输出始终是 NumPy 数组
```

## 更多
| **操作**               | **方法/步骤**                     | **说明**                                                                 | **常用函数/方法**                                                                 |
|------------------------|-----------------------------------|--------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| **缺失值处理**         | 填充缺失值                        | 使用指定值（均值、中位数等）填充缺失值                                    | `df.fillna(value)`                                                              |
|                        | 删除缺失值                        | 删除包含缺失值的行或列                                                   | `df.dropna()`                                                                   |
| **重复数据处理**       | 删除重复数据                      | 删除 DataFrame 中的重复行                                                 | `df.drop_duplicates()`                                                           |
| **异常值处理**         | 异常值检测（统计方法）            | 通过 Z-score 或 IQR 方法识别异常值                                       | 自定义函数（如 `scipy.stats.zscore` 或 IQR 计算）                                 |
|                        | 替换异常值                        | 用均值/中位数替换异常值                                                  | 自定义函数（如 `df[df > threshold] = median`）                                   |
| **数据格式转换**       | 转换数据类型                      | 将数据类型转换（如字符串→数值）                                          | `df.astype()`                                                                    |
|                        | 日期时间格式转换                  | 转换字符串/数字为日期时间类型                                            | `pd.to_datetime()`                                                              |
| **标准化与归一化**     | 标准化                            | 数据转换为均值为0、标准差为1的分布                                        | `sklearn.preprocessing.StandardScaler()`                                         |
|                        | 归一化                            | 数据缩放到指定范围（如 [0, 1]）                                         | `sklearn.preprocessing.MinMaxScaler()`                                           |
| **类别数据编码**       | 标签编码                          | 将类别变量转换为整数形式                                                 | `sklearn.preprocessing.LabelEncoder()`                                           |
|                        | 独热编码（One-Hot Encoding）      | 将每个类别转换为二进制特征                                               | `pd.get_dummies()`                                                              |
| **文本数据处理**       | 去除停用词                        | 移除无关紧要的词（如 "the", "is"）                                       | 自定义函数（基于 `nltk` 或 `spaCy`）                                            |
|                        | 词干化与词形还原                  | 提取词干或恢复单词基本形式                                               | `nltk.stem.PorterStemmer()`                                                     |
|                        | 分词                              | 将文本分割为单词或子词                                                   | `nltk.word_tokenize()`                                                          |
| **数据抽样**           | 随机抽样                          | 从数据中随机抽取样本                                                     | `df.sample(frac=0.1)`                                                           |
|                        | 上采样与下采样                    | 通过过采样（复制少数类）或欠采样（减少多数类）平衡类别分布               | `imblearn.over_sampling.SMOTE()`<br>`imblearn.under_sampling.RandomUnderSampler()` |
| **特征工程**           | 特征选择                          | 选择对目标变量有影响的特征                                               | `sklearn.feature_selection.SelectKBest()`                                        |
|                        | 特征提取                          | 从原始数据创建新特征（如多项式特征）                                     | `sklearn.preprocessing.PolynomialFeatures()`                                     |
|                        | 特征缩放                          | 对数值特征缩放至相同量级                                                 | `MinMaxScaler()`、`StandardScaler()`                                              |
|                        | 类别特征映射                      | 将类别变量映射为数字编码                                                 | 自定义映射函数（如 `df['col'].map({'A':1, 'B':2})`）                             |
| **数据合并与连接**     | 合并数据                          | 按列合并多个 DataFrame（支持内/外/左/右连接）                            | `pd.merge(df1, df2, on='key', how='inner')`                                      |
|                        | 连接数据                          | 按行或列拼接多个 DataFrame                                               | `pd.concat([df1, df2], axis=0)`                                                 |
| **数据重塑**           | 数据透视表                        | 按维度分组并计算聚合结果                                                 | `pd.pivot_table(df, values='col', index='group', aggfunc='mean')`                |
|                        | 数据变形                          | 长格式↔宽格式转换                                                        | `df.melt()`、`df.pivot()`                                                        |
| **字符串处理**         | 字符串操作                        | 去除空格、转换大小写等                                                   | `str.replace()`、`str.upper()`                                                  |
| **分组计算**           | 分组聚合                          | 按特征分组后计算统计量（如均值、求和）                                   | `df.groupby('col').agg({'target': 'mean'})`                                      |
| **缺失值预测填充**     | 模型预测填充                      | 用回归模型预测缺失值并填充                                               | `sklearn.linear_model.LinearRegression()`                                        |
| **时间序列处理**       | 时间序列缺失值填充                | 用前向/后向填充等方法处理时间序列缺失值                                  | `df.fillna(method='ffill')`                                                     |
|                        | 滚动窗口计算                      | 用滑动窗口计算统计量（如滚动均值）                                       | `df.rolling(window=5).mean()`                                                    |
| **数据转换与映射**     | 数据替换                          | 将数据中的某些值替换为其他值                                             | `df.replace({'old': 'new'})`                                                     |

---

# 小结
## 读取数据
pd.read_csv(filename)	 
pd.read_excel(filename)	  
pd.read_sql(query, connection_object)	  
pd.read_json(json_string)	  
pd.read_html(url)	  
## 查看数据
df.head(n)	  
df.tail(n)	  
df.info()	  
df.describe()	  
df.shape  
## 数据清洗
df.dropna()	  
df.fillna(value)	  
df.replace(old_value, new_value)	  
df.duplicated()	  
df.drop_duplicates()   
## 数据选择与切片
df[column_name]	  
df.loc[row_index, column_name]	  
df.iloc[row_index, column_index]	  
df.filter()	  
df.sample(n)   

>```python
>df.filter(
>    items=None,       # 选择列名列表（如 ['col1', 'col2']）
>    like=None,        # 模糊匹配列名（如包含 "temp" 的列）
>    regex=None,       # 正则表达式匹配列名（如 '^A' 开头的列）
>    axis=0            # 0/'index'（筛选行），1/'columns'（筛选列）
>)
>``` 
>多用于名称匹配（列名/索引名），支持模糊匹配和正则表达式
>```python
>df.sample(
>    n=None,          # 要抽取的样本数量（与 frac 二选一）
>    frac=None,       # 要抽取的样本比例（0.0~1.0，与 n 二选一）
>    replace=False,   # 是否允许重复抽样（默认 False）
>    weights=None,    # 指定抽样权重（列名或数组）
>    random_state=None, # 随机种子（确保结果可复现）
>    axis=None,       # 抽样方向（0/'index' 抽行，1/'columns' 抽列）
>    ignore_index=False # 是否重置索引（默认 False）
>)
>```
用于随机抽取数据



```python
import pandas as pd

df = pd.DataFrame({
    'temperature': [20, 25, 30],
    'humidity': [30, 40, 50],
    'wind_speed': [5, 10, 15]
})

# 选择列名包含 'temp' 或 'humidity' 的列
filtered_df = df.filter(items=['temperature', 'humidity'])

# 选择列名包含 'temp' 的列（模糊匹配，类似 SQL 的 LIKE ）
filtered_df = df.filter(like='temp')

# 选择列名以 'h' 或 'w' 开头的列
filtered_df = df.filter(regex='^[hw]')

# 选择所有列，除了 'humidity'
cols_to_keep = [col for col in df.columns if col != 'humidity']
df.filter(items=cols_to_keep)
```


```python
import pandas as pd

df = pd.DataFrame({'A': range(1, 11), 'B': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']})

# 随机抽取 3 行
sampled_rows = df.sample(n=3)

# 随机抽取 1 列
sampled_cols = df.sample(n=1, axis=1)

# 抽取 30% 的行
sampled_frac = df.sample(frac=0.3)

# 有放回地抽取 5 行（可能重复）
sampled_with_replacement = df.sample(n=5, replace=True)

# 假设列 'A' 的值越大，被抽中的概率越高
weights = df['A'] / df['A'].sum()  # 归一化权重
weighted_sample = df.sample(n=3, weights=weights)

# 确保每次运行结果相同
fixed_sample = df.sample(n=3, random_state=42)
print(fixed_sample)

# 抽样后重新生成连续索引
reset_index_sample = df.sample(n=3, ignore_index=True)

```

## 数据排序
df.sort_values()  
df.sort_index()	  

>```python
>df.sort_values(
>    by,                 # 排序依据的列名（字符串或列表）
>    axis=0,             # 排序方向：0/'index'（默认，按行排序），1/'columns'（按列排序）
>    ascending=True,     # 升序（True）或降序（False），可传列表控制多列
>    inplace=False,      # 是否原地修改（不返回新对象）
>    kind='quicksort',   # 排序算法：'quicksort', 'mergesort', 'heapsort', 'stable'
>    na_position='last', # 缺失值位置：'last'（默认）或 'first'
>    ignore_index=False  # 是否重置索引（Pandas 1.0+）
>)
>
>df.sort_index(
>    axis=0,               # 排序方向：0/'index'（默认，按行索引排序），1/'columns'（按列名排序）
>    level=None,           # 多级索引时指定排序的层级（整数或名称）
>    ascending=True,       # 升序（True）或降序（False）
>    kind='quicksort',     # 排序算法：'quicksort', 'mergesort', 'heapsort', 'stable'
>    na_position='last',   # 缺失值位置：'last'（默认）或 'first'
>    sort_remaining=True,  # 多级索引时是否对未指定的层级排序
>    ignore_index=False,   # 是否重置索引（Pandas 1.0+）
>    key=None              # 对索引应用自定义函数后再排序（Pandas 1.1+）
>)
>```


```python
import pandas as pd

df = pd.DataFrame({
    'A': [3, 1, 2],
    'B': ['x', 'y', 'z'],
    'C': [0.5, 1.2, None]
})

# 按列 'A' 升序排序
sorted_df = df.sort_values(by='A')

# 先按列 'A' 升序，再按列 'C' 降序
sorted_df = df.sort_values(by=['A', 'C'], ascending=[True, False])

# 将缺失值（NaN）放在开头
sorted_df = df.sort_values(by='C', na_position='first')

# 排序后生成新索引
sorted_df = df.sort_values(by='A', ignore_index=True)

# 按第 0 列（列 'A'）排序
sorted_df = df.sort_values(by=df.columns[0], ascending=False)

# 直接修改原 DataFrame
df.sort_values(by='A', inplace=True)  

```


```python
import pandas as pd

df = pd.DataFrame(
    {'A': [3, 1, 2], 'B': ['x', 'y', 'z']},
    index=[2, 0, 1]  # 故意打乱索引顺序
)

# 按行索引升序排序
sorted_df = df.sort_index()

# 按列索引降序排序
sorted_df_desc = df.sort_index(axis=1,ascending=False)

# 多级索引
arrays = [
    ['a', 'a', 'b', 'b'],
    [2, 1, 2, 1]
]
multi_index = pd.MultiIndex.from_arrays(arrays, names=('letter', 'number'))
df_multi = pd.DataFrame({'data': [10, 20, 30, 40]}, index=multi_index)
# 按多级索引的第一级（'letter'）升序，第二级（'number'）降序
sorted_multi = df_multi.sort_index(level=['letter', 'number'], ascending=[True, False])

# 按行索引的字符串长度排序（假设索引是字符串）
df_str_index = pd.DataFrame({'A': [1, 2, 3]}, index=['aa', 'b', 'ccc'])
sorted_by_len = df_str_index.sort_index(key=lambda x: x.str.len())

```

## 数据分组和聚合
df.groupby(column_name)	  
df.agg(function_name)	  
df.pivot_table(values, index, columns, aggfunc)  

>```python
>df.groupby(
>    by=None,          # 分组依据（列名、函数、字典、Series等）
>    axis=0,           # 分组方向：0/'index'（默认，按行分组）
>    level=None,       # 多级索引时指定分组层级
>    as_index=True,    # 分组键是否作为结果索引（默认True）
>    sort=True,        # 是否对分组键排序（默认True）
>    group_keys=True,  # 是否在结果中保留分组键（默认True）
>    observed=False,   # 是否仅显示分类变量的观测值（默认False）
>    dropna=True       # 是否丢弃包含NA的分组（默认True）
>)
>```
groupby() 通常与聚合方法（如 sum(), mean(), count() 等）或 agg() 结合使用  
agg() 可以接受以下类型的参数
>```python
>df.agg('sum')  # 求和
>df.agg('mean') # 均值
>df.agg('max')  # 最大值
>df.agg(['sum', 'mean', 'std'])  #列表（多个聚合函数）
>df.agg({'A': 'sum', 'B': 'mean'})  #字典（不同列不同聚合）
>df.agg(lambda x: x.max() - x.min())  # 自定义函数如 lambda
>df.agg(np.median)  # NumPy 函数
>```
  
>```python
>df.pivot_table(
>    values=None,       # 要聚合的数值列
>    index=None,        # 行分组键
>    columns=None,      # 列分组键
>    aggfunc='mean',    # 聚合函数（默认求均值）
>    fill_value=None,   # 替换缺失值的填充值
>    margins=False,     # 是否显示总计（All）
>    dropna=True,       # 是否删除全为 NaN 的列
>    margins_name='All' # 总计行的名称
>)
>```



```python
import pandas as pd

df = pd.DataFrame({
    'Category': ['A', 'B', 'A', 'B', 'A'],
    'Values': [10, 20, 30, 40, 50]
})

# 按 'Category' 列分组并计算每组的均值
grouped = df.groupby('Category').mean()
#           Values
# Category        
# A           30.0  (10 + 30 + 50) / 3
# B           30.0  (20 + 40) / 2

# 按组计算多个统计量
df.groupby('Category').agg(['mean', 'std', 'count'])

# 使用 lambda 或自定义函数
df.groupby('Category').agg(lambda x: x.max() - x.min())



df = pd.DataFrame({
    'Category': ['A', 'B', 'A', 'B', 'A'],
    'Subcat': ['X', 'X', 'Y', 'Y', 'X'],
    'Values': [10, 20, 30, 40, 50]
})

# 按 'Category' 和 'Subcat' 多列分组
grouped = df.groupby(['Category', 'Subcat']).sum()
#                  Values
# Category Subcat        
# A        X           60
#          Y           30
# B        X           20
#          Y           40

# 按组求和
df.groupby('Category')['Values'].sum()
# Category
# A    90
# B    60
# Name: Values, dtype: int64
```


```python
df = pd.DataFrame({
    'Category': ['A', 'B', 'A', 'B', 'A'],
    'Subcat': ['X', 'X', 'Y', 'Y', 'X'],
    'Values': [10, 20, 30, 40, 50]
})

# 对不同列应用不同的聚合函数
df.groupby('Category').agg({
    'Values': ['sum', 'mean'],  # 对 Values 列求和和均值
    'Subcat': 'count'           # 对 Subcat 列计数
})


# 遍历分组
for name, group in df.groupby('Category'):
    print(f"Group: {name}")
    print(group)

# 筛选出组内均值大于 30 的分组
filtered = df.groupby('Category').filter(lambda x: x['Values'].mean() > 30)

# 对每个分组进行标准化（不改变原数据形状）
df['Normalized'] = df.groupby('Category')['Values'].transform(lambda x: (x - x.mean()) / x.std())

# 按字符串长度分组
df.groupby(df['Category'].str.len()).sum()

# 对多级索引的某一层级分组
df_multi = df.set_index(['Category', 'Subcat'])
df_multi.groupby(level=0).sum()  # 按第一级索引分组

# 默认会丢弃 NA 分组，可通过 dropna=False 保留
df = pd.DataFrame({'Category': ['A', None, 'A'], 'Values': [1, 2, 3]})
df.groupby('Category', dropna=False).sum()
```


```python
import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [10, 20, 30, 40],
    'C': ['x', 'y', 'z', 'w']  # 字符串列
})

# 对所有数值列求和
print(df.agg('sum'))
# A      10
# B     100
# C    xyzw    字符串列默认拼接
# dtype: object

result = df.agg({
    'A': 'sum',    # 对 A 列求和
    'B': 'mean',   # 对 B 列求均值
    'C': 'count'   # 对 C 列计数（非空值数量）
})

# agg() 最常用于 groupby() 后，对每个分组进行聚合
df = pd.DataFrame({
    'Category': ['A', 'B', 'A', 'B', 'A'],
    'Values': [10, 20, 30, 40, 50],
    'Subcat': ['X', 'X', 'Y', 'Y', 'X']
})

# 按 Category 分组，对不同列应用不同聚合
result = df.groupby('Category').agg({
    'Values': ['sum', 'mean', lambda x: x.max() - x.min()],  # 求和、均值、极差
    'Subcat': 'count'  # 统计每个分组的 Subcat 数量
})

```


```python
import pandas as pd
data = {
    'Date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02', '2023-01-03'],
    'Region': ['East', 'West', 'East', 'West', 'East'],
    'Product': ['A', 'B', 'A', 'B', 'A'],
    'Sales': [100, 150, 200, 50, 300],
    'Profit': [20, 30, 40, 10, 50]
}
df = pd.DataFrame(data)

# 基本透视表
pivot1 = df.pivot_table(values='Sales', index='Region', aggfunc='mean')
#         Sales
# Region       
# East    200.0
# West    100.0

pivot2 = df.pivot_table(values='Sales', index=['Region', 'Date'], aggfunc='sum') # Region 和 Date 分组，计算 Sales 的总和

pivot3 = df.pivot_table(values='Sales', index='Region', columns='Product', aggfunc='sum', fill_value=0) # 按 Region 分行，Product 分列，计算 Sales 的总和
# Product    A    B
# Region           
# East     600    0
# West       0  200

pivot4 = df.pivot_table(values=['Sales', 'Profit'], index='Region', aggfunc={'Sales': 'sum', 'Profit': 'mean'}) #同时计算 Sales 的总和和 Profit 的均值
#            Profit  Sales
# Region                  
# East    36.666667    600
# West    20.000000    200

pivot5 = df.pivot_table(values='Sales', index='Region', columns='Product', aggfunc='sum', margins=True, margins_name='Total') #显示总计

pivot6 = df.pivot_table(values='Sales', index='Region', aggfunc=['sum', 'mean', 'count']) # 对同一列应用多个聚合函数

```

## 数据合并
pd.concat([df1, df2])    
pd.merge(df1, df2, on=column_name)     
## 数据选择和过滤
df.loc[]	  
df.iloc[]	  
df[df['column_name'] > value]	  
df.query('column_name > value')  
``df.query(expr, inplace=False, **kwargs)``
类似于 SQL 中的 WHERE 子句  
注意：字符串表达式需用引号包裹，字符串操作需指定 engine='python'  
  
query() 优势：  
代码更简洁（尤其适合复杂条件）  
对大型数据框可能更快（底层优化）  
布尔索引优势：
支持更复杂的逻辑（如嵌套函数调用）  
无需字符串表达式，适合动态条件  
## 数据统计和描述
df.describe()	  
df.mean()	  
df.median()	   
df.mode()	  
df.count()  


```python
import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': ['x', 'y', 'z', 'x'],
    'C': [10, 20, 30, 40]
})

# 查询 A 列大于 2 的行
result = df.query("A > 2")
# 查询 A > 1 且 C < 40 的行
result = df.query("(A > 1) & (C < 40)")
# 查询 B 列包含 'x' 的行
result = df.query("B.str.contains('x')", engine='python') # 使用 str 前缀调用字符串方法（如 str.contains）
# 用 @ 符号引用外部变量
threshold = 30
result = df.query("C > @threshold")
# 查询 A 列值在 [1, 3] 中的行
result = df.query("A in [1, 3]")
# 调用 NumPy 函数
import numpy as np
mean_C = np.mean(df['C'])
result = df.query("C > @mean_C")
# 多级索引查询
df_multi = pd.DataFrame(
    [[1, 'x', 10], [2, 'y', 20], [3, 'z', 30]],
    columns=['A', 'B', 'C']
).set_index(['A', 'B'])
result = df_multi.query("A == 2")


# 列名含空格或特殊字符
# 用反引号 ` 包裹列名：
df = pd.DataFrame({'Sales 2023': [100, 200, 300], 'Region': ['East', 'West', 'North']})
result = df.query("`Sales 2023` > 150")

```

# 相关性分析
- 皮尔逊相关系数：衡量变量之间的线性关系，适用于数值型变量
- 斯皮尔曼等级相关系数：衡量变量之间的单调关系，适用于数值型和顺序型变量
- 肯德尔秩相关系数：衡量变量之间的秩次关系，适用于小样本数据
- 相关性矩阵：用来查看各个变量之间的相关性
- 热图：一种有效的可视化方式，可以帮助我们直观地查看变量之间的相关性

## df.corr()
``df.corr(method='pearson', min_periods=1)``
- method (可选): 字符串类型，用于指定计算相关系数的方法。默认是 'pearson'，还可以选择 'kendall'或 'spearman'
- min_periods (可选): 表示计算相关系数时所需的最小观测值数量。默认值是 1，即只要有至少一个非空值，就会进行计算  
如果指定了 min_periods，并且在某些列中的非空值数量小于该值，则相应列的相关系数将被设为 NaN  
  
df.corr() 方法返回一个相关系数矩阵，矩阵的行和列对应数据框的列名，矩阵的元素是对应列之间的相关系数。

常见的相关性系数包括 Pearson 相关系数和 Spearman 秩相关系数：


```python
import pandas as pd
data = {
    'Height': [150, 160, 170, 180, 190],
    'Weight': [45, 55, 65, 75, 85],
    'Age': [20, 25, 30, 35, 40]
}
df = pd.DataFrame(data)

# 计算皮尔逊相关系数,衡量两个变量之间的线性关系强度和方向
correlation = df.corr(method='pearson')
print(correlation)
# 斯皮尔曼相关系数用于衡量两个变量的单调关系（无论是线性还是非线性），它是基于变量的排名计算的
correlation=df.corr(method='spearman')
print(correlation)
# 肯德尔秩相关系数也用于衡量变量之间的单调关系，它是通过计算两个变量排名之间的一致性来得出的。
# 肯德尔相关系数的计算较为复杂，适用于较小的数据集
correlation=df.corr(method='kendall')
```

## 热力图
为了更直观地呈现相关性矩阵，可以使用热图（Heatmap）来可视化各个变量之间的相关性  
使用 seaborn 库绘制相关性热图是一个常见的做法  


```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 示例数据
data = {
    'Height': [150, 160, 170, 180, 190],
    'Weight': [45, 55, 65, 75, 85],
    'Age': [20, 25, 30, 35, 40]
}
df = pd.DataFrame(data)
# 绘制相关性热图
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f', vmin=-1, vmax=1)
# annot=True 表示在热图上显示数值，cmap='coolwarm' 设置颜色范围，vmin=-1, vmax=1 限制颜色范围为 -1 到 1
plt.title('Correlation Heatmap')
plt.show()
```

# 数据排序与聚和
见‘补充函数，数据排序’  
``sort_values(by, ascending)``  
``sort_index(axis)``  

见‘补充函数，数据分钟与聚合’  
``groupby(by)``	   
``agg()``  
agg([func1, func2])多个聚合函数  
	  
``apply(lambda x: x.sort_values(...))``   
df.groupby('column').apply(lambda x: x.sort_values(...))      
  
``df.pivot_table(values, index, columns, aggfunc)``  
|特性	|.pivot()	|.pivot_table()|
|---|---|---|
|功能	|单纯重塑数据（无聚合）	|可聚合数据（支持分组统计）|
|重复索引处理	|报错（要求 index + columns 唯一组合）	|自动聚合重复项（默认用 mean）|
|聚合函数	|不支持	|支持（通过 aggfunc 参数指定）|
|填充缺失值	|不支持	|支持（通过 fill_value 填充）|
|多级索引	|不支持	|支持（可处理多级分组）|


```python
import pandas as pd


data = {'Department': ['HR', 'Finance', 'HR', 'IT', 'IT'],
        'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Salary': [50000, 60000, 55000, 70000, 75000]}
df = pd.DataFrame(data)

# 使用 pivot_table 计算每个部门的薪资平均值
pivot_table = df.pivot_table(values='Salary', index='Department', aggfunc='mean')
print(pivot_table)
```

# 数据可视化
Pandas 提供了与 Matplotlib 和 Seaborn 等可视化库的集成，使得数据的可视化变得简单而高效  
   
在 Pandas 中，数据可视化功能主要通过 DataFrame.plot() 和 Series.plot() 方法实现，这些方法实际上是对 Matplotlib 库的封装，简化了图表的绘制过程  

## plot
|参数 |说明|
|---|---|
|x / y	|指定列名（用于散点图等）|
|title	||
|figsize|	|
|grid	|显示网格（True/False）|
|legend	|显示图例（默认 True）|
|color	|指定颜色（如 'red' 或 ['#FF0000', '#00FF00']）|
|style	|线型样式（如 '--' 虚线）|
|alpha	|透明度（0~1）|
|rot	|旋转x轴标签角度（如 45）|  
|xlabel||
  

|kind参数|说明|
|---|---|
|'line'                    |默认|
|'bar'                      |柱状图|
|'hist'                     |直方图|
|'box'                      |箱线图|
|'scatter', x='A', y='B'    |散点图（需指定x、y）|
|'pie', y='A'               |饼图（需指定y列）|
|'barh'|水平柱状图|
| 'kde'|密度图|
|'area'|面积图 |
|'hexbin'|六边形箱线图|


```python
import pandas as pd
import matplotlib.pyplot as plt

# 示例数据
data = {'Year': [2015, 2016, 2017, 2018, 2019, 2020],
        'Sales': [100, 150, 200, 250, 300, 350]}
df = pd.DataFrame(data)

# 绘制折线图
df.plot(kind='line', x='Year', y='Sales', title='Sales Over Years', xlabel='Year', ylabel='Sales', figsize=(10, 6))
plt.show()
```


```python
# 示例数据
data = {'Scores': [55, 70, 85, 90, 60, 75, 80, 95, 100, 65]}
df = pd.DataFrame(data)

# 绘制箱线图
df.plot(kind='box', title='Scores Boxplot', ylabel='Scores', figsize=(8, 5))
plt.show()
```

## seaborn


```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data)

# 绘制热力图
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()
```


```python
# 数据集中所有数值特征之间的散点图矩阵:

data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data)

sns.pairplot(df)
plt.show()
```

## matplotlib

# 高级功能
## 数据合并与连接
``merge() — 数据库风格的连接``  
允许根据某些列对两个 DataFrame 进行合并，类似 SQL 中的 JOIN 操作。支持内连接、外连接、左连接和右连接  
  
``concat() — 沿轴连接``   
将多个 DataFrame 沿指定轴（行或列）进行连接，常用于行合并（垂直连接）或列合并（水平连接）  
  
``join() — 基于索引连接``  
是 Pandas 中的简化连接操作，通常用于基于索引将多个 DataFrame 连接


```python
import pandas as pd

left = pd.DataFrame({'A': [1, 2, 3]}, index=[1, 2, 3])
right = pd.DataFrame({'B': [4, 5, 6]}, index=[1, 2, 4])

# 使用 join 进行连接
result = left.join(right, how='inner')
print(result)
```

## 透视表与交叉表
``pivot_table() — 创建透视表``   
  
``crosstab(index,columns,values,aggfunc)— 创建交叉表``  
- index	行标签
- columns	列标签
- values	用于计算的数据（可选）
- aggfunc	聚合函数，默认 count


```python
import pandas as pd
data = {'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
        'Region': ['North', 'South', 'North', 'South', 'West', 'East']}
df = pd.DataFrame(data)

# 创建交叉表
cross_table = pd.crosstab(df['Category'], df['Region'])
print(cross_table)
```

## 自定义函数
``map()``   
- arg	应用的函数，字典或 Series
  
``apply(func,axis,raw,result_type)``  
- func	需要应用的函数
- axis	默认为 0，表示按列应用；1 表示按行应用
- raw	是否传递原始数据（默认为 False）
- result_type  定义输出的类型，如 expand, reduce, broadcast
  
map原本是 Series 的方法，但在较新版本中也可用于 DataFrame  
apply更通用支持更复杂的逻辑  
|函数	|适用对象	|说明|
|---|---|---|
|map()	|Series 或 DataFrame	|对每个元素进行独立操作|
|apply()	|Series 或 DataFrame	|对行/列或元素进行灵活操作|


```python
import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [10, 20, 30, 40]})

# 定义自定义函数
def custom_func(x):
    return x * 2
# 在列上应用函数
df['A'] = df['A'].apply(custom_func)
print(df)

df = df.map(lambda x: x ** 2)
print(df)


df = pd.DataFrame({'A': ['cat', 'dog', 'rabbit']})
# 使用字典进行映射
df['A'] = df['A'].map({'cat': 'kitten', 'dog': 'puppy'})
print(df)
```

## 分组操作与聚合
``groupby()``  
``agg()``  

## 时间序列处理
``date_range() — 生成时间序列``  
- 参数	说明
- start	起始日期
- end	结束日期
- periods	生成的时间点数
- freq	频率（如 D 表示天，H 表示小时等）
  
``pd.Timedelta() — 日期和时间的偏移``  
- days: 天数（整数或浮点数）
- seconds: 秒数（整数或浮点数）
- minutes: 分钟数（整数或浮点数）
- hours: 小时数（整数或浮点数）
- weeks: 周数（整数或浮点数）
- unit: 当传入数值时，指定单位（如 "s"、"min"、"h" 等）


```python
import pandas as pd

# 生成时间序列
date_range = pd.date_range(start='2024-01-01', periods=5, freq='D')
td = pd.Timedelta(days=2, hours=5, minutes=30, seconds=10)
td = pd.Timedelta("3 days 2 hours 15 minutes")
td = pd.Timedelta(120, unit="s")

# 日期偏移
date = pd.to_datetime('2024-01-01')
new_date = date + pd.Timedelta(days=10)
print(new_date)
```

## 多重索引的创建
``pd.MultiIndex.from_tuples()``  
使用元组来创建多重索引，每个元组对应一个索引层级   
``pd.MultiIndex.from_product()``  
使用多个列表的笛卡尔积来创建多重索引，适合用于数据维度较多的情况  
``set_index()``  
将 DataFrame 的列转换为多重索引，适用于从已有的数据创建多重索引


```python
import pandas as pd
## pd.MultiIndex.from_tuples()
# 创建元组
index_tuples = [('A', 1), ('A', 2), ('B', 1), ('B', 2)]

# 创建多重索引
multi_index = pd.MultiIndex.from_tuples(index_tuples, names=['Letter', 'Number'])

# 创建 DataFrame
df = pd.DataFrame({'Value': [10, 20, 30, 40]}, index=multi_index)


## pd.MultiIndex.from_product()
# 创建多个列表
index_values = [['A', 'B'], [1, 2]]

# 创建多重索引
multi_index = pd.MultiIndex.from_product(index_values, names=['Letter', 'Number'])

# 创建 DataFrame
df = pd.DataFrame({'Value': [10, 20, 30, 40]}, index=multi_index)

## set_index()
# 示例数据
data = {
    'Letter': ['A', 'A', 'B', 'B'],
    'Number': [1, 2, 1, 2],
    'Value': [10, 20, 30, 40]
}

df = pd.DataFrame(data)

# 设置多重索引
df.set_index(['Letter', 'Number'], inplace=True)


## 输出结果
#                Value
# Letter Number       
# A      1          10
#        2          20
# B      1          30
#        2          40
```

## 多重索引的操作
通过层级索引来访问数据。通过 loc[] 或 xs()可以方便地进行数据选择  


```python
data = {
    'Letter': ['A', 'A', 'B', 'B'],
    'Number': [1, 2, 1, 2],
    'Value': [10, 20, 30, 40]
}
df = pd.DataFrame(data)

# 设置多重索引
df.set_index(['Letter', 'Number'], inplace=True)

# 选择 'A' 类别，所有 'Number' 为 1 的数据
print(df.loc['A', 1])
# 使用 xs 获取 'Number' 为 1 的所有数据
print(df.xs(1, level='Number'))
# 选择 Letter 为 'A' 的所有数据
print(df.loc['A'])
# 按照多重索引排序
df_sorted = df.sort_index(level=['Letter', 'Number'], ascending=[True, False])
# 使用 groupby 对多重索引进行聚合
df_grouped = df.groupby(['Letter', 'Number']).sum()
# 重设索引
df_reset = df.reset_index()
```

# 示例：股票数据分析
>```python
>import yfinance as yf # yfinance（雅虎财经库）
>
># 获取茅台（600519.SS）的股票数据，日期范围从 2020-01-01 到 2021-01-01
>stock_data = yf.download('600519.SS', start='2020-01-01', end='2021-01-01')
>
># 查看数据的前几行
>print(stock_data.head())
>
># 返回的数据包含以下列：
># Open：开盘价
># High：最高价
># Low：最低价
># Close：收盘价
># Adj Close：调整后的收盘价（考虑了股息、拆股等因素）
># Volume：成交量
>
># 检查缺失值
>print(stock_data.isnull().sum())
>
># 使用前向填充替换缺失值
>stock_data.ffill(inplace=True)
>
># 或者使用后向填充
># stock_data.bfill(inplace=True)
>
># 检查缺失值是否已经处理
>print(stock_data.isnull().sum())
>
># 删除"Volume"和"Adj Close"列
>stock_data_cleaned = stock_data.drop(columns=['Adj Close', 'Volume'])
>print(stock_data_cleaned.head())
>
># 绘制茅台收盘价曲线
>plt.figure(figsize=(10, 6))
>plt.plot(stock_data_cleaned['Close'], label='Close Price')
>plt.title('Maotai Stock Price (2020)', fontsize=14)
>plt.xlabel('Date', fontsize=12)
>plt.ylabel('Close Price (CNY)', fontsize=12)
>plt.legend()
>plt.grid(True)
>plt.show()
>
>## 技术指标
>
># 计算 50 日和 200 日的移动平均线
>stock_data_cleaned['SMA_50'] = stock_data_cleaned['Close'].rolling(window=50).mean()
>stock_data_cleaned['SMA_200'] = stock_data_cleaned['Close'].rolling(window=200).mean()
># plt.plot(stock_data_cleaned['SMA_50'], label='50-Day SMA')
># plt.plot(stock_data_cleaned['SMA_200'], label='200-Day SMA')
>
># 计算 RSI 指标
>delta = stock_data_cleaned['Close'].diff(1)
>gain = delta.where(delta > 0, 0)
>loss = -delta.where(delta < 0, 0)
># 计算平均收益和损失
>avg_gain = gain.rolling(window=14).mean()
>avg_loss = loss.rolling(window=14).mean()
># 计算相对强弱指数 RSI
>rs = avg_gain / avg_loss
>rsi = 100 - (100 / (1 + rs))
># 添加 RSI 到数据中
>stock_data_cleaned['RSI'] = rsi
># plt.plot(stock_data_cleaned['RSI'], label='RSI')
># plt.axhline(y=70, color='r', linestyle='--', label='Overbought (70)') 一般来说，RSI 大于 70 表示过度买入，小于 30 表示过度卖出
># plt.axhline(y=30, color='g', linestyle='--', label='Oversold (30)')
>
># 计算日收益率
>stock_data_cleaned['Daily_Return'] = stock_data_cleaned['Close'].pct_change()
># 计算累计收益率
>stock_data_cleaned['Cumulative_Return'] = (1 + stock_data_cleaned['Daily_Return']).cumprod()
># plt.plot(stock_data_cleaned['Cumulative_Return'], label='Cumulative Return')
>
># 计算日收益率的标准差（波动率）
>volatility = stock_data_cleaned['Daily_Return'].std()
># 显示波动率
>print(f"Daily Volatility: {volatility:.4f}")
>```
