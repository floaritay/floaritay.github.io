```python
from matplotlib import pyplot as plt
import numpy as np

plt.plot([1, 2, 3, 4], [1, 4, 2, 3],color='blue')
plt.plot([1, 2, 3, 4], [2, 2, 1, 4],color='red')  
```


```python
x = np.linspace(0, 2, 100)

plt.plot(x, x, label='linear') 
plt.plot(x, x**2, label='quadratic')  
plt.plot(x, x**3, label='cubic')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend()
```


```python
# step 1 
# 创建一个Figure实例
fig = plt.figure()

# step 2
# 用Figure实例创建了一个两行一列(即可以有两个subplot)的绘图区，并同时在第一个位置创建了一个subplot
ax = fig.add_subplot(2, 1, 1) # two rows, one column, first plot

# step 3
# 用Axes实例的方法画了一条曲线
t = np.arange(0.0, 1.0, 0.01)
s = np.sin(2*np.pi*t)
line, = ax.plot(t, s, color='blue', lw=2)
```


```python
# 创建数据
x=np.linspace(0,2*np.pi,100)
y=np.sin(x)

plt.figure()
plt.subplot(2,1,1)
plt.plot(x,y,label='sin(x)',color='blue')
plt.title('Sin Curve')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.legend() # 显示图例
plt.grid(True) # 显示网格

plt.tight_layout() # 自动调整子图间距
plt.show()
```

# 创建画布和子图

## plt.figure()
用于创建一个新的图形窗口，可通过参数设置大小（figsize）和分辨率（dpi）  
| 参数名       | 类型        | 说明                                                                 |
|--------------|-------------|----------------------------------------------------------------------|
| `num`        | int/str     | 图形的编号或名称。如果为整数，表示图形编号；如果为字符串，表示图形名称。 |
| `figsize`    | tuple       | 图形的宽度和高度（单位为英寸），格式为 `(width, height)`。             |
| `dpi`        | int         | 分辨率（每英寸点数），默认为 `100`。                                  |
| `facecolor`  | color       | 图形的背景颜色。                                                      |
| `edgecolor`  | color       | 图形的边框颜色。                                                      |
| `frameon`    | bool        | 是否显示图形边框，默认为 `True`。                                     |
| `clear`      | bool        | 如果为 `True`，则清除当前图形的内容，默认为 `False`。


```python
import matplotlib.pyplot as plt

# 创建一个图形，设置大小为 8x6 英寸，分辨率为 150，背景为浅灰色
plt.figure(num='MyPlot', figsize=(8, 6), dpi=150, facecolor='#f0f0f0', edgecolor='black')

# 在图形中绘制一条简单的曲线
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.plot(x, y, marker='o', linestyle='--', color='blue')

# 添加标题和标签
plt.title('Customized Figure')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# 显示图形
plt.show()
```

## plt.subplot()
用于创建子图，例如 plt.subplot(2, 1, 1) 表示创建一个 2 行 1 列的子图布局，并激活第 1 个子图  
plt.subplot(nrows, ncols, index, **kwargs)  

| 参数名     | 类型   | 说明                                                                 |
|------------|--------|----------------------------------------------------------------------|
| `nrows`    | `int`  | 子图布局的行数。                                                     |
| `ncols`    | `int`  | 子图布局的列数。                                                     |
| `index`    | `int`  | 当前子图的索引，从 1 开始编号。索引顺序是从左到右、从上到下。         |
| `**kwargs` | 关键字参数 | 用于设置子图的属性，包括但不限于：                                  |
|            |        | - `adjustable`: 控制子图的调整行为。                                |
|            |        | - `aspect`: 设置子图的宽高比。                                      |
|            |        | - `anchor`: 设置子图的位置锚点。                                    |
|            |        | - `polar`: 如果为 `True`，则子图为极坐标图。                         |


```python
import matplotlib.pyplot as plt
import numpy as np
 
# 创建一个 2x2 的子图布局
plt.figure(figsize=(10, 8))
 
# 子图 1: 左上角
plt.subplot(2, 2, 1)
x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x), color='blue')
plt.title('Subplot 1: sin(x)')
 
# 子图 2: 右上角
plt.subplot(2, 2, 2)
plt.plot(x, np.cos(x), color='red')
plt.title('Subplot 2: cos(x)')
 
# 子图 3: 左下角
plt.subplot(2, 2, 3)
plt.plot(x, np.tan(x), color='green')
plt.title('Subplot 3: tan(x)')
 
# 子图 4: 右下角
plt.subplot(2, 2, 4)
plt.plot(x, np.exp(-x), color='purple')
plt.title('Subplot 4: exp(-x)')
 
# 调整子图之间的间距
plt.tight_layout()
 
# 显示图形
plt.show()
```

## 颜色说明
1. 颜色名称  
'red', 'green', 'blue'  
'cyan', 'magenta', 'yellow'  
'black', 'white', 'gray'  
'orange', 'purple', 'pink'  

2. 十六进制  
'#FF0000' 红色  
'#00FF00' 绿色  
'#0000FF' 蓝色  
'#FFFFFF' 白色  
'#000000' 黑色  

3. RGB 或 RGBA 元组  
其中 R, G, B, A 都是在 [0, 1] 之间的浮点数  
(1.0, 0.0, 0.0) 红色  
(0.0, 1.0, 0.0) 绿色  
(0.0, 0.0, 1.0) 蓝色  
(1.0, 1.0, 1.0) 白色  
(0.0, 0.0, 0.0) 黑色  
(1.0, 0.0, 0.0, 0.5) 半透明红色  

