# 常量

## np.nan
表示空值  
nan = NaN = NAN  
NaN 是不等于任何值的，包括它自己


```python
import numpy as np

print(np.nan == np.nan)  # False
print(np.nan != np.nan)  # True
print(0*np.nan) # nan
print(np.nan-np.nan) # nan
print(np.inf>np.nan) # False
```

## np.isnan  
逐元素测试是否为 NaN（Not a Number，非数字），并将结果以布尔数组的形式返回
## np.count_nonzero


```python
import numpy as np

x = np.array([1, 1, 8, np.nan, 10])
print(x)
# [ 1.  1.  8. nan 10.]

y = np.isnan(x)
print(y)
# [False False False  True False]

z = np.count_nonzero(y)
print(z)  # 1
```

## np.inf
表示正无穷大。inf = infinity
Inf = inf = infty = Infinity = PINF
## np.pi
表示圆周率
pi = 3.1415926535897932384626433...
## np.e
表示自然常数
e = 2.71828182845904523536028747135266249775724709369995...

# 数据类型

## 常见数据类型
为了加以区分 numpy 在这些类型名称末尾都加了“_”
| 类型                   | 备注    | 说明                     |
|------------------------|---------|--------------------------|
| `bool_` = `bool8`      | 8位     | 布尔类型                 |
| `int8` = `byte`        | 8位     | 整型                     |
| `int16` = `short`      | 16位    | 整型                     |
| `int32` = `intc`       | 32位    | 整型                     |
| `int_` = `int64` = `long` = `int0` = `intp` | 64位    | 整型                     |
| `uint8` = `ubyte`      | 8位     | 无符号整型               |
| `uint16` = `ushort`    | 16位    | 无符号整型               |
| `uint32` = `uintc`     | 32位    | 无符号整型               |
| `uint64` = `uintp` = `uint0` = `uint` | 64位    | 无符号整型               |
| `float16` = `half`     | 16位    | 浮点型                   |
| `float32` = `single`   | 32位    | 浮点型                   |
| `float_` = `float64` = `double` | 64位    | 浮点型                   |
| `str_` = `unicode_` = `str0` = `unicode` |         | Unicode 字符串           |
| `datetime64`           |         | 日期时间类型             |
| `timedelta64`          |         | 表示两个时间之间的间隔   |

## 创建数据类型 np.dtype
numpy 的数值类型实际上是 dtype 对象的实例
>```
>class dtype(object):
>    def __init__(self, obj, align=False, copy=False):
>        pass
>```
| 字符 | 对应类型                     | 备注                                  |
|------|------------------------------|---------------------------------------|
| b    | boolean                      | 'b1'                                  |
| i    | signed integer               | 'i1', 'i2', 'i4', 'i8'               |
| u    | unsigned integer             | 'u1', 'u2', 'u4', 'u8'               |
| f    | floating-point               | 'f2', 'f4', 'f8'                     |
| c    | complex floating-point        |                                       |
| m    | timedelta64                  | 表示两个时间之间的间隔               |
| M    | datetime64                   | 日期时间类型                         |
| O    | object                       |                                       |
| S    | (byte-)string                | S3表示长度为3的字符串                 |
| U    | Unicode                      | Unicode 字符串                       |
| V    | void                         |                                       |


```python
import numpy as np

a = np.dtype('b1')
print(a.type)  # <class 'numpy.bool_'>
print(a.itemsize)  # 1

a = np.dtype('i1')
print(a.type)  # <class 'numpy.int8'>
print(a.itemsize)  # 1
a = np.dtype('i2')
print(a.type)  # <class 'numpy.int16'>
print(a.itemsize)  # 2
a = np.dtype('i4')
print(a.type)  # <class 'numpy.int32'>
print(a.itemsize)  # 4
a = np.dtype('i8')
print(a.type)  # <class 'numpy.int64'>
print(a.itemsize)  # 8

a = np.dtype('u1')
print(a.type)  # <class 'numpy.uint8'>
print(a.itemsize)  # 1

a = np.dtype('f4')
print(a.type)  # <class 'numpy.float32'>
print(a.itemsize)  # 4

a = np.dtype('S')
print(a.type)  # <class 'numpy.bytes_'>
print(a.itemsize)  # 0
a = np.dtype('S3')
print(a.type)  # <class 'numpy.bytes_'>
print(a.itemsize)  # 3

a = np.dtype('U3')
print(a.type)  # <class 'numpy.str_'>
print(a.itemsize)  # 12
```

## 数据类型信息 np.iinfo
Python 的浮点数通常是64位浮点数，几乎等同于 np.float64  

NumPy和Python整数类型的行为在整数溢出方面存在显着差异，与 NumPy 不同，Python 的int 是灵活的。这意味着Python整数可以扩展以容纳任何整数并且不会溢出。

>```
>class iinfo(object):
>    def __init__(self, int_type):
>        pass
>    def min(self):
>        pass
>    def max(self):
>        pass
>```


```python
import numpy as np

ii16 = np.iinfo(np.int16)
print(ii16.min)  # -32768
print(ii16.max)  # 32767

ii32 = np.iinfo(np.int32)
print(ii32.min)  # -2147483648
print(ii32.max)  # 2147483647

ff16 = np.finfo(np.float16)
print(ff16.bits)  # 16
print(ff16.min)  # -65500.0
print(ff16.max)  # 65500.0
print(ff16.eps)  # 0.000977

ff32 = np.finfo(np.float32)
print(ff32.bits)  # 32
print(ff32.min)  # -3.4028235e+38
print(ff32.max)  # 3.4028235e+38
print(ff32.eps)  # 1.1920929e-07
```

# 时间日期和时间增量

## np.datetime64    
在 numpy 中，我们很方便的将字符串转换成时间日期类型 datetime64（datetime 已被 python 包含的日期时间库所占用）。

datatime64是带单位的日期时间类型，其单位如下：

| 日期单位 | 代码含义 | 时间单位 | 代码含义 |
| :--: | :--: | :--: | :--: |
| Y | 年 | h | 小时 |
| M | 月 | m | 分钟 |
| W | 周 | s | 秒 |
| D | 天 | ms | 毫秒 |
| - | - | us | 微秒 |
| - | - | ns | 纳秒 |
| - | - | ps | 皮秒 |
| - | - | fs | 飞秒 |
| - | - | as | 阿托秒 |

1秒 = 1000 毫秒  
1毫秒 = 1000 微秒  
从字符串创建 datetime64 类型时，默认情况下，numpy 会根据字符串自动选择对应的单位


```python
import numpy as np

a = np.datetime64('2020-03-01')
print(a, a.dtype)  # 2020-03-01 datetime64[D]

a = np.datetime64('2020-03-08 20:00:05')
print(a, a.dtype)  # 2020-03-08T20:00:05 datetime64[s]

###################################################################
# 也可以强制指定
a = np.datetime64('2020-03', 'D')
print(a, a.dtype)  # 2020-03-01 datetime64[D]

a = np.datetime64('2020-03', 'Y')
print(a, a.dtype)  # 2020 datetime64[Y]

print(np.datetime64('2020-03') == np.datetime64('2020-03-01'))  # True
print(np.datetime64('2020-03') == np.datetime64('2020-03-02'))  #False

###################################################################
# 从字符串创建 datetime64 数组时，如果单位不统一，则一律转化成其中最小的单位。
a = np.array(['2020-03', '2020-03-08', '2020-03-08 20:00'], dtype='datetime64')
print(a, a.dtype)  # ['2020-03-01T00:00' '2020-03-08T00:00' '2020-03-08T20:00'] datetime64[m]

###################################################################
# 使用arange()创建 datetime64 数组，用于生成日期范围。
a = np.arange('2020-08-01', '2020-08-10',2, dtype=np.datetime64)
print(a)
# ['2020-08-01' '2020-08-03' '2020-08-05' '2020-08-07' '2020-08-09']
print(a.dtype)  # datetime64[D]

a = np.arange('2020-08-01 20:00', '2020-08-10', dtype=np.datetime64)
print(a)
# ['2020-08-01T20:00' '2020-08-01T20:01' '2020-08-01T20:02' ...
#  '2020-08-09T23:57' '2020-08-09T23:58' '2020-08-09T23:59']
print(a.dtype)  # datetime64[m]

a = np.arange('2020-05', '2020-12', dtype=np.datetime64)
print(a)
# ['2020-05' '2020-06' '2020-07' '2020-08' '2020-09' '2020-10' '2020-11']
print(a.dtype)  # datetime64[M]
```

## np.timedelta64时间运算  
timedelta64 表示两个 datetime64 之间的差。timedelta64 也是带单位的，并且和相减运算中的两个 datetime64 中的较小的单位保持一致。


```python
import numpy as np

a = np.datetime64('2020-03-08') - np.datetime64('2020-03-07')
b = np.datetime64('2020-03-08') - np.datetime64('202-03-07 08:00')
c = np.datetime64('2020-03-08') - np.datetime64('2020-03-07 23:00', 'D')

print(a, a.dtype)  # 1 days timedelta64[D]
print(b, b.dtype)  # 956178240 minutes timedelta64[m]
print(c, c.dtype)  # 1 days timedelta64[D]

a = np.datetime64('2020-03') + np.timedelta64(20, 'D')
b = np.datetime64('2020-06-15 00:00') + np.timedelta64(12, 'h')
print(a, a.dtype)  # 2020-03-21 datetime64[D]
print(b, b.dtype)  # 2020-06-15T12:00 datetime64[m]

###################################################################
# 注意年（'Y'）和月（'M'）这两个单位无法和其它单位进行运算（一年有几天？一个月有几个小时？这些都是不确定的）
a = np.timedelta64(1, 'Y')
b = np.timedelta64(a, 'M')
print(a)  # 1 years
print(b)  # 12 months
print(np.timedelta64(a, 'D'))
# TypeError: Cannot cast NumPy timedelta64 scalar from metadata [Y] to [D] according to the rule 'same_kind

###################################################################
# 运算示例
a = np.timedelta64(1, 'Y')
b = np.timedelta64(6, 'M')
c = np.timedelta64(1, 'W')
d = np.timedelta64(1, 'D')
e = np.timedelta64(10, 'D')

print(a)  # 1 years
print(b)  # 6 months
print(a + b)  # 18 months
print(a - b)  # 6 months
print(2 * a)  # 2 years
print(a / b)  # 2.0
print(c / d)  # 7.0
print(c % e)  # 7 days

```

## .astype() 转换


```python
# numpy.datetime64 与 datetime.datetime 相互转换
import numpy as np,datetime

dt = datetime.datetime(year=2020, month=6, day=1, hour=20, minute=5, second=30)
print(dt) #2020-06-01 20:05:30
dt64 = np.datetime64(dt, 's')
print(dt64, dt64.dtype) # 2020-06-01T20:05:30 datetime64[s]

dt2 = dt64.astype(datetime.datetime)
print(dt2, type(dt2))
# 2020-06-01 20:05:30 <class 'datetime.datetime'>
```

## np.busday_offset 工作日
为了能够在仅对一周中的某些特定日子有效的上下文中使用日期时间，NumPy 包含一组“busday”（工作日）功能。

`numpy.busday_offset(dates, offsets, roll='raise', weekmask='1111100', holidays=None, busdaycal=None, out=None)`
首先根据 `roll` 规则调整日期，使其落在有效的工作日上，然后以有效工作日为单位对给定日期应用偏移量。
参数 ：{'raise', 'nat', 'forward', 'following', 'backward', 'preceding', 'modifiedfollowing', 'modifiedpreceding'}

'raise' 表示对于无效的日期抛出异常。
'nat' 表示对于无效的日期返回 NaT（非时间）。
'forward' 和 'following' 表示取时间上稍后的第一个有效工作日。
'backward' 和 'preceding' 表示取时间上稍早的第一个有效工作日。


```python
# 将指定的偏移量应用于工作日，单位天（'D'）。计算下一个工作日，如果当前日期为非工作日，默认报错。
# 可以指定 forward 或 backward 规则来避免报错。（一个是向前取第一个有效的工作日，一个是向后取第一个有效的工作日）

import numpy as np

# 2020-07-10 星期五
a = np.busday_offset('2020-07-10', offsets=1)# 计算下一个工作日
print(a)  # 2020-07-13

a = np.busday_offset('2020-07-11', offsets=1)# 当前日期为非工作日，默认报错
print(a)
# ValueError: Non-business day date in busday_offset

a = np.busday_offset('2020-07-11', offsets=0, roll='forward')
b = np.busday_offset('2020-07-11', offsets=0, roll='backward')
print(a)  # 2020-07-13
print(b)  # 2020-07-10

a = np.busday_offset('2020-07-11', offsets=1, roll='forward')
b = np.busday_offset('2020-07-11', offsets=1, roll='backward')
print(a)  # 2020-07-14
print(b)  # 2020-07-13

###################################################################
# 返回指定日期是否是工作日
a = np.is_busday('2020-07-10')
b = np.is_busday('2020-07-11')
print(a)  # True
print(b)  # False

###################################################################
# 统计一个 datetime64[D] 数组中的工作日天数。
begindates = np.datetime64('2020-07-10')
enddates = np.datetime64('2020-07-20')
a = np.arange(begindates, enddates, dtype='datetime64')
b = np.count_nonzero(np.is_busday(a))
print(a)
# ['2020-07-10' '2020-07-11' '2020-07-12' '2020-07-13' '2020-07-14'
#  '2020-07-15' '2020-07-16' '2020-07-17' '2020-07-18' '2020-07-19']
print(b)  # 6


# 返回两个日期之间的工作日数量。
a = np.busday_count(begindates, enddates)
b = np.busday_count(enddates, begindates)
print(a)  # 6
print(b)  # -6
```

# 数组的创建 np.array
numpy 提供的最重要的数据结构是ndarray，它是 python 中list的扩展  
`def array(p_object, dtype=None, copy=True, order='K', subok=False, ndmin=0): `


```python
import numpy as np
# 创建一维数组
a = np.array([0, 1, 2, 3, 4])# 列表
b = np.array((0, 1, 2, 3, 4))# 元组
print(a, type(a))
# [0 1 2 3 4] <class 'numpy.ndarray'>
print(b, type(b))
# [0 1 2 3 4] <class 'numpy.ndarray'>

# 创建二维数组
c = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28, 29, 30],
              [31, 32, 33, 34, 35]])
print(c, type(c))
# [[11 12 13 14 15]
#  [16 17 18 19 20]
#  [21 22 23 24 25]
#  [26 27 28 29 30]
#  [31 32 33 34 35]] <class 'numpy.ndarray'>

# 创建三维数组
d = np.array([[(1.5, 2, 3), (4, 5, 6)],
              [(3, 2, 1), (4, 5, 6)]])
print(d, type(d))
# [[[1.5 2.  3. ]
#   [4.  5.  6. ]]
#
#  [[3.  2.  1. ]
#   [4.  5.  6. ]]] <class 'numpy.ndarray'>
```

## asarray()
array()和asarray()主要区别就是当数据源是ndarray 时，array()仍然会 copy 出一个独立的副本，占用新的内存,但不改变 dtype 时 asarray()不会  
asarray()返回输入的视图（view），如果输入已经是一个 numpy 数组（如 x），那么 z 和 x 指向的是同一块内存  
`def asarray(a, dtype=None, order=None):    return array(a, dtype, copy=False, order=order)`


```python
import numpy as np

x = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
y = np.array(x)
z = np.asarray(x)
x[1][2] = 2
print(x,type(x))
# [[1, 1, 1], [1, 1, 2], [1, 1, 1]] <class 'list'>

print(z,type(z))# 由列表转换为一个独立的ndarray，不会随x改变
# [[1 1 1]
#  [1 1 1]
#  [1 1 1]] <class 'numpy.ndarray'>

x = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
z = np.asarray(x)
print(z,type(z),z.dtype)# x本身为ndarray，dtype不变，会随x改变
# [[1 1 1]
#  [1 1 2]
#  [1 1 1]] <class 'numpy.ndarray'> int32
```

## fromfunction()
fromfunction 函数根据提供的函数和数组的形状生成一个数组，其中数组的每个元素是通过将索引传递给提供的函数来计算的  
`def fromfunction(function, shape, **kwargs):`


```python
import numpy as np

def f(x, y):
    return 10 * x + y

x = np.fromfunction(f, (5, 4), dtype=int)
print(x)
# [[ 0  1  2  3]
#  [10 11 12 13]
#  [20 21 22 23]
#  [30 31 32 33]
#  [40 41 42 43]]
# 每个元素 (i, j) 的值是通过 f(i, j) 计算的，其中 i 是行索引，j 是列索引

x = np.fromfunction(lambda i, j: i == j, (3, 3), dtype=int)
print(x)
# [[ True False False]
#  [False  True False]
#  [False False  True]]
```

## 零数组 zeros() zeros_like()
zeros()函数：返回给定形状和类型的零数组  
zeros_like()函数：返回与给定数组形状和类型相同的零数组  
`def zeros(shape, dtype=None, order='C'):`  
`def zeros_like(a, dtype=None, order='K', subok=True, shape=None):`


```python
import numpy as np

x = np.zeros(5)
print(x)  # [0. 0. 0. 0. 0.]
x = np.zeros([2, 3])
print(x)
# [[0. 0. 0.]
#  [0. 0. 0.]]

x = np.array([[1, 2, 3], [4, 5, 6]])
y = np.zeros_like(x)
print(y)
# [[0 0 0]
#  [0 0 0]]
```

## 1数组 ones() ones_like()
ones()函数：返回给定形状和类型的1数组  
ones_like()函数：返回与给定数组形状和类型相同的1数组  
`def ones(shape, dtype=None, order='C'):`  
`def ones_like(a, dtype=None, order='K', subok=True, shape=None):`  

## 空数组 empty() empty_like()
empty()函数：返回一个空数组，数组元素为随机数  
empty_like()函数：返回与给定数组具有相同形状和类型的新数组  
`def empty(shape, dtype=None, order='C'): `  
`def empty_like(prototype, dtype=None, order='K', subok=True, shape=None):`  

## 单位数组 eye() identity()
eye()函数：返回一个对角线上为1，其它地方为零的单位数组  
identity()函数：返回一个方阵的单位数组  
`def eye(N, M=None, k=0, dtype=float, order='C'):`  
`def identity(n, dtype=None):`  

## 对角数组 diag()
diag()函数：提取对角线或构造对角数组  
`def diag(v, k=0):`  


