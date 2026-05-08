# 一  列表
定义


```python
number=[1,2,3,4,5]
mixed=["amy",1.34,True]
kong=[]#空列表
```

## 1 切片操作


```python
number=[1,2,3,4,5]
sub_list = number[1:4]  # 对应下标为1，2，3，左闭右开 array[start:stop:step]
# 输出[2, 3, 4] 
print(sub_list)
```

## 2 长度和成员关系


```python
length = len(number)  # 3
is_2_in_list = 2 in number  # True
# in 用于检查一个值是否存在于某个序列（如列表、元组、字符串或集合）中。如果值存在，则返回 True，否则返回 False。
# is 用于检查两个变量是否引用同一个对象（即它们的内存地址是否相同）。这与检查两个变量是否具有相等的值不同。
```

## 3迭代


```python
number=[1,2,3,4]
for num in number:
    print(num)
```

## 4方法*


```python
#append 向列表末尾添加一个元素
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)  # 输出：[1, 2, 3, 4]

#extend 将可迭代对象的元素添加到列表末尾。
number1 = [1, 2, 3]
number2= [4, 5]
number1.extend(number2)
print(number1)  # 输出：[1, 2, 3, 4, 5]

#index 返回元素在列表中第一次出现的索引
numbers = [1, 2, 3, 2]
index = numbers.index(2)
print(index)  # 输出：1

#insert 在指定索引处插入一个元素。
numbers = [1, 2, 3]
numbers.insert(1, 4)
print(numbers)  # 输出：[1, 4, 2, 3]

#remove 从列表中移除指定的元素（第一个匹配项）
numbers = [1, 2, 3, 2]
numbers.remove(2)
print(numbers)  # 输出：[1, 3, 2]

#pop 移除并返回指定索引处的元素，如果不指定索引，默认移除并返回最后一个元素。
numbers = [1, 2, 3]
popped_element = numbers.pop(1)
print(popped_element)  # 输出：2

#count 计算元素在列表中出现的次数。
numbers = [1, 2, 3, 2, 2]
count = numbers.count(2)
print(count)  # 输出：3

#sort 对列表进行原地排序
numbers = [3, 1, 2]
numbers.sort()
print(numbers)  # 输出：[1, 2, 3]

#reverse 将列表中的元素反转
numbers = [1, 2, 3]
numbers.reverse()
print(numbers)  # 输出：[3, 2, 1]

#clear
#copy
```

## list函数


```python
# list() 函数是一个内置函数，用于创建一个新的列表。这个函数可以接受任何可迭代对象（比如字符串、元组、集合、字典的键或值等）以及range作为输入，并将其转换为一个列表。
s = "hello"
lst = list(s)
print(lst)  # 输出: ['h', 'e', 'l', 'l', 'o']
tup = (1, 2, 3)
lst = list(tup)
print(lst)  # 输出: [1, 2, 3]
dict1 = {'a': 1, 'b': 2, 'c': 3}
keys_lst = list(dict1.keys())
values_lst = list(dict1.values())
print(keys_lst)  # 输出: ['a', 'b', 'c']
print(values_lst)  # 输出: [1, 2, 3]
```

# 二 字符串

1 基础


```python
# 单引号、双引号、三引号(用于多行)
# 在三引号中够可以自由使用单双引号
# 转义：单双引号、斜杆(\)等：'what\'s your \\name?'
# 用多行表达一行：
# "this is the first line.\
# this is the second line."
```

2 方法


```python
#capitalize 将字符串的第一个字符大写
#upper 将字符串中的所有字符转换为大写
#lower 将字符串中的所有字符转换为小写
#replace(old, new) 替换字符串中的指定子串

#startwith 检查是否以特定字符开头
text = "Hello, World"
starts_with_hello = text.startswith("Hello")
print(starts_with_hello)  # 输出：True

#endwith
#split 将字符串分割成子字符串列表，使用指定的分隔符
text = "apple,banana,kiwi"
fruits = text.split(",")
print(fruits)  # 输出：['apple', 'banana', 'kiwi']
```

# 三 元组

1方法


```python
#.count 计算元组中指定元素出现的次数
numbers = (1, 2, 2, 3, 2)
count = numbers.count(2)
print(count)  # 输出：3

#.index

#len() 返回元组中元素的个数
numbers = (1, 2, 3)
length = len(numbers)
print(length)  # 输出：3

#sorted() 返回一个新的列表，其中包含了排序后的元组元素。
fruits = ("banana", "apple", "cherry")
sorted_fruits = sorted(fruits)
print(sorted_fruits)  # 输出：['apple', 'banana', 'cherry']

#sum 返回元组中所有数值元素的总和（仅适用于包含数值的元组)
numbers=(1,2,3,4)
total=sum(numbers)
print (total) # 输出：10

#min
numbers = (5, 2, 8, 1, 3)
minimum = min(numbers)
print(minimum)  # 输出：1

#max
numbers = (5, 2, 8, 1, 3)
maximum = max(numbers)
print(maximum)  # 输出：8
```

# 四 集合

1 方法


```python
#add
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)  # 输出：{'apple', 'cherry', 'banana', 'orange'}

#update 合并可迭代集合
colors = {"red", "green", "blue"}
additional_colors = {"yellow", "purple"}
colors.update(additional_colors)
print(colors)  # 输出：{'red', 'green', 'yellow', 'purple', 'blue'}

#remove 从集合中移除指定元素，如果元素不存在则引发 KeyError 异常
numbers = {1, 2, 3, 4}
numbers.remove(2)
print(numbers)  # 输出：{1, 3, 4}

#discard 从集合中移除指定元素，如果元素不存在则不引发异常
numbers = {1, 2, 3, 4}
numbers.discard(5)
print(numbers)  # 输出：{1, 2, 3, 4} 

#pop 移除并返回集合中的任意一个元素
colors = {"red", "green", "blue"}
popped_color = colors.pop()
print(popped_color)  # 输出：'red' 或 'green' 或 'blue' 

#clear 清空
numbers = {1, 2, 3}
numbers.clear()
print(numbers)  # 输出：set()

#len()
numbers={1,2,3,4}
lenth=len(numbers)
print(lenth) # 输出：4

#union 返回两个集合的并集
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)  # 输出：{1, 2, 3, 4, 5}

#.intersection
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.intersection(set2)
print(union_set)  # 输出：{3}

#copy
fruits = {"apple", "banana", "cherry"}
fruits_copy = fruits.copy()
print(fruits_copy)  # 输出：{'apple', 'cherry', 'banana'}
```

# 五 字典


```python
student = { #建立字典
   'name': 'Alice', 
   'age': 25, 
   'grade': 'A'
}
            #使用中括号
name=student['name']
age=student['age']  #访问
print(name)

student['age']=26   #修改
student['nation']='china' #添加
print(age)

del student['grade']  #删除
nation = student.pop('nation') #pop方法删除并获取值
print(nation)

for key in student:  #遍历键 
    print(key)

for value in student.values():  #遍历值
    print(value)

for key,value in student.items():   #遍历键值对
    print(key,value)

if 'name' in student:           #检查键是否在字典中
    print("Name exists in the dictionary")

# 获取所有的键
keys = student.keys()
print(keys)
# 获取所有的值
values = student.values()
print(values)
# 获取所有的键值对
items = student.items()
print(items)
```