4. 灰度字符串  
'0.75' 表示 75% 灰度  
'0.5' 表示 50% 灰度  
'0.25' 表示 25% 灰度  

# 绘制图形

## plt.plot() 折线图
plt.plot(x, y, color, linestyle, marker, markersize, markeredgewidth, markeredgecolor, markerfacecolor, alpha, linewidth)  绘制折线图  
  
1. 线型（linestyle 简写为 ls）：

| 简写 | 类型       |
|------|------------|
| `-`  | 实线       |
| `--` | 虚线       |
| `:`  | 点线       |
| `-.` | 点横线     |  
   
2. 点型（标记marker）：

| 简写 | 形状       |
|------|------------|
| `+`  | 加号       |
| `o`  | 圆圈       |
| `*`  | 星号       |
| `.`  | 实心点     |
| `x`  | 叉号       |
| `s`  | 正方形     |
| `d`  | 钻石形     |
| `^`  | 上三角     |
| `v`  | 下三角     |
| `p`  | 五角星     |  
   
3. 曲线颜色（color 简写为 c）:

| 简写 | 颜色   |
|------|--------|
| `r`  | 红色   |
| `g`  | 绿色   |
| `b`  | 蓝色   |
| `y`  | 黄色   |
| `k`  | 黑色   |  

4. 剩余参数说明  

| 参数                | 简写    | 说明                          | 取值范围/示例               |
|---------------------|---------|-------------------------------|-----------------------------|
| `markersize`        | `ms`    | 标记大小                      | 实数（如 `10`）             |
| `markeredgewidth`   | `mew`   | 标记边缘宽度                  | 实数（如 `1.5`）            |
| `markeredgecolor`   | `mec`   | 标记边缘颜色                  | 颜色选项中的任意值（如 `'r'`）|
| `markerfacecolor`   | `mfc`   | 标记表面颜色                  | 颜色选项中的任意值（如 `'g'`）|
| `alpha`             | -       | 透明度                        | `[0, 1]` 之间的浮点数（如 `0.5`）|
| `linewidth`         | -       | 线宽                          | 实数（如 `2`）              |
 

## plt.scatter(x, y)散点图
plt.scatter(x, y, s=None, c=None, marker=None, cmap=None, alpha=None, linewidths=None, edgecolors=None, label=None, **kwargs)
| 参数名        | 类型               | 说明                                                                 |
|---------------|--------------------|----------------------------------------------------------------------|
| `x`           | array-like         | 数据点的 x 坐标                                                   |
| `y`           | array-like         | 数据点的 y 坐标                                                   |
| `s`           | scalar or array-like | 数据点的大小，可以是单个数值或与数据点数量相同的数组               |
| `c`           | color or array-like | 数据点的颜色，可以是单个颜色或与数据点数量相同的颜色数组           |
| `marker`      | str or MarkerStyle | 数据点的标记样式，默认为 'o'                                       |
| `cmap`        | str or Colormap    | 用于将数值映射到颜色的颜色映射，仅在 `c` 是数值数组时使用          |
| `alpha`       | float              | 数据点的透明度，取值范围为 0（完全透明）到 1（完全不透明）         |
| `linewidths`  | scalar or array-like | 数据点标记的边框宽度                                              |
| `edgecolors`  | color or array-like | 数据点标记的边框颜色                                              |
| `label`       | str                | 用于图例的标签                                                    |
| `**kwargs`    | 关键字参数         | 其他用于自定义数据点样式的参数                                    |


```python
import matplotlib.pyplot as plt
import numpy as np

# 生成随机数据
np.random.seed(42)  # 设置随机种子，以确保结果可重复
x = np.random.rand(50) * 10  # 生成 50 个 0 到 10 之间的随机数
y = np.random.rand(50) * 10  # 生成 50 个 0 到 10 之间的随机数

# 绘制散点图
plt.figure(figsize=(8, 6))  # 设置图形大小
plt.scatter(x, y, color='blue', marker='o', label='Data Points')

# 添加标题和标签
plt.title('Scatter Plot Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# 添加图例
plt.legend()

# 显示图形
plt.show()
```

## plt.bar(x, height)柱状图
plt.bar(x, height, width=0.8, bottom=None, *, align='center', data=None, **kwargs)

| 参数名        | 类型               | 说明                                                                 |
|---------------|--------------------|----------------------------------------------------------------------|
| `x`           | array-like         | 柱子的位置，通常是一个类别列表或数值列表                           |
| `height`      | array-like         | 柱子的高度，表示每个柱子的数值大小                                 |
| `width`       | float or array-like | 柱子的宽度，默认为 0.8可以是一个数值或与柱子数量相同的数组       |
| `bottom`      | array-like         | 柱子的底部位置，默认为 0用于绘制堆叠柱状图时设置基础高度         |
| `align`       | str                | 柱子对齐方式，可以是 'center'（默认，居中对齐）或 'edge'（对齐边缘）|
| `data`        | dict or DataFrame  | 如果提供，可以从字典或 DataFrame 中读取数据                        |
| `**kwargs`    | 关键字参数         | 其他用于自定义柱子样式的参数，包括颜色、边框等                     |

常用关键字参数  