```python
import numpy as np

x = np.arange(9).reshape((3, 3))
print(x)
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]
print(np.diag(x))  # [0 4 8]
print(np.diag(x, k=1))  # [1 5]
print(np.diag(x, k=-1))  # [3 7]

v = [1, 3, 5, 7]
x = np.diag(v)
print(x)
# [[1 0 0 0]
#  [0 3 0 0]
#  [0 0 5 0]
#  [0 0 0 7]]
```

## 常数数组 full() full_like()
full()函数：返回一个常数数组   
full_like()函数：返回与给定数组具有相同形状和类型的常数数组  
`def full(shape, fill_value, dtype=None, order='C'):`  
`def full_like(a, fill_value, dtype=None, order='K', subok=True, shape=None):`


```python
import numpy as np

x = np.full(2, 7)
print(x)
# [7 7]

x = np.full((2, 7), True)
print(x)
# [[ True  True  True  True  True  True  True]
#   [ True  True  True  True  True  True  True]]

x = np.array([[1, 2, 3], [4, 5, 6]])
y = np.full_like(x, 7)
print(y)
# [[7 7 7]
#  [7 7 7]]
```

## 范围数组 arange() linspace() logspace() numpy.random.rand()
arange()函数：返回给定间隔内的均匀间隔的值  
linspace()函数：返回指定间隔内的等间隔数字  
logspace()函数：返回数以对数刻度均匀分布  
numpy.random.rand() 返回一个由[0,1)内的随机数组成的数组  

`def arange([start,] stop[, step,], dtype=None): `  
`def linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0):`  
`def logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None, axis=0):`  
`def rand(d0, d1, ..., dn):`  


```python
import numpy as np

x = np.arange(5)
print(x)  # [0 1 2 3 4]

x = np.arange(3, 7, 2)
print(x)  # [3 5]

x = np.linspace(start=0, stop=2, num=9)# num=9 指定要生成的样本数量
print(x)  
# [0.   0.25 0.5  0.75 1.   1.25 1.5  1.75 2.  ]

x = np.logspace(0, 1, 5)# 0表示 10^0  1表示 10^1  5 是要生成的样本数量
print(np.around(x, 2))
# [ 1.    1.78  3.16  5.62 10.  ]            
#np.around 返回四舍五入后的值，可指定精度。
# around(a, decimals=0, out=None)
# a 输入数组
# decimals 要舍入的小数位数。 默认值为0。 如果为负，整数将四舍五入到小数点左侧的位置

x = np.random.random(5)
print(x)
# [0.41768753 0.16315577 0.80167915 0.99690199 0.11812291]随机的

x = np.random.random([2, 3])
print(x)
#[[0.33150306 0.02528108 0.01043121]
# [0.19817739 0.19836231 0.13301785]]
```

## 结构数组的创建
结构数组，首先需要定义结构，然后利用np.array()来创建数组，其参数dtype为定义的结构 


```python
# 利用字典来定义结构
import numpy as np

personType = np.dtype({
    'names': ['name', 'age', 'weight'],
    'formats': ['U30', 'i8', 'f8']})
# 'names' 指定字段的名称。
# 'formats' 指定每个字段的数据类型。
# 'U30' 表示一个长度最多为 30 的 Unicode 字符串。
# 'i8' 表示一个 64 位整数。
# 'f8' 表示一个 64 位浮点数。

a = np.array([('Liming', 24, 63.9), ('Mike', 15, 67.), ('Jan', 34, 45.8)],
             dtype=personType)
print(a, type(a))
# [('Liming', 24, 63.9) ('Mike', 15, 67. ) ('Jan', 34, 45.8)] <class 'numpy.ndarray'>
```


```python
# 利用包含多个元组的列表来定义结构

import numpy as np

personType = np.dtype([('name', 'U30'), ('age', 'i8'), ('weight', 'f8')])
a = np.array([('Liming', 24, 63.9), ('Mike', 15, 67.), ('Jan', 34, 45.8)],dtype=personType)
print(a, type(a))
# [('Liming', 24, 63.9) ('Mike', 15, 67. ) ('Jan', 34, 45.8)]
# <class 'numpy.ndarray'>

# 结构数组的取值方式和一般数组差不多，可以通过下标取得元素：
print(a[0])
# ('Liming', 24, 63.9)

print(a[-2:])
# [('Mike', 15, 67. ) ('Jan', 34, 45.8)]

# 我们可以使用字段名作为下标获取对应的值
print(a['name'])
# ['Liming' 'Mike' 'Jan']
print(a['age'])
# [24 15 34]
print(a['weight'])
# [63.9 67.  45.8]
```

## 数组的属性
numpy.ndarray.ndim      返回数组的维数  
numpy.ndarray.shape     
numpy.ndarray.size      数组中所有元素的个数
numpy.ndarray.dtype     ndarray 对象的元素类型。
numpy.ndarray.itemsize  以字节的形式返回数组中每一个元素的大小。
>```
>class ndarray(object):
>    shape = property(lambda self: object(), lambda self, v: None, lambda self: None)
>    dtype = property(lambda self: object(), lambda self, v: None, lambda self: None)
>    size = property(lambda self: object(), lambda self, v: None, lambda self: None)
>    ndim = property(lambda self: object(), lambda self, v: None, lambda self: None)
>    itemsize = property(lambda self: object(), lambda self, v: None, lambda self: None)
>```   
>
>在ndarray中所有元素必须是同一类型，否则会自动向下转换，int->float->str。


```python
import numpy as np

a = np.array([1, 2, 3, 4, 5])
print(a.shape)  # (5,)
print(a.dtype)  # int32
print(a.size)  # 5
print(a.ndim)  # 1
print(a.itemsize)  # 4

b = np.array([[1, 2, 3], [4, 5, 6.0]])
print(b.shape)  # (2, 3)
print(b.dtype)  # float64
print(b.size)  # 6
print(b.ndim)  # 2
print(b.itemsize)  # 8


c = np.array([1, 2, 3, 4, '5'])
print(c)  # ['1' '2' '3' '4' '5']
d = np.array([1, 2, 3, 4, 5.0])
print(d)  # [1. 2. 3. 4. 5.]
```

# 索引，切片，迭代 .copy()

## 副本与视图 .copy()
在 Numpy 中，尤其是在做数组运算或数组操作时，返回结果不是数组的 副本 就是 视图   
在 Numpy 中，所有赋值运算不会为数组和数组中的任何元素创建副本  

numpy.ndarray.copy() 函数创建一个副本。 对副本数据进行修改，不会影响到原始数据，它们物理内存不在同一位置  


```python
import numpy as np

x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = x   #相同内存地址
y[0] = -1
print(x)
# [-1  2  3  4  5  6  7  8]
print(y)
# [-1  2  3  4  5  6  7  8]

x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = x.copy()
y[0] = -1
print(x)
# [1 2 3 4 5 6 7 8]
print(y)
# [-1  2  3  4  5  6  7  8]
```

## 索引与切片


```python
# 索引
import numpy as np

x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(x[2])  # 3

x = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28, 29, 30],
              [31, 32, 33, 34, 35]])
print(x[2])  # [21 22 23 24 25]
print(x[2][1])  # 22
print(x[2, 1])  # 22
```


```python
# 切片[start:stop:step]前闭后开
import numpy as np
# 对一维数组的切片
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(x[0:2])  # [1 2]
print(x[1:5:2])  # [2 4]
print(x[2:])  # [3 4 5 6 7 8]
print(x[:2])  # [1 2]
print(x[-2:])  # [7 8]
print(x[:-2])  # [1 2 3 4 5 6]
print(x[:])  # [1 2 3 4 5 6 7 8]
print(x[::-1])  # [8 7 6 5 4 3 2 1]


# 对二维数组切片[行(start:stop:step)，列(start:stop:step)]
x = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28, 29, 30],
              [31, 32, 33, 34, 35]])
print(x[0:2])
# [[11 12 13 14 15]
#  [16 17 18 19 20]]

print(x[1:5:2])
# [[16 17 18 19 20]
#  [26 27 28 29 30]]

print(x[-2:])
# [[26 27 28 29 30]
#  [31 32 33 34 35]]

print(x[:-2])
# [[11 12 13 14 15]
#  [16 17 18 19 20]
#  [21 22 23 24 25]]

print(x[:])
# [[11 12 13 14 15]
#  [16 17 18 19 20]
#  [21 22 23 24 25]
#  [26 27 28 29 30]
#  [31 32 33 34 35]]

print(x[2, :])  # [21 22 23 24 25]  访问第 3 行的所有列元素
print(x[:, 2])  # [13 18 23 28 33]  访问所有行的第 3 列元素
print(x[0, 1:4])  # [12 13 14]      1 行的第 2 到第 4 列元素
print(x[1:4, 0])  # [16 21 26]
print(x[1:3, 2:4])
# [[18 19]
#  [23 24]]

print(x[:, :])
# [[11 12 13 14 15]
#  [16 17 18 19 20]
#  [21 22 23 24 25]
#  [26 27 28 29 30]
#  [31 32 33 34 35]]

print(x[::2, ::2])
# [[11 13 15]
#  [21 23 25]
#  [31 33 35]]

print(x[::-1, :])
# [[31 32 33 34 35]
#  [26 27 28 29 30]
#  [21 22 23 24 25]
#  [16 17 18 19 20]
#  [11 12 13 14 15]]

print(x[:, ::-1])
# [[15 14 13 12 11]
#  [20 19 18 17 16]
#  [25 24 23 22 21]
#  [30 29 28 27 26]
#  [35 34 33 32 31]]
```

## dots 索引
NumPy 允许使用...表示足够多的冒号来构建完整的索引列表  

比如，如果 x 是 5 维数组：  
>```
>x[1,2,...] 等于 x[1,2,:,:,:]
>x[...,3] 等于 x[:,:,:,:,3]
>x[4,...,5,:] 等于 x[4,:,:,5,:]
>```

## 数组索引 np.take()


```python
import numpy as np

x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(x[0, 1, 2])
# [1 2 3]
print(x[0, 1, -1])
# [1 2 8]

x = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28, 29, 30],
              [31, 32, 33, 34, 35]])
print(x[0, 1, 2])
# [[11 12 13 14 15]
#  [16 17 18 19 20]
#  [21 22 23 24 25]]
print(x[0, 1, -1])
# [[11 12 13 14 15]
#  [16 17 18 19 20]
#  [31 32 33 34 35]]

y = x[[0, 1, 2], [2, 3, 4]]#[0,2][1,3][2,4]
print(y)
# [13 19 25]

###################################################################

x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
r = np.array([[0, 1], [3, 4]])
print(x[r])
# [[1 2]
#  [4 5]]

x = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28, 29, 30],
              [31, 32, 33, 34, 35]])

r = np.array([[0, 1], [3, 4]])
print(x[r])
# [[[11 12 13 14 15]
#   [16 17 18 19 20]]
#
#  [[26 27 28 29 30]
#   [31 32 33 34 35]]]

# 获取数组中的四个角的元素
r = np.array([[0, 0], [4, 4]])
c = np.array([[0, 4], [0, 4]])
y = x[r, c]
print(y)
# [[11 15]
#  [31 35]]

###################################################################
# 与普通索引结合
x = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28, 29, 30],
              [31, 32, 33, 34, 35]])

y = x[0:3, [1, 2, 2]]
print(y)
# [[12 13 13]
#  [17 18 18]
#  [22 23 23]]

###################################################################

# numpy. take(a, indices, axis=None, out=None, mode='raise') 沿指定轴从数组中提取元素

x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
r = [0, 1, 2]
print(np.take(x, r))
# [1 2 3]

r = [0, 1, -1]
print(np.take(x, r))
# [1 2 8]

x = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28, 29, 30],
              [31, 32, 33, 34, 35]])

r = [0, 1, 2]
print(np.take(x, r, axis=0))
# [[11 12 13 14 15]
#  [16 17 18 19 20]
#  [21 22 23 24 25]]

r = [0, 1, -1]
print(np.take(x, r, axis=0))
# [[11 12 13 14 15]
#  [16 17 18 19 20]
#  [31 32 33 34 35]]
###################################################################
# 注意：使用切片时，生成的是视图，会影响原数组
#  但是数组索引，是副本，不影响原数组。 

# 切片
a=np.array([[1,2],
            [3,4],
            [5,6]])
b=a[0:1,0:1]#[[1]]
b[0,0]=2
print(a[0,0]==b)
#[[True]]

# 数组索引
b=a[0,0]
b=2
print(a[0,0]==b)
#False
```

## 布尔索引


```python
import numpy as np

x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = x > 5
print(y)
# [False False False False False  True  True  True]
print(x[x > 5])
# [6 7 8]

x = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28, 29, 30],
              [31, 32, 33, 34, 35]])
y = x > 25
print(y)
# [[False False False False False]
#  [False False False False False]
#  [False False False False False]
#  [ True  True  True  True  True]
#  [ True  True  True  True  True]]
print(x[x > 25])
# [26 27 28 29 30 31 32 33 34 35]

# 使用 np.isnan(x) 生成一个布尔数组，指示哪些元素是 NaN
# 然后使用 np.logical_not() 取反，得到一个布尔数组，指示哪些元素不是 NaN
x = np.array([np.nan, 1, 2, np.nan, 3, 4, 5])
y = np.logical_not(np.isnan(x))
# 使用布尔索引来过滤掉 NaN 值
print(x[y])
# [1. 2. 3. 4. 5.]
```


```python
import numpy as np
import matplotlib.pyplot as plt
# x 是一个从 0 到 2π 的等间距数组，包含 50 个点。
# y 是 x 中每个点对应的正弦值
x = np.linspace(0, 2 * np.pi, 50)
y = np.sin(x)
print(len(x))  # 50
plt.plot(x, y)
# 布尔掩码 mask:
# y >= 0 生成一个布尔数组，表示 y 中每个值是否大于或等于 0。
# mask 是一个布尔数组，与 x 和 y 的长度相同
mask = y >= 0
print(len(x[mask]))  # 25
print(mask)
'''
[ True  True  True  True  True  True  True  True  True  True  True  True
  True  True  True  True  True  True  True  True  True  True  True  True
  True False False False False False False False False False False False
 False False False False False False False False False False False False
 False False]
'''
# 绘制筛选出的点，使用蓝色圆圈标记 ('bo')。
plt.plot(x[mask], y[mask], 'bo')
# 复合条件 mask:
# np.logical_and(y >= 0, x <= np.pi / 2) 生成一个布尔数组，表示 y 大于等于 0 且 x 小于等于 π/2 的点。
# 打印 mask，可以看到满足条件的点为 [0, π/2] 区间内的正弦正半周期点
mask = np.logical_and(y >= 0, x <= np.pi / 2)
print(mask)
'''
[ True  True  True  True  True  True  True  True  True  True  True  True
  True False False False False False False False False False False False
 False False False False False False False False False False False False
 False False False False False False False False False False False False
 False False]
'''
# 绘制满足复合条件的点，使用绿色圆圈标记 ('go')
plt.plot(x[mask], y[mask], 'go')
plt.show()
```

## 数组迭代 np.apply_along_axis
apply_along_axis(func, axis, arr) 沿指定轴(axis=0 列,axis=1 行)对 arr 应用一个函数func


```python
import numpy as np

x = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28, 29, 30],
              [31, 32, 33, 34, 35]])
# 对每一列求和
y = np.apply_along_axis(np.sum, 0, x)
print(y)  # [105 110 115 120 125]
y = np.apply_along_axis(np.sum, 1, x)
print(y)  # [ 65  90 115 140 165]

y = np.apply_along_axis(np.mean, 0, x)
print(y)  # [21. 22. 23. 24. 25.]
y = np.apply_along_axis(np.mean, 1, x)
print(y)  # [13. 18. 23. 28. 33.]


def my_func(x):
    return (x[0] + x[-1]) * 0.5

# 对每一列的第一和最后一个求均值
y = np.apply_along_axis(my_func, 0, x)
print(y)  # [21. 22. 23. 24. 25.]
y = np.apply_along_axis(my_func, 1, x)
print(y)  # [13. 18. 23. 28. 33.]
```

# 数组操作

## 更改形状

### .shape      
numpy.ndarray.shape表示数组的维度，返回一个元组，这个元组的长度就是维度的数目，即 ndim 属性(秩)


```python

x = np.array([1, 2, 9, 4, 5, 6, 7, 8])
print(x.shape)  # (8,)
x.shape = [2, 4]
print(x)
# [[1 2 9 4]
#  [5 6 7 8]]
```

### .flat
numpy.ndarray.flat 将数组转换为一维的迭代器，可以用for访问数组每一个元素


```python
# .flat会影响原数组

x = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28, 29, 30],
              [31, 32, 33, 34, 35]])
y = x.flat
print(y)
# <numpy.flatiter object at 0x0000020F9BA10C60> 表示 y 是一个 numpy.flatiter 对象，并给出了它的内存地址
for i in y:
    print(i, end=' ')
# 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35

y[3] = 0
print(x)
# [[11 12 13  0 15]
#  [16 17 18 19 20]
#  [21 22 23 24 25]
#  [26 27 28 29 30]
#  [31 32 33 34 35]]
```

###  .flatten()
numpy.ndarray.flatten([order='C']) 将数组的副本转换为一维数组，并返回
    order：'C' -- 按行(默认)，'F' -- 按列，'A' -- 原顺序，'k' -- 元素在内存中的出现顺序


```python
# flatten()函数返回的是副本，不影响原数组

x = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28, 29, 30],
              [31, 32, 33, 34, 35]])
y = x.flatten()# 默认为order='C'
print(y)
# [11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35]

y[3] = 0
print(x)
# [[11 12 13 14 15]
#  [16 17 18 19 20]
#  [21 22 23 24 25]
#  [26 27 28 29 30]
#  [31 32 33 34 35]]
```

### np.ravel()
numpy.ravel(a, order='C')返回一个连续展平的数组


```python
# ravel()返回的是视图,影响原数组

x = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28, 29, 30],
              [31, 32, 33, 34, 35]])
y = np.ravel(x)
print(y)
# [11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35]

y[3] = 0
print(x)
# [[11 12 13  0 15]
#  [16 17 18 19 20]
#  [21 22 23 24 25]
#  [26 27 28 29 30]
#  [31 32 33 34 35]]

# 【例】order=F 就是拷贝

x = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28, 29, 30],
              [31, 32, 33, 34, 35]])

y = np.ravel(x, order='F')
print(y)
# [11 16 21 26 31 12 17 22 27 32 13 18 23 28 33 14 19 24 29 34 15 20 25 30
#  35]

y[3] = 0
print(x)
# [[11 12 13 14 15]
#  [16 17 18 19 20]
#  [21 22 23 24 25]
#  [26 27 28 29 30]
#  [31 32 33 34 35]]
```