1 方法


```python
# 使用 update 方法合并字典
additional_info = {'hobby': 'reading', 'country': 'USA'}
student.update(additional_info)

# 使用 copy 方法复制字典
dict_copy = student.copy()

# 清空字典中的所有键值对
student.clear()
```

# 六 推导式


```python
#列表推导式
# new_list = [expression for item in iterable if condition]
# condition 是一个可选的条件表达式，用于筛选元素。只有当条件为真时，当前元素才会被包含在新列表中。
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x ** 2 for x in numbers]
print(squared_numbers)
other_numbeers=[x ** 2 for x in numbers if x%2==0]
print(other_numbeers)# [4, 16]

#集合推导式
numbers = [1, 2, 2, 3, 3, 4, 5]
unique_numbers = {x for x in numbers}
print(unique_numbers)

#字典推导式
fruits = ["apple", "banana", "cherry"]
fruit_lengths = {x: len(x) for x in fruits}
print(fruit_lengths)# {'apple': 5, 'banana': 6, 'cherry': 6}

```

# 七 生成器


```python
#生成器函数
#生成器函数是一个包含 yield 语句的函数
# 当调用生成器函数时，它不会立即执行，而是返回一个生成器对象
# 每次迭代生成器时，函数会从上一次 yield 语句暂停
# 并在下一次迭代时从上一次暂停的地方继续执行，直到函数结束或再次遇到 yield
def generator():
    yield 1
    yield 2
    yield 3
my_generator=generator()
for i in my_generator:
    print(i)
# 输出：1 2 3
```


```python
#生成器表达式
# 生成器表达式是一种类似于列表推导式的表达式
# 使用圆括号 () 而不是方括号 []
# 它返回一个生成器对象
generator=(x for x in range(6))
for i in generator:
    print(i)
# 输出：0,1,2,3,4,5
```

# 八 if elif else


```python
# 三元表达式
n = 123
print('yes' if n%2==0 else 'no') # 奇数，输出 yes
```

# 九 while for


```python
for i in range(5):
    print("a")    # 执行循环体内的代码，循环 5 次，i 从 0 到 4
for char in "Hello":
    print(char)# 执行与 char 相关的操作，char 依次是 "H"、"e"、"l"、"l"、"o"
dict = {"name": "John", "age": 30}
for key in dict:
    # 遍历字典的键
    print(key)  # 输出: "name", "age"
for value in dict.values():
    # 遍历字典的值
    print(value)  # 输出: "John", 30
for key, value in dict.items():
    # 遍历字典的键值对
    print(key, value)  # 输出: "name John", "age 30"
    
```

1 print格式


```python
#enumerate() 函数用于同时获取元素的索引和值
list=["a","b","c"]
for index,value in enumerate(list):
    print(index,value)

#break 用于跳出循环，而 continue 用于跳过当前循环的迭代

#嵌套
for i in range(9):
  for j in range(9):
    if j<=i:
      print(str(i+1)+'*'+str(j+1)+'='+'{: >2}'.format(str((i+1)*(j+1))),end=' ')
#{} 这对大括号是格式化字符串的占位符，用于插入变量或表达式的值。
#: 分隔符，用于分隔格式说明符的开始
#^ 这是一个对齐符号，表示居中对齐。在这个例子中，>用于将数字在宽度为2的区域内居右对齐。  
#2 这表示格式化的宽度。在这个例子中，它指定了至少要有2个字符宽的空间来显示数字。

#.format() 方法用于字符串格式化
# name = "Alice"
# age = 30
# print("My name is {} and I am {} years old.".format(name, age))
# 在这个例子中，{} 是占位符，format() 方法将 name 和 age 变量的值分别插入到这两个占位符中

#end 默认情况下是 '\n',但你可以将其设置为任何字符串，包括空字符串 ''
# print("Hello", end=' ')
# print("World")
# 输出结果：
# Hello World

  print('')#默认换一行

#for 循环可以与 else 子句一起使用，当循环正常结束时执行 else 中的代码          
for i in range(5):
   print(i)
else:
   print("循环结束")

```

# 十 异常处理


```python
# - 使用 `try` 块来包裹可能会引发异常的代码。
# - 使用 `except` 块来捕获并处理特定类型的异常。
# - 可以在 `except` 块中添加多个异常类型，或使用通用的 `except` 块。
# - 使用 `finally` 块来执行无论是否发生异常都会执行的代码。
try:
    # 代码块，可能会引发异常
    num = int(input("请输入一个整数: "))
    result = 10 / num
except ZeroDivisionError:
    # 处理除以零的异常
    print("不能除以零！")
except ValueError:
    # 处理输入无效的整数的异常
    print("请输入有效的整数！")
except Exception as e:
    # 处理其他异常
    print("发生了未知错误：", e)
else:
    # 没有异常发生时执行的代码
    print("结果是：", result)
finally:
    # 无论是否发生异常，都会执行的代码
    print("程序执行完毕！") 

# Python 还有一些内置的常见异常类，如下所示：
# 1. TypeError：            当操作或函数对不支持的数据类型执行操作时引发的异常。
# 2. IndexError：           在使用索引访问列表、元组或其他序列时引发的异常，当索引超出范围时出现。
# 3. NameError：            当访问一个不存在的变量或名称时引发的异常。
# 4. ValueError：           在函数接收到正确类型但无效值的参数时引发的异常。
# 5. KeyError：             当试图在字典中查找不存在的键时引发的异常。
# 6. FileNotFoundError：    在试图打开不存在的文件时引发的异常。
# 7. OSError：              在操作系统级别发生错误时引发的异常。
# 8. ZeroDivisionError：    在除以零时引发的异常。
# 9. AttributeError：       当试图访问对象没有的属性时引发的异常。
# 10. ImportError：         在导入模块失败时引发的异常。
```

# 十一 逻辑运算符和条件表达式


```python
# end or not

# 条件表达式（三元运算符）：
x = 10
message = "true" if x > 0 else "false"
# true_value if condition else false_value
print(message)

# is 和 is not 是用于检查两个对象是否是同一个对象（内存地址)，而不仅仅是值是否相等
x=[1,2,3]
y=[1,2,3]
z=x
print(x is y) #False
print(x is z) #True
print(x is not y) #True
if x==y:
   print("x==y")
if x==z:
   print("x==z")
if x is y:
   print("x is y")
if(x is z):
   print("x is z")

# 来检查变量 x 是否为真值（即非零、非空、非空字符串、非空列表等）
if x is True:
   print("x is true")
else:
   print("x is not true")
if x:
  print("x is True")
else:
    print("x is not True")

```


```python
# try ... except

# 完整结构：
# try:
#     # 可能出错
# except:
#     # 出错执行
# else:
#     # 没出错才执行
# finally:
#     # 无论出不出错，最后一定执行（常用于关闭文件、释放资源）

try:
    num = int(input("输入数字："))
    print(10 / num)
except ZeroDivisionError:
    print("不能除以0")
except ValueError:
    print("你输入的不是数字")

try:
    int("abc")
except Exception as e:
    print("错误类型：", type(e))
    print("错误信息：", e)    
```

# 十二 注释