| 参数名          | 类型               | 说明                                                                 |
|-----------------|--------------------|----------------------------------------------------------------------|
| `color`         | color or array-like | 柱子的颜色，可以是单个颜色或与柱子数量相同的颜色数组               |
| `edgecolor`     | color or array-like | 柱子边框的颜色                                                     |
| `linewidth`     | float              | 柱子边框的宽度                                                     |
| `label`         | str                | 用于图例的标签                                                     |
| `alpha`         | float              | 柱子的透明度，取值范围为 0（完全透明）到 1（完全不透明）           |
| `hatch`         | str                | 柱子的填充图案，可以是 '/'、'\\'、'|'、'-'、'+'、'x'、'o'、'O'、'.'、'*' 等|


```python
# 示例数据
categories = ['A', 'B', 'C', 'D', 'E'] # 是一个列表，包含柱状图的类别名称
values = [15, 25, 30, 10, 20] # 是一个列表，包含每个类别对应的数值

# 绘制柱状图
plt.figure(figsize=(8, 6))  # 设置图形大小
plt.bar(categories, values, color='skyblue', edgecolor='black', label='Values')

# 添加标题和标签
plt.title('Bar Chart Example')
plt.xlabel('Categories')
plt.ylabel('Values')

# 添加图例
plt.legend()

# 显示图形
plt.show()
```

## plt.pie(sizes, labels=labels)饼图
plt.pie(sizes, explode=None, labels=None, colors=None, autopct=None, pctdistance=0.6, shadow=False,   
labeldistance=1.1, startangle=None, radius=None, counterclock=True, wedgeprops=None, textprops=None,   
center=(0, 0), frame=False, rotatelabels=False, *, data=None)    

参数说明  
| 参数名          | 类型               | 说明                                                                 |
|-----------------|--------------------|----------------------------------------------------------------------|
| `sizes`         | array-like         | 每个部分的大小，表示各个部分在整体中的比例。                         |
| `explode`       | array-like         | 每个部分的偏移量，用于突出显示某个部分。                             |
| `labels`        | list of str        | 每个部分的标签，用于标识饼图的各个部分。                             |
| `colors`        | array-like         | 每个部分的颜色，可以是单个颜色或与部分数量相同的颜色数组。           |
| `autopct`       | str or function    | 用于在饼图上显示百分比，可以是格式字符串或函数。                     |
| `pctdistance`   | float              | 百分比标签的距离，默认为 0.6。                                       |
| `shadow`        | bool               | 是否为饼图添加阴影效果。                                             |
| `labeldistance` | float              | 标签的距离，默认为 1.1。                                            |
| `startangle`    | float              | 饼图的起始角度，默认为 0 度（从右侧开始）。                          |
| `radius`        | float              | 饼图的半径，默认为 1。                                              |
| `counterclock`  | bool               | 是否按逆时针方向绘制饼图，默认为 True。                              |
| `wedgeprops`    | dict               | 用于自定义饼图部分的属性，如边框颜色、宽度等。                       |
| `textprops`     | dict               | 用于自定义文本属性的字典，如字体大小、颜色等。                       |
| `center`        | tuple of floats    | 饼图的中心位置，默认为 (0, 0)。                                     |
| `frame`         | bool               | 是否绘制饼图的外框。                                                 |
| `rotatelabels`  | bool               | 是否旋转标签以适应饼图。                                             |
| `data`          | dict or DataFrame  | 如果提供，可以从字典或 DataFrame 中读取数据。                        |


```python
import matplotlib.pyplot as plt

# 示例数据
sizes = [15, 30, 45, 10]  # 每个部分的大小
labels = ['A', 'B', 'C', 'D']  # 每个部分的标签

# 绘制饼图
plt.figure(figsize=(8, 6))  # 设置图形大小
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['lightcoral', 'lightskyblue', 'lightgreen', 'gold'])
# autopct='%1.1f%%' 用于在每个部分上显示百分比，保留一位小数
# startangle=90 用于设置饼图的起始角度为 90 度（从顶部开始）

# 添加标题
plt.title('Pie Chart Example')

# 显示图形
plt.show()
```

## plt.hist(data, bins=30)直方图
plt.hist(data, bins=30, range=None, density=None, weights=None, cumulative=False, bottom=None, histtype='bar',   
align='mid', orientation='vertical', rwidth=None, log=False, color=None, label=None, stacked=False, **kwargs)  

| 参数名          | 类型               | 说明                                                                 |
|-----------------|--------------------|----------------------------------------------------------------------|
| `data`          | array-like         | 输入数据，可以是单个数组或多个数组的列表。                           |
| `bins`          | int or array-like  | 直方图的柱子数量或柱子边界，默认为 30。                             |
| `range`         | tuple or None      | 数据的范围，用于限制显示的数据范围。                                 |
| `density`       | bool               | 如果为 True，则直方图的面积将归一化为 1。                            |
| `weights`       | array-like         | 每个数据点的权重。                                                   |
| `cumulative`    | bool               | 是否绘制累积直方图，默认为 False。                                   |
| `bottom`        | float or array-like | 柱子的底部位置，默认为 0。                                           |
| `histtype`      | str                | 直方图的类型，可以是 'bar'（默认）、'barstacked'、'step' 或 'stepfilled'。|
| `align`         | str                | 柱子的对齐方式，可以是 'left'、'mid'（默认）或 'right'。             |
| `orientation`   | str                | 直方图的方向，可以是 'vertical'（默认）或 'horizontal'。             |
| `rwidth`        | float              | 柱子的相对宽度，默认为 None，表示自动计算。                          |
| `log`           | bool               | 是否对计数使用对数刻度，默认为 False。                               |
| `color`         | color or array-like | 柱子的颜色，可以是单个颜色或与柱子数量相同的颜色数组。               |
| `label`         | str                | 用于图例的标签。                                                     |
| `stacked`       | bool               | 是否将多个数据集堆叠在一起，默认为 False。                           |
| `**kwargs`      | 关键字参数         | 其他用于自定义柱子样式的参数，包括边框颜色、线宽等。                 |