### np.reshape()
numpy.reshape(a, newshape[, order='C'])在不更改数据的情况下为数组赋予新的形状


```python
# reshape()函数当参数newshape = [rows,-1]时，将根据行数自动确定列数,rows=-1时同理
# 修改会影响原数组
# 当参数newshape = -1时，表示将数组降为一维

x = np.arange(12)
y = np.reshape(x, [3, 4])
print(y)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

y = np.reshape(x,[-1,3])
print(y)
# [[ 0  1  2]
#  [ 3  4  5]
#  [ 6  7  8]
#  [ 9 10 11]]

y = np.reshape(x, -1)
print(y)
# [ 0  1  2  3  4  5  6  7  8  9 10 11]

y[1] = 10
print(x)
# [ 0 10  2  3  4  5  6  7  8  9 10 11]
```

## 数组转置

### np.transpose(a)
np.transpose(a, axes=None)
对数组的维度进行置换(重排)

### numpy.ndarray.T
与 self.transpose() 相同，但如果 self.ndim < 2（数组的维度小于 2），则直接返回 self


```python
import numpy as np

x = np.random.rand(5, 5) * 10   # 创建一个 5x5 的二维数组（矩阵），其中的每个元素都是从 0 到 1*10 之间的随机浮点数
x = np.around(x, 2)   # 对数组 x 中的每个元素进行四舍五入，保留两位小数
print(x)
# [[6.74 8.46 6.74 5.45 1.25]
#  [3.54 3.49 8.62 1.94 9.92]
#  [5.03 7.22 1.6  8.7  0.43]
#  [7.5  7.31 5.69 9.67 7.65]
#  [1.8  9.52 2.78 5.87 4.14]]
y = x.T
print(y)
# [[6.74 3.54 5.03 7.5  1.8 ]
#  [8.46 3.49 7.22 7.31 9.52]
#  [6.74 8.62 1.6  5.69 2.78]
#  [5.45 1.94 8.7  9.67 5.87]
#  [1.25 9.92 0.43 7.65 4.14]]
y = np.transpose(x)
print(y)
# [[6.74 3.54 5.03 7.5  1.8 ]
#  [8.46 3.49 7.22 7.31 9.52]
#  [6.74 8.62 1.6  5.69 2.78]
#  [5.45 1.94 8.7  9.67 5.87]
#  [1.25 9.92 0.43 7.65 4.14]]
```

## 更改维度


### np.newaxis


```python
import numpy as np
x = np.array([1, 2, 9, 4, 5, 6, 7, 8])
print(x.shape)  # (8,)
print(x)  # [1 2 9 4 5 6 7 8]

y = x[np.newaxis, :]
print(y.shape)  # (1, 8)
print(y)  # [[1 2 9 4 5 6 7 8]]

y = x[:, np.newaxis]
print(y.shape)  # (8, 1)
print(y)
# [[1]
#  [2]
#  [9]
#  [4]
#  [5]
#  [6]
#  [7]
#  [8]]
```

### np.squeeze(a) 
numpy.squeeze(a, axis=None) 
从数组的形状中删除单维度条目，即把shape中为1的维度去掉。
a表示输入的数组；
axis用于指定需要删除的维度，但是指定的维度必须为单维度，否则将会报错


```python
# 在机器学习和深度学习中，通常算法的结果是可以表示向量的数组（即包含两对或以上的方括号形式[[]]），
# 如果直接利用这个数组进行画图可能显示界面为空
# 我们可以利用squeeze()函数将表示向量的数组转换为秩为1的数组，这样利用 matplotlib 库函数画图时，就可以正常的显示结果了

import numpy as np

x = np.arange(10)
print(x.shape)  # (10,)
x = x[np.newaxis, :]
print(x.shape)  # (1, 10)
y = np.squeeze(x)
print(y.shape)  # (10,)

##################################################################
x = np.array([[[0], [1], [2]]])
print(x.shape)  # (1, 3, 1)
print(x)
# [[[0]
#   [1]
#   [2]]]

y = np.squeeze(x)
print(y.shape)  # (3,)
print(y)  # [0 1 2]

y = np.squeeze(x, axis=0)
print(y.shape)  # (3, 1)
print(y)
# [[0]
#  [1]
#  [2]]

y = np.squeeze(x, axis=2)
print(y.shape)  # (1, 3)
print(y)  # [[0 1 2]]

y = np.squeeze(x, axis=1)
# ValueError: cannot select an axis to squeeze out which has size not equal to one

##################################################################
# 画图示例
import matplotlib.pyplot as plt

x = np.array([[1, 4, 9, 16, 25]])
print(x.shape)  # (1, 5)
plt.plot(x)
plt.show()

##################################################################

x = np.array([[1, 4, 9, 16, 25]])
x = np.squeeze(x)
print(x.shape)  # (5, )
plt.plot(x)
plt.show()
```

## 数组组合

### np.concatenate((a1, a2, ...))
np.concatenate((a1, a2, ...), axis=0, out=None)
沿现有轴连接一系列数组


```python
# 【例】连接沿现有轴的数组序列
# 原来x，y都是一维的，拼接后也是一维的

x = np.array([1, 2, 3])
y = np.array([7, 8, 9])
z = np.concatenate([x, y])
print(z)
# [1 2 3 7 8 9]

z = np.concatenate([x, y], axis=0)# 按行
print(z)
# [1 2 3 7 8 9]

# 【例】原来x，y都是二维的，拼接后也是二维的

x = np.array([1, 2, 3]).reshape(1, 3)
y = np.array([7, 8, 9]).reshape(1, 3)
z = np.concatenate([x, y])
print(z)
# [[ 1  2  3]
#  [ 7  8  9]]
z = np.concatenate([x, y], axis=1)
print(z)
# [[ 1  2  3  7  8  9]]

# 【例】x，y在原来的维度上进行拼接

x = np.array([[1, 2, 3], [4, 5, 6]])
y = np.array([[7, 8, 9], [10, 11, 12]])
z = np.concatenate([x, y])
print(z)
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]
z = np.concatenate([x, y], axis=1)
print(z)
# [[ 1  2  3  7  8  9]
#  [ 4  5  6 10 11 12]]
```

### np.stack([a1, a2], axis=0默认)
numpy.stack([a1, a2], axis=0, out=None)
沿一个新轴连接一系列数组


```python
# 沿着新的轴加入一系列数组（stack为增加维度的拼接）

x = np.array([1, 2, 3])
y = np.array([7, 8, 9])
z = np.stack([x, y])
print(z.shape)  # (2, 3)
print(z)
# [[1 2 3]
#  [7 8 9]]

z = np.stack([x, y], axis=1)
print(z.shape)  # (3, 2)
print(z)
# [[1 7]
#  [2 8]
#  [3 9]]

##################################################################

x = np.array([1, 2, 3]).reshape(1, 3)
y = np.array([7, 8, 9]).reshape(1, 3)
z = np.stack([x, y])
print(z.shape)  # (2, 1, 3)
print(z)
# [[[1 2 3]]
#
#  [[7 8 9]]]

z = np.stack([x, y], axis=1)
print(z.shape)  # (1, 2, 3)
print(z)
# [[[1 2 3]
#   [7 8 9]]]

z = np.stack([x, y], axis=2)
print(z.shape)  # (1, 3, 2)
print(z)
# [[[1 7]
#   [2 8]
#   [3 9]]]

##################################################################

x = np.array([[1, 2, 3], [4, 5, 6]])
y = np.array([[7, 8, 9], [10, 11, 12]])
z = np.stack([x, y])
print(z.shape)  # (2, 2, 3)
print(z)
# [[[ 1  2  3]
#   [ 4  5  6]]
# 
#  [[ 7  8  9]
#   [10 11 12]]]

z = np.stack([x, y], axis=1)
print(z.shape)  # (2, 2, 3)
print(z)
# [[[ 1  2  3]
#   [ 7  8  9]]
# 
#  [[ 4  5  6]
#   [10 11 12]]]

z = np.stack([x, y], axis=2)
print(z.shape)  # (2, 3, 2)
print(z)
# [[[ 1  7]
#   [ 2  8]
#   [ 3  9]]
# 
#  [[ 4 10]
#   [ 5 11]
#   [ 6 12]]]
```

### numpy.vstack()
按行堆叠数组

### numpy.hstack()
按列堆叠数组
hstack(),vstack()在数据维度等于1时，比较特殊
而当维度大于或等于2时，它们的作用相当于concatenate，用于在已有轴上进行操作


```python
# 【例】一维的情况
import numpy as np

x = np.array([1, 2, 3])
y = np.array([7, 8, 9])
z = np.vstack((x, y))
print(z.shape)  # (2, 3)
print(z)
# [[1 2 3]
#  [7 8 9]]

z = np.stack([x, y])
print(z.shape)  # (2, 3)
print(z)
# [[1 2 3]
#  [7 8 9]]

z = np.hstack((x, y))
print(z.shape)  # (6,)
print(z)
# [1  2  3  7  8  9]

z = np.concatenate((x, y))
print(z.shape)  # (6,)
print(z)  # [1 2 3 7 8 9]

# 【例】二维的情况

x = np.array([1, 2, 3]).reshape(1, 3)
y = np.array([7, 8, 9]).reshape(1, 3)
z = np.vstack((x, y))
print(z.shape)  # (2, 3)
print(z)
# [[1 2 3]
#  [7 8 9]]

z = np.concatenate((x, y), axis=0)
print(z.shape)  # (2, 3)
print(z)
# [[1 2 3]
#  [7 8 9]]

z = np.hstack((x, y))
print(z.shape)  # (1, 6)
print(z)
# [[ 1  2  3  7  8  9]]

z = np.concatenate((x, y), axis=1)
print(z.shape)  # (1, 6)
print(z)
# [[1 2 3 7 8 9]]

# 【例】二维的情况

x = np.array([[1, 2, 3], [4, 5, 6]])
y = np.array([[7, 8, 9], [10, 11, 12]])
z = np.vstack((x, y))
print(z.shape)  # (4, 3)
print(z)
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]

z = np.concatenate((x, y), axis=0)
print(z.shape)  # (4, 3)
print(z)
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]

z = np.hstack((x, y))
print(z.shape)  # (2, 6)
print(z)
# [[ 1  2  3  7  8  9]
#  [ 4  5  6 10 11 12]]

z = np.concatenate((x, y), axis=1)
print(z.shape)  # (2, 6)
print(z)
# [[ 1  2  3  7  8  9]
#  [ 4  5  6 10 11 12]]
```

## 数组拆分

### np.split()
numpy.split(ary, indices_or_sections, axis)：将一个数组沿指定轴分割为多个子数组，是原数组的视图
indices_or_sections:索引或段数  [1, 3] 表示在索引 1 和 3 处进行分割     3表示将数组分割成 3 个子数组


```python
import numpy as np

x = np.array([[11, 12, 13, 14],
              [16, 17, 18, 19],
              [21, 22, 23, 24]])
y = np.split(x, [1, 3])
print(y)
# [array([[11, 12, 13, 14]]), array([[16, 17, 18, 19],
#        [21, 22, 23, 24]]), array([], shape=(0, 4), dtype=int32)]

y = np.split(x, [1, 3], axis=1)# axis=1按列
print(y)
# [array([[11],
#        [16],
#        [21]]), array([[12, 13],
#        [17, 18],
#        [22, 23]]), array([[14],
#        [19],
#        [24]])]
```

### np.vsplit()
numpy.vsplit(ary, indices_or_sections)：将一个数组按行分割为多个子数组
等于numpy.split(ary, indices_or_sections, axis=0)

### np.hsplit()
numpy.hsplit(ary, indices_or_sections)：将一个数组按列分割为多个子数组
等于等于numpy.split(ary, indices_or_sections, axis=1)


```python
import numpy as np

x = np.array([[11, 12, 13, 14],
              [16, 17, 18, 19],
              [21, 22, 23, 24]])
y = np.vsplit(x, 3)
print(y)
# [array([[11, 12, 13, 14]]), array([[16, 17, 18, 19]]), array([[21, 22, 23, 24]])]

y = np.split(x, 3)
print(y)
# [array([[11, 12, 13, 14]]), array([[16, 17, 18, 19]]), array([[21, 22, 23, 24]])]

y=np.hsplit(x,4)
print(y)
# [array([[11],
#        [16],
#        [21]]), array([[12],
#        [17],
#        [22]]), array([[13],
#        [18],
#        [23]]), array([[14],
#        [19],
#        [24]])]
```

## 数组平铺

### np.tile()
numpy.tile(A, reps)：通过将数组 A 按照 reps 指定的次数进行重复，构造一个新的数组  
reps:(1,3)表示在第一个轴（行）上重复 1 次，在第二个轴（列）上重复 3 次  


```python
import numpy as np

x = np.array([[1, 2], [3, 4]])
print(x)
# [[1 2]
#  [3 4]]

y = np.tile(x, (1, 3))
print(y)
# [[1 2 1 2 1 2]
#  [3 4 3 4 3 4]]

y = np.tile(x, (3, 1))
print(y)
# [[1 2]
#  [3 4]
#  [1 2]
#  [3 4]
#  [1 2]
#  [3 4]]

y = np.tile(x, (3, 3))
print(y)
# [[1 2 1 2 1 2]
#  [3 4 3 4 3 4]
#  [1 2 1 2 1 2]
#  [3 4 3 4 3 4]
#  [1 2 1 2 1 2]
#  [3 4 3 4 3 4]]
```

### np.repeat()
numpy.repeat(a, repeats, axis=None) 重复数组中的元素  
repeats，可以为一个数，也可以为一个矩阵 
- 数字表示重复次数
- [2, 3] 表示在对应axis轴上，第一行(列)重复 2 次，第二行(列)重复 3 次
axis=0，沿着y轴复制，实际上增加了行数  
axis=1，沿着x轴复制，实际上增加了列数  
axis=None时就会flatten当前矩阵，实际上就是变成了一个行向量  


```python
x = np.repeat(3, 4)
print(x)  # [3 3 3 3]

x = np.array([[1, 2], [3, 4]])
y = np.repeat(x, 2)
print(y)
# [1 1 2 2 3 3 4 4]

y = np.repeat(x, 2, axis=0)
print(y)
# [[1 2]
#  [1 2]
#  [3 4]
#  [3 4]]

y = np.repeat(x, 2, axis=1)
print(y)
# [[1 1 2 2]
#  [3 3 4 4]]

y = np.repeat(x, [2, 3], axis=0)# [2, 3] 表示在第一个轴（行）上，第一行重复 2 次，第二行重复 3 次
print(y)
# [[1 2]
#  [1 2]
#  [3 4]
#  [3 4]
#  [3 4]]

y = np.repeat(x, [2, 3], axis=1)
print(y)
# [[1 1 2 2 2]
#  [3 3 4 4 4]]

```

## 数组比较

### np.allclose(A, B)
np.allclose 用于比较两个数组的元素是否在指定的容差范围内近似相等。
默认情况下，np.allclose 的相对容差为 1e-05，绝对容差为 1e-08。

### np.array_equal(A, B)
np.array_equal 用于检查两个数组的形状和元素是否完全相同。
这里的比较是严格的，不允许有任何容差


```python
A = np.array([1,2,3])
B = np.array([1,2,3])

equal = np.allclose(A,B)
print(equal)
# True
equal = np.array_equal(A,B)
print(equal)
# True
```

## 添加和删除元素

### np.unique
numpy.unique(arr, return_index=False, return_inverse=False, return_counts=False, axis=None)：查找数组中的唯一元素   
return_index：返回输入数组中唯一值对应的索引  
return_inverse：返回用于重构输入数组的唯一数组的索引  
return_counts：返回每个唯一值在输入数组中出现的次数  
axis：指定沿着哪个轴查找唯一元素（如果未指定，则查找展平后的数组中的唯一元素）  


```python
# 查找只出现一次的唯一值
a=np.array([1,1,2,3,3,4,4])
b=np.unique(a,return_counts=True)
print(b)
# (array([1, 2, 3, 4]), array([2, 1, 2, 2]))
print(b[0][list(b[1]).index(1)])
# 2
```

# 逻辑函数*

### np.all()
### np.any()
numpy.all(a, axis=None, out=None, keepdims=np._NoValue)  
测试沿指定轴的所有数组元素是否都评估为 True  
numpy.any(a, axis=None, out=None, keepdims=np._NoValue)  
测试沿指定轴的数组元素中是否有任意一个评估为 True   


```python
a = np.array([0, 4, 5])
b = np.copy(a)
print(np.all(a == b))  # True
print(np.any(a == b))  # True

b[0] = 1
print(np.all(a == b))  # False
print(np.any(a == b))  # True

print(np.all([1.0, np.nan]))  # True
print(np.any([1.0, np.nan]))  # True
```

### np.isnan()
numpy.isnan(x, *args, **kwargs)
按元素检查是否为 NaN（非数字），并以布尔数组的形式返回结果

### np.logical_not()
### np.logical_and()
### np.logical_or()
### np.logical_xor()
异或


```python
print(np.logical_not(3))  
# False
print(np.logical_not([True, False, 0, 1]))
# [False  True  True False]

print(np.logical_or(True, False))
# True
print(np.logical_and([True, False], [True, False]))# 对两个数组的对应元素执行逻辑操作。它逐元素比较两个数组，并返回一个新的布尔数组
# [ True False]
print(np.logical_xor([True, True, False, False], [True, False, True, False]))
# [False  True  True False]

x = np.arange(5)
print(np.logical_and(x > 1, x < 4))
# [False False  True  True False]
```

### np.greater()
### np.greater_equal()
### np.equal()
### np.not_equal()
### np.less()
### np.less_equal()
np.greater      (x1, x2, *args, **kwargs)            按元素返回 (x1 > x2) 的真值  
np.greater_equal(x1, x2, *args, **kwargs)                      (x1 >= x2)  
np.equal        (x1, x2, *args, **kwargs)                      (x1 == x2)  
np.not_equal    (x1, x2, *args, **kwargs)                      (x1 != x2)  
np.less         (x1, x2, *args, **kwargs)                      (x1 < x2)  
np.less_equal   (x1, x2, *args, **kwargs)                      (x1 <= x2)  