```python
#多行注释（块注释）：三个单引号 ''' 或三个双引号 """ 
'''
包围的多行文本将被视为注释。
多行注释可以用于多行代码块或函数的说明。
'''
#文档字符串（Docstring）：在函数、类、模块等定义的第一个语句可以用作文档字符串，也就是对定义的对象进行详细的注释说明。
#文档字符串可以通过 help() 函数获取。文档字符串的内容应包含对对象的描述、参数、返回值等信息
def add(a, b):
    """
    This function adds two numbers.
    
    :param a: The first operand.
    :param b: The second operand.
    :return: The sum of a and b.
    """
    return a + b

class MyClass:
    """
    This is a sample class.
    It demonstrates the usage of docstrings.
    """
    def __init__(self, value):
        """
        Constructor for MyClass.
        
        :param value: An initial value for the class instance.
        """
        self.value = value
print(add(1,2))
help(add)
help(MyClass)

# 文档字符串中除了 `:param` 和 `:return` 外，还有一些其他常用的标记：
# :param name: description`描述函数或方法的参数，其中 `name` 是参数的名称，`description` 是参数的说明。
# :type name: type` 指定参数的数据类型。
# :rtype: type` 指定返回值的数据类型。
# :raises ExceptionType: description` 描述函数可能抛出的异常。
# :return: description` 描述函数的返回值。
# :example: 给出一个示例代码块，说明如何使用函数或方法。
# :note:提供附加信息或注意事项。
# :warning: 给出警告信息。


```

# 十三 函数


```python
# 默认参数
def greet(name,greeting="hello"):
    print(f"{greeting},{name}!")
greet("Bob","Hi")
greet("Amy")#未给出，默认hello
print("\n")

# 关键字参数
def pet(animal,name):
    print(f"My {animal} named {name}")
pet("dog","pidan")
pet(name="mimi",animal="cat")#指定位置
print("\n")

# *args 和 **kwargs
# 让函数接受任意数量的位置参数和关键字参数
#通过 *args，可以将传递的位置参数打包成一个元组。通过 **kwargs，可以将传递的关键字参数打包成一个字典
def function(*args,**kwargs):
    print("*args:")
    for arg in args:
        print(arg)
    print("**kwargs:")
    for key,value in kwargs.items(): #注意括号
        print(f"{key}: {value}")
function(1,2,3,name="Lili",age="30")
print("\n")

# 多返回值
# 你可以在函数的 return 语句中指定多个值，Python 会自动将这些值打包成一个元组，然后返给调用者。
def student(id):
    if id == 0:
        return "Bob",18
    elif id == 1:
        return "Amy",17
    else:
        return "unknow",0
name,age=student(1)
print(f"This id is {name},{age}")
```


```python

# 按值和按引用传递
# 在Python中，函数参数传递的是对象的内存地址，而不是对象本身的副本
def modify(lst):
    lst.append(4)
    print("Inside function:", lst)
my_list=[1,2,3]
print("Before function call:", my_list)
modify(my_list)
print("After function call:", my_list)#函数内部对列表的修改也反映在了原始列表 my_list 上，这是因为 modify_list 函数接收的是 my_list 的引用，而不是它的副本。
                                      #可改变的包括列表，字典  不可改变的包括整数，浮点数，字符串，元组等
```


```python
# 函数嵌套
def outer_function(x):
    # 适用函数内部做了复杂运算，且外部函数中要多次调用，且这个函数不希望其他外部函数调用
    def inner_function(y):
        return y*2
    return inner_function(x)
print(outer_function(1))

#递归

#回调函数
def hander(event,back):#以函数作为函数参数
    print(f"{event}")
    back()
def callback():
    print("called")
hander("a",callback)

#lambda函数
add = lambda x,y:x+y
print(add(2,3))
square = lambda x:x**2
print(square(4))
```


```python
#闭包
# 闭包是指在一个函数内部定义的函数，并且内部函数可以引用外部函数的变量
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function
closure = outer_function(10)
result = closure(5)
print(result)  # 输出 15


```

# 十四 输入输出与格式化

1 input print


```python
# input() 函数返回的结果是一个字符串
# name = input("请输入您的姓名：")
# age = int(input("请输入您的年龄："))
# 多个输入
a,b=input().split() #用户输入1 2，则a='1' b='2'
a,b,c=input().split()
a,b,c=map(int,input().split()) # map对第二个参数的每一项做第一个参数的运算
# 更多输入
#lst1=input().split() #lst1中存储了用户输入的字符串分离后的列表
#lst1=map(int,input().split())
list1=input().split()#hello world
print(list1)#['hello', 'world']

# print(*objects, sep=' ', end='\\n', file=sys.stdout, flush=False)
# objects: 复数，表示可以一次输出多个对象。输出多个对象时，需要用逗号分隔
# sep: 用来间隔多个对象，默认值是一个空格。
# end: 用来设定以什么结尾，默认值是换行符\\n，我们可以换成其他字符串
# file: 要写入的文件对象，默认值是标准输出sys.stdout
    # stdout= standard output 控制台
# flush: 输出是否被缓存通常决定于file，但如果flush关键字参数为True，流会被强制刷新

print("Hello", "world", "!") # 输出结果为 Hello world ! 默认空格分隔
print("Hello", "world", "!",sep="-")
print("Hello","world",end="!!!")

# 使用file参数
# f = open("output.txt", "w") # 打开一个文件，模式为写入
# print("Hello, file!", file=f) # 将输出写入文件中
# f.close() # 关闭文件
```

2 format


```python
# format 见第九章第一节
print('{:+}'.format(10))# 冒号后面是填充的字符
print('{:,}'.format(10000000))# 千位分隔符
print('{:_<10}'.format("hello"))# <左对齐,10宽度
print('{:06d}'.format(5))#填充0，长度6，整型
print('{:.2f}'.format(3.1415926))#保留两位小数
print('{:s}'.format("222")) #指定输出的数据类型
#d整型 f浮点 s字符串 b二进制 o八进制 x十六进制(X十六进制英文大写) c字符 %百分比
print('{:b}'.format(5))
print('{:%}'.format(0.75))
print('{:c}'.format(65))

##f：强制输出小数点
print('{:#f}'.format(1))
##e：使用科学计数法，并强制输出指数
print('{:#e}'.format(123456))
##E：使用科学计数法（大写字母形式），并强制输出指数

```


```python
# 使用位置参数进行格式化
print('{1}{0}'.format("world","hello"))#输出 helloworld 
# 使用关键字参数进行格式化
print("网站名：{name}, 地址：{url}".format(name="必应", url="www.bing.com"))
#使用字典参数
my_dict = {"name": "必应", "url": "www.bing.com"}
print("网站名：{name}, 地址：{url}".format(**my_dict))
# 使用列表索引
my_list = ["必应", "www.bing.com"]
print("网站名：{0[0]}, 地址：{0[1]}".format(my_list))
# 使用对象属性
class Site(object):
        def __init__(self, name, url):
            self.name = name
            self.url = url