```python
import matplotlib.pyplot as plt
import numpy as np

# 生成随机数据
np.random.seed(42)  # 设置随机种子，以确保结果可重复
data = np.random.randn(1000)  # 生成 1000 个服从标准正态分布的随机数

# 绘制直方图
plt.figure(figsize=(8, 6))  # 设置图形大小
plt.hist(data, bins=30, color='skyblue', edgecolor='black', alpha=0.7, label='Data Distribution')

# 添加标题和标签
plt.title('Histogram Example')
plt.xlabel('Value')
plt.ylabel('Frequency')

# 添加图例
plt.legend()

# 显示图形
plt.show()
```

# 美化图形

## plt.title('Title') 标题
plt.title(label, fontdict=None, loc='center', pad=None, **kwargs)

参数说明

| 参数名      | 类型               | 说明                                                                 |
|-------------|--------------------|----------------------------------------------------------------------|
| `label`     | str                | 标题的文本内容。                                                     |
| `fontdict`  | dict               | 一个字典，用于指定标题的字体属性，例如字体大小、颜色、粗细等。       |
| `loc`       | str                | 标题的对齐方式，可以是 'left'、'center'（默认）或 'right'。          |
| `pad`       | float              | 标题与图形之间的间距，默认为 None，表示自动计算。                    |
| `**kwargs`  | 关键字参数         | 其他用于自定义标题样式的参数，包括字体大小、颜色、粗细等。           |

常用关键字参数

| 参数名      | 类型               | 说明                                                                 |
|-------------|--------------------|----------------------------------------------------------------------|
| `fontsize`  | int or float       | 标题的字体大小。                                                     |
| `color`     | color              | 标题的颜色。                                                         |
| `fontweight`| str or int         | 字体的粗细，可以是 'normal'、'bold'、'heavy'、'light'、'ultrabold' 等。|
| `style`     | str                | 字体的样式，可以是 'normal'、'italic' 或 'oblique'。                 |
| `verticalalignment` | str       | 标题的垂直对齐方式，可以是 'top'、'bottom'、'center' 或 'baseline'。|
| `horizontalalignment` | str     | 标题的水平对齐方式，可以是 'left'、'center' 或 'right'。            |


```python
import matplotlib.pyplot as plt
import numpy as np

# 生成随机数据
np.random.seed(42)
data = np.random.randn(1000)

# 绘制直方图
plt.figure(figsize=(8, 6))
plt.hist(data, bins=30, color='skyblue', edgecolor='black', alpha=0.7)

# 添加标题
plt.title('Distribution of Random Data', fontsize=14, color='navy', fontweight='bold')
#   'Distribution of Random Data' 是标题的文本内容
#   fontsize=14 设置标题的字体大小为 14
#   color='navy' 设置标题的颜色为海军蓝
#   fontweight='bold' 设置标题的字体为粗体
# 添加轴标签
plt.xlabel('Value')
plt.ylabel('Frequency')

# 显示图形
plt.show()
```

## plt.xlabel('X-axis Label') x轴标签
## plt.ylabel('Y-axis Label') y轴标签
plt.xlabel(xlabel, fontdict=None, labelpad=None, **kwargs)  
plt.ylabel(ylabel, fontdict=None, labelpad=None, **kwargs)  
参数说明

| 参数名      | 类型               | 说明                                                                 |
|-------------|--------------------|----------------------------------------------------------------------|
| `xlabel`    | str                | x 轴的标签文本内容。                                                 |
| `ylabel`    | str                | y 轴的标签文本内容。                                                 |
| `fontdict`  | dict               | 一个字典，用于指定标签的字体属性，例如字体大小、颜色、粗细等。       |
| `labelpad`  | float              | 标签与轴之间的距离，默认为 None，表示自动计算。                      |
| `**kwargs`  | 关键字参数         | 其他用于自定义标签样式的参数，包括字体大小、颜色、粗细等。           |

常用关键字参数

| 参数名      | 类型               | 说明                                                                 |
|-------------|--------------------|----------------------------------------------------------------------|
| `fontsize`  | int or float       | 标签的字体大小。                                                     |
| `color`     | color              | 标签的颜色。                                                         |
| `fontweight`| str or int         | 字体的粗细，可以是 'normal'、'bold'、'heavy'、'light'、'ultrabold' 等。|
| `style`     | str                | 字体的样式，可以是 'normal'、'italic' 或 'oblique'。                 |
| `labelpad`  | float              | 标签与轴之间的距离，默认为 None，表示自动计算。                      |