```python
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])

y = x > 2
print(y)
print(np.greater(x, 2))
# [False False  True  True  True  True  True  True]

x = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28, 29, 30],
              [31, 32, 33, 34, 35]])
y = x > 20
print(y)
print(np.greater(x, 20))
# [[False False False False False]
#  [False False False False False]
#  [ True  True  True  True  True]
#  [ True  True  True  True  True]
#  [ True  True  True  True  True]]

y = np.array([[32,28,31,33,37]
              [23,37,37,30,29]
              [32,24,10,33,15]
              [27,17,10,36,16]
              [25,32,23,39,34]])
z = x > y
print(z)
print(np.greater(x, y))
# [[False False False False False]
#  [False False False False False]
#  [False False  True False  True]
#  [False  True  True False  True]
#  [ True False  True False  True]]
```


```python
#注意 numpy 的广播规则
x = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28, 29, 30],
              [31, 32, 33, 34, 35]])
y=np.array([32,37,30,24,10])
# y 的形状为 (5,)，会被视为 (1, 5)，然后进一步扩展为 (5, 5)，以便与 x 的形状匹配
# y 被广播为：
# [[32, 37, 30, 24, 10],
#  [32, 37, 30, 24, 10],
#  [32, 37, 30, 24, 10],
#  [32, 37, 30, 24, 10],
#  [32, 37, 30, 24, 10]]
# 然后，x 和广播后的 y 进行逐元素比较
z = x > y
print(z)
print(np.greater(x, y))
# [[False False False False  True]
#  [False False False False  True]
#  [False False False False  True]
#  [False False False  True  True]
#  [False False  True  True  True]]

```

### np.isclose
numpy.isclose(a, b, rtol=1.e-5, atol=1.e-8, equal_nan=False) 返回一个布尔数组，其中两个数组在给定的容差范围内逐元素比较是否相等   
a, b: 要比较的两个数组  
rtol: 相对容差（relative tolerance），默认值为 1.e-5  
atol: 绝对容差（absolute tolerance），默认值为 1.e-8  
equal_nan: 如果为 True，则认为 NaN 值是相等的；默认为 False  
### np.allclose
numpy.allclose(a, b, rtol=1.e-5, atol=1.e-8, equal_nan=False) 如果两个数组在给定的容差范围内逐元素比较均相等，则返回 True   
等价于 numpy.all(isclose(a, b, rtol=rtol, atol=atol, equal_nan=equal_nan))  


```python
# 比较两个数组是否可以认为相等
import numpy as np

x = np.isclose([1e10, 1e-7], [1.00001e10, 1e-8])
print(x)  # [ True False]

x = np.allclose([1e10, 1e-7], [1.00001e10, 1e-8])
print(x)  # False

x = np.isclose([1e10, 1e-8], [1.00001e10, 1e-9])
print(x)  # [ True  True]

x = np.allclose([1e10, 1e-8], [1.00001e10, 1e-9])
print(x)  # True

x = np.isclose([1.0, np.nan], [1.0, np.nan])
print(x)  # [ True False]

x = np.allclose([1.0, np.nan], [1.0, np.nan])
print(x)  # False

x = np.isclose([1.0, np.nan], [1.0, np.nan], equal_nan=True)
print(x)  # [ True  True]

x = np.allclose([1.0, np.nan], [1.0, np.nan], equal_nan=True)
print(x)  # True
```

## np.where()


```python
# 获取a和b元素匹配的位置
a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
mask=np.equal(a,b) 
print(np.where(mask)) # np.where(mask) 返回一个元组，其中包含 mask 中值为 True 的索引

# 获取5到10 之间的所有元素
a = np.array([2, 6, 1, 9, 10, 3, 27])
mask=np.logical_and(np.less_equal(a,10),np.greater_equal(a,5))
print(np.where(mask)) #对应的索引
x = np.where(mask)
print(a[x])  # [ 6  9 10]
```

    (array([1, 3, 5, 7]),)
    (array([1, 3, 4]),)
    [ 6  9 10]
    

# 数学函数

## 向量化和广播
有了向量化，编写代码时无需使用显式循环。这些循环实际上不能省略，只不过是在内部实现，被代码中的其他结构代替  
向量化的应用使得代码更简洁，可读性更强    
  
广播机制描述了 numpy 如何在算术运算期间处理具有不同形状的数组，让较小的数组在较大的数组上“广播”，以便它们具有兼容的形状  
并不是所有的维度都要彼此兼容才符合广播机制的要求，但它们必须满足一定的条件  
若两个数组的各维度兼容，也就是两个数组的每一维等长，或其中一个数组为 一维，那么广播机制就适用。如果这两个条件不满足，numpy就会抛出异常，说两个数组不兼容  

总结来说，广播的规则有三个：  
如果两个数组的维度数dim不相同，那么小维度数组的形状将会在左边补1  
如果shape维度不匹配，但是有维度是1，那么可以扩展维度是1的维度匹配另一个数组  
如果shape维度不匹配，但是没有任何一个维度是1，则匹配引发错误  


```python
import numpy as np

x = np.arange(4).reshape(4, 1)
y = np.ones(5)

print(x.shape)  # (4, 1)
# [[0.]
#  [1.]
#  [2.]
#  [3.]]
print(y.shape)  # (5,)
# [1. 1. 1. 1. 1.]

print((x + y).shape)  # (4, 5)
# x:
# [[0. 0. 0. 0. 0.]
#  [1. 1. 1. 1. 1.]
#  [2. 2. 2. 2. 2.]
#  [3. 3. 3. 3. 3.]]
# y:
# [[1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]]

print(x + y)
# [[1. 1. 1. 1. 1.]
#  [2. 2. 2. 2. 2.]
#  [3. 3. 3. 3. 3.]
#  [4. 4. 4. 4. 4.]]

# 不匹配报错的例子

x = np.arange(4)
y = np.ones(5)

print(x.shape)  # (4,)
print(y.shape)  # (5,)

print(x + y)
# ValueError: operands could not be broadcast together with shapes (4,) (5,) 
```

## 算数运算

### np.add()
numpy.add(x1, x2, *args, **kwargs)
### np.subtract()
### np.multiply()
### np.divide()
### np.floor_divide()
按元素逐一执行向下取整除法
### np.power() 幂次
将第一个数组的元素逐一提升到第二个数组中对应元素的幂次(按元素逐一计算幂)


```python
import numpy as np
# 一维数组
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = x / 2
print(y)
print(np.divide(x, 2))
# [0.5 1.  1.5 2.  2.5 3.  3.5 4. ]

y = x ** 2
print(y)
print(np.power(x, 2))
# [ 1  4  9 16 25 36 49 64]

#二维数组
x = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28, 29, 30],
              [31, 32, 33, 34, 35]])
y = x // 2
print(y)
print(np.floor_divide(x, 2))
# [[ 5  6  6  7  7]
#  [ 8  8  9  9 10]
#  [10 11 11 12 12]
#  [13 13 14 14 15]
#  [15 16 16 17 17]]

#一维与二维
y = np.arange(1, 6)
print(y)
# [1 2 3 4 5]

z = x + y
print(z)
print(np.add(x, y))
# [[12 14 16 18 20]
#  [17 19 21 23 25]
#  [22 24 26 28 30]
#  [27 29 31 33 35]
#  [32 34 36 38 40]]

#二维与二维
y = np.arange(1, 26).reshape([5, 5])
print(y)
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]
#  [11 12 13 14 15]
#  [16 17 18 19 20]
#  [21 22 23 24 25]]

z = x - y
print(z)
print(np.subtract(x, y))
# [[10 10 10 10 10]
#  [10 10 10 10 10]
#  [10 10 10 10 10]
#  [10 10 10 10 10]
#  [10 10 10 10 10]]
```

### np.sqrt() 开根号
numpy.sqrt(x, *args, **kwargs) 返回数组中每个元素的非负平方根（逐元素计算）。
### np.square() 平方
numpy.square() 返回输入数组中每个元素的平方（逐元素计算）


```python
import numpy as np

x = np.arange(1, 5)
print(x)  # [1 2 3 4]

y = np.sqrt(x)
print(y)
# [1.         1.41421356 1.73205081 2.        ]
print(np.power(x, 0.5))
# [1.         1.41421356 1.73205081 2.        ]

y = np.square(x)
print(y)
# [ 1  4  9 16]
print(np.power(x, 2))
# [ 1  4  9 16]
```

## 三角函数

### np.sin()
### np.cos()
### np.tan()
### np.arcsin()
### np.arccos()
### np.arctan()


```python
import numpy as np

x = np.linspace(start=0, stop=np.pi*2, num=5)
print(x)
# [0.         1.57079633 3.14159265 4.71238898 6.28318531] 即0,pi/2,pi,2pi/3,2*pi

y = np.sin(x)
print(y)
# [ 0.0000000e+00  1.0000000e+00  1.2246468e-16 -1.0000000e+00
#  -2.4492936e-16]
```

## 指数和对数

### np.exp()
### np.log() 
e为底，即ln()
### np.exp2()
每个元素的 2 的 n 次方
### np.log2()
### np.log10()


```python
import numpy as np

x = np.arange(1, 5)
print(x)
# [1 2 3 4]
y = np.exp(x)
print(y)
# [ 2.71828183  7.3890561  20.08553692 54.59815003]
z = np.log(y)
print(z)
# [1. 2. 3. 4.]
```

## 加法函数、乘法函数

### np.sum() 求和
numpy.sum(a[, axis=None, dtype=None, out=None, …])   
通过不同的 axis，numpy 会沿着不同的方向进行操作：如果不设置，那么对所有的元素操作；如果axis=0，则沿着纵轴进行操作；axis=1，则沿着横轴进行操作。axis=i，则 numpy 沿着第i个下标变化的方向进行操作  
### np.cumsum() 累和
numpy.cumsum(a, axis=None, dtype=None, out=None) 返回沿着给定轴的元素的累积和   


```python
import numpy as np

x = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28, 29, 30],
              [31, 32, 33, 34, 35]])
y = np.sum(x)
print(y)  # 575

y = np.sum(x, axis=0)
print(y)  # [105 110 115 120 125]

y = np.sum(x, axis=1)
print(y)  # [ 65  90 115 140 165]

###############################################################
y = np.cumsum(x)
print(y)
# [ 11  23  36  50  65  81  98 116 135 155 176 198 221 245 270 296 323 351
#  380 410 441 473 506 540 575] 从数组的第一个元素开始，依次累加每个元素的值，生成一个新的数组

y = np.cumsum(x, axis=0)
print(y)
# [[ 11  12  13  14  15]
#  [ 27  29  31  33  35]
#  [ 48  51  54  57  60]
#  [ 74  78  82  86  90]
#  [105 110 115 120 125]] 以列累加，生成一个新的数组

y = np.cumsum(x, axis=1)
print(y)
# [[ 11  23  36  50  65]
#  [ 16  33  51  70  90]
#  [ 21  43  66  90 115]
#  [ 26  53  81 110 140]
#  [ 31  63  96 130 165]] 以行累加，生成一个新的数组
```

### np.prod() 求积
numpy.prod(a[, axis=None, dtype=None, out=None, …]) 返回沿着给定轴的数组元素的乘积。

### np.cumprod() 累积
numpy.cumprod(a, axis=None, dtype=None, out=None) 返回沿着给定轴的元素的累积乘积。


```python
import numpy as np

x = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28, 29, 30],
              [31, 32, 33, 34, 35]])
y = np.prod(x)
print(y)  # 788529152

y = np.prod(x, axis=0)
print(y)
# [2978976 3877632 4972968 6294624 7875000]

y = np.prod(x, axis=1)
print(y)
# [  360360  1860480  6375600 17100720 38955840]

###############################################################
y = np.cumprod(x)
print(y)
# [         11         132        1716       24024      360360     5765760
#     98017920  1764322560  -837609728   427674624   391232512    17180672
#    395155456   893796352   870072320  1147043840   905412608  -418250752
#    755630080  1194065920 -1638662144  -897581056   444596224 -2063597568
#    788529152]

y = np.cumprod(x, axis=0)
print(y)
# [[     11      12      13      14      15]
#  [    176     204     234     266     300]
#  [   3696    4488    5382    6384    7500]
#  [  96096  121176  150696  185136  225000]
#  [2978976 3877632 4972968 6294624 7875000]]

y = np.cumprod(x, axis=1)
print(y)
# [[      11      132     1716    24024   360360]
#  [      16      272     4896    93024  1860480]
#  [      21      462    10626   255024  6375600]
#  [      26      702    19656   570024 17100720]
#  [      31      992    32736  1113024 38955840]]
```

### np.diff() 差值
`numpy.diff(a, n=1, axis=-1, prepend=np._NoValue, append=np._NoValue)` 计算沿着给定轴的 `n` 阶离散差分。

- **a**：输入矩阵
- **n**：可选参数，代表要执行几次差分操作
- **axis**：默认是最后一个轴（维度）

**计算方式**：
- 一阶差分由公式 `out[i] = a[i+1] - a[i]` 沿着给定轴计算得出。
- 高阶差分通过递归地使用 `diff` 函数进行计算。


```python
import numpy as np

A = np.arange(2, 14).reshape((3, 4))
A[1, 1] = 8
print(A)
# [[ 2  3  4  5]
#  [ 6  8  8  9]
#  [10 11 12 13]]
print(np.diff(A))
# [[1 1 1]
#  [2 0 1]
#  [1 1 1]]
print(np.diff(A, axis=0))
# [[4 5 4 4]
#  [4 3 4 4]]
```


```python
# 在一维数组中找到所有的局部极大值（或峰值）
import numpy as np

a = np.array([1, 3, 7, 1, 2, 6, 0, 1])
b1 = np.diff(a)
# [ 2  4 -6  1  4 -6  1]
b2 = np.sign(b1)
# [ 1  1 -1  1  1 -1  1]
b3 = np.diff(b2)
# [ 0 -2  2  0 -2  2] 

index = np.where(np.equal(b3, -2))[0] + 1

print(index) # [2 5]
```

## 四舍五入

### np.around() 舍入
`numpy.around(a, decimals=0, out=None)` 将数组中的元素舍入到指定的小数位数。

- **a**：输入数组
- **decimals**：可选参数，指定要保留的小数位数，默认为 0
- **out**：可选参数，用于指定输出数组


```python
import numpy as np

x = np.random.rand(3, 3) * 10
print(x)
# [[6.59144457 3.78566113 8.15321227]
#  [1.68241475 3.78753332 7.68886328]
#  [2.84255822 9.58106727 7.86678037]]

y = np.around(x)
print(y)
# [[ 7.  4.  8.]
#  [ 2.  4.  8.]
#  [ 3. 10.  8.]]

y = np.around(x, decimals=2)
print(y)
# [[6.59 3.79 8.15]
#  [1.68 3.79 7.69]
#  [2.84 9.58 7.87]]
```

### np.ceil() 上限
`numpy.ceil(x, *args, **kwargs)` 逐元素地返回输入值的向上取整

- **x**：输入数组

### np.floor() 下限
`numpy.floor(x, *args, **kwargs)` 逐元素地返回输入值的向下取整

- **x**：输入数组


```python
import numpy as np

x = np.random.rand(3, 3) * 10
print(x)
# [[0.67847795 1.33073923 4.53920122]
#  [7.55724676 5.88854047 2.65502046]
#  [8.67640444 8.80110812 5.97528726]]

y = np.ceil(x)
print(y)
# [[1. 2. 5.]
#  [8. 6. 3.]
#  [9. 9. 6.]]

y = np.floor(x)
print(y)
# [[0. 1. 4.]
#  [7. 5. 2.]
#  [8. 8. 5.]]
```

## 杂项

### np.clip() 裁剪
`numpy.clip(a, a_min, a_max, out=None, **kwargs)`：裁剪（限制）数组中的值。
- 给定一个区间 `[a_min, a_max]`，将数组中不在该区间内的值裁剪到区间的边缘。例如，如果指定区间为 `[0, 1]`，则小于 0 的值会被裁剪为 0，大于 1 的值会被裁剪为 1。
- **a**：输入数组
- **a_min**：裁剪的下限值
- **a_max**：裁剪的上限值
- **out**：可选参数，用于指定输出数组


```python
import numpy as np

x = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28, 29, 30],
              [31, 32, 33, 34, 35]])
y = np.clip(x, a_min=20, a_max=30)
print(y)
# [[20 20 20 20 20]
#  [20 20 20 20 20]
#  [21 22 23 24 25]
#  [26 27 28 29 30]
#  [30 30 30 30 30]]
```

### np.abs() 绝对值
`numpy.absolute(x, *args, **kwargs)`：逐元素地计算绝对值。

- **x**：输入数组


```python
import numpy as np

x = np.arange(-5, 5)
print(x)
# [-5 -4 -3 -2 -1  0  1  2  3  4]

y = np.abs(x)
print(y)
# [5 4 3 2 1 0 1 2 3 4]

y = np.absolute(x)
print(y)
# [5 4 3 2 1 0 1 2 3 4]
```

### np.sign() 返回数字符号的逐元素指示
`numpy.sign(x, *args, **kwargs)`：逐元素地返回数字的符号指示。

- **x**：输入数组

- 对于数组中的每个元素，返回其符号指示：
  - 如果元素为正数，则返回 `1`
  - 如果元素为零，则返回 `0`
  - 如果元素为负数，则返回 `-1`


```python
x = np.arange(-5, 5)
print(x)
#[-5 -4 -3 -2 -1  0  1  2  3  4]
print(np.sign(x))
#[-1 -1 -1 -1 -1  0  1  1  1  1]
```

### 平均,中位,方差,标准差
### 相关性矩阵,协方差矩阵


```python
import numpy as np
arr1 = np.random.randint(1,10,10)
arr2 = np.random.randint(1,10,10)

print(f"arr1的平均数为:{np.mean(arr1)}")
print(f"arr1的中位数为:{np.median(arr1)}" )
print(f"arr1的方差为:{np.var(arr1)}" )
print(f"arr1的标准差为:{np.std(arr1)}" )
print(f"arr1,arr的相关性矩阵为:{np.cov(arr1,arr2)}" )
print(f"arr1,arr的协方差矩阵为:{np.corrcoef(arr1,arr2)}" )
```

# 排序，搜索和计数*

## 排序

### np.sort()
numpy.sort(a[, axis=-1, kind='quicksort', order=None])   

axis：方向，0表示按列，1表示按行，None表示展开来排序，默认为-1，表示沿最后的轴排序  

kind：算法，快排'quicksort'、混排'mergesort'、堆排'heapsort'， 默认为‘quicksort'  

order：排序的字段名，可指定字段排序，默认为None  