my_class=Site("必应", "www.bing.com")
print("网站名：{0.name}, 地址：{0.url}".format(my_class))
```

3 f-string

格式化语法完整速查表

格式结构：
>```
>f"{变量 :[填充字符][对齐方式][宽度][.精度][类型]}"
>```

## 1. 完整参数说明表

| 位置 | 写法 | 含义 | 示例 | 结果 |
|------|------|------|----------------|---------|
| 填充字符 | 0 / * / 空格 | 不够宽时用什么补 | `f"{123:05}"` | `00123` |
| 对齐方式 | `<` | 左对齐 | `f"{123:<5}"` | `123  ` |
| | `>` | 右对齐（默认） | `f"{123:>5}"` | `  123` |
| | `^` | 居中 | `f"{123:^5}"` | ` 123 ` |
| 宽度 | 数字 | 总占多少位 | `f"{123:5}"` | `  123` |
| 精度 | .数字 | 小数位数 / 有效数字 | `f"{3.1415:.2f}"` | `3.14` |
| 类型 | f | 浮点数（固定小数） | `f"{1:.2f}"` | `1.00` |
| | d | 整数 | `f"{123:d}"` | `123` |
| | % | 百分比 | `f"{0.12:.1%}"` | `12.0%` |

- 不写对齐 = 右对齐
- 不写填充 = 补空格


```python
name="john"
age=18
print("My name is "+name+",Im "+str(age))
print(f"My name is {name},Im {age}")
#函数与表达式
import math
print(f"The square root of 16 is {math.sqrt(16)}.")
#格式说明
pi = 3.14159265
print(f"Pi to three decimal places is {pi:.3f}.") # :.3f 保留3位小数，不足3位补零；:.3 只显示3位数字 
print(f"Right aligned: {pi:>10}")#小数点占一位，会四舍五入
print(f"Width 10, precision 3: {pi:10.3}")#默认填充空格，小数点占一位
#字典和属性访问
person = {"name": "Bob", "age": 25}
print(f"{person['name']} is {person['age']} years old.")
# 使用等号= ：将填充字符放在符号和数字之间
number= -123.456
print(f"Number with padding: {number:+=10.2f}")#把+填充到-与123.456之间
#千位分隔
num=10000000
print(f"Number with comma: {num:,}")
```

4 join


```python
# 分隔符.join(列表)
# - join 里面必须是可迭代的（列表、元组、字符串都行）
# - 里面每一项必须是字符串
ls = ['h','e','l','l','o']
print(''.join(ls))

ls.reverse() # 反转
print(''.join(ls))
```

# 十五 常见函数

## range() enumerate() zip()


```python
#range
for i in range(5):
    print(i)

#enumerate 枚举
list=["Amy","Bob","Mark"]
for index,name in enumerate(list):
    print(f"Index:{index},Name:{name}")

#zip 打包 将多个可迭代对象的元素逐个组合成元组
numbers=[1,2,3]
letters=["a","b","c"]
zipped=zip(numbers,letters)# [(1,'a'),(2,'b'),(3,'c')]
for num,letter in zipped:
    print(f"Num:{num},Letter:{letter}")


```

## map() filter()


```python
#map 映射
def square(x):
    return x*x
num=[1,2,3]
square_num=map(square,num)
print(squared_numbers)
#map()函数返回的是一个惰性的迭代器,它不会立即执行函数，而是等到需要时才会计算出结果。
#如果您想要立即执行，您可以使用list()函数或for循环来强制遍历map()函数返回的迭代器，并触发函数的调用。
for i in square_num:
    print(i)


#filter 过滤
def is_even(x):
    return x % 2 == 0 
#return True or False
# print(is_even(2))
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(is_even, numbers)
for num in even_numbers:
    print(num)
```

## reduce()


```python
# reduce(function, iterable[, initial])
# 工作原理是将 function 应用于 iterable 中的前两个元素（或者是 initial 和第一个元素）
# 并得到的结果再与下一个元素一同传入 function 进行运算，直到处理完所有元素
from functools import reduce
num=[1,2,3,4]
def add(x,y):
    return x+y
result=reduce(add,num)
print(result)
```

## len()

## sorted()


```python
# sorted(可迭代对象, key=..., reverse=False) 默认升序
key_dict={
    'a':3,
    'b':3,
    'c':4
}
sorted(key_dict.items(), key = lambda x : (-x[1], x[0])) # 按数字降序，字母升序
```

# 十六 类


```python
class Dog:
    def __init__(self,name,age):#__init__ 方法
        self.name=name
        self.age=age
    def bark(self):
        print(f"{self.name} is barking")#方法的第一个参数通常是 self，代表实例（具体对象）本身。self必须出现在成员函数的第一个参数中，但在调用时却是忽略的

dog1=Dog("小白",3)
dog2=Dog("旺财",2)
print(dog1.name)
dog2.bark() 
dog2.age=1#通过点符号访问和修改对象的属性
print(dog2.age)
```

1 类属性 实例属性


```python
class Dog:
    # 类属性，不需要实例化就可以访问，通常用于保存一些全局属性
    # 比如，某个软件的版本号和版权信息
    BelongTo="animal"
    #实例属性
    def __init__(self,name,age):
        self.name=name
        self.age=age

dog3=Dog("小黑",2)
print(Dog.BelongTo)# 类属性通过类访问
print(dog3.name)# 实例属性通过实例访问
print(dog3.BelongTo)#类属性也可以被实例访问  但是实例属性无法被类访问

```

2 类方法 实例方法


```python
class Dog:
    count=0 # 类级别的属性
    def __init__(self,name,age):
        self.name=name
        self.age=age
        Dog.count+=1    # 类方法可以操作类属性

    @classmethod    #类方法定义时使用装饰器 @classmethod。
    def total(cls):
        # cls == class
        # 特别注意，第一个参数是 cls
        # cls 就是类本身，self 是实例本身
        # cls 和 self 名字是可以该的，只是习惯
        return cls.count
    
# dog4=Dog("皮蛋",5) #加上输出为1
# 直接使用，无需实例化
print(Dog.total()) #0
```

3 静态方法


```python
# 定义时使用装饰器 @staticmethod
# 如果方法与类和实例都没有直接的关系，可以使用静态方法。
# 如果方法涉及类级别的操作或属性，可以使用类方法
class Add:
    @staticmethod
    def add(x,y):
        return x+y
    
print(Add.add(2,3))
```

4 @property


```python
# 让方法在使用时看起来像访问类的属性一样，而不是像调用方法
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2 * self.radius

    @property
    def area(self):
        return 3.14 * self.radius ** 2

    @property
    def circumference(self):
        return 2 * 3.14 * self.radius

# 创建一个 Circle 对象
circle = Circle(5)

# 使用属性访问方法，不需要括号
print(circle.diameter)       # 输出: 10
print(circle.area)           # 输出: 78.5
print(f"{circle.circumference:.2f}")  # 输出: 31.4

# 不使用@property
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def diameter(self):
        return 2 * self.radius

    def area(self):
        return 3.14 * self.radius ** 2

    def circumference(self):
        return 2 * 3.14 * self.radius

# 创建一个 Circle 对象
circle = Circle(5)

# 使用方法访问，需要括号
print(circle.diameter())       # 输出: 10
print(circle.area())           # 输出: 78.5
print(circle.circumference())  # 输出: 31.400000000000002
```

5 getter/setter/deleter

6 封装 继承 多态


```python
class Animal :
    def __init__(self,name):
        self.name=name
    def speek(self):
        pass    #空操作语句。它不做任何事情，只是作为一个占位符。当你想要定义一个方法或者类，但是暂时不想实现任何功能，或者你想要保持代码的完整性而不希望它抛出错误