```python
import matplotlib.pyplot as plt
import numpy as np

# 生成随机数据
np.random.seed(42)
data = np.random.randn(1000)

# 绘制直方图
plt.figure(figsize=(8, 6))
plt.hist(data, bins=30, color='skyblue', edgecolor='black', alpha=0.7)

# 添加轴标签
plt.xlabel('Value', fontsize=12, color='darkgreen', fontweight='bold')
plt.ylabel('Frequency', fontsize=12, color='darkred', fontweight='bold')
#   'Value' 是 x 轴的标签文本内容。
#   'Frequency' 是 y 轴的标签文本内容。
#   fontsize=12 设置标签的字体大小为 12。
#   color='darkgreen' 和 color='darkred' 分别设置 x 轴和 y 轴标签的颜色。
#   fontweight='bold' 设置标签的字体为粗体。
# 添加标题
plt.title('Distribution of Random Data')

# 显示图形
plt.show()
```

## plt.legend() 图例
plt.legend(*args, **kwargs)
参数说明

| 参数名          | 类型               | 说明                                                                 |
|-----------------|--------------------|----------------------------------------------------------------------|
| `labels`        | list of str        | 每个数据系列的标签列表。                                             |
| `loc`           | str or int         | 图例的位置，可以是字符串（如 'upper right'、'lower left' 等）或整数（如 0、1 等）。|
| `bbox_to_anchor`| tuple of floats    | 用于将图例放置在图形外部的锚点坐标。                                 |
| `ncol`          | int                | 图例中每行显示的标签数量，默认为 1。                                 |
| `mode`          | str                | 图例的扩展模式，可以是 'expand' 或 None。                            |
| `borderaxespad` | float              | 图例与轴之间的间距，默认为 None。                                    |
| `borderpad`     | float              | 图例边框与图例内容之间的间距，默认为 None。                          |
| `handlelength`  | float              | 图例中每个条目的长度，默认为 None。                                  |
| `handletextpad` | float              | 图例中条目与文本之间的间距，默认为 None。                            |
| `axespad`       | float              | 图例与轴之间的间距，默认为 None。                                    |
| `labelspacing`  | float              | 图例中标签之间的垂直间距，默认为 None。                              |
| `frameon`       | bool               | 是否绘制图例的边框，默认为 True。                                    |
| `shadow`        | bool               | 是否为图例添加阴影效果，默认为 False。                               |
| `framealpha`    | float              | 图例边框的透明度，默认为 None。                                      |
| `facecolor`     | color              | 图例的背景颜色，默认为 None。                                        |
| `edgecolor`     | color              | 图例边框的颜色，默认为 None。                                        |
| `title`         | str                | 图例的标题。                                                         |
| `bbox_transform`| Transform          | 用于指定 `bbox_to_anchor` 的坐标系。                                 |
| `title_fontsize`| str or int         | 图例标题的字体大小，可以是 'xx-small'、'x-small'、'small'、'medium'、'large'、'x-large'、'xx-large' 或整数。|
| `prop`          | dict or FontProperties | 用于自定义图例文本的字体属性。                                       |
| `markerscale`   | float              | 图例中标记的缩放比例，默认为 None。                                  |
| `numpoints`     | int                | 图例中每个条目的标记数量，默认为 None。                              |
| `scatterpoints` | int                | 图例中散点图条目的标记数量，默认为 None。                            |
| `scatteryoffsets`| list of floats    | 散点图条目的垂直偏移量，默认为 None。                                |
| `markevery`     | int or list of ints | 用于指定图例中标记的显示间隔，默认为 None。                          |
| `**kwargs`      | 关键字参数         | 其他用于自定义图例样式的参数。                                       |


```python
import matplotlib.pyplot as plt
import numpy as np

# 生成随机数据
np.random.seed(42)
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# 绘制图形
plt.figure(figsize=(8, 6))
plt.plot(x, y1, label='sin(x)', color='blue', linestyle='-')
plt.plot(x, y2, label='cos(x)', color='red', linestyle='--')

# 添加图例
plt.legend(loc='upper right', fontsize=12, title='Functions', frameon=True, shadow=True)
#   - loc='upper right' 设置图例的位置为右上角。
#   - fontsize=12 设置图例的字体大小为 12。
#   - title='Functions' 为图例添加标题。
#   - frameon=True 和 shadow=True 分别为图例添加边框和阴影效果。
# 添加标题和轴标签
plt.title('Sine and Cosine Functions')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# 显示图形
plt.show()
```

## plt.xlim(xmin, xmax) x轴范围
## plt.ylim(ymin, ymax) y轴范围

plt.xlim(*args, **kwargs)
plt.ylim(*args, **kwargs)


参数说明

| 参数名   | 类型               | 说明                                                                 |
|----------|--------------------|----------------------------------------------------------------------|
| `xmin`   | float or int       | x 轴的最小值。                                                       |
| `xmax`   | float or int       | x 轴的最大值。                                                       |
| `**kwargs` | 关键字参数         | 其他用于自定义坐标轴的参数。                                         |



| 参数名   | 类型               | 说明                                                                 |
|----------|--------------------|----------------------------------------------------------------------|
| `ymin`   | float or int       | y 轴的最小值。                                                       |
| `ymax`   | float or int       | y 轴的最大值。                                                       |
| `**kwargs` | 关键字参数         | 其他用于自定义坐标轴的参数。                                         |


```python
import matplotlib.pyplot as plt
import numpy as np

# 生成随机数据
np.random.seed(42)
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 绘制图形
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='sin(x)', color='blue', linestyle='-')

# 设置坐标轴范围
plt.xlim(0, 5)  # 设置 x 轴显示范围为 0 到 5
plt.ylim(-1.5, 1.5)  # 设置 y 轴显示范围为 -1.5 到 1.5

# 添加图例、标题和轴标签
plt.legend(loc='upper right')
plt.title('Sine Function')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# 显示图形
plt.show()
```

