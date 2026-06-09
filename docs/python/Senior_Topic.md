# 目录

  - [1 add_argument()](#1-add_argument)
  - [2 示例与使用方法](#2-示例与使用方法)
  - [1 XML](#1-xml)
  - [2 JSON](#2-json)
  - [3 YAML](#3-yaml)
  - [1 基础](#1-基础)
  - [2 示例](#2-示例)
- [1 匹配邮箱地址：](#1-匹配邮箱地址)
- [2 替换文本：](#2-替换文本)
- [3 查找并提取数字：](#3-查找并提取数字)
- [4 分组提取信息:](#4-分组提取信息)
  - [3 转义](#3-转义)
  - [4 示例](#4-示例)
- [1 匹配点.:](#1-匹配点)
- [2 匹配星号*：](#2-匹配星号)
- [3 匹配反斜杠\:](#3-匹配反斜杠)

---
# Jupyter Notebook


```python
# Jupyter Notebook（此前被称为 IPython notebook）是一个交互式笔记本，支持运行 40 多种编程语言。安装 Anaconda 后就自带了。
# 扩展名：.ipynb
# Jupyter Notebook 的本质是一个 Web 应用程序，便于创建和共享程序文档，支持实时代码，数学方程，可视化和 markdown
# 用途包括：数据清理和转换，数值模拟，统计建模，机器学习等等  

```

## Markdown

### 标题·区块·列表
> 区块引用中也可以包含列表：
> - 项目一
> - 项目二
>   - 子项目一
>   - 子项目二
>> 区块嵌套
>> 1. 第一步
>> 2. 第二步
>>   - 子步骤一
>>   - 子步骤二
>> 3. 第三步（注意这里的数字是自动生成的，你不需要手动输入）

> 这是一个区块引用，其中包含了一个代码块：
> 
>     ```python
>     def hello_world():
>         print("Hello, world!")
>     ```


```python
# 标题层级：可以根据#号的数量设置不同的标题层级。例如，一级标题使用“# 标题内容”，二级标题使用“## 标题内容”，以此类推，直到六级标题。 注意:#与文字之间必须要有空格。
# 区块引用：在文本前加上>。数量越多，层级越低。例如，“> 这是一级引用”，“>> 这是二级引用”。 注意:>与文字之间必须要有空格。
# 区块中可以使用列表，也可以包含代码块。注意：由于区块引用本身已经使用了大于号，需要三个反引号（```）包围代码块,并在代码块前使用额外的缩进（通常是四个空格或一个制表符）
# 无序列表：使用+、-或*均可实现无序列表。例如，“* 项目1”，“- 项目2”，“+ 项目3”。 注意:符号与文字之间必须要有空格。
# 有序列表：在文本前加入1.、2.等序号即可实现有序列表。例如，“1. 项目1”，“2. 项目2”。
# 子列表的缩进（通常是两个或四个空格）用于表示层级关系。
```

 ### 文本格式

**这是加粗**  
__这也是加粗__  
*这是斜体*  
_这也是斜体_  
~~这是删除线~~  
>```这是高亮```  
>
>---
>分割线
>***
>
>| 表头1 | 表头2 |
>|-------|-------|
>| 内容1 | 内容2 |
>
>\*\*不要加粗,但保留星号**
>
>https://www.google.com  
>[访问Google](https://www.google.com)   
>“<img src="http://example.com/image.jpg" />”
>
><!--不显示这段内容 -->


```python
# 加粗文本：在文本两旁加上**或__
# 斜体文本：在文本两旁加上*或_
# 删除线文本：在文本两旁加上~~
# 高亮文本：在文本两旁加上```(反引号)
# 水平分割线:可以使用三个及其以上的-或*
# 表格：每两个管道符||中间视为一个单元格，-为表头和内容的分割标识。
# 转义：使用\来转义Markdown中的特殊符号，以避免其被解释为Markdown语法。例如，“*”表示星号字符本身，而不是斜体文本的开头。
# 换行：在行尾加两个空格
# 不显示:Ctrl+/ 或者<!-- 内容 -->
# 链接：直接输入网址链接，或者输入网址链接的同时，使用中括号[ ]重命名，小括号( )添加网址。例如，[显示文本](链接地址)
# 图片：使用“<img src="" />”语法添加图片链接。
```

# ArgumemtParser*


```python
# ArgumentParser是Python标准库中argparse模块提供的一个用于解析命令行参数和选项的工具。它可以帮助您创建具有自定义参数和选项的命令行界面

# import argparse
# parser=argparse.ArgumentParser()#创建对象
# parser.add_argument('arg_name', help='Description of the argument')#添加参数和选项
# parser.add_argument('-o', '--option', help='Description of the option')
# args=parser.parse_args()#解析命令行参数
# print(args.arg_name)#使用解析结果
# print(args.option)

```

## 1 add_argument()


```python
import argparse
parser=argparse.ArgumentParser()
# add_argument方法用于向ArgumentParser对象添加参数和选项。它提供了多个参数来定义每个参数或选项的属性。下面是add_argument方法的常用参数：

# name or flags：指定参数的名称或选项的标志。对于位置参数，直接指定参数的名称；对于选项参数，可以使用短标志（如-o）或长标志（如--option）。
parser.add_argument('arg_name')
parser.add_argument('-o','--option')
# action：指定参数的动作。默认为store，表示将参数值存储到属性中。
# 其他常用的动作包括store_true（存储True值，适用于开关选项）、store_false（存储False值，适用于开关选项）和append（将多个参数值附加到列表中）
# 如果你想要定义一个参数，只要它在命令行中存在即可，不需要带值，你可以在 add_argument 方法中指定 action 参数为 ‘store_true’ 或者 ‘store_false’
# 如果用store_false，则命令行带此参数为false，不带反而是true。
parser.add_argument('-v','--verbose',action='store_true')
parser.add_argument('--name',action='append')
# type：指定参数的类型。默认为字符串类型。可以指定的类型包括int、float、str等。
parser.add_argument('--count',type='int')
parser.add_argument('--threshold',type='float')
# default：指定参数的默认值。如果未提供该参数，则使用默认值
parser.add_argument('--output',default='output.txt')
# required：指定参数是否为必需的。默认为False。如果将其设置为True，则在解析时必须提供该参数，否则将显示错误信息。
parser.add_argument('--input',required=True)
# help：指定参数的帮助文本。当用户使用-h或--help选项时，将显示该文本。
parser.add_argument('--input',help='Path to input file')
# dest：指定解析后的命令行参数的目标属性名称
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", dest="filename", help="input file")
args = parser.parse_args()
print(args.filename)


# default参数只是指定了当命令行中没有出现该选项时，属性的默认值是什么。它并不影响当命令行中出现该选项时，属性的值是什么。
# 如果只使用default参数，而不使用action参数，那么就不能实现一个开关或标志的效果。因为当命令行中出现该选项时，属性的值会被设置为选项后面跟着的值，而不是一个固定的True或False。
# 如果想实现一个开关或标志的效果，您就需要使用action参数，并且选择store_true或store_false作为action类型。
# 这样，当命令行中出现该选项时，属性的值就会被设置为True或False，而不需要指定一个值。
# 当action类型是store_true或store_false时，它会自动将default参数的值设为与action类型相反的布尔值
parser = argparse.ArgumentParser(description='Inference code to lip-sync videos in the wild using Wav2Lip models')
parser.add_argument('--one_shot', action='store_true')
args = parser.parse_args()
print(args.one_shot)
# 直接运行，打印结果是False，而不是None
```

## 2 示例与使用方法


```python
# 示例：见 use_argparse.py
# 使用步骤；
# 打开命令行或终端。
# 导航到脚本所在的目录：
# 如果你的脚本在桌面上，你需要先使用 cd 命令改变当前目录到桌面。例如，在 Windows 上可能是 cd Desktop，在 macOS 或 Linux 上可能是 cd ~/Desktop。
# 如果你的脚本在其他位置，使用相应的 cd 命令导航到那个位置。
# 运行脚本：
# 输入 python use_argparse.py hello --foo 42 并按下回车键。
# 注意：如果你的系统同时安装了 Python 2 和 Python 3，并且 python 命令默认指向 Python 2，你可能需要使用 python3 命令来运行脚本，即 python3 use_argparse.py hello --foo 42。
# 查看输出：
# 脚本运行后，你应该会在命令行或终端中看到输出，类似于 foo: 42 和 bar: hello
```

# xml/json/yaml

## 1 XML


```python
# XML（可扩展标记语言）是一种用于存储和传输数据的文本格式，它具有结构清晰、易于理解和可扩展的特点。
# 在Python中，你可以使用多个库来进行XML编程，其中最常用的包括内置的 xml 模块和第三方的 ElementTree 模块。

#示例 - 解析XML：
import xml.etree.ElementTree as ET
# 解析XML字符串
xml_str="<person><name>John</name><age>30</age></person>"
root=ET.fromstring(xml_str)
# 访问XML元素和属性
print("name:",root.find('name').text)
print("Age:", root.find('age').text)

# 示例 - 生成XML：
import xml.etree.ElementTree as ET
# 创建XML元素
root=ET.Element('person')
name=ET.SubElement(root,'name')
name.text='John'
age=ET.SubElement(root,'age')
age.text="30"
# 生成XML字符串
xml_str=ET.tostring(root,encoding='utf-8').decode('utf-8')
print(xml_str)
```

## 2 JSON


### 基础


```python
# JSON（JavaScript Object Notation）是一种轻量级的数据交换格式，在Python中使用 json 模块可以方便地进行JSON数据的解析和生成

# 将Python数据结构转换为JSON格式：
import json
# 创建一个Python字典
date={
    'name':'Jhon',#最后加逗号，中间是冒号
    'age':30,
    'city':'New York'
}
### dumps=dump str
# 将Python字典转换为JSON格式
json_date=json.dumps(date,indent=4)# 使用indent参数来格式化输出
print(json_date)

# 将JSON数据解析为Python数据结构：
import json
# JSON格式的字符串
json_str='{"name": "John", "age": 30, "city": "New York"}'#外层用单引号，内层用双引号
### loads=load str
# 解析JSON字符串为Python数据结构
parsed_date=json.loads(json_str)
print(parsed_date["name"])
print(parsed_date["age"])
print(parsed_date["city"])
```


```python
# 将Python对象保存为JSON文件：
import json
date={
    'name':'Jhon',#最后加逗号，中间是冒号
    'age':30,
    'city':'New York'
}
with open('date.json','w') as json_file:
    json.dump(date,json_file,indent=4)

# 从JSON文件读取并解析为Python数据结构：
import json
with open('date.json', 'r') as json_file:
    parsed_date = json.load(json_file)
print(parsed_date["name"])
print(parsed_date["age"])
print(parsed_date["city"])
```

### 数据类型对应


```python
# 数据类型对应
# |    JSON    |    Python  |
# |object      |dict        |
# |array       |list        |
# |string      |str         |
# |number(int) |int         |
# |number(real)|float       |
# |true        |True        |
# |false       |False       |
# |null        |None        |
# 它还将“NaN”、“Infinity”和“-Infinity”理解为它们对应的“float”值。
```

### 编码


```python
# 编码：重写 default 方法 或 给个子类(cls)

import json
# 定义一个名为 ComplexEncoder 的类，它继承自 json.JSONEncoder
# 这个类将用于自定义 JSON 序列化过程，特别是处理复数类型
class ComplexEncoder(json.JSONEncoder):
    # 重写 default 方法，该方法在序列化过程中遇到无法直接转换为 JSON 格式的对象时被调用
    def default(self, obj):
        # 检查传入的对象是否为复数类型
        if isinstance(obj, complex):
            # isinstance 函数是 Python 的一个内置函数。它用于检查一个对象是否是一个已知的类型或其子类的实例。
            # isinstance(object, classinfo)
            # object：要检查的对象。
            # classinfo：可以是一个类型或者一个包含多个类型的元组，用来指定要检查的类型或其子类
            # 如果 object 是 classinfo 指定的类型或其子类的实例，isinstance 函数将返回 True，否则返回 False
            # 如果是复数，将其转换为一个包含实部和虚部的列表，并返回这个列表
            # 这样 JSON 序列化器就可以将这个列表转换为 JSON 格式的数组
            return [obj.real, obj.imag]
        # 如果传入的对象不是复数，则调用基类（json.JSONEncoder）的 default 方法.会抛出一个 TypeError 异常，表明该对象类型无法被序列化
        return json.JSONEncoder.default(self, obj)

# 使用 json.dumps 函数序列化一个复数对象，指定 cls 参数为我们自定义的 ComplexEncoder 类
# 这将调用 ComplexEncoder 的 encode 方法来处理序列化过程
# 由于我们重写了 default 方法，复数对象会被正确转换为 JSON 格式的数组
print(json.dumps(2 + 1j, cls=ComplexEncoder))  # 输出: '[2.0, 1.0]'

# 直接创建一个 ComplexEncoder 实例，并调用其 encode 方法来序列化一个复数对象
# 这与上面使用 json.dumps 的效果相同
print(ComplexEncoder().encode(2 + 1j))  # 输出: '[2.0, 1.0]'

# 创建一个 ComplexEncoder 实例，并调用其 iterencode 方法来序列化一个复数对象
# iterencode 方法返回一个生成器，该生成器会逐步产出序列化后的 JSON 格式的字符串片段
# 我们将这些片段转换为一个列表并打印出来，以查看中间步骤
# 注意：这里的输出是字符串片段的列表，而不是一个完整的 JSON 字符串
print(list(ComplexEncoder().iterencode(2 + 1j)))  # 输出: ['[2.0', ', 1.0', ']']
```


```python
# 处理自定义对象，比如一个包含 name 和 age 属性的 Person 类。可以这样扩展 ComplexEncoder：

import json

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, complex):
            return [obj.real, obj.imag]
        elif isinstance(obj, Person):
            return {'name': obj.name, 'age': obj.age}
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)

# 测试代码
p = Person("Alice", 30)
print(json.dumps(p, cls=ComplexEncoder))  # 输出: {"name": "Alice", "age": 30}
print(json.dumps(2 + 1j, cls=ComplexEncoder))  # 输出: [2.0, 1.0]
```

### 解码


```python
# 重写 object_hook，有两种方式：子类或直接重写方法

import json
# 定义一个名为 as_complex 的函数，它将作为 object_hook 传递给 json.loads 函数
# 这个函数用于将特定的字典结构解码为复数类型
def as_complex(dct):
    # 检查字典中是否包含 '__complex__' 键，并且其值为 true
    # (注意：这里应该是字符串 'true'，但通常应为布尔值 True 的 JSON 表示，即 true 无需引号，
    # 不过 JSON 解析时字符串 'true' 也会被转换为布尔值 True，这里的检查也能够工作）
    if '__complex__' in dct and dct['__complex__'] :  # 更严谨的做法是检查 dct['__complex__'] == True或is True。
        # 如果字典表示一个复数，则根据其实部和虚部创建一个复数对象并返回
        return complex(dct['real'], dct['imag'])
    # 如果字典不表示复数，则直接返回该字典
    return dct

# 使用 json.loads 函数解析一个 JSON 字符串，指定 object_hook 参数为我们自定义的 as_complex 函数
# 由于我们重写了 object_hook，当遇到字典时，会调用 as_complex 函数来处理，从而能够正确地将该字典解码为复数类型
# 注意：这里的 JSON 字符串中的 'true' 应该是无引号的布尔值，但由于 Python 字符串表示的限制，这里保留了引号。
# 在实际的 JSON 数据中，它应该是没有引号的。
print(json.loads('{"__complex__": true, "real": 1, "imag": 2}', object_hook=as_complex))  # 输出: (1+2j)
# 注意：为了严谨性，上述 JSON 字符串在实际应用中应该是 '{"__complex__": true, "real": 1, "imag": 2}'（无引号围绕 true）
# 但由于 Python 字符串表示的限制和 json.loads 的解析行为，这里的代码仍然能够工作。

# 导入 decimal 模块，它提供了 Decimal 类型，用于高精度的十进制浮点运算
import decimal

# 使用 json.loads 函数解析一个表示浮点数的 JSON 字符串，指定 parse_float 参数为 decimal.Decimal
# 这将使得解析出的浮点数以 Decimal 类型表示，而不是 Python 内置的 float 类型
# Decimal 类型提供了更高精度的十进制运算，避免了浮点数运算中的精度问题
print(json.loads('1.1', parse_float=decimal.Decimal))  # 输出: Decimal('1.1')

# 在实际应用中，不需要（也不应该）在JSON字符串中为布尔值加上引号。这里的示例代码是为了在Python环境中表示JSON字符串而加上了引号。
# 在实际的JSON数据中，布尔值true和false是不带引号的。
# 当在Python中使用json.loads函数时，它会正确地解析不带引号的布尔值。
# 在上面的代码中，尽管我们在Python字符串表示中使用了带引号的'true'，
# 但json.loads函数会将其正确解析为布尔值True，因此代码能够按预期工作。然而，为了代码的清晰性和避免混淆，最好在注释中明确指出这一点。
```

### 日期序列化


```python
import json
import datetime
from json import JSONEncoder

employee = {
    "id": 456,
    "name": "William Smith",
    "salary": 8000,
    "joindate": datetime.datetime.now()
}
 
# subclass JSONEncoder
class DateTimeEncoder(JSONEncoder):
        #Override the default method
        def default(self, obj):
            if isinstance(obj, (datetime.date, datetime.datetime)):
                return obj.isoformat()
 
print("Printing to check how it will look like")
print(DateTimeEncoder().encode(employee))
 
print("Encode DateTime Object into JSON using custom JSONEncoder")
employeeJSONData = json.dumps(employee, indent=4, cls=DateTimeEncoder)
print(employeeJSONData)

```


```python
import json
import datetime
 
employee = {
    "id": 456,
    "name": "William Smith",
    "salary": 8000,
    "joindate": datetime.datetime.now()
}
print("JSON Data")
print(json.dumps(employee, default=str))
```

## 3 YAML


```python
# YAML（YAML Ain't Markup Language）是一种人类可读的数据序列化格式，用于表示数据结构和配置信息。
# 它的设计目标是易读性和易编写，强调人类友好的语法，并支持多种数据类型
```

### XML，JSON，YAML 比较


```python
# XML: 
# 优点:
#     - 强大的扩展性和灵活性，支持自定义标签和数据类型
#     - 结构化数据表示，适合用于文档表示和数据交换
#     - 支持命名空间和约束机制，可以定义严格的文档结构和数据验证规则
# 缺点:
#     - 语法冗长，可读性较差
#     - 处理和解析复杂，对于简单数据表示不够直观
#     - 标签嵌套和属性使用会增加文件大小


# YAML: 
# 优点:
#     - 简洁、可读性高的语法，类似于自然语言的表示方式。
#     - 支持多种数据类型和结构，易于表示复杂数据。
#     - 支持注释和处理指令，方便添加说明和控制数据处理。
# 缺点:
#     - 规范性和严格性较弱，不如 XML 支持约束和验证。
#     - 扩展性相对较弱，没有内置的命名空间机制。
#     - 一些编程语言的支持可能相对较少。


# JSON: 
# 优点:
#     - 简洁、易于理解和编写的语法。
#     - 轻量级，适合网络传输和数据交换。
#     - 广泛的支持和成熟的库和工具。
# 缺点:
#     - 不支持注释，可读性略逊于 YAML。
#     - 不支持自定义数据类型，对于复杂数据结构表示有限制。
#     - 对于嵌套数据的处理较为繁琐。
```

### 应用场景


```python
# - XML 适用于描述复杂的文档结构和包含大量元数据的文档，具有强大的约束和验证机制，适合于应用于复杂文档的表示和处理。
# - JSON 适用于网络传输和数据交换，具有简洁、易于理解和编写的语法，被广泛用于前后端数据交互、API 数据传输等。
# - YAML 适用于配置文件，具有简洁、可读性高的语法和支持多种数据类型和结构的特点，被广泛用于各种应用程序、脚本和工具的配置文件。

# 请注意，这只是对它们的常见用途进行概括，并不意味着它们仅限于这些场景。实际使用时，应根据具体需求、项目要求和技术栈来选择适合的格式。
```

### 示例

# 正则表达式


```python
# 正则表达式（Regular Expression）是用于处理字符串的强大工具，它在自然语言处理中有着广泛的应用，如文本搜索、数据提取和清洗等。
# Python中的正则表达式模块是re。
```

## 1 基础


```python
# 1.字符匹配：
#        . ：匹配除换行符以外的任意字符
#    [...] ：匹配方括号内的任意字符（字符集）
#   [^...] ：匹配不在方括号内的任意字符（否定字符集）
#    \d    ：匹配任意数字，等价于[0-9]
#    \D    ：匹配任意非数字字符，等价于[^0-9]
#    \w    ：匹配任意字母数字字符，等价于[a-zA-Z0-9_]
#    \W    ：匹配任意非字母数字字符，等价于[^a-zA-Z0-9_]
#    \s    ：匹配任意空白字符（空格、制表符、换行符等）
#    \S    ：匹配任意非空白字符

# 2. 量词：
#     *     ：匹配前面的子表达式零次或多次
#     +     ：匹配前面的子表达式一次或多次
#     ?     ：匹配前面的子表达式零次或一次
#   {m,n}   ：匹配前面的子表达式至少m次，不超过n次

# 3. 定位符：
#     ^     ：匹配字符串的开头  ^h
#     $     ：匹配字符串的末尾  d$
#     \b    ：匹配单词边界
#     \B    ：匹配非单词边界

# 4. 分组：
#     (exp) ：匹配exp并捕获文本到自动命名的组里。
#     (?:exp)：匹配exp但不捕获匹配的文本
#     (?<name>exp)：匹配exp并捕获文本到名称为name的组里（Python 3.6+）

# 5. 贪婪与非贪婪：
#     贪婪量词（如*、+、?、{m,n}）默认是贪婪的，会尽可能多地匹配字符
#     非贪婪量词（如*?、+?、??、{m,n}?）尽可能少地匹配字符

```

## 2 示例


```python
# 1 匹配邮箱地址：

# 导入Python的正则表达式模块
import re
text = "我的邮箱是example@gmail.com"
# 定义一个正则表达式模式用于匹配邮箱地址
# \b 表示单词边界，确保我们匹配的是完整的单词
# [A-Za-z0-9._%+-]+ 匹配邮箱地址的用户名部分，可以包含字母、数字、点(.)、下划线(_)、百分号(%)、加号(+)和减号(-)
# @ 匹配邮箱地址中的"@"符号
# [A-Za-z0-9.-]+ 匹配邮箱地址的域名部分，可以包含字母、数字、点(.)和减号(-)
# \. 匹配点(.)字符，在正则表达式中点(.)是一个特殊字符，表示任意字符，所以这里使用\进行转义
# [A-Z|a-z]{2,} 匹配顶级域名(TLD)，{2,}匹配至少两个字母的顶级域名
# \b 再次表示单词边界
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
# 使用re.findall函数在文本中查找所有匹配正则表达式的子串
# 返回值是一个列表，包含所有匹配的子串
matches = re.findall(pattern, text)
print(matches)  # 输出：['example@gmail.com']
```


```python
# 2 替换文本：

import re
text = "Hello, my phone number is 123-456-7890."
# 使用re.sub函数替换文本中的电话号码
#     \d 表示匹配一个数字
#     {3} 表示前面的元素（这里是\d，即数字）重复3次
#     - 表示匹配字符“-”
# 'XXX-XXX-XXXX' 是替换后的文本，即电话号码被替换成的形式
new_text = re.sub(r'\d{3}-\d{3}-\d{4}', 'XXX-XXX-XXXX', text)
print(new_text)  # 输出：Hello, my phone number is XXX-XXX-XXXX.
```


```python
# 3 查找并提取数字：

import re
text = "我的身高是1.75米,体重是65公斤"
#     \d+ 表示匹配一个或多个数字
#     (\.\d+)? 表示匹配一个小数点后跟一个或多个数字，整个小数部分是可选的（即可以没有)
matches = re.findall(r'\d+(\.\d+)?', text)
print(matches)  # 输出：['1.75']
```


```python
# 4 分组提取信息:

import re
text = "我的名字是张三,年龄是28岁"
# - 我的名字是 和 年龄是 是字面文本，用于匹配输入字符串中的相应部分
# - (?P<name>\w+) 是一个命名捕获组，用于匹配一个或多个单词字符（字母、数字或下划线），并将匹配到的内容命名为 'name'
# - , 是一个字面逗号，用于匹配输入字符串中的逗号
# - (?P<age>\d+) 是另一个命名捕获组，用于匹配一个或多个数字，并将匹配到的内容命名为 'age'
# - 岁 是字面文本，用于匹配输入字符串中的“岁”字
pattern = r'我的名字是(?P<name>\w+), 年龄是(?P<age>\d+)岁'
match = re.search(pattern, text)
# 如果找到了匹配项
if match:
    # 使用group方法根据捕获组的名称提取匹配到的内容
    print(f"名字：{match.group('name')}, 年龄：{match.group('age')}")
# 输出：名字：张三, 年龄：28
```

## 3 转义


```python
# 在正则表达式中，转义是指对某些特殊字符进行特殊处理，使其被视为普通字符。
# 这些特殊字符包括各种元字符（如`.`、`*`、`+`、`?`、`^`、`$`、`[`、`}`、`(`、`)`、`|`等）和转义字符本身（`\`）。
# 当你在模式中想要匹配这些字符本身而不是它们的特殊功能时，就需要使用转义。

# 1. 转义元字符：要匹配这些特殊字符，需要在它们前面加上反斜杠（`\`）。
# 2. 转义反斜杠：在许多编程语言中，反斜杠本身也是一个特殊字符，因此在字符串中需要双重转义（`\\`）来表示一个字面的反斜杠。
# 3. Python中的raw字符串：在Python中，可以使用原始字符串（raw string）来避免双重转义的问题。
# 原始字符串通过在字符串前加上`r`或`R`来表示，例如 `r'\n'` 表示一个包含字面反斜杠和`n`的字符串，而不是一个换行符。
```

## 4 示例


```python
# 1 匹配点.:

import re
pattern = r'\.'
text = "这是一个句子.这是另一个句子."
matches = re.findall(pattern, text)
print(matches)  # 输出：['.', '.']
```


```python
# 2 匹配星号*：

import re
pattern = r'\*'
text = "这个句子中有*星号*符号。"
matches = re.findall(pattern, text)
print(matches)  # 输出：['*', '*']
```


```python
# 3 匹配反斜杠\:

import re
pattern = r'\\'
text = "这个句子中有\\反斜杠\\符号。"
matches = re.findall(pattern, text)
print(matches)  # 输出：['\\', '\\']
```


```python
# 4 匹配方括号[]：

import re
pattern = r'[\[\]]'
text = "这个句子中有[方括号]符号。"
# 由于方括号在正则表达式中有特殊含义（用于定义字符类），因此需要使用反斜杠进行转义
# 所以，\[ 匹配左方括号 [，\] 匹配右方括号 ]
# 整个字符类 [\[\]] 意味着匹配单个的左方括号或右方括号
matches = re.findall(pattern, text)
print(matches)  # 输出：['[', ']']

pattern = r'\[\]'
matches = re.findall(pattern, text)
print(matches)  # 输出：[]
```

# tkinter

# 泛型


```python
# 泛型的含义是在运行时才确定真正的数据类型。

#泛型用于函数
from typing import TypeVar
# 定义了一个类型变量 T。类型变量允许函数接受任意类型的参数，只要两个参数的类型相同。
T = TypeVar("T")

def give_me_the_bigger_one(num0: T, num1: T) -> T:
    # 检查num0和num1的类型是否一致。如果不一致，则抛出ValueError异常。
    if type(num0) != type(num1):
        raise ValueError(f"The two number {num0} and {num1} must have the same type!")

    if num0 > num1:
        return num0
    else:
        return num1

print(give_me_the_bigger_one(1,2))
print(give_me_the_bigger_one(1.1,2.2))
```


```python
# 泛型用于类
from typing import List, TypeVar, Generic

T = TypeVar('T')
# 这个类模拟了一个简单的队列，其中可以存储任意类型的元素（由T指定）
class Queue(Generic[T]):
    def __init__(self) -> None:
        self.items: List[T] = []
        # 初始化一个空列表，用于存储队列中的元素。
        # 这个列表的类型是List[T]，意味着它可以存储任意类型的元素，但所有元素的类型必须相同
    def push(self, item: T) -> None:
        # 将一个元素添加到队列的末尾。
        # 参数item的类型是T，与队列中存储的元素类型相同。
        self.items.append(item)
    def pop(self) -> T:
        # 从队列的开头移除并返回一个元素。
        # 返回的元素类型是T，与队列中存储的元素类型相同。
        # 注意：这里使用pop(0)可能会导致性能问题，因为列表在Python中是基于数组的，
        # 弹出列表的第一个元素需要O(n)的时间复杂度来移动剩余的元素。
        return self.items.pop(0)
# 创建一个整数类型的Queue实例
# 这意味着这个队列只能存储整数类型的元素。
q = Queue[int]()
q.push(1)
q.pop()  # 1
q.push("string")  # 也不会报错

```

# 内嵌类


```python
# 在你自己的框架中实现类似于 Peewee 中的元数据配置机制，可以考虑创建一个基类，该基类包含一个内嵌的 Meta 类用于配置类的元数据。
# 然后，让你的其他类继承这个基类，并使用内嵌的 Meta 类来配置各个类的元数据信息。

# 自定义的基类，用于配置类的元数据
class MyBaseClass:
    class Meta:
        option1 = 'value1'
        option2 = 'value2'

# 其他类继承 MyBaseClass，并使用内嵌的 Meta 类进行配置
class MyClass1(MyBaseClass):
    class Meta:
        option3 = 'value3'

class MyClass2(MyBaseClass):
    class Meta:
        option4 = 'value4'

# print(MyClass1.Meta.option1)  # 输出: value1
# print(MyClass1.Meta.option2)  # 输出: value2
# print(MyClass1.Meta.option3)  # 输出: value3

# print(MyClass2.Meta.option1)  # 输出: value1
# print(MyClass2.Meta.option2)  # 输出: value2
# print(MyClass2.Meta.option4)  # 输出: value4

# 在这个示例中，`MyBaseClass` 是一个基类，内嵌了一个 `Meta` 类来配置基类的元数据。
# 然后，`MyClass1` 和 `MyClass2` 继承自 `MyBaseClass`，并在各自的内嵌 `Meta` 类中配置了自己的元数据选项。
# 通过这种方式，你可以在你的框架中实现类似于 Peewee 的元数据配置机制。
```


```python
# 因为 Python 并不直接支持通过类继承来“合并”内嵌类的属性。
# 当访问 MyClass1.Meta.option1 时，Python 实际上是在查找 MyClass1 中直接定义的 Meta 类里的 option1 属性，而不是回退到基类 MyBaseClass 中的 Meta 类。
# 由于 MyClass1 的 Meta 类中并没有定义 option1，因此抛出了 AttributeError。


class MyBaseClass:
    class Meta:
        option1 = 'value1'
        option2 = 'value2'

    # 一个类方法，用于获取合并后的元数据
    @classmethod
    def get_meta_options(cls):
        # 创建一个字典来存储合并后的元数据
        meta_options = {}
        # 从当前类的Meta类中获取属性
        for attr_name, attr_value in vars(cls.Meta).items():
            meta_options[attr_name] = attr_value
        # 递归地从基类的Meta类中获取属性（如果有的话）
        for base in cls.__bases__:
            if hasattr(base, 'Meta') and hasattr(base.Meta, '__dict__'):
                for attr_name, attr_value in vars(base.Meta).items():
                    # 如果当前类的Meta中没有该属性，则添加到合并后的字典中
                    if attr_name not in meta_options:
                        meta_options[attr_name] = attr_value
        return meta_options

class MyClass1(MyBaseClass):
    class Meta:
        option3 = 'value3'

class MyClass2(MyBaseClass):
    class Meta:
        option4 = 'value4'

# 使用 get_meta_options 方法来获取合并后的元数据
print(MyClass1.get_meta_options()['option1'])  # 输出: value1
print(MyClass1.get_meta_options()['option2'])  # 输出: value2
print(MyClass1.get_meta_options()['option3'])  # 输出: value3

print(MyClass2.get_meta_options()['option1'])  # 输出: value1
print(MyClass2.get_meta_options()['option2'])  # 输出: value2
print(MyClass2.get_meta_options()['option4'])  # 输出: value4
```

# Iterable 和 Iterator


```python
# 如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
# 这样就不必创建完整的list，从而节省大量的空间。
# 在python中这种一边循环一边计算的机制（惰性计算），称为生成器：generator。
a=[x for x in range(10)]
print(a)

# iter、next 为主要两个函数。
# iter() 函数用于获取一个迭代器对象。next() 函数用于获取迭代器的下一个元素。
# 如果一个对象是迭代器，那么这个对象肯定是可迭代的；但是反过来，如果一个对象是可迭代的，那么这个对象不一定是迭代器。
# 凡是可作用于for循环的对象都是Iterable类型；
# 凡是可用作next()函数的对象都是Iterator类型，它表示一个惰性计算的序列。
# 集合数据类型如list，dict，str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。


```

# 生成注释文档

# 源代码保护


```python
# - 生成.pyc文件：这是最基础的加密方法，利用Python自带的编译器将源代码文件.py编译得到的二进制的字节码文件.pyc。
# 这种方法简单方便，但是也很容易被反编译，有现成的工具如uncompyle6可以一键还原源代码。

# - 代码混淆：这是一种通过修改代码的格式、结构、命名等方式，使得代码难以阅读和理解的方法。
# 这种方法可以提高一点破解的门槛，但是也不能完全防止被还原。有一些在线工具或库可以进行代码混淆，如oxyry、pyobfuscate等。

# - 使用py2exe：这是一种将Python代码打包成可执行文件.exe的方法，可以避免用户直接看到源代码。
# 但是这种方法也有缺点，比如打包后的文件体积较大，运行速度较慢，平台兼容性差，而且也有可能被反汇编或内存dump。

# - 使用Cython：这是一种将Python代码转换成C语言代码，并编译成动态链接库.dll或.so的方法，可以提高代码的执行效率和安全性。
# 但是这种方法也有缺点，比如需要安装Cython和相应的编译器，转换后的代码可能存在兼容性或稳定性问题，而且也不能完全防止被反汇编或内存dump。
```

## py2exe

### 基础


```python
# - 安装py2exe：使用pip命令来安装py2exe，例如：`pip install py2exe`
# - 编写Python脚本：使用你喜欢的文本编辑器编写Python脚本。确保你的脚本以.py为扩展名
# - 编写设置脚本：你需要编写一个用于发布程序的设置脚本，例如mysetup.py，在其中的setup函数前插入语句`import py2exe`。
# 然后在setup函数中指定你要打包的Python脚本，以及一些打包选项，例如是否压缩，是否打包成一个文件等。例如：

# from distutils.core import setup
# import py2exe

# setup(
#     console=["hello.py"], # 指定要打包的Python脚本
#     options={
#         "py2exe":{
#             "compressed": 1, # 压缩
#             "bundle_files": 1, # 所有文件打包成一个exe文件
#         }
#     }
# )
# compressed参数是用来指定是否压缩exe文件的大小的。如果设置为1，表示压缩；如果设置为0，表示不压缩。
# 压缩可以减少exe文件的体积，但也可能增加运行时的开销。不压缩可以保持exe文件的原始大小，但也可能占用更多的磁盘空间。

# - 运行设置脚本：在命令行中导航到包含你的Python脚本和设置脚本的目录，并运行以下命令：`python mysetup.py py2exe`。
# 这将使用py2exe将你的Python脚本转换为可执行文件，并生成一个名为dist的子目录，其中包含了可执行文件和一些依赖文件。
# - 运行或分发可执行文件：你可以在Windows环境下直接运行dist目录中的可执行文件，或者将dist目录中的所有内容一起分发给其他用户。
```

### 引入文件


```python
# ## 如果你的hello.py包含了其他的Python模块或包，py2exe会尝试自动检测并打包进来。但是有些情况下，py2exe可能无法正确识别你的依赖，比如你使用了动态导入或者第三方库。
# 这时候，你可以在设置脚本中使用includes或packages选项来强制包含你需要的模块或包。例如：

# from distutils.core import setup
# import py2exe
# setup(
#     console=["hello.py"], # 指定要打包的Python脚本
#     options={
#         "py2exe":{
#             "compressed": 1, # 压缩
#             "bundle_files": 1, # 所有文件打包成一个exe文件
#             "includes": ["numpy", "pandas"], # 强制包含numpy和pandas模块
#             "packages": ["requests"], # 强制包含requests包
#         }
#     }
# )

# ## 你想要手动指定要打包的py文件，而不是让py2exe自动扫描你的依赖。这样的话，你可以使用packages或者py_modules参数来指定要打包的包或者模块，例如：

# setup(
#     # 其他参数
#     packages = ['mypackage1', 'mypackage2'], # 指定要打包的包
#     py_modules = ['mymodule1', 'mymodule2'], # 指定要打包的模块
# ) 
# 这样的话，py2exe只会打包你指定的包或者模块，而不会自动分析你的导入语句。不过，这样做的话，你需要确保你指定的包或者模块能够满足你的程序的所有依赖，否则可能会出现运行时错误。
#  如果你写了packages或者py_modules，那么py2exe就不会自动扫描你的其他依赖了。它只会打包你指定的包或者模块，以及它们的子包或者子模块。
#  但是，它仍然会扫描你在console里指定的.py文件作为你的程序的入口点，因为它需要知道你的程序要从哪里开始运行。

# ## 如果你有几个包含.py文件的目录，且有子目录，你应该确保每个目录和子目录都有__init__.py文件，这样它们才能被识别为包。然后你可以用packages参数来指定要打包的包，例如

# setup(
#     # 其他参数
#     packages = ['dir1', 'dir2', 'dir3'], # 指定要打包的包,只要列出最顶层的目录就可以了。
# )

# ## 如果你的hello.py需要一些非Python的文件，比如图片、音频、配置文件等，py2exe不会自动打包进来。
# 这时候，你可以在设置脚本中使用data_files选项来指定那些额外的文件，那么py2exe能将这些文件拷贝到dist子目录中。例如：

# from distutils.core import setup
# import py2exe
# setup(
#     console=["hello.py"], # 指定要打包的Python脚本
#     options={
#         "py2exe":{
#             "compressed": 1, # 压缩
#             "bundle_files": 1, # 所有文件打包成一个exe文件
#         }
#     },
#     data_files=[("images", ["images/logo.png", "images/background.jpg"]), # 指定要打包的图片文件
#                 ("config", ["config/settings.ini"]), # 指定要打包的配置文件
#                ]
# )

```

### 启动前处理


```python
# 如果你想在运行可执行文件之前执行一些动作、脚本或命令
# 1.使用批处理文件：你可以编写一个批处理文件（.bat），在其中写入你想要执行的动作、脚本或命令，然后调用你的可执行文件。例如：(Batch语言)

# @echo off
# rem 这里写入你想要执行的动作、脚本或命令
# echo Hello, this is a batch file
# python some_script.py
# rem 这里调用你的可执行文件
# hello.exe

# 2.使用启动脚本：你可以在设置脚本中使用startup选项来指定一个Python脚本，该脚本会在运行可执行文件之前被执行。例如：

# from distutils.core import setup
# import py2exe
# setup(
#     console=["hello.py"], # 指定要打包的Python脚本
#     options={
#         "py2exe":{
#             "compressed": 1, # 压缩
#             "bundle_files": 1, # 所有文件打包成一个exe文件
#             "startup": "startup.py", # 指定启动脚本
#         }
#     }
# )

# 3.使用初始化函数：你可以在设置脚本中使用initscript选项来指定一个Python函数，该函数会在运行可执行文件之前被调用。例如：

# from distutils.core import setup
# import py2exe
# def init_func():
#     # 这里写入你想要执行的动作、脚本或命令
#     print("Hello, this is an init function")
#     import some_module
# setup(
#     console=["hello.py"], # 指定要打包的Python脚本
#     options={
#         "py2exe":{
#             "compressed": 1, # 压缩
#             "bundle_files": 1, # 所有文件打包成一个exe文件
#             "initscript": init_func, # 指定初始化函数
#         }
#     }
# )
```

###　环境


```python
# py2exe会将Python运行环境的一部分打包进exe文件中：
# - 你的Python脚本和它依赖的Python模块或包（如果py2exe能自动检测到的话）
# - 一些必要的Python库文件，如python**.dll，加上其它的.dll文件
# - 一个library.zip文件，它包含了已编译的纯的Python模块如.pyc或.pyo

# 不会打包以下内容：
# - Python解释器本身，你仍然需要在目标机器上安装Python才能运行exe文件
# 　　如果你使用bundle_files = 3的打包模式，那么py2exe不会打包Python解释器本身，你仍然需要在目标机器上安装Python才能运行exe文件。
# 　　但是，如果你使用bundle_files = 1或者2的打包模式，那么py2exe会把Python解释器本身也打包到zip文件或者exe文件里，这样你就不需要在目标机器上安装Python了。
# - 一些额外的文件，如配置文件、字体、图标等，你需要在设置脚本中用data_files选项来指定那些额外的文件
# - 一些难以检测或导入的模块或包，如numpy、scipy等，你需要在设置脚本中用includes或packages选项来强制包含那些模块或包
```

### 命令行参数


```python
# 如果你的hello.py是接受命令行参数的，那么打包为exe之后，也可以接受命令行参数。你只需要在命令行中调用exe文件，并传入相应的参数即可。例如，如果你的hello.py是这样的：


# import sys
# def say_hello(name):
#     print("Hello, " + name)
# if __name__ == "__main__":
#     name = sys.argv[1] # 接受命令行参数
#     say_hello(name)

# 那么你可以在命令行中运行`hello.exe Alice`，就会输出`Hello, Alice`。
```

### 设定图标


```python
# 在py2exe中添加图标的方法是在设置脚本中使用icon_resources选项来指定图标文件的路径和资源ID。例如：

# from distutils.core import setup
# import py2exe
# setup(
#     console=[{"script": "hello.py", "icon_resources": [(1, "hello.ico")]}] # 指定图标文件的路径和资源ID
# )

# 这样，打包后的exe文件就会使用hello.ico作为图标。注意，图标文件必须是.ico格式的，如果不是，可以使用一些工具如Greenfish Icon Editor Pro来转换。
# 另外，如果想要打包GUI形式的exe文件，可以使用windows选项代替console选项。
```

### 打包文件查看


```python
# py2exe打包后会在当前目录下生成一个dist文件夹，里面包含了exe文件和一些依赖的文件。你可以查看dist文件夹的内容来了解py2exe打包了哪些文件。一般来说，dist文件夹中会有以下这些文件：

# - 一个或多个exe文件，这是你的程序的可执行文件。
# - python**.dll，这是Python运行环境的动态链接库。
# - 一些.pyd文件，这些是已编译的扩展模块，是exe文件所需要的。
# - 一些.dll文件，这些是.pyd文件所需要的动态链接库。
# - 一个library.zip文件，这个文件包含了已编译的纯Python模块，如.pyc或.pyo。

# 如果你在设置脚本中使用了data_files选项来指定一些额外的文件，比如配置文件、图片、音频等，那么py2exe也会将这些文件拷贝到dist子目录中。你可以在dist子目录中找到这些额外的文件。
```

### 常见错误

# 变量的作用域

## 分类


```python
# 1. 局部作用域（Local Scope）：变量在函数内部定义，只在函数内部可见。
# 2. 嵌套作用域（Enclosing Scope）：变量在嵌套的函数内部定义，可以在外层函数以及内部函数中访问。
# 3. 全局作用域（Global Scope）：变量在函数外部定义，对整个模块都可见。
# 4. 内置作用域（Built-in Scope）：变量是 Python 内置的，在整个程序中都可见。
```

## 示例


```python
# 全局作用域
global_a = 10

def example_function():
    # 局部作用域
    local_a = 20
    
    def nested_function():
        # 嵌套作用域
        nested_a = 30
        print(nested_a)
        print(local_a)  # 可以访问外层函数的变量
    
    nested_function()
    print(local_a)

example_function()
print(global_a)

# 在这个示例中，global_a 是在全局作用域中定义的，可以在整个模块中访问
# local_a 是在 example_function 函数内部定义的，只能在该函数内部访问
# nested_a 是在 nested_function 函数内部定义的，可以在嵌套作用域和外层函数的作用域中访问
```

## 修改作用域的变量


```python
# 全局作用域
global_a = 10

def outer_function():
    # 闭包作用域
    enclosing_a = 20
    
    def inner_function():
        # 局部作用域
        local_a = 30
        # 修改闭包作用域的变量
        nonlocal enclosing_a
        enclosing_a = 25
        # 修改全局作用域的变量
        global global_a #使用 global 关键字来告诉 Python global_a是一个全局变量：
        global_a = 15
    
    inner_function()
    print("Enclosing variable after modification:", enclosing_a)  # 输出 25

outer_function()
print("Global variable after modification:", global_a)  # 输出 15
```

## 声明


```python
x = 5
def fun1():
    print(x)
def fun2():
    print(x)
print(x)
fun1()
fun2()
# 5
# 5
# 5

x = 5
def fun1():
    x = 4
    print(x)
def fun2():
    x = 3
    print(x)
print(x)
fun1()
fun2()
# 5
# 4
# 3

```

## 示例


```python
# x = 5
# def fun1():
#     x = x+1
#     print(x)

# print(x)
# fun1()

# 输出，UnboundLocalError: local variable 'x' referenced before assignment
# 在函数内部使用变量 x 时，Python 首先假设 x 是一个局部变量（因为它是在函数内部被赋值的）。
# 然而，在赋值之前，Python 需要知道 x 的初始值来进行加法运算。
# 由于此时 x 还未被声明为局部变量（赋值操作尚未执行），Python 抛出了一个 UnboundLocalError 错误，指出局部变量 x 在赋值前就被引用了。

x = 5
def fun1():#使用全局变量
    global x
    x = x + 1
    print(x)
print(x)  # 输出 5
fun1()    # 输出 6
print(x)  # 输出 6，显示全局变量已被修改

x = 5
def fun1(x):# 参数传递
    x = x + 1
    print(x)
print(x)  # 输出 5
fun1(x)   # 输出 6，但这不会改变全局的 x
print(x)  # 仍然输出 5

```

# Counter类


```python
# Counter 是 Python 中 collections 模块提供的一个类，它用于计数器。它可以用于统计列表、字典、元组等数据结构中各个元素的出现次数。
# `Counter` 类非常适用于需要统计元素出现次数的场景，尤其是当你处理的是可哈希对象（比如整数、字符串）的时候。它比使用内置的 `dict` 更高效，因为 `Counter` 专门为计数而优化。
```

## 基础


```python
from collections import Counter

# 1. 创建 Counter 对象：
# 直接从列表创建 Counter 对象
c = Counter([1, 2, 2, 3, 4, 4, 4])
print(c)  # 输出：Counter({4: 3, 2: 2, 1: 1, 3: 1})
# 或者从字典创建 Counter 对象
d = Counter({'a': 4, 'b': 2, 'c': 0})
print(d)  # 输出：Counter({'a': 4, 'b': 2, 'c': 0})

# 2. 获取元素数量：
print(c[2])  # 输出：2

# 3. 获取唯一元素的列表：
print(c.keys())  # 输出：dict_keys([1, 2, 3, 4])

# 4. 获取元素计数：
print(c.values())  # 输出：dict_values([1, 2, 1, 3])

# 5. 获取所有元素的组合：
print(c.items())  # 输出：dict_items([(1, 1), (2, 2), (3, 1), (4, 3)])

# 6. 元素累加：
c += Counter([5, 5, 5])
print(c)  # 输出：Counter({4: 3, 5: 3, 2: 2, 1: 1, 3: 1})

# 7. 元素相减：
c -= Counter({2: 1, 4: 1})
print(c)  # 输出：Counter({5: 3, 4: 2, 1: 1, 2: 1, 3: 1})

# 8. 元素比较：
print(c == Counter({1: 1, 2: 1, 3: 1, 4: 2, 5: 3}))  # 输出：True

# 9. 元素合并：
c.update([6, 7, 8])
print(c)  # 输出：Counter({5: 3, 4: 2, 1: 1, 2: 1, 3: 1, 6: 1, 7: 1, 8: 1})

# 10. 元素去重：
c.clear()
print(c)  # 输出：Counter()
```

# 多线程

# Server

# asynico

# 其他

# 性能优化

# 单分派泛函数

# 函数可变默认参数问题

## 可变默认参数问题


```python
# - 当定义函数（包括类的方法，如`__init__`方法）时，默认参数只在函数定义时被创建一次。
# - 在你的`__init__(type,points = [])`这个构造函数中，`points`是一个默认参数，并且它是一个可变对象（列表）。当第一次调用构造函数并且没有传递`points`参数时，会使用默认的空列表。
# - 但是，下次再调用构造函数（同样没有传递`points`参数）时，仍然会使用最初定义函数时创建的那个列表对象。这就导致如果之前对这个列表进行了修改，修改后的状态会被保留。

class MyClass:
    def __init__(self, type, points=[]):
        self.type = type
        self.points = points

obj1 = MyClass("Type1")
obj1.points.append(1)
print(obj1.points)  # 输出 [1]

obj2 = MyClass("Type2")
print(obj2.points)  # 输出 [1]，而不是期望的 []

#  在这个例子中，`obj1`修改了`points`列表（添加了元素1）。
# 当创建`obj2`时，由于`points`默认参数是在函数定义时创建的同一个列表对象，所以`obj2.points`也包含了之前添加的元素1。
```

## 解决方法相关知识


```python
# - 一种常见的解决方法是使用`None`作为默认参数，然后在函数内部根据参数是否为`None`来创建可变对象。例如：

class MyClass:
    def __init__(self, type, points=None):
        self.type = type
        if points is None:
            self.points = []
        else:
            self.points = points

# - 这样，每次创建新的实例时，如果没有传递`points`参数，都会创建一个新的空列表，而不是共享之前的列表。
# - 或者每次都传递一个[]进去，这样默认参数的含义就不大了，但也可以达成不共享的问题
```

# 面对对象编程
计算机编程经过多年的发展，演变出了三种不同且常用的编程思想，分别是：

- 面向过程编程思想（POP）
- 面向对象编程思想（OOP）
- 函数式思想（FP）

## 解释
比如我们想把一只大象装进冰箱，分别用三种思想，我们看看有什么不一样。

1. 面向过程思想  
如果我们采用面向过程的思想，可以分为三步：  
- 打开冰箱门  
- 把大象塞进去  
- 关上冰箱门  

面向过程编程就是分析出解决问题所需要步骤，然后分别实现每一步，再一步步执行即可。

2. 面向对象思想  

面向对象是什么？

比如我们可以把你家的冰箱理解为一个对象，我们就可以研究你家冰箱由哪些部分（指令装置等）组成，你家冰箱能干什么（制冷、调温等）？

接着我们开始下定义，就是取个高大上的名字

|冰箱	|定义	|举例|
|---|---|---|
|冰箱的组成部分	|冰箱的属性	|制冷器，调温旋钮、灯带等|
|冰箱能干什么	|冰箱的行为	|制冷，调温、照明等|

对象的行为其实是对其属性的操作，比如对制冷器操作就可以制冷，给灯带通电就可以照明。

对象 = 属性+行为

接着我们开始采用OOP的方法把大象装进冰箱

- 调用：冰箱->打开门(行为)  
- 调用：冰箱->装东西(行为)
- 调用：冰箱->关闭门(行为)

看起来和面向过程没啥区别，但我们的思想发生了重大的转变，我们把冰箱当作了一个独立的对象，我们是通过和冰箱这个对象交互完成了整个过程。

3. 函数式编程
定义关进（冰箱，大象）函数  
实现函数：关门(放入(开门(冰箱)，大象))  

## 重要概念
面向对象中有五个重要的概念

1. 类与对象（抽象与具体）

我们通过调用你家美的冰箱的开门、装东西和关门三个行为来把大象装进冰箱。这时我们可以把你家的美的冰箱（具体的）称之为一个对象，而冰箱（抽象的）就称为一个类。

2. 封装、继承与多态

封装,将属性和行为封装在一起。上面已经介绍了对象 = 属性+行为，比如冰箱将冰箱的温度值（属性）和对温度值的操作（行为）等封装在一起。

继承，

多态，我们可以说鲤鱼是鱼类，草鱼是鱼类。同一个鱼类可以有多种不同的类型，即多态。