#封装
class Cat(Animal): # 重写父类方法
    def speek(self):
        print(f"{self.name} says meow!")

class Dog(Animal):
    def speek(self):
        return f"{self.name} says woof!"
    
def sound(animal):
    return animal.speek() #注意a小写 加括号
cat=Cat("咪咪")
dog=Dog("小七")
sound(cat)       # 输出: 咪咪 says meow!
print(sound(dog))# 输出: 小七 says woof!  相当于print(f"{self.name} says woof!")

# 封装：Animal 类封装了 name 属性和 speak 方法，外部代码只能通过 speak 方法访问动物的声音。这样，动物类的内部细节被隐藏起来了
# 继承：Cat 和 Dog 类分别继承了 Animal 类，它们继承了 name 属性和 speak 方法，并在各自的类中实现了特定的声音
# 多态：animal_sound 函数接受一个动物对象作为参数，无论是 Cat 还是 Dog 对象，都可以调用该函数并获得不同的声音输出。这里，不同的对象通过相同的接口（speak 方法）表现出了不同的行为

```

7 重载 重写


```python
# 重载指的是在同一个类中，可以定义多个同名但参数不同的方法。在 Python 中，重载是通过函数的默认参数或者通过 *args 和 **kwargs 参数来实现的
class Dog:
    def __init__(self,name):
        self.name=name
    def bark(self):
        return "animal sound"
    def bark(self,message):
        return f"{self.name} is barking {message}"
    
dog5 =Dog("wuwu")
# print(dog5.bark)  # 输出: Error! speak() missing 1 required positional argument: 'message'
print(dog5.bark("woof"))
# 由于 Python 不直接支持方法重载，上面的代码会报错，因为最后一个定义的 speak 方法会覆盖前面的定义。


# 重写指的是在子类中重新定义父类中已有的方法，以实现不同的功能。 见十六/6 封装
class Animal:
    def speak(self):
        return "animal sound"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Dog(Animal):
    def speak(self):
        return "Woof!"

cat = Cat()
dog = Dog()

print(cat.speak())  # 输出: Meow!
print(dog.speak())  # 输出: Woof!
```

8 super() 函数来调用父类的方法和属性


```python
#多用于重写
class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        return f"{self.name} make a noise"
    
class Dog(Animal): #子类
    def __init__(self,name,message): #重写父类方法
        super().__init__(name)# 调用父类的 __init__ 方法
        self.message=message
    def speak(self):
        return super().speak() + " " + f"{self.name} says {self.message}" #方法speak与super后面都要加括号
    
dog6=Dog("peter","woof")
print(dog6.speak()) #输出 peter make a noise peter says woof
# Animal 是一个基类，有一个 __init__ 方法用于初始化 name 属性，还有一个 speak 方法。
# Dog 是 Animal 的子类，它有自己的 __init__ 方法来初始化 name 和 breed 属性。通过 super().__init__(name)，它调用了 Animal 类的 __init__ 方法来初始化 name。
# Dog 类也重写了 speak 方法，但首先通过 super().speak() 调用了 Animal 类的 speak 方法，然后添加了额外的行为
    
```

9 魔法方法


```python
# 1. `__init__(self, ...)`: 初始化方法，在创建对象时自动调用，用于初始化对象的属性。
# 2. `__del__(self)` 销毁方法就是用于在对象被销毁时调用的。
# 3. `__str__(self)`: 当使用 `str(obj)` 或 `print(obj)` 时调用，返回一个描述对象的字符串。
# 4. `__repr__(self)`: 返回对象的可打印字符串，通常用于开发和调试，可使用 `repr(obj)` 调用。
# 5. `__len__(self)`: 返回对象的长度，通常用于序列类型（如列表、字符串等）。
# 6. `__getitem__(self, key)`: 允许通过索引访问对象的元素，可用于实现迭代和切片。
# 7. `__setitem__(self, key, value)`: 允许通过索引设置对象的元素。
# 8. `__delitem__(self, key)`: 允许通过索引删除对象的元素。
# 9. `__contains__(self, item)`: 判断某个元素是否在对象中，通常用于序列类型。
# # 10. `__eq__(self, other)`: 定义对象相等性的比较，使用 `==` 运算符。
# # 11. `__lt__(self, other)`: 定义对象的小于比较，使用 `<` 运算符。
# # 12. `__gt__(self, other)`: 定义对象的大于比较，使用 `>` 运算符。
# # 13. `__add__(self, other)`: 定义对象相加操作，使用 `+` 运算符。
# # 14. `__sub__(self, other)`: 定义对象相减操作，使用 `-` 运算符。
# # 15. `__mul__(self, other)`: 定义对象相乘操作，使用 `*` 运算符。
# # 16. `__call__(self, ...)`: 将对象实例作为函数调用，可以接受参数。
# # 17. `__enter__(self)`, `__exit__(self, exc_type, exc_value, traceback)`: 用于定义上下文管理器的进入和退出行为，通常与 `with` 语句一起使用。
# # 18. `__getattr__(self, name)`: 当访问不存在的属性时调用，可以用于动态属性访问。
# # 19. `__setattr__(self, name, value)`: 当设置属性时调用，可以用于控制属性赋值行为。
# # 20. `__delattr__(self, name)`: 当删除属性时调用，可以用于控制属性删除行为。
# # 21. `__iter__(self)`, `__next__(self)`: 用于定义迭代器，使对象可以在循环中遍历。
class Student:
    def __init__(self,name):
        self.name=name
        print(f"{self.name} is created")
    def __del__(self):
        print(f"{self.name} is deleted")
student1=Student("Amy")
student2=Student("John")
del student2
    
```

10 高级


```python
# __slots__ 属性： Python 中的对象在默认情况下可以动态地添加任意属性。
# 使用 __slots__ 属性，限制对象可以拥有的属性，提升性能并减少内存使用。
# 通过将属性名放入这个特殊的类属性中，你可以告诉Python对象只能拥有这些属性，而不能动态添加新的属性

class Student:
    __slots__=("name","age") #加等于号

student=Student("Mike","18")
student.city=("NewYork")# 会引发 AttributeError，因为 city 不在 __slots__ 中

# 抽象基类（ABC）： 抽象基类是一种用于定义接口和规范的类，它不能被实例化。通过继承抽象基类，可以确保子类实现了特定的方法
```


```python
# 依赖倒置原则
# 高层模块不应该依赖于低层模块，而是应该依赖于抽象接口。
# 抽象不应该依赖于具体实现，而是具体实现应该依赖于抽象。
# 这有助于解耦不同模块之间的依赖关系
class LightBulb:
    def turn_on(self):
        print("Light Bulb is on")
    def turn_off(self):
        print("Light Bulb is off")
class Switch:
    def __init__(self,bulb):
        self.bulb=bulb
    def operator(self):
        self.bulb.turn_on()
bulb=LightBulb()     #要加空括号
switch=Switch(bulb) #参数是一个类
switch.operator()  #要加空括号
# Output: Light Bulb is on       
# Switch 类依赖于 LightBulb 类，而不是直接控制开关操作
```

11 异常处理与异常子类


```python
# 在类中使用异常处理与在普通函数中使用类似。
class Calculator:
    def divide(self,a,b):
        try:
            result=a/b
        except ZeroDivisionError:
            print("Error: Cannot divide by zero")
        else:
            return result