## plt.grid() 网格线
plt.grid(b=None, which='major', axis='both', **kwargs)  
参数说明

| 参数名      | 类型               | 说明                                                                 |
|-------------|--------------------|----------------------------------------------------------------------|
| `b`         | bool               | 是否显示网格线。如果为 True，则显示网格线；如果为 False，则不显示。默认情况下，如果 `grid` 之前未被调用，则网格线默认不显示。|
| `which`     | str                | 指定要显示的网格线类型，可以是 'major'（主要网格线）、'minor'（次要网格线）或 'both'（同时显示主要和次要网格线）。默认为 'major'。|
| `axis`      | str                | 指定要在哪个轴上显示网格线，可以是 'x'（仅 x 轴）、'y'（仅 y 轴）或 'both'（同时在 x 和 y 轴上）。默认为 'both'。|
| `**kwargs`  | 关键字参数         | 其他用于自定义网格线样式的参数。                                       |

常用关键字参数

| 参数名          | 类型               | 说明                                                                 |
|-----------------|--------------------|----------------------------------------------------------------------|
| `color`         | color              | 网格线的颜色。                                                       |
| `linestyle`     | str                | 网格线的样式，可以是 '-'（实线）、'--'（虚线）、'-.'（点划线）、':'（点线）等。|
| `linewidth`     | float              | 网格线的宽度。                                                       |
| `alpha`         | float              | 网格线的透明度，范围为 0（完全透明）到 1（完全不透明）。              |


```python
import matplotlib.pyplot as plt
import numpy as np

# 生成随机数据
np.random.seed(42)
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 绘制图形
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='sin(x)', color='blue', linestyle='-')

# 添加网格线
plt.grid(True, which='both', axis='both', color='gray', linestyle='--', alpha=0.5)
#   - True 表示显示网格线。
#   - which='both' 表示同时显示主要和次要网格线。
#   - axis='both' 表示在 x 和 y 轴上都显示网格线。
#   - color='gray' 设置网格线的颜色为灰色。
#   - linestyle='--' 设置网格线的样式为虚线。
#   - alpha=0.5 设置网格线的透明度为 0.5。
# 添加图例、标题和轴标签
plt.legend(loc='upper right')
plt.title('Sine Function with Grid')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# 显示图形
plt.show()
```

## plt.xticks() x轴
## plt.yticks() y轴
设置 x 轴刻度位置和标签的函数  
plt.xticks(ticks=None, labels=None, **kwargs)  
参数说明

| 参数名      | 类型               | 说明                                                                 |
|-------------|--------------------|----------------------------------------------------------------------|
| `ticks`     | array-like         | 一个数组或列表，指定 x 轴上要显示的刻度位置。如果为 None，则使用默认的刻度位置。|
| `labels`    | array-like         | 一个数组或列表，指定每个刻度位置对应的标签。如果为 None，则使用默认的刻度标签。|
| `rotation`  | float              | 刻度标签的旋转角度，以度为单位。默认为 0，即不旋转。                 |
| `**kwargs`  | 关键字参数         | 其他用于自定义刻度标签样式的参数。                                   |

常用关键字参数

| 参数名          | 类型               | 说明                                                                 |
|-----------------|--------------------|----------------------------------------------------------------------|
| `fontsize`      | int or float       | 刻度标签的字体大小。                                                 |
| `color`         | color              | 刻度标签的颜色。                                                     |
| `ha`            | str                | 刻度标签的水平对齐方式，可以是 'center'、'right' 或 'left'。          |
| `va`            | str                | 刻度标签的垂直对齐方式，可以是 'center'、'top' 或 'bottom'。          |


```python
import matplotlib.pyplot as plt
import numpy as np

# 生成随机数据
np.random.seed(42)
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 绘制图形
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='sin(x)', color='blue', linestyle='-')

# 设置 x 轴刻度
plt.xticks(ticks=[0, 2, 4, 6, 8, 10], labels=['Zero', 'Two', 'Four', 'Six', 'Eight', 'Ten'], rotation=45, fontsize=12, color='red')
#   - ticks=[0, 2, 4, 6, 8, 10] 指定 x 轴上显示的刻度位置。
#   - labels=['Zero', 'Two', 'Four', 'Six', 'Eight', 'Ten'] 指定每个刻度位置对应的标签。
#   - rotation=45 将刻度标签旋转 45 度。
#   - fontsize=12 设置刻度标签的字体大小为 12。
#   - color='red' 设置刻度标签的颜色为红色。
# 添加图例、标题和轴标签
plt.legend(loc='upper right')
plt.title('Sine Function with Custom X-Ticks')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# 显示图形
plt.show()
```

## plt.axis() 坐标轴范围
设置或获取图形坐标轴范围的函数。它可以用于控制图形的显示范围，以便更好地展示数据的特定部分或细节  
plt.axis(*args, **kwargs)  
参数说明  

`plt.axis()` 函数可以通过多种方式调用，具体参数取决于调用方式：

1. **获取当前坐标轴范围**

>   ```python
>   plt.axis()
>   ```

   这个调用方式不接受任何参数，并返回一个包含四个元素的元组，表示当前坐标轴的范围 `(xmin, xmax, ymin, ymax)`。

2. **设置坐标轴范围**

>   ```python
>   plt.axis([xmin, xmax, ymin, ymax])
>   ```

   - `xmin` 和 `xmax`：设置 x 轴的最小值和最大值。
   - `ymin` 和 `ymax`：设置 y 轴的最小值和最大值。