```python
import numpy as np

np.random.seed(20200612) # 设置随机数生成器的种子，保证每次运行代码时生成的随机数是相同的
x = np.random.rand(5, 5) * 10
x = np.around(x, 2)
print(x)
# [[2.32 7.54 9.78 1.73 6.22]
#  [6.93 5.17 9.28 9.76 8.25]
#  [0.01 4.23 0.19 1.73 9.27]
#  [7.99 4.97 0.88 7.32 4.29]
#  [9.05 0.07 8.95 7.9  6.99]]

y = np.sort(x)
print(y)
# [[1.73 2.32 6.22 7.54 9.78]
#  [5.17 6.93 8.25 9.28 9.76]
#  [0.01 0.19 1.73 4.23 9.27]
#  [0.88 4.29 4.97 7.32 7.99]
#  [0.07 6.99 7.9  8.95 9.05]]

y = np.sort(x, axis=0)
print(y)
# [[0.01 0.07 0.19 1.73 4.29]
#  [2.32 4.23 0.88 1.73 6.22]
#  [6.93 4.97 8.95 7.32 6.99]
#  [7.99 5.17 9.28 7.9  8.25]
#  [9.05 7.54 9.78 9.76 9.27]]

y = np.sort(x, axis=1)
print(y)
# 同y = np.sort(x)


dt = np.dtype([('name', 'S10'), ('age', np.int)])
a = np.array([("Mike", 21), ("Nancy", 25), ("Bob", 17), ("Jane", 27)], dtype=dt)
b = np.sort(a, order='name')
print(b)
# [(b'Bob', 17) (b'Jane', 27) (b'Mike', 21) (b'Nancy', 25)]

b = np.sort(a, order='age')
print(b)
# [(b'Bob', 17) (b'Mike', 21) (b'Nancy', 25) (b'Jane', 27)]
```

### np.argsort()
   
numpy.argsort(a[, axis=-1, kind='quicksort', order=None]) 返回能够对数组进行排序的索引


```python
import numpy as np
## 一维
np.random.seed(20200612)
x = np.random.randint(0, 10, 10) # 生成整数随机数(0-9的随机10个整数)([low,high),size)
print(x)
# [6 1 8 5 5 4 1 2 9 1]

y = np.argsort(-x)
print(y)
# [8 2 0 3 4 5 7 1 6 9]

print(x[y])
# [9 8 6 5 5 4 2 1 1 1]

## 二维
x = np.random.rand(5, 5) * 10
x = np.around(x, 2)
print(x)
# [[2.32 7.54 9.78 1.73 6.22]
#  [6.93 5.17 9.28 9.76 8.25]
#  [0.01 4.23 0.19 1.73 9.27]
#  [7.99 4.97 0.88 7.32 4.29]
#  [9.05 0.07 8.95 7.9  6.99]]

y = np.argsort(x)
print(y)
# [[3 0 4 1 2]
#  [1 0 4 2 3]
#  [0 2 3 1 4]
#  [2 4 1 3 0]
#  [1 4 3 2 0]]

y = np.argsort(x, axis=0)
print(y)
# [[2 4 2 0 3]
#  [0 2 3 2 0]
#  [1 3 4 3 4]
#  [3 1 1 4 1]
#  [4 0 0 1 2]]

y = np.argsort(x, axis=1)
print(y)
# 同y = np.argsort(x)

# 根据第二列排序
Z = np.random.randint(0,10,(3,3))
print(Z)
print (Z[Z[:,2].argsort()])
```

### np.lexsort()
numpy.lexsort(keys[, axis=-1])     
注意顺序：**先次键，再主键**  最后一个键是主键  
首先根据**主键**排序，然后在**主值相同**的情况下根据**次键**排序   
它返回一个索引数组  


```python
import numpy as np
np.random.seed(20200612)
x = np.random.rand(5, 5) * 10
x = np.around(x, 2)
print(x)
# [[2.32 7.54 9.78 1.73 6.22]
#  [6.93 5.17 9.28 9.76 8.25]
#  [0.01 4.23 0.19 1.73 9.27]
#  [7.99 4.97 0.88 7.32 4.29]
#  [9.05 0.07 8.95 7.9  6.99]]

## 一个键
index = np.lexsort([x[:, 0]]) # 按照第一列(即索引为 0 的列)进行排序
print(index)
# [2 0 1 3 4]
y = x[index]
print(y)
# [[0.01 4.23 0.19 1.73 9.27]
#  [2.32 7.54 9.78 1.73 6.22]
#  [6.93 5.17 9.28 9.76 8.25]
#  [7.99 4.97 0.88 7.32 4.29]
#  [9.05 0.07 8.95 7.9  6.99]]

##降序
index = np.lexsort([-1 * x[:, 0]])
print(index)
# [4 3 1 0 2]
y = x[index]
print(y)
# [[9.05 0.07 8.95 7.9  6.99]
#  [7.99 4.97 0.88 7.32 4.29]
#  [6.93 5.17 9.28 9.76 8.25]
#  [2.32 7.54 9.78 1.73 6.22]
#  [0.01 4.23 0.19 1.73 9.27]]

###########################################

## 主键与次键
x=np.array([[1,2,3,4],[1,4,3,3]])
y=np.lexsort((x[0,:],x[1,:])) # 按照第二行进行排序(即索引为 1 的行),若相同,再按照第一行(即索引为 0 的行)进行排序
print(y)
print(x[:,y])

```

### np.partition()

`numpy.partition(a, kth, axis=-1, kind='introselect', order=None)`  

创建一个数组的副本，并将其元素重新排列    
例如kth=2：前三个最小的排前面   kth=-2:前两个最大的排后面  (不一定有序)  

---
- **`a`**：输入数组。
- **`kth`**：指定分区的位置（可以是单个整数或整数序列）
- **`axis`**：沿哪个轴进行分区，默认是最后一个轴（`-1`）
- **`kind`**：分区算法的实现方式，默认是 `'introselect'`
- **`order`**：如果数组是结构化数组，指定按照哪些字段进行排序
---
不会对数组进行完全排序，而是仅确保第 `k` 个位置的元素处于它在完全排序数组中的正确位置，同时将小于它的元素放在前面，大于或等于它的元素放在后面  
这种操作比完全排序更快，适合需要快速找到第 `k` 小（或第 `k` 大）元素的场景  


```python
import numpy as np

np.random.seed(100)
x = np.random.randint(1, 30, [8, 3]) # [1-30)的8*3的二维整数数组
print(x)
# [[ 9 25  4]
#  [ 8 24 16]
#  [17 11 21]
#  [ 3 22  3]
#  [ 3 15  3]
#  [18 17 25]
#  [16  5 12]
#  [29 27 17]]

z = np.partition(x, kth=2, axis=0) # 对于每一列，将第 kth=2 小的元素移动到该列的前 kth 个位置（包括第 kth 个位置本身），而较大的元素移动到后面。
print(z)
# [[ 3  5  3]
#  [ 3 11  3]
#  [ 8 15  4]
#  [ 9 22 21]
#  [17 24 16]
#  [18 17 25]
#  [16 25 12]
#  [29 27 17]]

# 【例】选取每一列第三小的数
z = np.partition(x, kth=2, axis=0)
print(z[2])
# [ 8 15  4]

# 【例】选取每一列第三大的数据
z = np.partition(x, kth=-3, axis=0)
print(z[-3])
# [17 24 17]
```

### np.argpartition()
numpy.argpartition(a, kth, axis=-1, kind='introselect', order=None)  

## 搜索

### np.argmax()
numpy.argmax(a[, axis=None, out=None])  
返回沿指定轴的最大值的索引  
如果未指定 axis，则返回整个数组展平后最大值的索引  


```python
import numpy as np

np.random.seed(20200612)
x = np.random.rand(5, 5) * 10
x = np.around(x, 2)
print(x)
# [[2.32 7.54 9.78 1.73 6.22]
#  [6.93 5.17 9.28 9.76 8.25]
#  [0.01 4.23 0.19 1.73 9.27]
#  [7.99 4.97 0.88 7.32 4.29]
#  [9.05 0.07 8.95 7.9  6.99]]

y = np.argmax(x)
print(y)  # 2

y = np.argmax(x, axis=0)
print(y)
# [4 0 0 1 2]

y = np.argmax(x, axis=1)
print(y)
# [2 3 4 0 0]
```

### np.argmin()
numpy.argmin(a[, axis=None, out=None])  

### np.nonzero()
numpy.nonzero(a)
返回数组中非零元素的索引

1. 只有a中非零元素才会有索引值，那些零值元素没有索引值  
2. 返回一个长度为a.ndim的元组，元组的每个元素都是一个整数数组
3. 每一个array均是从一个维度上来描述其索引值。比如，如果a是一个二维数组，则tuple包含两个array，第一个array从行维度来描述索引值；第二个array从列维度来描述索引值  
4. 该 np.transpose(np.nonzero(x)) 函数能够描述出每一个非零元素在不同维度的索引值  
5. 通过a[nonzero(a)]得到所有a中的非零值  


```python
# 一维数组
import numpy as np

x = np.array([0, 2, 3])
print(x)  # [0 2 3]
print(x.shape)  # (3,)
print(x.ndim)  # 1

y = np.nonzero(x)
print(y)  # (array([1, 2], dtype=int64),)
print(np.array(y))  # [[1 2]]
print(np.array(y).shape)  # (1, 2)
print(np.array(y).ndim)  # 2
print(np.transpose(y))
# [[1]
#  [2]]
print(x[np.nonzero(x)])
#[2, 3]

#########################################
# 二维数组

x = np.array([[3, 0, 0], [0, 4, 0], [5, 6, 0]])
print(x)
# [[3 0 0]
#  [0 4 0]
#  [5 6 0]]
print(x.shape)  # (3, 3)
print(x.ndim)  # 2

y = np.nonzero(x)
print(y) # (array([0, 1, 2, 2], dtype=int64), array([0, 1, 0, 1], dtype=int64))
print(np.array(y))
# [[0 1 2 2]
#  [0 1 0 1]] 即索引[0,0][1,1][2,0][2,1]
print(np.array(y).shape)  # (2, 4)
print(np.array(y).ndim)  # 2

y = x[np.nonzero(x)]
print(y)  # [3 4 5 6]

y = np.transpose(np.nonzero(x))
print(y)
# [[0 0]
#  [1 1]
#  [2 0]
#  [2 1]] 即索引[0,0][1,1][2,0][2,1]
#########################################
# 三维数组

x = np.array([[[0, 1], [1, 0]], [[0, 1], [1, 0]], [[0, 0], [1, 0]]])
print(x)
# [[[0 1]
#   [1 0]]
#
#  [[0 1]
#   [1 0]]
#
#  [[0 0]
#   [1 0]]]
print(np.shape(x))  # (3, 2, 2)
print(x.ndim)  # 3

y = np.nonzero(x)
print(np.array(y))
# [[0 0 1 1 2]
#  [0 1 0 1 1]
#  [1 0 1 0 0]]
print(np.array(y).shape)  # (3, 5)
print(np.array(y).ndim)  # 2
print(y)
# (array([0, 0, 1, 1, 2], dtype=int64), array([0, 1, 0, 1, 1], dtype=int64), array([1, 0, 1, 0, 0], dtype=int64))
print(x[np.nonzero(x)])
#[1 1 1 1 1]
```


```python
# nonzero()将布尔数组转换成整数数组进行操作

import numpy as np

x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(x)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

y = x > 3
print(y)
# [[False False False]
#  [ True  True  True]
#  [ True  True  True]]

y = np.nonzero(x > 3)
print(y)
# (array([1, 1, 1, 2, 2, 2], dtype=int64), array([0, 1, 2, 0, 1, 2], dtype=int64))

y = x[np.nonzero(x > 3)]
print(y)
# [4 5 6 7 8 9]

y = x[x > 3]
print(y)
# [4 5 6 7 8 9]
```

### np.where()
numpy.where(condition, [x=None, y=None])  
根据条件 condition，从 x 或 y 中选择元素并返回  


```python
# 满足条件condition，输出x，不满足输出y
import numpy as np

x = np.array([[0, 1, 2],
              [0, 2, 4],
              [0, 3, 6]])
y = np.where(x < 4, x, -1) # 不满足输出-1
print(y)
# [[ 0  1  2]
#  [ 0  2 -1]
#  [ 0  3 -1]]

# 提取所有奇数
index = np.where(x % 2 == 1) # 这里返回索引
print(x[index])
# [1 3]

#####################################################################################################
# 只有condition，没有x和y，则输出满足条件 (即非0) 元素的坐标 (等价于numpy.nonzero)
# 这里的坐标以tuple的形式给出，通常原数组有多少维，输出的tuple中就包含几个数组，分别对应符合条件元素的各维坐标
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.where(x > 5)
print(y)
# (array([5, 6, 7], dtype=int64),)
print(x[y])
# [6 7 8]

y = np.nonzero(x > 5)
print(y)
# (array([5, 6, 7], dtype=int64),)
print(x[y])
# [6 7 8]
```

### np.searchsorted()

`numpy.searchsorted(a, v[, side='left', sorter=None])`  
查找元素应插入的位置索引，以保持数组的顺序。

**参数说明**：  
- **`a`**：一维输入数组    
  - `a` 必须为升序数组    
  - 否则，`sorter` 不能为空，它存放 `a` 中元素的索引，用于反映 `a` 数组的升序排列方式   
- **`v`**：需要插入到 `a` 数组中的值，可以是单个元素、列表（`list`）或 NumPy 数组（`ndarray`）    
- **`side`**：查询方向    
  - 当为 `'left'` 时，将返回第一个符合条件的元素的下标    
  - 当为 `'right'` 时，将返回最后一个符合条件的元素的下标    
- **`sorter`**：一维数组，存放 `a` 数组元素的索引，索引对应的元素为升序排列  


```python
import numpy as np

x = np.array([0, 1, 5, 9, 11, 18, 26, 33]) # 必须为升序，否则sorter不应为空

y = np.searchsorted(x, 11)# 返回应该插入位置的索引
print(y)  # 4

y = np.searchsorted(x, 11, side='right')# 插入位置尽可能靠右，适用数组有相同值
print(y)  # 5

##########################################################################
y = np.searchsorted(x, [-1, 0, 11, 15, 33, 35])
print(y)  # [0 0 4 5 7 8]

y = np.searchsorted(x, [-1, 0, 11, 15, 33, 35], side='right')
print(y)  # [0 1 5 5 8 8]

##########################################################################
# sorter不为空的情况：sorter一维数组，对应数组元素的升序索引
np.random.shuffle(x) # 对x随机打乱
print(x)  # [33  1  9 18 11 26  0  5]

x_sort = np.argsort(x)
print(x_sort)  # [6 1 7 2 4 3 5 0]

y = np.searchsorted(x, [-1, 0, 11, 15, 33, 35], sorter=x_sort)
print(y)  # [0 0 4 5 7 8]

y = np.searchsorted(x, [-1, 0, 11, 15, 33, 35], side='right', sorter=x_sort)
print(y)  # [0 1 5 5 8 8]

```

## 计数

### np.count_nonzero()
numpy.count_nonzero(a, axis=None)
统计数组 a 中非零值的数量


```python
import numpy as np

x = np.count_nonzero([[0, 1, 7, 0, 0], [3, 0, 0, 2, 19]])
print(x)  # 5

x = np.count_nonzero([[0, 1, 7, 0, 0], [3, 0, 0, 2, 19]], axis=0)
print(x)  # [1 1 1 1 1]

x = np.count_nonzero([[0, 1, 7, 0, 0], [3, 0, 0, 2, 19]], axis=1)
print(x)  # [2 3]
```

# 集合操作

### np.unique() 构造集合
numpy.unique(ar, return_index=False, return_inverse=False, return_counts=False, axis=None) 
return_index=True 表示返回新列表元素在旧列表中的位置。
return_inverse=True表示返回旧列表元素在新列表中的位置。
return_counts=True表示返回新列表元素在旧列表中出现的次数


```python
# 找出数组中的唯一值并返回已排序的结果

import numpy as np

x = np.unique([1, 1, 3, 2, 3, 3])
print(x)  # [1 2 3]

x = sorted(set([1, 1, 3, 2, 3, 3])) # set() 转换为集合,将列表 [1, 1, 3, 2, 3, 3] 转换为集合时，重复的元素会被移除
print(x)  # [1, 2, 3]

x = np.array([[1, 1], [2, 3]])
u = np.unique(x)
print(u)  # [1 2 3]

x = np.array([[1, 0, 0], [1, 0, 0], [2, 3, 4]])
y = np.unique(x, axis=0) # 去除重复行
print(y)
# [[1 0 0]
#  [2 3 4]]

x = np.array(['a', 'b', 'b', 'c', 'a'])
u, index = np.unique(x, return_index=True)
print(u)  # ['a' 'b' 'c']
print(index)  # [0 1 3]
print(x[index])  # ['a' 'b' 'c']

x = np.array([1, 2, 6, 4, 2, 3, 2])
u, index = np.unique(x, return_inverse=True)
print(u)  # [1 2 3 4 6]
print(index)  # [0 1 4 3 1 2 1]
print(u[index])  # [1 2 6 4 2 3 2]

u, count = np.unique(x, return_counts=True)
print(u)  # [1 2 3 4 6]
print(count)  # [1 3 1 1 1]
```

### np.in1d() 布尔运算
`numpy.in1d(ar1, ar2, assume_unique=False, invert=False)` 用于测试一维数组中的每个元素是否也存在于第二个数组中  
返回一个与 `ar1` 长度相同的布尔数组，当 `ar1` 的某个元素存在于 `ar2` 中时，对应位置为 `True`，否则为 `False`


```python
import numpy as np

test = np.array([0, 1, 2, 5, 0])
states = [0, 2]
mask = np.in1d(test, states)
print(mask)  # [ True False  True False  True]
print(test[mask])  # [0 2 0]

mask = np.in1d(test, states, invert=True) # 反转为不存在为True
print(mask)  # [False  True False  True False]
print(test[mask])  # [1 5]
```

### np.intersect1d() 交集
numpy.intersect1d(ar1, ar2, assume_unique=False, return_indices=False) 用于查找两个数组的交集  
返回两个输入数组中均存在的、已排序且唯一的值