cal=Calculator()    #加括号
print(cal.divide(10,5))
print(cal.divide(10,0))# Output: Error: Cannot divide by zero
# None 是 Python 中未指定返回值的函数或方法的默认返回值。在 divide 方法中，
# 如果 ZeroDivisionError 被触发，else 代码块不会执行，因此 result 不会被返回，导致方法默认返回 None。
# 要解决这个问题，您可以在捕获异常后明确返回一个值，比如 None 或其他错误指示符。
```

# 十七 日期与时间


```python
# datetime 模块提供了处理日期和时间的类和函数，用于表示和操作日期、时间、日期时间以及时间间隔。
# 常用的类包括 datetime、date、time、timedelta 等。
import datetime
print(datetime.datetime.now())#获取当前的日期时间
# 使用 datetime.datetime(year, month, day, hour, minute, second) 来创建一个日期时间对象。
# 类似地，可以使用 datetime.date(year, month, day) 创建日期对象，datetime.time(hour, minute, second) 创建时间对象。
# 使用 strftime(format) 方法可以将日期时间对象格式化为字符串，其中 format 是一个字符串格式化模板。
# datetime.datetime.strptime(date_string, format) 可以将字符串解析为日期时间对象
# timedelta 对象来表示时间间隔，进行日期时间的加减运算
# 比较日期时间
# timezone 类来处理时区相关的操作，可以创建不同时区的日期时间对象
# 可以通过减法操作来计算两个日期时间之间的时间差，得到一个 timedelta 对象
# 可以使用 time 模块中的 sleep 函数来实现暂停程序一段时间。sleep(1)休息一秒
# Python 中还有其他库，如 dateutil、pytz 等，可以进一步增强日期与时间处理的功能。使用这些工具，可以方便地进行日期时间的表示、运算、比较和格式化，以满足各种不同的应用需求
# Python 中提供了对时间日期的多种多样的处理方式，主要是在 time 和 datetime 这两个模块里  datetime 比 time 高级了不少，可以理解为 datetime 基于 time 进行了封装，提供了更多实用的函数
```

1 常用任务


```python
from datetime import datetime,timedelta
#获取当前日期
print(datetime.now())
#创建日期时间对象
custom_datetime=datetime(2024,12,25,20,30,00)
print(custom_datetime)
#格式化日期时间字符串
formatted_datetime=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(formatted_datetime)
#解析字符串为日期时间
str_datetime="2024-12-25 21:00:00"
parsed_datetime=datetime.strptime(str_datetime,'%Y-%m-%d %H:%M:%S')
print(parsed_datetime)
#日期时间运算(timedelta)
one_week_later=datetime.now()+timedelta(weeks=1)
print(one_week_later)#晚一周
five_hour_earlier=datetime.now()-timedelta(hours=5)
print(five_hour_earlier)#早五小时
delta=timedelta(days=1,hours=2,minutes=30,seconds=20)
print(delta.total_seconds())#总秒数
#比较日期时间
datetime1=datetime(2024,12,25)
datetime2=datetime(2024,12,21)
if datetime1<datetime2:
    print("datetime1 is earlier")
else:
    print("datetime2 is earlier")  
#时区处理
# import pytz                               Waring:No module  pip install pytz
# utc_datetime = datetime.now(pytz.utc)
# print(utc_datetime)
#计算时差
datetime3=datetime(2024,12,26,19,00,00)
datetime4=datetime(2024,12,26,17,00,00)
datetime_difference=datetime3-datetime4
print(datetime_difference)
#睡眠
import time
print("Strat")
time.sleep(3)
print("3 seconds later")
```

2 格式化


```python
# %Y: 年（四位数）
# %y: 年（两位数）
# %m: 月（01 至 12）
# %d: 日（01 至 31）
# %H: 时（00 至 23）
# %I: 时（01 至 12）
# %M: 分（00 至 59）
# %S: 秒（00 至 59）
# %a: 周几（缩写）
# %A: 周几（完整）
# %b: 月份（缩写）
# %B: 月份（完整）
# %c: 完整的日期时间表示
# %x: 适用于当前区域设置的日期表示
# %X: 适用于当前区域设置的时间表示
# %j: 年中的天数（001 至 366）
# %U: 年中的周数，以星期日为一周的开始（00 至 53）
# %W: 年中的周数，以星期一为一周的开始（00 至 53）


from datetime import datetime

current_datetime = datetime.now()

formatted_date = current_datetime.strftime('%Y-%m-%d')
formatted_time = current_datetime.strftime('%H:%M:%S')
formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
formatted_weekday = current_datetime.strftime('%A')

print('Formatted Date:', formatted_date)
print('Formatted Time:', formatted_time)
print('Formatted Datetime:', formatted_datetime)
print('Formatted Weekday:', formatted_weekday)
```

3 时区

# 十八 路径与文件

1 路径


```python
# 相对路径是相对于当前工作目录的路径，指定文件相对于当前脚本或程序所在的位置。
# 绝对路径是完整的文件路径，从根目录开始，指定文件的完整位置。
# cd：将当前目录更改为用户的主目录（通常是C:\Users\用户名）。
# cd 目录路径：将当前目录更改为指定的目录路径
# cd .：表示当前目录。
# cd ..：将当前目录更改为父目录。
# cd \：将当前目录更改为根目录
# cd %变量名%：将当前目录更改为指定环境变量的值。例如，cd %USERPROFILE%会将当前目录更改为用户的主目录
# 可以用 dir 显示当前目录下的文件夹和文件
### 几乎不要使用绝对路径，因为你本地硬盘里面的路径与用户是不一样的。
```

2 file


```python
# 当在Python中编写一个模块时，可以使用__file__特殊变量来获取当前模块的文件路径。
# 当一个 Python 文件被作为模块导入或直接执行时，__file__ 会包含该文件的绝对路径。然而，对于交互式环境（比如在 Python 解释器中），__file__ 可能会被设置为 None。
# __name__：用于获取模块的名称。当一个模块直接执行时，其 __name__ 属性被设置为 "__main__"，而当该模块被导入时，__name__ 属性则被设置为模块的名称
# __package__：用于获取当前模块所属的包的名称。如果模块不属于任何包，那么 __package__ 将被设置为 None。
# __path__：用于获取包的搜索路径列表。当一个模块是一个包的一部分时，__path__ 属性会包含该包的搜索路径