3. **使用关键字参数设置坐标轴范围**

>   ```python
>   plt.axis(xmin=xmin_value, xmax=xmax_value, ymin=ymin_value, ymax=ymax_value)
>   ```

   - `xmin` 和 `xmax`：设置 x 轴的最小值和最大值。
   - `ymin` 和 `ymax`：设置 y 轴的最小值和最大值。

4. **特殊选项**

>   ```python
>   plt.axis('auto')
>   plt.axis('tight')
>   plt.axis('equal')
>   plt.axis('scaled')
>   plt.axis('normal')
>   plt.axis('off')
>   ```

   - `'auto'`：自动调整坐标轴范围以适应数据。
   - `'tight'`：设置坐标轴范围以包含所有数据。
   - `'equal'`：设置 x 和 y 轴的缩放比例相同，使图形显示为正方形。
   - `'scaled'`：类似于 `'equal'`，但不会强制 x 和 y 轴的缩放比例相同。
   - `'normal'`：恢复到默认的坐标轴范围。
   - `'off'`：隐藏坐标轴。


```python
import matplotlib.pyplot as plt
import numpy as np

# 生成随机数据
np.random.seed(42)
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 绘制图形
plt.figure(figsize=(8, 6))
# 原图
plt.subplot(211)
plt.plot(x, y, label='sin(x)', color='blue', linestyle='-')
# plt.axis('auto')
# 添加图例、标题和轴标签
plt.legend(loc='upper right')
plt.title('No Custom Axis')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# 范围图
plt.subplot(2,1,2)
plt.plot(x, y, label='sin(x)', color='blue', linestyle='-')
# 设置坐标轴范围
plt.axis([0, 5, -1.5, 1.5]) #设置 x 轴的范围为 0 到 5，y 轴的范围为 -1.5 到 1.5
print(plt.axis()) #  打印范围
# 添加图例、标题和轴标签
plt.legend(loc='upper right')
plt.title('Sine Function with Custom Axis')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# 显示图形
plt.tight_layout()
plt.show()
```

# 调整子图布局
## plt.tight_layout() 自动调整子图间距
避免重叠 
## plt.subplots_adjust() 手动调整子图间
`plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)`

# 保存和显示图形
## plt.savefig() 将图形保存为文件
`plt.savefig('plot.png', dpi=300, bbox_inches='tight')`

| 参数 | 描述 |
| --- | --- |
| `fname` | 指定保存的文件名或文件路径。支持多种图像格式 `'png'`、`'jpg'`、`'pdf'`、`'svg'`、`'eps'` 等。如果未指定扩展名，`matplotlib` 会根据文件名的扩展名决定保存的格式。 |
| `dpi` | 设置图像的分辨率（每英寸点数）。默认值为 `100`。较高的 `dpi` 会生成更高分辨率的图像，但文件大小也会更大。 |
| `quality` | 设置图像质量，适用于 `'jpg'` 格式。取值范围为 `1`（最低质量）到 `95`（最高质量），默认值为 `95`。 |
| `optimize` | 对于 `'png'` 格式，启用优化选项，减少文件大小。 |
| `transparent` | 如果设置为 `True`，保存的图像背景将为透明。 |
| `bbox_inches` | 指定保存图像的边界框。可以使用 `'tight'` 自动裁剪图像以去除空白区域，也可以手动指定边界框。 |
| `facecolor` 和 `edgecolor` | 设置保存图像的背景颜色和边框颜色。 |
| `format` | 显式指定保存的图像格式，覆盖文件名的扩展名。 |

注意：  
在调用 plt.savefig() 之前，确保已经绘制了所有需要的图形元素（例如标题、标签、图例等），因为 savefig() 会保存当前图形的状态  
plt.savefig() 应该在 plt.show() 之前调用，因为 plt.show() 会清除图形状态，导致无法保存  
使用 bbox_inches='tight' 可以自动裁剪图像，去除多余的空白区域，使保存的图像更加紧凑  

## plt.show() 显示图形 
## plt.imshow() 显示图片 

| 参数 | 描述 |
| --- | --- |
| **`X`** | 要显示的图像数据，可以是二维数组（灰度图像）或三维数组（RGB 图像）。 |
| **`cmap`** | 指定颜色映射（colormap），用于将数值映射到颜色。例如，`'viridis'`、`'plasma'`、`'gray'`、`'hot'` 等。 |
| **`vmin`** 和 **`vmax`** | 设置颜色映射的范围。`vmin` 是最小值，`vmax` 是最大值。 |
| **`alpha`** | 设置图像的透明度，范围为 `0`（完全透明）到 `1`（完全不透明）。 |
| **`interpolation`** | 指定插值方法，用于在像素之间进行插值。例如，`'nearest'`、`'bilinear'`、`'bicubic'` 等。 |
| **`aspect`** | 控制图像的纵横比。例如，`'auto'`、`'equal'` 或一个浮点数。 |
| **`origin`** | 设置图像的原点位置。`'upper'`（默认）或 `'lower'`。 |
| **`extent`** | 设置图像的边界范围，格式为 `[left, right, bottom, top]`。 |
| **`norm`** | 指定一个 `Normalize` 实例，用于将数据标准化到 `[0, 1]` 范围。 |
| **`resample`** | 当图像缩放时，指定是否使用插值。如果 `interpolation` 设置为 `'none'`，则忽略此参数。 |
| **`url`** | 设置图像的超链接，用于交互式环境中的点击跳转。 |