```python
# 求两个数组的唯一化+求交集+排序函数

import numpy as np
from functools import reduce

x = np.intersect1d([1, 3, 4, 3], [3, 1, 2, 1])
print(x)  # [1 3]

x = np.array([1, 1, 2, 3, 4])
y = np.array([2, 1, 4, 6])
xy, x_ind, y_ind = np.intersect1d(x, y, return_indices=True) # 返回索引
# x_ind 是交集元素在数组 x 中的索引
# y_ind 是交集元素在数组 y 中的索引
print(xy)  # [1 2 4]
print(x_ind)  # [0 2 4]
print(y_ind)  # [1 0 2]
print(x[x_ind])  # [1 2 4]
print(y[y_ind])  # [1 2 4]

x = reduce(np.intersect1d, ([1, 3, 4, 3], [3, 1, 2, 1], [6, 3, 4, 2]))
print(x)  # [3] 
# reduce 函数会对 arrays 中的数组依次应用 np.intersect1d,这里相当于找出所有集合的交集
```

### np.union1d() 并集
numpy.union1d(ar1, ar2) 


```python
import numpy as np
from functools import reduce

x = np.union1d([-1, 0, 1], [-2, 0, 2])
print(x)  # [-2 -1  0  1  2]
x = reduce(np.union1d, ([1, 3, 4, 3], [3, 1, 2, 1], [6, 3, 4, 2]))
print(x)  # [1 2 3 4 6]
```

### np.setdiff1d() 差集
numpy.setdiff1d(ar1, ar2, assume_unique=False)元素存在于第一个函数不存在于第二个函数中


```python
import numpy as np

a = np.array([1, 2, 3, 2, 4, 1])
b = np.array([3, 4, 5, 6])
x = np.setdiff1d(a, b)
print(x)  # [1 2]
```

### np.setxor1d() 异或
numpy.setxor1d(ar1, ar2, assume_unique=False)两个数组中各自独自拥有的元素的集合


```python
import numpy as np

a = np.array([1, 2, 3, 2, 4, 1])
b = np.array([3, 4, 5, 6])
x = np.setxor1d(a, b)
print(x)  # [1 2 5 6]
```

# 输入输出

##  numpy 二进制文件
以 numpy 专用的二进制类型（.npy、.npz）保存和读取数据，这三个函数会自动处理ndim、dtype、shape等信息，使用它们读写数组非常方便  
但是save()和savez()输出的文件很难与其它语言编写的程序兼容  

### np.save()
def save(file, arr, allow_pickle=True, fix_imports=True):    
以 `.npy` 格式将数组保存到二进制文件中  

- `file`：文件名或文件对象。  
- `arr`：需要保存的数组。  
- `allow_pickle`（可选，默认值：`True`）：是否允许保存对象数组（通过 pickle 序列化）。  
- `fix_imports`（可选，默认值：`True`）：若为 `True`，在 Python 2 和 Python 3 之间兼容时，会尝试映射旧的 Python 2 名称到 Python 3。

**.npy 格式**：  
- 以二进制方式存储文件。  
- 文件的第一行以文本形式保存了数据的元信息（如 `ndim`、`dtype`、`shape` 等）。  
- 可用二进制工具查看内容  


```python
import numpy as np

file = r'.\test.npy'
np.random.seed(20200619)
x = np.random.uniform(low=0, high=1,size = [3, 5])
np.save(file, x)
y = np.load(file)
print(y)
# [[0.01123594 0.66790705 0.50212171 0.7230908  0.61668256]
#  [0.00668332 0.1234096  0.96092409 0.67925305 0.38596837]
#  [0.72342998 0.26258324 0.24318845 0.98795012 0.77370715]]
```

### np.savez()
def savez(file, *args, **kwds):    
以未压缩的 `.npz` 格式将多个数组保存到单个文件中  
 
- `file`：文件名  
- `*args`：需要保存的数组（非关键字参数）  
- `**kwds`：需要保存的数组（关键字参数，可以为数组指定名称）  

**.npz 格式**：  
- 以压缩打包的方式存储文件，可用压缩软件解压。  
- 输出的是一个压缩文件（扩展名为 `.npz`）。  
- `.npz` 文件中的每个文件都是一个 `save()` 保存的 `.npy` 文件，文件名对应于数组名。  

**特性**：  
- `load()` 自动识别 `.npz` 文件，并返回一个类似于字典的对象。  
- 可以通过数组名作为关键字获取数组的内容。  
- 非关键字参数传递的数组会自动起名为 `arr_0`, `arr_1`, ...  


```python
import numpy as np

file = r'.\test.npz'
x = np.linspace(0, np.pi, 5)
y = np.sin(x)
z = np.cos(x)
np.savez(file, x, y, z_d=z)
data = np.load(file)
np.set_printoptions(suppress=True)
print(data.files)  
# ['z_d', 'arr_0', 'arr_1']

print(data['arr_0'])
# [0.         0.78539816 1.57079633 2.35619449 3.14159265]

print(data['arr_1'])
# [0.         0.70710678 1.         0.70710678 0.        ]

print(data['z_d'])
# [ 1.          0.70710678  0.         -0.70710678 -1.        ]

# 用解压软件打开 test.npz 文件，会发现其中有三个文件：arr_0.npy,arr_1.npy,z_d.npy，其中分别保存着数组x,y,z的内容。
```

### np.load()
def load(file, mmap_mode=None, allow_pickle=False, fix_imports=True, encoding='ASCII'):    
从 `.npy`、`.npz` 或 pickled 文件加载数组或 pickled 对象  
 
- `file`：文件名或文件对象。  
- `mmap_mode`（可选，默认值：`None`）：  
  - 读取文件的方式，可选值：`None`、`'r+'`、`'r'`、`'w+'`、`'c'`  
- `allow_pickle`（可选，默认值：`False`）：是否允许加载存储在 `.npy` 文件中的 pickled 对象数组  
- `fix_imports`（可选，默认值：`True`）：  
  - 若为 `True`，pickle 将尝试将旧的 Python 2 名称映射到 Python 3 中使用的新名称  
- `encoding`（可选，默认值：`'ASCII'`）：  
  - 指定编码格式，默认为 `'ASCII'`  



## 文本文件
savetxt()，loadtxt()和genfromtxt()函数用来存储和读取文本文件（如.TXT，.CSV等）   
genfromtxt()比loadtxt()更加强大，可对缺失数据进行处理  

### np.savetxt()
def savetxt(fname, X, fmt='%.18e', delimiter=' ', newline='\n',header='', footer='', comments='# ', encoding=None)  
将数组 `X` 的内容以文本格式保存到文件中  
  
- `fname`：文件路径，指定保存的文件名  
- `X`：需要存入文件的数组  
- `fmt='%.18e'`：写入文件中每个元素的字符串格式，默认为 `'%.18e'`（保留 18 位小数的浮点数形式）  
- `delimiter=' '`：分割字符串，默认以空格分隔  
- `newline='\n'`：行与行之间的分隔符，默认为换行符 `\n`  
- `header=''`：写入文件的头部字符串，默认为空  
- `footer=''`：写入文件的尾部字符串，默认为空  
- `comments='# '`：注释前缀，默认为 `'# '`，若 `header` 或 `footer` 不为空，会在其前添加此注释前缀  
- `encoding=None`：指定文件编码，默认为 `None`（使用系统默认编码）


```python
import numpy as np

file = r'.\test.txt'
x = np.arange(0, 10).reshape(2, -1)
np.savetxt(file, x)
y = np.loadtxt(file)
print(y)
# [[0. 1. 2. 3. 4.]
#  [5. 6. 7. 8. 9.]]

# test.txt文件如下：
# 0.000000000000000000e+00 1.000000000000000000e+00 2.000000000000000000e+00 3.000000000000000000e+00 4.000000000000000000e+00
# 5.000000000000000000e+00 6.000000000000000000e+00 7.000000000000000000e+00 8.000000000000000000e+00 9.000000000000000000e+00

file = r'.\test.csv'
x = np.arange(0, 10, 0.5).reshape(4, -1)
np.savetxt(file, x, fmt='%.3f', delimiter=',')
y = np.loadtxt(file, delimiter=',')
print(y)
# [[0.  0.5 1.  1.5 2. ]
#  [2.5 3.  3.5 4.  4.5]
#  [5.  5.5 6.  6.5 7. ]
#  [7.5 8.  8.5 9.  9.5]]

# test.csv文件如下：
# 0.000,0.500,1.000,1.500,2.000
# 2.500,3.000,3.500,4.000,4.500
# 5.000,5.500,6.000,6.500,7.000
# 7.500,8.000,8.500,9.000,9.500
```

### np.genfromtxt()
def genfromtxt(fname, dtype=float, comments='#', delimiter=None,  
               skip_header=0, skip_footer=0, converters=None,  
               missing_values=None, filling_values=None, usecols=None,  
               names=None, excludelist=None,  
               deletechars=''.join(sorted(NameValidator.defaultdeletechars)),  
               replace_space='_', autostrip=False, case_sensitive=True,  
               defaultfmt="f%i", unpack=None, usemask=False, loose=True,  
               invalid_raise=True, max_rows=None, encoding='bytes'):  
从文本文件加载数据，并按指定方式处理缺失值，适用于结构化数组和缺失数据的处理  
names=None：设置为True时，程序将把第一行作为列名称   
  
- `fname`：文件路径，指定加载的文件名  
- `dtype=float`：数据类型，默认为 `float`  
- `comments='#'`：字符串或字符串组成的列表，默认为 `'#'`，表示注释字符集开始的标志  
- `delimiter=None`：分隔符，默认为 `None`（自动检测空格或制表符）  
- `skip_header=0`：跳过的头部行数，默认为 0  
- `skip_footer=0`：跳过的尾部行数，默认为 0  
- `converters=None`：字典，指定列的转换函数  
- `missing_values=None`：字符串或字符串组成的列表，指定缺失值的表示方式，默认为 `None`  
- `filling_values=None`：字典或单一值，指定缺失值的填充方式，默认为 `None`  
- `usecols=None`：元组，指定需要读取的列（列索引从 0 开始）  
- `names=None`：  
  - 若为 `True`，将第一行作为列名称  
  - 若为字符串列表，指定列名称  
  - 默认为 `None`  
- `excludelist=None`：字符串列表，指定需要排除的列名称  
- `deletechars=''.join(sorted(NameValidator.defaultdeletechars))`：在列名称中需要删除的字符  
- `replace_space='_'`：将列名称中的空格替换为下划线 `_`  
- `autostrip=False`：布尔值，若为 `True`，自动去除列名称两端的空格  
- `case_sensitive=True`：布尔值，列名称是否区分大小写，默认为 `True`  
- `defaultfmt="f%i"`：默认的列名称格式，默认为 `"f%i"`  
- `unpack=None`：布尔值，若为 `True`，将多列数据解耦为多个变量  
- `usemask=False`：布尔值，若为 `True`，返回掩码数组（MaskedArray）  
- `loose=True`：布尔值，若为 `True`，宽松解析输入数据  
- `invalid_raise=True`：布尔值，若为 `True`，在遇到无效数据时抛出异常  
- `max_rows=None`：读取的最大行数，默认为 `None`  
- `encoding='bytes'`：指定文件编码，默认为 `'bytes'`


```python
## data.csv文件（不带缺失值）
# id,value1,value2,value3
# 1,123,1.4,23
# 2,110,0.5,18
# 3,164,2.1,19
import numpy as np

file = r'.\data.csv'
x = np.loadtxt(file, delimiter=',', skiprows=1, usecols=(1, 2)) #跳过第一行,选择二三列
print(x)
# [[123.    1.4]
#  [110.    0.5]
#  [164.    2.1]]

val1, val2 = np.loadtxt(file, delimiter=',', skiprows=1, usecols=(1, 2), unpack=True)
print(val1)  # [123. 110. 164.]
print(val2)  # [1.4 0.5 2.1]

x = np.genfromtxt(file, delimiter=',', names=True)
print(x)
# [(1., 123., 1.4, 23.) (2., 110., 0.5, 18.) (3., 164., 2.1, 19.)]

print(type(x))  
# <class 'numpy.ndarray'>

print(x.dtype)
# [('id', '<f8'), ('value1', '<f8'), ('value2', '<f8'), ('value3', '<f8')]

print(x['id'])  # [1. 2. 3.]
print(x['value1'])  # [123. 110. 164.]
print(x['value2'])  # [1.4 0.5 2.1]
print(x['value3'])  # [23. 18. 19.]

## data1.csv文件（带有缺失值）
# id,value1,value2,value3
# 1,123,1.4,23
# 2,110,,18
# 3,,2.1,19

file = r'.\data1.csv'
x = np.genfromtxt(file, delimiter=',', names=True)
print(x)
# [(1., 123., 1.4, 23.) (2., 110., nan, 18.) (3.,  nan, 2.1, 19.)]

print(type(x))  
# <class 'numpy.ndarray'>

print(x.dtype)
# [('id', '<f8'), ('value1', '<f8'), ('value2', '<f8'), ('value3', '<f8')]

print(x['id'])  # [1. 2. 3.]
print(x['value1'])  # [123. 110.  nan]
print(x['value2'])  # [1.4 nan 2.1]
print(x['value3'])  # [23. 18. 19.]
```

### np.loadtxt()
def loadtxt(fname, dtype=float, comments='#', delimiter=None,    
            converters=None, skiprows=0, usecols=None, unpack=False,   
            ndmin=0, encoding='bytes', max_rows=None):    
  
从文本文件加载数据并返回数组   
    
- `fname`：文件路径，指定加载的文件名  
- `dtype=float`：数据类型，默认为 `float`  
- `comments='#'`：字符串或字符串组成的列表，默认为 `'#'`，表示注释字符集开始的标志，注释行会被忽略  
- `delimiter=None`：分隔符，默认为 `None`（自动检测空格或制表符）  
- `converters=None`：字典，指定列的转换函数，例如 `{0: float}` 表示将第 0 列转换为浮点数  
- `skiprows=0`：跳过的行数，默认为 0（不跳过任何行）  
- `usecols=None`：元组，指定需要读取的列（列索引从 0 开始），默认为 `None`（读取所有列）  
- `unpack=False`：布尔值，若为 `True`，将多列数据解耦为多个变量  
- `ndmin=0`：返回数组的最小维度，默认为 0  
- `encoding='bytes'`：指定文件编码，默认为 `'bytes'`  
- `max_rows=None`：读取的最大行数，默认为 `None`（读取所有行）

## 文本格式选项

### np.set_printoptions()
def set_printoptions(precision=None, threshold=None, edgeitems=None,
                     linewidth=None, suppress=None, nanstr=None, infstr=None,
                     formatter=None, sign=None, floatmode=None, **kwarg):   
设置打印选项，用于控制浮点数、数组和其它 NumPy 对象的显示方式  
  
- `precision=8`：  
  设置浮点数的精度，控制输出的小数点位数，默认值为 `8`

- `threshold=1000`：  
  数组的概略显示阈值，超过该值时以 `"..."` 的形式省略部分内容，默认值为 `1000`

- `edgeitems=None`：  
  控制概略显示时，数组开头和结尾显示的元素个数  
  （若未指定，则使用默认值，具体与 NumPy 版本相关）

- `linewidth=75`：  
  用于确定每行显示的最大字符数，超过该值时插入换行符，默认值为 `75`

- `suppress=False`：  
  是否禁止使用科学计数法显示小数：  
  - `True`：小数以普通形式输出，而非科学计数法  
  - `False`：默认使用科学计数法，默认值为 `False`

- `nanstr='nan'`：  
  浮点数中 `NaN`（非数字）的字符串表示形式，默认值为 `'nan'`

- `infstr='inf'`：  
  浮点数中正无穷大（`inf`）的字符串表示形式，默认值为 `'inf'`

- `formatter=None`：  
  一个字典，用于自定义格式化显示数组元素的规则  
  字典的键为需要格式化的数据类型，值为对应的格式化字符串  
  支持的类型键包括：  
  - `'bool'`：布尔值  
  - `'int'`：整数  
  - `'float'`：浮点数  
  - `'str'`：其他字符串  
  - `'all'`：应用于所有数据类型  

- `sign=None`：  
  控制浮点数的符号显示方式（较旧版本参数，部分版本可能已废弃）  

- `floatmode=None`：  
  控制浮点数的显示模式：  
  - `'fixed'`：固定小数点格式  
  - `'maxprec'`：最大精度模式（默认行为）  
  - `'maxprec_equal'`：等价的最大精度模式  

- `**kwarg`：  
  其他可选参数（根据具体 NumPy 版本可能有所不同）


```python
import numpy as np

np.set_printoptions(precision=4) # 小数位为4
x = np.array([1.123456789])
print(x)  # [1.1235]

np.set_printoptions(threshold=20) # 显示的阈值
x = np.arange(50)
print(x)  # [ 0  1  2 ... 47 48 49]

np.set_printoptions(threshold=np.iinfo(np.int).max) # 显示所有元素,可以看作固定搭配
print(x)
# [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
#  24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
#  48 49]

eps = np.finfo(float).eps # 返回浮点数类型 float 的机器精度，即两个相邻浮点数之间的最小间隔。对于大多数系统约为 2.220446049250313e-16
x = np.arange(4.)
x = x ** 2 - (x + eps) ** 2
print(x)  
# [-4.9304e-32 -4.4409e-16  0.0000e+00  0.0000e+00]

np.set_printoptions(suppress=True) # 不使用科学计数法
print(x)  # [-0. -0.  0.  0.]

x = np.linspace(0, 10, 10)
print(x)
# [ 0.      1.1111  2.2222  3.3333  4.4444  5.5556  6.6667  7.7778  8.8889
#  10.    ]
np.set_printoptions(precision=2, suppress=True, threshold=5)
print(x)  # [ 0.    1.11  2.22 ...  7.78  8.89 10.  ]

np.set_printoptions(formatter={'all': lambda x: 'int: ' + str(-x)}) #将输入值 x 转换为字符串，并在前面加上 'int: '，同时将 x 取反
x = np.arange(3)
print(x)  # [int: 0 int: -1 int: -2]

np.set_printoptions()  # formatter 重置了
print(x)  # [0 1 2]

# 恢复默认选项
np.set_printoptions(edgeitems=3, infstr='inf', linewidth=75,
                    nanstr='nan', precision=8, suppress=False, 
                    threshold=1000, formatter=None)
```

### np.get_printoptions()
def get_printoptions()  
获取当前打印选项  


```python
import numpy as np

x = np.get_printoptions()
print(x)
# {
# 'edgeitems': 3, 
# 'threshold': 1000, 
# 'floatmode': 'maxprec', 
# 'precision': 8, 
# 'suppress': False, 
# 'linewidth': 75, 
# 'nanstr': 'nan', 
# 'infstr': 'inf', 
# 'sign': '-', 
# 'formatter': None, 
# 'legacy': False
# }
```