```

3 pathlib


```python
from pathlib import Path
#创建路径
path=Path('/home/user/documents/file.txt')#注意大小写，小写是文件路径
#当前工作目录路径
current_path = Path.cwd()
#家目录
home_path = Path.home()
#/用来连接路径
new_path = current_path / 'new_folder' / 'new_file.txt'
#read_text 方法读取文本文件的内容：
#read_bytes 方法读取二进制文件的内容
content=path.read_text()
print(content)
#write_text 方法写入文本内容
#write_bytes 方法写入二进制内容
path.write_text('Hello World')
# 检查路径是否存在：
exists=path.exists#path是文件路径
# 检查是否是文件：
is_file=path.is_file()
# 检查是否是目录：
is_dir=path.is_dir()
# 使用 mkdir 方法创建目录，可以指定 parents=True 来创建多级目录：
new_dir = Path('/home/user/new_directory')
new_dir.mkdir(parents=True)
# 删除文件：
path.unlink()
# 删除目录（仅当目录为空时）：
new_dir.rmdir()
# 递归删除目录及其内容：
import shutil
shutil.rmtree(new_dir)
# 获取文件名：
file_name = path.name
# 获取父目录：
parent_dir = path.parent
# 获取文件的后缀：
suffix = path.suffix
# 去掉后缀的文件名：
stem = path.stem
# 使用 iterdir 方法遍历目录中的文件和子目录：
for item in new_dir.iterdir():
    print(item)
```

4 示例


```python
from pathlib import Path
import shutil

# 创建路径对象
path = Path("C:\\Users\\LENOVO\\Desktop\\cs.txt")#在Python字符串中，反斜杠 \ 被用作转义字符。在文件路径中使用时，它可能会导致问题
# 因为像 \U 这样的序列会被尝试解释为Unicode字符的开始，但随后没有足够的字符来形成一个有效的Unicode转义序列.使用双斜杠以解决。

# 检查路径是否存在
print(f"Path exists: path.exists()")

# 读取文件内容
if path.exists() and path.is_file():
    content = path.read_text(encoding='utf-8')#Python默认使用系统的编码来打开文件，在Windows上通常是GBK。如果文件不是用GBK编码的（比如它是UTF-8编码的），那么在读取时就会遇到解码错误
    print(f"File content:\n{content}")

# 创建新目录
new_dir = Path('C:\\Users\\LENOVO\\Desktop\\python_file_test')
new_dir.mkdir(parents=True, exist_ok=True)#parents=True如果目录的父目录不存在，则连同父目录一起创建。exist_ok=True这个参数指定如果目录已经存在，不要抛出异常

# 写入新文件
new_file = new_dir / 'new_file.txt'
new_file.write_text('Hello, new file!')

# 遍历新目录
print("Files and directories in new_directory:")
for item in new_dir.iterdir():
    print(item)

# 删除新文件
new_file.unlink()

# 删除新目录（确保目录为空）
new_dir.rmdir()
# 或者使用 shutil.rmtree(new_dir) 递归删除目录及其内容
```

5 文件读写


```python
##使用open()函数打开文件，需要指定文件名和模式：文本模式（'t'，默认）或二进制模式（'b'），以及是否进行写操作（'w'）、追加（'a'）、读取（'r'，默认）
# 以只读模式打开文件（默认）
file = open('example.txt', 'r')
# 以写入模式打开文件（会覆盖文件内容）
file = open('example.txt', 'w')
# 以追加模式打开文件（在文件末尾添加内容）
file = open('example.txt', 'a')
# 以二进制模式打开文件（用于非文本文件）
file = open('example.bin', 'rb')

##使用read()、readline()或readlines()方法来读取文件内容。
# 读取整个文件内容
content = file.read()
# 读取文件的下一行
line = file.readline()
# 逐行读取文件内容
line = file.readline()
while line:
    print(line.strip())  # 使用 strip() 方法去除行尾的换行符
    line = file.readline()
# 读取文件的所有行，并将它们作为列表返回（每行是一个列表元素）
lines = file.readlines()

##使用write()方法将字符串写入文件。
# 将字符串写入文件
file.write('Hello, world!\n')

##使用close()方法关闭文件，以释放系统资源。更好的做法是使用with语句，它会在代码块执行完毕后自动关闭文件。
# 使用with语句自动关闭文件
with open('example.txt', 'w') as file:
    file.write('Hello, world!\n')
# 文件在这里已经被自动关闭

# 始终检查文件操作是否成功，特别是写入文件时。虽然open()函数在失败时会抛出异常，但了解如何捕获和处理这些异常是一个好习惯。

```

6 示例


```python
# 以下是一个完整的示例，展示了如何读取一个文件的内容，并将其写入另一个文件。

# 打开源文件进行读取
with open('source.txt', 'r') as source_file:
    content = source_file.read()

# 打开目标文件进行写入
with open('destination.txt', 'w') as destination_file:
    destination_file.write(content)
```

7 文件操作


```python
import os
import shutil
# 文件重命名：使用 os.rename(src, dst) 函数可以将文件从源路径 src 重命名为目标路径 dst。
# 文件删除：使用 os.remove(path) 函数可以删除指定路径下的文件。path是文件路径
# 文件复制：使用 shutil.copy(src, dst) 函数可以将源文件 src 复制到目标路径 dst，保留文件内容和权限。
# 文件移动：使用 shutil.move(src, dst) 函数可以将源文件 src 移动到目标路径 dst，同时修改文件的位置和名称。
# 文件存在性检查：使用 os.path.exists(path) 函数可以检查指定路径下的文件是否存在。
# 文件大小：使用 os.path.getsize(path) 函数可以获取文件的大小（以字节为单位）。
# 文件创建时间与修改时间：使用 os.path.getctime(path) 和 os.path.getmtime(path) 函数可以获取文件的创建时间和修改时间

```

8 对象序列化和反序列化

# 十九 排序 判断素数与闰年


```python
#判断素数
def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i==0:
            return False
    return True
print(is_prime(5))
#判断润年
def is_leap_year(year):
    if year % 4 ==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
print(is_leap_year(2000))

#排序
# sort 对原列表进行排序，不返回任何值（或者说返回 None），它是一个就地操作。
# sorted 不会修改原始的可迭代对象，而是返回一个新的排序后的列表。
# sort只适用列表#sorted是内置函数
my_list=[1,5,8,7,5,56,49,514,48,9]
my_list.sort()
print(my_list)

#sorted(iterable,key=None,reverse=False)reverse:用于指定排序顺序（默认为 False 表示升序，True 表示降序）。
my_tuple=(1,5,8,6,3,4,9,9954,44,64,585,46)
sorted_tuple=sorted(my_tuple)
print(sorted_tuple)

# 按字符串长度排序:key=len
# 按数字的绝对值排序:key=abs
# 按元组的第二个元素排序:
tuples = [(1, 3), (3, 1), (2, 2)]
sorted_tuples = sorted(tuples, key=lambda item: item[1])# item 是 tuples 里面的某一项
print(sorted_tuples)  # 输出: [(3, 1), (2, 2), (1, 3)]
# 逆序排序字符串列表:reverse=True
# 多列排序：
data = [
    ("apple", 2, 5),
    ("banana", 1, 3),
    ("cherry", 2, 2),
    ("date", 3, 1),
    ("elderberry", 2, 5),
    ("fig", 1, 4)
]
sorted_data = sorted(data, key=lambda x: (x[0], x[1], x[2]))# 我们希望首先根据第一列排序，如果第一列相同，则根据第二列排序，最后根据第三列排序
print(sorted_data)
```

#　二十 包与模块


```python
# 包（Package）是一种组织和管理代码的方式，它可以包含多个相关的模块（Module）和其他资源文件。
# 包的目的是将相关功能的代码组织在一起，提供更好的模块化和复用性。
# 包可以包含模块文件和其他子包。模块是包的组成部分，用于封装一些功能或类。
# 一个.py文件就是一个模块，一个含 __init__.py文件的目录就是一个包。
# 包可以多层嵌套，形成一个层次结构，例如 package.subpackage
```

1 import


```python
#import #使用逗号可以导入多个
#as:使用别名
import math as ma
print(ma.sqrt(16))  
#from...import... :从模块中导入特定功能
from pathlib import Path #使用逗号可以导入多个
# from math import *:导入所有内容（不推荐，可能会引起命名冲突)
#注意两种导入方式的区别
import math
print(math.sqrt(16))
from math import *
print(sqrt(25))
```

2 组织


```python
# 包（Package）是一种组织模块的方式，它允许您将相关的模块放在同一个文件夹中
# 一个包实际上就是一个包含了特殊的 __init__.py 文件的文件夹
# 如果你有几个包含.py文件的目录，且有子目录，你应该确保每个目录和子目录都有__init__.py文件，这样它们才能被识别为包。