- `plt.imshow()` 显示的是数组数据，因此要确保数组的形状和类型与期望的图像类型匹配。
- 使用 `plt.colorbar()` 可以添加颜色条，显示颜色映射的数值范围。
- 参数 `interpolation` 可以用于调整图像的显示效果，尤其是在放大或缩小图像时。
- 参数 `origin` 和 `extent` 可以用于调整图像在坐标系中的位置和范围。


```python
import matplotlib.pyplot as plt
import numpy as np

# 创建一个简单的图像数据
image_data = np.random.rand(10, 10)  # 随机生成一个 10x10 的矩阵

# 显示图像并设置颜色映射和范围
plt.imshow(image_data, cmap='hot', vmin=0, vmax=1, interpolation='bilinear', aspect='auto')

# 添加颜色条
plt.colorbar()

# 显示图形
plt.show()
```

# 多子图绘制
## plt.subplots()
一次性创建多个子图，返回一个图形对象和子图数组  
>```
>fig, axes = plt.subplots(2, 2, figsize=(10, 8))
>axes[0, 0].plot(x, y)  # 在第一个子图中绘图
>```

# 自定义样式
| 名称 | 简述 |
| --- | --- |
| `'default'` | `matplotlib` 的默认风格，简单线条和颜色，适合快速绘制基础图表 |
| `'classic'` | 经典 `matplotlib` 风格，与较早版本风格相似 |
| `'bmh'` | 模仿 JMP 软件默认风格，有独特布局和配色 |
| `'fivethirtyeight'` | 模仿 FiveThirtyEight 网站风格，粗线条、大字体，适合数据新闻等 |
| `'ggplot'` | 模仿 R 语言 `ggplot2` 包风格，简洁美观，白色背景灰色网格线 |
| `'xkcd'` | 模仿 xkcd 漫画风格，幽默随性，适合非正式场合 |
| `'seaborn'` | 基于 `Seaborn` 库的基础风格，现代感，美观专业 |
| `'seaborn-bright'` | `Seaborn` 明亮颜色风格，鲜艳夺目，突出数据差异 |
| `'seaborn-colorblind'` | `Seaborn` 色盲优化颜色方案，提高信息可访问性 |
| `'seaborn-dark'` | `Seaborn` 深色风格，适合浅色背景演示或网页 |
| `'seaborn-darkgrid'` | `Seaborn` 深色背景加网格线风格，方便读取数据 |
| `'seaborn-deep'` | `Seaborn` 颜色较深且丰富风格，表现数据层次感 |
| `'seaborn-muted'` | `Seaborn` 柔和低调颜色风格，优雅专业不刺眼 |
| `'seaborn-notebook'` | 模仿 Jupyter Notebook 风格，适合 Notebook 数据分析展示 |
| `'seaborn-paper'` | `Seaborn` 适合学术论文打印风格，简洁清晰 |
| `'seaborn-pastel'` | `Seaborn` 柔和粉彩色调风格，温馨舒适 |
| `'seaborn-poster'` | `Seaborn` 适合海报等大幅面展示风格，字体元素大 |
| `'seaborn-talk'` | `Seaborn` 适合幻灯片演示风格，字体大小和线条粗细适中 |
| `'seaborn-ticks'` | `Seaborn` 强调坐标轴刻度风格，方便读取数据 |
| `'seaborn-white'` | `Seaborn` 白色背景风格，简洁明了 |
| `'seaborn-whitegrid'` | `Seaborn` 白色背景加网格线风格，简洁且方便读取数据 |
| `'dark_background'` | 深色背景风格，适合浅色背景演示或网页 |
| `'fast'` | 快速样式，可能在绘制速度或资源占用上优化 |
| `'grayscale'` | 灰度风格，只显示黑白颜色，适合黑白打印等 |
| `'tableau-colorblind10'` | 基于 Tableau 的色盲友好颜色方案，10 种适合色盲分辨的颜色 |


```python
# 全局样式设置：
plt.style.use('ggplot')  # 使用预设样式
# 自定义颜色和线型：
plt.plot(x, y, color='#FF5733', linewidth=2, linestyle=':')
```


```python
plt.style.use('default') # 恢复默认
```

# 中文显示支持

| 字体名称           | `matplotlib` 中的写法                  |
|--------------------|----------------------------------------|
| **黑体**         | `plt.rcParams['font.sans-serif'] = ['SimHei']`          |
| **微软雅黑** | `plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']`  |
| **宋体**         | `plt.rcParams['font.sans-serif'] = ['SimSun']`            |
| **仿宋**       | `plt.rcParams['font.sans-serif'] = ['FangSong']`          |
| **楷体**          | `plt.rcParams['font.sans-serif'] = ['KaiTi']`             |
| **Arial Unicode MS** | `plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']` |
| **Noto Sans CJK SC** (简体中文) | `plt.rcParams['font.sans-serif'] = ['Noto Sans CJK SC']` |
| **Noto Sans CJK TC** (繁体中文) | `plt.rcParams['font.sans-serif'] = ['Noto Sans CJK TC']` |
| **文泉驿正黑** | `plt.rcParams['font.sans-serif'] = ['WenQuanYi Zen Hei']` |



```python
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用于支持中文
plt.rcParams['axes.unicode_minus'] = False  # 用于正常显示负号
```