# 随机抽样

### np.random.seed()
numpy.random.seed(seed=None)  

## 二项分布 np.random.binomial()
numpy.random.binomial(n, p, size=None)  
size表示采样的次数，n表示做了n重伯努利试验，p表示成功的概率，函数的返回值表示n中成功的次数  


```python
# 野外正在进行9（n=9）口石油勘探井的发掘工作，每一口井能够开发出油的概率是0.1（p=0.1）。请问，最终所有的勘探井都勘探失败的概率？

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(20200605)
n = 9# 做某件事情的次数
p = 0.1# 做某件事情成功的概率
size = 50000
x = np.random.binomial(n, p, size)
'''或者使用binom.rvs
#使用binom.rvs(n, p, size=1)函数模拟一个二项随机变量,可视化地表现概率
y = stats.binom.rvs(n, p, size=size)#返回一个numpy.ndarray
'''
print(np.sum(x == 0) / size)  # 0.3897

plt.hist(x)
plt.xlabel('随机变量：成功次数')
plt.ylabel('样本中出现的次数')
plt.show()
#它返回一个列表，列表中每个元素表示随机变量中对应值的概率
s = stats.binom.pmf(range(10), n, p)
print(np.around(s, 3))
# [0.387 0.387 0.172 0.045 0.007 0.001 0.    0.    0.    0.   ]
```

## 泊松分布 np.random.poisson()
numpy.random.poisson(lam=1.0, size=None)  
size表示采样的次数，lam表示一个单位内发生事件的平均值，函数的返回值表示一个单位内事件发生的次数  


```python
# 假定某航空公司预定票处平均每小时接到42次订票电话，那么10分钟内恰好接到6次电话的概率是多少？

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

np.random.seed(20200605)
lam = 42 / 6# 平均值：平均每十分钟接到42/6次订票电话
size = 50000
x = np.random.poisson(lam, size)
'''或者
#模拟服从泊松分布的50000个随机变量
x = stats.poisson.rvs(lam,size=size)
'''
print(np.sum(x == 6) / size)  # 0.14988

plt.hist(x)
plt.xlabel('随机变量：每十分钟接到订票电话的次数')
plt.ylabel('50000个样本中出现的次数')
plt.show()
#用poisson.pmf(k, mu)求对应分布的概率:概率质量函数 (PMF)
x = stats.poisson.pmf(6, lam)
print(x)  # 0.14900277967433773
```

## 超几何分布 np.random.hypergeometric()
numpy.random.hypergeometric(ngood, nbad, nsample, size=None)  
size表示采样的次数，ngood表示总体中具有成功标志的元素个数，nbad表示总体中不具有成功标志的元素个数  
ngood+nbad表示总体样本容量，nsample表示抽取元素的次数（小于或等于总体样本容量），函数的返回值表示抽取nsample个元素中具有成功标识的元素个数   


```python
# 一共20只动物里有7只是狗，抽取12只有3只狗的概率（无放回抽样）。

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

np.random.seed(20200605)
size = 500000
x = np.random.hypergeometric(ngood=7, nbad=13, nsample=12, size=size)
'''或者
#用rvs(M, n, N, loc=0, size=1, random_state=None)模拟
x = stats.hypergeom.rvs(M=20,n=7,N=12,size=size)
'''
print(np.sum(x == 3) / size)  # 0.198664

plt.hist(x, bins=8)
plt.xlabel('狗的数量')
plt.ylabel('50000个样本中出现的次数')
plt.title('超几何分布',fontsize=20)
plt.show()

"""
M 为总体容量
n 为总体中具有成功标志的元素的个数
N,k 表示抽取N个元素有k个是成功元素
"""
x = range(8)
#用hypergeom.pmf(k, M, n, N, loc)来计算k次成功的概率
s = stats.hypergeom.pmf(k=x, M=20, n=7, N=12)
print(np.round(s, 3))
# [0.    0.004 0.048 0.199 0.358 0.286 0.095 0.01 ]

```

## 均匀分布 np.random.uniform() 
numpy.random.uniform(low=0.0, high=1.0, size=None) 


```python
# 在low到high范围内，创建大小为size的均匀分布的随机数。

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(20200614)
a = 0
b = 100
size = 50000
x = np.random.uniform(a, b, size=size)
print(np.all(x >= 0))  # True
print(np.all(x < 100))  # True
y = (np.sum(x < 50) - np.sum(x < 10)) / size
print(y)  # 0.40144

plt.hist(x, bins=20)
plt.show()

a = stats.uniform.cdf(10, 0, 100)
b = stats.uniform.cdf(50, 0, 100)
print(b - a)  # 0.4
```

## np.random.rand()
## np.random.uniform()
numpy.random.rand(d0, d1, ..., dn) d指维度
## np.random.randint(1, 10, [3, 4])
np.random.randint(low, high, size)

## 正态分布 np.random.randn()
numpy.random.randn(d0, d1, ..., dn)


```python
# 根据指定大小产生满足标准正态分布的数组（均值为0，标准差为1）

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(20200614)
size = 50000
x = np.random.randn(size)
y1 = (np.sum(x < 1) - np.sum(x < -1)) / size
y2 = (np.sum(x < 2) - np.sum(x < -2)) / size
y3 = (np.sum(x < 3) - np.sum(x < -3)) / size
print(y1)  # 0.68596
print(y2)  # 0.95456
print(y3)  # 0.99744

plt.hist(x, bins=20)
plt.show()

y1 = stats.norm.cdf(1) - stats.norm.cdf(-1)
y2 = stats.norm.cdf(2) - stats.norm.cdf(-2)
y3 = stats.norm.cdf(3) - stats.norm.cdf(-3)
print(y1)  # 0.6826894921370859
print(y2)  # 0.9544997361036416
print(y3)  # 0.9973002039367398
```

## 指数分布 np.random.exponential()
numpy.random.exponential(scale=1.0, size=None)


```python
# scale = 1/lambda

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(20200614)
lam = 7
size = 50000
x = np.random.exponential(1 / lam, size)
'''或者
#rvs(loc=0, scale=1/lam, size=size, random_state=None)模拟
'''
y1 = (np.sum(x < 1 / 7)) / size
y2 = (np.sum(x < 2 / 7)) / size
y3 = (np.sum(x < 3 / 7)) / size
print(y1)  # 0.63218
print(y2)  # 0.86518
print(y3)  # 0.95056

plt.hist(x, bins=20)
plt.show()

y1 = stats.expon.cdf(1 / 7, scale=1 / lam)
y2 = stats.expon.cdf(2 / 7, scale=1 / lam)
y3 = stats.expon.cdf(3 / 7, scale=1 / lam)
print(y1)  # 0.6321205588285577
print(y2)  # 0.8646647167633873
print(y3)  # 0.950212931632136
```

## 随机从序列中获取元素
### np.random.choice()
numpy.random.choice(a, size=None, replace=True, p=None)  
从序列中获取元素，若a为整数，元素取值从np.range(a)中随机获取  
若a为数组，取值从a数组元素中随机获取  
该函数还可以控制生成数组中的元素是否重复replace，以及选取元素的概率p  


```python
import numpy as np

np.random.seed(20200614)
x = np.random.choice(10, 3)
print(x)  # [2 0 1]

x = np.random.choice(10, 3, p=[0.05, 0, 0.05, 0.9, 0, 0, 0, 0, 0, 0])
print(x)  # [3 2 3]

x = np.random.choice(10, 3, replace=False, p=[0.05, 0, 0.05, 0.9, 0, 0, 0, 0, 0, 0])
print(x)  # [3 0 2]

aa_milne_arr = ['pooh', 'rabbit', 'piglet', 'Christopher']
x = np.random.choice(aa_milne_arr, 5, p=[0.5, 0.1, 0.1, 0.3])
print(x) # ['pooh' 'rabbit' 'pooh' 'pooh' 'pooh']
```

## 对数据集进行洗牌操作
### np.random.shuffle(x)
对x进行重排序，如果x为多维数组，只沿第 0 轴洗牌，改变原来的数组，输出为None
### np.random.permutation(x)
作用与shuffle()函数相同，可以打乱第0轴的数据，但是它不会改变原来的数组


```python
import numpy as np

np.random.seed(20200614)
x = np.arange(10)
np.random.shuffle(x)
print(x) # 改变原来的数组
# [6 8 7 5 3 9 1 4 0 2]

print(np.random.shuffle(x))
# None

x = np.arange(20).reshape((5, 4))
np.random.shuffle(x)
print(x) # 只沿第 0 轴洗牌
# [[ 4  5  6  7]
#  [ 0  1  2  3]
#  [ 8  9 10 11]
#  [16 17 18 19]
#  [12 13 14 15]]
```


```python
import numpy as np

np.random.seed(20200614)
x = np.arange(10)
y = np.random.permutation(x)
print(y)
# [6 8 7 5 3 9 1 4 0 2]

z=[1, 4, 9, 12, 15]
print(np.random.permutation(z))
# [ 4  1  9 15 12]
print(z) 
# [1, 4, 9, 12, 15] 不会改变原来的数组
```

# 统计相关*

### np.min()
numpy.amin(a[, axis=None, out=None, keepdims=np._NoValue, initial=np._NoValue, where=np._NoValue])


```python
import numpy as np

x = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28, 29, 30],
              [31, 32, 33, 34, 35]])
y = np.amin(x)
print(y)  # 11

y = np.amin(x, axis=0)
print(y)  # [11 12 13 14 15]

y = np.amin(x, axis=1)
print(y)  # [11 16 21 26 31]
```

### np.max()
numpy.amax(a[, axis=None, out=None, keepdims=np._NoValue, initial=np._NoValue, where=np._NoValue])

### np.ptp() 极差
numpy.ptp(a, axis=None, out=None, keepdims=np._NoValue) Range of values (maximum - minimum)   
计算最值之差  


```python
import numpy as np

np.random.seed(20200623)
x = np.random.randint(0, 20, size=[4, 5])
print(x)
# [[10  2  1  1 16]
#  [18 11 10 14 10]
#  [11  1  9 18  8]
#  [16  2  0 15 16]]

print(np.ptp(x))  # 18
print(np.ptp(x, axis=0))  # [ 8 10 10 17  8]
print(np.ptp(x, axis=1))  # [15  8 17 16]
```

### np.percentile() 分位数
numpy.percentile(a, q, axis=None, out=None, overwrite_input=False, interpolation='linear', keepdims=False)  
- a：array，用来算分位数的对象，可以是多维的数组   
- q：介于0-100的float，用来计算是几分位的参数，如四分之一位就是25，如要算两个位置的数就[25,75]  
- axis：坐标轴的方向，一维的就不用考虑了，多维的就用这个调整计算的维度方向，取值范围0/1  


```python
import numpy as np

np.random.seed(20200623)
x = np.random.randint(0, 20, size=[4, 5])
print(x)
# [[10  2  1  1 16]
#  [18 11 10 14 10]
#  [11  1  9 18  8]
#  [16  2  0 15 16]]

print(np.percentile(x, [25, 50]))  
# [ 2. 10.]

print(np.percentile(x, [25, 50], axis=0))
# [[10.75  1.75  0.75 10.75  9.5 ]
#  [13.5   2.    5.   14.5  13.  ]]

print(np.percentile(x, [25, 50], axis=1))
# [[ 1. 10.  8.  2.]
#  [ 2. 11.  9. 15.]]
```

### np.median() 中位数
numpy.median(a, axis=None, out=None, overwrite_input=False, keepdims=False)


```python
import numpy as np

np.random.seed(20200623)
x = np.random.randint(0, 20, size=[4, 5])
print(x)
# [[10  2  1  1 16]
#  [18 11 10 14 10]
#  [11  1  9 18  8]
#  [16  2  0 15 16]]
print(np.percentile(x, 50))
print(np.median(x))
# 10.0

print(np.percentile(x, 50, axis=0))
print(np.median(x, axis=0))
# [13.5  2.   5.  14.5 13. ]
```

### np.mean() 均值
numpy.mean(a[, axis=None, dtype=None, out=None, keepdims=np._NoValue])


```python
import numpy as np

x = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28, 29, 30],
              [31, 32, 33, 34, 35]])
y = np.mean(x)
print(y)  # 23.0

y = np.mean(x, axis=1)
print(y)  # [13. 18. 23. 28. 33.]
```

### np.averange() 加权均值
numpy.average(a[, axis=None, weights=None, returned=False])
不指定权重weights的时候average和mean是一样的


```python
# 将各数值乘以相应的权数，然后加总求和得到总体值，再除以总的单位数
# 不指定权重的时候average和mean是一样的
import numpy as np

x = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28, 29, 30],
              [31, 32, 33, 34, 35]])

# 权重
y = np.arange(1, 26).reshape([5, 5])
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]
#  [11 12 13 14 15]
#  [16 17 18 19 20]
#  [21 22 23 24 25]]

z = np.average(x, weights=y)
print(z)  # 27.0

z = np.average(x, axis=0, weights=y) # 沿着 axis=0（即每一列）计算加权平均值
print(z)
# [25.54545455 26.16666667 26.84615385 27.57142857 28.33333333]
# 乘积之和：
# 11×1+16×6+21×11+26×16+31×21
# =11+96+231+416+651=1405
# 权重之和：
# 1+6+11+16+21=55
# 加权平均：
# 1405/55≈25.54545455
```

### np.var() 方差
numpy.var(a[, axis=None, dtype=None, out=None, ddof=0, keepdims=np._NoValue])    
- ddof=0：是“Delta Degrees of Freedom”，表示自由度的个数 
   
要注意方差和样本方差的无偏估计，方差公式中分母上是n；样本方差无偏估计公式中分母上是n-1（n为样本个数）   


```python
import numpy as np

x = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28, 29, 30],
              [31, 32, 33, 34, 35]])
y = np.var(x)
print(y)  # 52.0
y = np.mean((x - np.mean(x)) ** 2)
print(y)  # 52.0

y = np.var(x, ddof=1) # ddof=1 表示计算样本方差（即除以 n - 1，n 是元素总数）
print(y)  # 54.166666666666664
y = np.sum((x - np.mean(x)) ** 2) / (x.size - 1)
print(y)  # 54.166666666666664

y = np.var(x, axis=0)
print(y)  # [50. 50. 50. 50. 50.]
```

### np.std() 标准差
numpy.std(a[, axis=None, dtype=None, out=None, ddof=0, keepdims=np._NoValue])  
标准差是一组数据平均值分散程度的一种度量，是方差的算术平方根。


```python
import numpy as np

x = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28, 29, 30],
              [31, 32, 33, 34, 35]])
y = np.std(x)
print(y)  # 7.211102550927978
y = np.sqrt(np.var(x))
print(y)  # 7.211102550927978

y = np.std(x, axis=0)
print(y)
# [7.07106781 7.07106781 7.07106781 7.07106781 7.07106781]
```

### np.cov() 协方差矩阵
numpy.cov(m, y=None, rowvar=True, bias=False, ddof=None, fweights=None,aweights=None)


```python
import numpy as np

x = [1, 2, 3, 4, 6]
y = [0, 2, 5, 6, 7]
print(np.cov(x))  # 3.7   #样本方差(即除以 n - 1)  等价于print(np.var(x,ddof=1))
print(np.cov(y))  # 8.5   #样本方差
print(np.cov(x, y)) # 协方差矩阵
# [[3.7  5.25]
#  [5.25 8.5 ]]
# 对角线元素是 x 和 y 的样本方差
# 非对角线元素是 x 和 y 的样本协方差


# 计算示例如下：
print(np.var(x))  # 2.96    #方差
print(np.var(x, ddof=1))  # 3.7    #样本方差
print(np.var(y))  # 6.8    #方差
print(np.var(y, ddof=1))  # 8.5    #样本方差

z = np.mean((x - np.mean(x)) * (y - np.mean(y)))    #协方差
print(z)  # 4.2

z = np.sum((x - np.mean(x)) * (y - np.mean(y))) / (len(x) - 1)   #样本协方差
print(z)  # 5.25

z = np.dot(x - np.mean(x), y - np.mean(y)) / (len(x) - 1)     #样本协方差     
print(z)  # 5.25
```

### np.corrcoef() 相关系数
numpy.corrcoef(x, y=None, rowvar=True, bias=np._NoValue, ddof=np._NoValue)  
理解了np.cov()函数之后，很容易理解np.correlate()，二者参数几乎一模一样  
np.cov()描述的是两个向量协同变化的程度，它的取值可能非常大，也可能非常小，这就导致没法直观地衡量二者协同变化的程度  
相关系数实际上是正则化的协方差，n个变量的相关系数形成一个n维方阵  


```python
import numpy as np

np.random.seed(20200623)
x, y = np.random.randint(0, 20, size=(2, 4))
print(x)  # [10  2  1  1]
print(y)  # [16 18 11 10]

z = np.corrcoef(x, y)
print(z)
# [[1.         0.48510096]
#  [0.48510096 1.        ]]
# 对角线元素是 x 和 y 与自身的相关系数（始终为 1）
# 非对角线元素是 x 和 y 的相关系数


# 计算示例如下：
a = np.dot(x - np.mean(x), y - np.mean(y))              # 计算协方差
b = np.sqrt(np.dot(x - np.mean(x), x - np.mean(x)))     # 计算 x 的标准差
c = np.sqrt(np.dot(y - np.mean(y), y - np.mean(y)))
print(a / (b * c))  # 0.4851009629263671                # 相关系数
```

### np.digitize() 直方图
numpy.digitize(x, bins, right=False)    
- x：numpy数组
- bins：区间  一维单调数组  `必须是升序或者降序`
- right：间隔是否包含最右  默认False
- 返回值：x在bins中的位置(每个元素所属的区间的索引)


```python
import numpy as np

x = np.array([0.2, 6.4, 3.0, 1.6]) # 元素
bins = np.array([0.0, 1.0, 2.5, 4.0, 10.0]) # 4个区间
inds = np.digitize(x, bins)
print(inds)  # [1 4 3 2] 每个元素所属的区间的索引
for n in range(x.size):
    print(bins[inds[n] - 1], "<=", x[n], "<", bins[inds[n]])
# 0.0 <= 0.2 < 1.0
# 4.0 <= 6.4 < 10.0
# 2.5 <= 3.0 < 4.0
# 1.0 <= 1.6 < 2.5


x = np.array([1.2, 10.0, 12.4, 15.5, 20.])
bins = np.array([0, 5, 10, 15, 20])
inds = np.digitize(x, bins, right=True) # 区间是左开右闭的
print(inds)  # [1 2 3 4 4]
# 10.0 落在 (5, 10] 索引为 2
# 20.0 落在 (15, 20] 索引为 4

inds = np.digitize(x, bins, right=False)
print(inds)  # [1 3 3 4 5]
# 10.0 落在 [10, 15) 索引为 3
```