# 以下是一个包的组织结构示例：
# my_package/
# |-- __init__.py
# |-- module1.py
# |-- module2.py
# |-- subpackage/
# |   |-- __init__.py
# |   |-- module3.py

# my_package 是包的根文件夹
# __init__.py 文件是一个空文件，它标识目录为一个包
# module1.py、module2.py 等是包内的模块文件
# subpackage 是一个子包，同样需要包含 __init__.py 文件
# module3.py 是子包内的模块文件。


```


```python
# 假定你的项目文件夹是my_project1，将上述my_package文件夹放入这个项目文件夹内部，并新建test.py来测试包组织是否成功，test.py文件内容如下：
# import 最终落脚在模块上
# import my_package.module1
# import my_package.module1 as mm1
# from my_package import module2
# from my_package.subpackage import module3

# my_package.module1.function1()
# mm1.function1()
# module2.function2()
# module3.function3()
```


```python
# 还有一种方案是在文件组织的时候可以多层，但用户使用时只需要一层，Numpy 基本就是这样用。

# 在 my_package/__init__.py 中，这样写：
# from .module1 import *
# from .module2 import *
# from .subpackage.module3 import *

# test.py文件内容如下：
# import my_package as pack1
# pack1.fun1()
# pack1.fun2()
# pack1.fun3()
```

3 多文件导入



```python
# 在Python中，每个模块都有一个独立的命名空间。当你在a.py中定义了一个全局变量msgs，并在该模块内部启动一个线程访问这个变量时，该线程访问的是a.py模块命名空间内的msgs对象。
# 如果你在b.py中导入a.py，并启动另一个线程访问msgs，那么这个线程访问的是b.py模块的命名空间内的msgs。
# 由于Python的模块是第一次导入时加载的，所以b.py中的msgs是a.py中msgs的一个引用。
# 然而，由于每个线程都有自己的局部变量栈，所以如果你在h1和h2中访问msgs，**它们实际上访问的是同一个对象**，前提是你没有在h1或h2中创建一个新的msgs对象
# 如果你发现h1和h2访问的不是同一个对象，可能是因为在h1或h2中有这样的操作，
# 例如在h1中执行了msgs = []来创建一个新的列表对象。这将导致h1中的msgs引用了一个新的对象，而h2仍然引用的是原始对象。
# 为了确保h1和h2访问的是同一个msgs对象，你需要在h1和h2中避免重新绑定msgs变量

# # a.py
# msgs = []
# def h1():
#     global msgs
#     # 访问msgs
#     print(msgs)
# import threading
# threading.Thread(target=h1).start()

# # b.py
# import a
# import threading
# def h2():
#     # 访问msgs
#     print(a.msgs)
# threading.Thread(target=h2).start()
# 在这个例子中，h1和h2都访问的是a.py中的msgs对象。注意，在多线程环境中，对共享资源的访问可能需要同步机制，如锁，以避免竞态条件和其他并发问题

# 如果a.py在c.py中也加载过，那么msgs是否是同一份变量取决于几个因素：
# 导入方式：如果c.py和b.py都是通过简单的import a来导入a.py，那么它们会共享a.py中的msgs变量，因为Python中的模块是单例的。
# 这意味着无论a.py被导入多少次，只要它是通过相同的导入方式，msgs都是同一个对像
# 模块重载：如果你在c.py中使用了某种方式来重新加载a.py模块，例如使用importlib.reload(a)，那么msgs可能会被重新定义，这可能导致c.py中的msgs与b.py中的msgs不是同一个对象。
# 线程间的共享：即使msgs是同一个对象，由于线程之间共享内存，任何线程对msgs的修改都会影响到其他线程。
# 然而，如果msgs是一个不可变数据类型（如整数、浮点数、字符串或元组），那么线程必须谨慎地处理它以避免条件竞争。
# 如果msgs是一个可变数据类型（如列表、字典或集合），那么线程间的同步就变得尤为重要
# 全局变量作用域：在a.py中定义的msgs是一个全局变量，它属于a.py的命名空间。在b.py和c.py中访问msgs时，应该使用a.msgs来确保访问的是a.py中的全局变量
```

4 pip


```python
# pip（Pip Installs Packages）是Python的默认包管理器，用于安装和管理Python包。
# 它是一个命令行工具，可以从Python Package Index (PyPI) 下载（https://pypi.org/）和安装第三方Python包

# 查看代理文件查找位置：在命令行输入pip -v config list
# 输出可能是：
# For variant 'global', will try loading 'C:\ProgramData\pip\pip.ini'
# For variant 'user', will try loading 'C:\Users\Mloong\pip\pip.ini'
# For variant 'user', will try loading 'C:\Users\Mloong\AppData\Roaming\pip\pip.ini'
# For variant 'site', will try loading 'C:\Python38\pip.ini'
# 设置代理
# 依据文件位置，在对应处创建 pip.ini 文件，设置代理，比如使用阿里云（推荐清华）：
# [global]
# index-url = http://mirrors.aliyun.com/pypi/simple/
# [install]
# trusted-host = mirrors.aliyun.com
# 再次使用上述命令，如果设置成功，输出内容会包含已经设置好的代理。
# 或（清华用的https，更安全）：
# pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```


```python
#常用命令
# pip install package_name:安装指定的包。
# pip install -r requirements.txt：从requirements.txt文件中安装所有依赖的包。
# pip uninstall package_name：卸载指定的包。
# pip freeze：列出已安装的包及其版本信息。
# pip search package_name：搜索包并显示相关信息
```

在 Windows 上，Python 包通常安装在 C:\Users\<用户名>\AppData\Local\Programs\Python\Python<版本号>\Lib\site-packages\ 目录下  
某些情况下，Python 包可能会被安装在用户级目录下，而不是全局系统目录。这通常是为了避免需要管理员权限来安装包  
在 Windows 上，用户级安装目录可能是 C:\Users\<用户名>\AppData\Roaming\Python\Python<版本号>\site-packages\  
要查找特定包的实际安装位置，你可以在 Python 环境中运行以下代码：  

>```py
>import 包名  
>print(包名.__file__)  
>```  
>将 包名 替换为你想要查找的包的实际名称（例如 numpy、matplotlib 或 skimage）。这将打印出该包的 __init__.py 文件的路径，从而指示包的安装位置    

5 Anaconda

6 编译分发版本/网上发行