# 线性代数
Numpy 定义了 matrix 类型，使用该 matrix 类型创建的是矩阵对象，它们的加减乘除运算缺省采用矩阵方式计算，因此用法和Matlab十分类似  
但是由于 NumPy 中同时存在 ndarray 和 matrix 对象，因此用户很容易将两者弄混  
这有违 Python 的“显式优于隐式”的原则，因此官方并不推荐在程序中使用 matrix  
在这里，我们仍然用 ndarray 来介绍  

### np.dot() 矩阵和向量积
矩阵的定义、矩阵的加法、矩阵的数乘、矩阵的转置与二维数组完全一致，不再进行说明，但矩阵的乘法有不同的表示  
numpy.dot(a, b[, out])计算两个矩阵的乘积，如果是一维数组则是它们的内积   
注意：在线性代数里面讲的维数和数组的维数不同，如线代中提到的n维行向量在 Numpy 中是一维数组，而线性代数中的n维列向量在 Numpy 中是一个shape为(n, 1)的二维数组   


```python
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 4, 5, 6])
z = np.dot(x, y) # 1*2+2*3+3*4...
print(z)  # 70

x = np.array([[1, 2, 3], [3, 4, 5], [6, 7, 8]])
# [[1 2 3]
#  [3 4 5]
#  [6 7 8]]
y = np.array([[5, 4, 2], [1, 7, 9], [0, 4, 5]])
# [[5 4 2]
#  [1 7 9]
#  [0 4 5]]
z = np.dot(x, y)
print(z) # z[0, 0]是 x 的第 0 行与 y 的第 0 列的点积=1*5+2*1+3*0=7
# [[  7  30  35]
#  [ 19  60  67]
#  [ 37 105 115]]

z = np.dot(y, x)
print(z)
# [[ 29  40  51]
#  [ 76  93 110]
#  [ 42  51  60]]
```

### np.linalg.eig() 特征值与特征向量
numpy.linalg.eig(a) 计算方阵的特征值和特征向量  
numpy.linalg.eigvals(a) 计算方阵的特征值  


```python
import numpy as np
# 创建一个对角矩阵
x = np.diag((1, 2, 3))  
# [[1 0 0]
#  [0 2 0]
#  [0 0 3]]

print(np.linalg.eigvals(x))
# [1. 2. 3.]
a, b = np.linalg.eig(x)  
# 特征值保存在a中，特征向量保存在b中
print(a)
# [1. 2. 3.]
print(b)
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

# 检验特征值与特征向量是否正确
for i in range(3): 
    if np.allclose(a[i] * b[:, i], np.dot(x, b[:, i])):
        print('Right')
    else:
        print('Error')
# Right
# Right
# Right
```


```python
# 判断对称阵是否为正定阵（特征值是否全部为正）
import numpy as np

A = np.arange(16).reshape(4, 4)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]]

A = A + A.T  # 将方阵转换成对称阵
# [[ 0  5 10 15]
#  [ 5 10 15 20]
#  [10 15 20 25]
#  [15 20 25 30]]

B = np.linalg.eigvals(A)  # 求A的特征值
print(B)
# [ 6.74165739e+01 -7.41657387e+00  1.82694656e-15 -1.72637110e-15]

# 判断是不是所有的特征值都大于0，用到了all函数，显然对称阵A不是正定的
if np.all(B > 0):
    print('Yes')
else:
    print('No')
# No
```

### np.linalg.svd() 奇异值分解
u, s, v = numpy.linalg.svd(a, full_matrices=True, compute_uv=True, hermitian=False)
- a 是一个形如(M,N)矩阵
- full_matrices的取值是为False或者True，默认值为True，这时u的大小为(M,M)，v的大小为(N,N)。否则u的大小为(M,K)，v的大小为(K,N) ，K=min(M,N)。
- compute_uv的取值是为False或者True，默认值为True，表示计算u,s,v。为False的时候只计算s。
- 总共有三个返回值u,s,v，u大小为(M,M)，s大小为(M,N)，v大小为(N,N)，a = u*s*v。
- 其中s是对矩阵a的奇异值分解。s除了对角元素不为0，其他元素都为0，并且对角元素从大到小排列。s中有n个奇异值，一般排在后面的比较接近0，所以仅保留比较大的r个奇异值。  

注：Numpy中返回的v是通常所谓奇异值分解a=u*s*v'中v的转置。


```python
import numpy as np

A = np.array([[4, 11, 14], [8, 7, -2]])
# [[ 4 11 14]
#  [ 8  7 -2]] M=2,N=3

u, s, vh = np.linalg.svd(A, full_matrices=False) # K=2(M<N)
print(u.shape)  # (2, 2)=(M,K)
print(u)
# [[-0.9486833  -0.31622777]
#  [-0.31622777  0.9486833 ]]

print(s.shape)  # (2,)
print(np.diag(s))
# [[18.97366596  0.        ]
#  [ 0.          9.48683298]]

print(vh.shape)  # (2, 3)=(K,N)
print(vh)
# [[-0.33333333 -0.66666667 -0.66666667]
#  [ 0.66666667  0.33333333 -0.66666667]]

a = np.dot(u, np.diag(s))
a = np.dot(a, vh)
print(a)
# [[ 4. 11. 14.]
#  [ 8.  7. -2.]]
```

## np.linalg.qr() QR分解
q,r = numpy.linalg.qr(a, mode='reduced')计算矩阵a的QR分解  
- a是一个(M, N)的待分解矩阵  
- mode = reduced：返回(M, N)的列向量两两正交的矩阵q，和(N, N)的三角阵r（Reduced QR分解）  
- mode = complete：返回(M, M)的正交矩阵q，和(M, N)的三角阵r（Full QR分解）  


```python
import numpy as np
A = np.array([[2, -2, 3], [1, 1, 1], [1, 3, -1]])
# [[ 2 -2  3]
#  [ 1  1  1]
#  [ 1  3 -1]] M=3,N=3

q, r = np.linalg.qr(A)
print(q.shape)  # (3, 3)=(M,N)
print(q)
# [[-0.81649658  0.53452248  0.21821789]
#  [-0.40824829 -0.26726124 -0.87287156]
#  [-0.40824829 -0.80178373  0.43643578]]

print(r.shape)  # (3, 3)=(N,N)
print(r)
# [[-2.44948974  0.         -2.44948974]
#  [ 0.         -3.74165739  2.13808994]
#  [ 0.          0.         -0.65465367]]

print(np.dot(q, r))
# [[ 2. -2.  3.]
#  [ 1.  1.  1.]
#  [ 1.  3. -1.]]

a = np.allclose(np.dot(q.T, q), np.eye(3))
print(a)  # True 说明q为正交矩阵
```

## np.linalg.cholesky() Cholesky分解
L = numpy.linalg.cholesky(a) 返回正定矩阵a的 Cholesky 分解a = L*L.T，其中L是下三角


```python
import numpy as np

A = np.array([[1, 1, 1, 1], [1, 3, 3, 3],
              [1, 3, 5, 5], [1, 3, 5, 7]])
print(A)
# [[1 1 1 1]
#  [1 3 3 3]
#  [1 3 5 5]
#  [1 3 5 7]]

print(np.linalg.eigvals(A))
# [13.13707118  1.6199144   0.51978306  0.72323135]

L = np.linalg.cholesky(A)
print(L)
# [[1.         0.         0.         0.        ]
#  [1.         1.41421356 0.         0.        ]
#  [1.         1.41421356 1.41421356 0.        ]
#  [1.         1.41421356 1.41421356 1.41421356]]

print(np.dot(L, L.T))
# [[1. 1. 1. 1.]
#  [1. 3. 3. 3.]
#  [1. 3. 5. 5.]
#  [1. 3. 5. 7.]]
```

## np.linalg.norm() 矩阵范数 
numpy.linalg.norm(x, ord=None, axis=None, keepdims=False) 计算向量或者矩阵的范数  
根据ord参数的不同，计算不同的范数：   
向量:  
- L1 范数（曼哈顿范数）：向量各元素绝对值之和  
- L2 范数（欧几里得范数）：向量各元素平方和的平方根  
- 无穷范数（最大范数）：向量各元素绝对值的最大值  

矩阵:  
- L1 范数：矩阵中所有列的绝对值之和的最大值   
- L2 范数：矩阵的最大奇异值
- 无穷范数：矩阵的所有行的绝对值之和的最大值
- Frobenius范数: 矩阵所有元素平方和的平方根


```python
# 求向量的范数
import numpy as np
x = np.array([1, 2, 3, 4])

# ord=1
print(np.linalg.norm(x, ord=1)) 
# 10.0  |1|+|2|+|3|+|4|=10
print(np.sum(np.abs(x)))  
# 10

# ord=2
print(np.linalg.norm(x, ord=2))  
# 5.477225575051661 根号下平方和
print(np.sqrt(np.sum(np.abs(x) ** 2)))  
# 5.477225575051661

# ord=np.inf
print(np.linalg.norm(x, ord=-np.inf))  
# 1.0   min(|1|,|2|,|3|,|4|)=1
print(np.min(np.abs(x)))  
# 1

print(np.linalg.norm(x, ord=np.inf))  
# 4.0    max(|1|,|2|,|3|,|4|)=4
print(np.max(np.abs(x)))  
# 4
```


```python
# 求矩阵的范数
import numpy as np
A = np.array([[1, 2, 3, 4], [2, 3, 5, 8],
              [1, 3, 5, 7], [3, 4, 7, 11]])
# [[ 1  2  3  4]
#  [ 2  3  5  8]
#  [ 1  3  5  7]
#  [ 3  4  7 11]]

# ord=1
print(np.linalg.norm(A, ord=1))  # 30.0
print(np.max(np.sum(A, axis=0)))  # 30

# ord=2
print(np.linalg.norm(A, ord=2))  
# 20.24345358700576
print(np.max(np.linalg.svd(A, compute_uv=False)))  
# 20.24345358700576

# ord=inf
print(np.linalg.norm(A, ord=np.inf))  # 25.0
print(np.max(np.sum(A, axis=1)))  # 25

# ord='fro'
print(np.linalg.norm(A, ord='fro'))  
# 20.273134932713294
print(np.sqrt(np.trace(np.dot(A.T, A))))  
# 20.273134932713294
```

## np.linalg.det() 方阵行列式
numpy.linalg.det(a) 计算行列式。


```python
import numpy as np

x = np.array([[1, 2], [3, 4]])
# [[1 2]
#  [3 4]]

print(np.linalg.det(x))
# -2.0000000000000004
```

## np.linalg.matrix_rank() 矩阵的秩
numpy.linalg.matrix_rank(M, tol=None, hermitian=False) 返回矩阵的秩  



```python
import numpy as np

I = np.eye(3)  # 先创建一个单位阵
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

r = np.linalg.matrix_rank(I)
print(r)  # 3

I[1, 1] = 0  # 将该元素置为0
print(I)
# [[1. 0. 0.]
#  [0. 0. 0.]
#  [0. 0. 1.]]

r = np.linalg.matrix_rank(I)  # 此时秩变成2
print(r)  # 2
```

## np.trace() 方阵的迹
numpy.trace(a, offset=0, axis1=0, axis2=1, dtype=None, out=None) 方阵的迹就是主对角元素之和


```python
import numpy as np

x = np.array([[1, 2, 3], [3, 4, 5], [6, 7, 8]])
# [[1 2 3]
#  [3 4 5]
#  [6 7 8]]

y = np.array([[5, 4, 2], [1, 7, 9], [0, 4, 5]])
# [[5 4 2]
#  [1 7 9]
#  [0 4 5]]

print(np.trace(x))  # A的迹等于A.T的迹
# 13
print(np.trace(np.transpose(x)))
# 13

print(np.trace(x + y))  # 和的迹 等于 迹的和
# 30
print(np.trace(x) + np.trace(y))
# 30
```

## np.linalg.inv() 逆矩阵
逆矩阵（inverse matrix）
设 A 是数域上的一个 n 阶矩阵，若在相同数域上存在另一个 n 阶矩阵 B，使得：AB=BA=E（E 为单位矩阵），则我们称 B 是 A 的逆矩阵，而 A 则被称为可逆矩阵  
numpy.linalg.inv(a) 计算矩阵a的逆矩阵（矩阵可逆的充要条件：det(a) != 0，或者a满秩）  


```python
import numpy as np

A = np.array([[1, -2, 1], [0, 2, -1], [1, 1, -2]])
# [[ 1 -2  1]
#  [ 0  2 -1]
#  [ 1  1 -2]]

# 求A的行列式，不为零则存在逆矩阵
A_det = np.linalg.det(A)  
print(A_det)
# -2.9999999999999996

A_inverse = np.linalg.inv(A)  # 求A的逆矩阵
print(A_inverse)
# [[ 1.00000000e+00  1.00000000e+00 -1.11022302e-16]
#  [ 3.33333333e-01  1.00000000e+00 -3.33333333e-01]
#  [ 6.66666667e-01  1.00000000e+00 -6.66666667e-01]]

x = np.allclose(np.dot(A, A_inverse), np.eye(3))
print(x)  # True
x = np.allclose(np.dot(A_inverse, A), np.eye(3))
print(x)  # True

A_companion = A_inverse * A_det  # 求A的伴随矩阵
print(A_companion)
# [[-3.00000000e+00 -3.00000000e+00  3.33066907e-16]
#  [-1.00000000e+00 -3.00000000e+00  1.00000000e+00]
#  [-2.00000000e+00 -3.00000000e+00  2.00000000e+00]]
```

## np.linalg.solve() 解线性方程组 
numpy.linalg.solve(a, b) 求解线性方程组或矩阵方程  



```python
#  x + 2y +  z = 7
# 2x -  y + 3z = 7
# 3x +  y + 2z =18

import numpy as np

A = np.array([[1, 2, 1], [2, -1, 3], [3, 1, 2]])
b = np.array([7, 7, 18])
x = np.linalg.solve(A, b)
print(x)  # [ 7.  1. -2.]

x = np.linalg.inv(A).dot(b)
print(x)  # [ 7.  1. -2.]

y = np.allclose(np.dot(A, x), b)
print(y)  # True
```

# 鸢尾花操作示例


```python
from sklearn import datasets
import numpy as np 

iris=datasets.load_iris()
# 求出鸢尾属植物萼片长度的平均值、中位数和标准差（第1列，sepallength）
sepal=iris.data[:,0] # 第1列 萼片长度
print(f'平均值:{np.mean(sepal):.2f}')
print(f'中位数:{np.median(sepal)}')
print(f'标准差:{np.std(sepal)}')

# 创建一种标准化形式的鸢尾属植物萼片长度，其值正好介于0和1之间，这样最小值为0，最大值为1（第1列，sepallength）
sepal_min=np.min(sepal)
sepal_max=np.max(sepal)
normalized_sepal_length = (sepal-sepal_min) / (sepal_max - sepal_min)
# print(sepal_max)
# print(sepal_min)
# print("标准化后的萼片长度:", normalized_sepal_length)

# 找到鸢尾属植物萼片长度的第5和第95百分位数（第1列，sepallength）
print(f'第5和第95百分位数:{np.percentile(sepal,5)}和{np.percentile(sepal,95)}')

# 把iris_data数据集中的20个随机位置修改为np.nan值
np.random.seed(42)

# 在iris_data的sepallength中查找缺失值的个数和位置（第1列）
count=np.isnan(sepal).sum()
indices=np.where(np.isnan(sepal))[0]
print(f"缺失值的个数: {count}")
print(f"缺失值的位置（索引）: {indices}")

#  筛选具有 sepallength（第1列）< 5.0 并且 petallength（第3列）> 1.5 的 iris_data行
petal=iris.data[:,2]
condition=(sepal<5.0)&(petal>1.5)
print(np.where(condition))
# np.where 返回一个元组，因此使用 [0] 来获取第一个元素，即满足条件的行的索引
indices=np.where(condition)[0]
print(indices)
print(iris.data[indices])

#  选择没有任何 nan 值的 iris_data行
mask = ~np.isnan(iris.data).any(axis=1)
# np.isnan(iris.data) True 表示对应位置的元素是 np.nan
# .any(axis=1) 对于每一行，它会检查该行中是否有任何 True
# ~ 取反
rows = iris.data[mask]
print("没有 np.nan 值的行数:", len(rows))
# print("没有 np.nan 值的行数据:")
# print(rows)

# 计算 iris_data 中sepalLength（第1列）和petalLength（第3列）之间的相关系数
print(f'相关系数:{np.corrcoef(sepal,petal)}')

# 找出iris_data是否有任何缺失值
values = np.isnan(iris.data).any() 
print(values)
if values:
    print("数据集中存在缺失值。")
else:
    print("数据集中没有缺失值。")

#  在numpy数组中将所有出现的nan替换为0
iris.data[np.isnan(iris.data)]=0

# 将 iris_data 的花瓣长度（第3列）以形成分类变量的形式显示。定义：Less than 3 --> 'small'；3-5 --> 'medium'；'>=5 --> 'large'
petal_categories = np.where(petal < 3, 'small',np.where((petal >= 3) & (petal < 5), 'medium', 'large'))
print("花瓣长度分类:")
print(petal_categories)

# 根据 sepallength 列对数据集进行排序
sorted_indices = np.argsort(iris.data[:,0])
# 特征（数据）和标签（目标）通常需要分别排序
sorted_data = iris.data[sorted_indices]
sorted_target = iris.target[sorted_indices]

# 在鸢尾属植物数据集中找到最常见的花瓣长度值(第3列)
values, counts = np.unique(iris.data, return_counts=True)
max_count_index = np.argmax(counts)
print(f"最常见的花瓣长度值是: {values[max_count_index]} cm")
print(f"该值出现了 {counts[max_count_index]} 次")

# 在鸢尾花数据集的 petalwidth（第4列）中查找第一次出现的值大于1.0的位置
petal_width=iris.data[:,3]
# 找到第一个大于1.0的值的索引
first_index = np.where(petal_width > 1.0)[0][0]
print(f"第一次出现 petal width 大于1.0的位置是索引: {first_index}")
print(f"对应的 petal width 值是: {petal_width[first_index]}")
```
