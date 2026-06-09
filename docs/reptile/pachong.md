# 目录


---
# http协议

http超文本传输协议
html超文本标记语言

请求 
请求行：请求方式，url地址，协议  
请求头：服务器使用的附加信息  
请求体：一些请求参数  
  
响应  
状态行：协议，状态码(200,404等)  
响应头：客户端要使用的附加信息(数据加密，密钥，cookie等)  
响应体：服务器返回的真正客户端要用到的内容(html,json)等  

要格外注意请求头和响应头，一般隐含重要内容

请求头重要内容：  
User-Agent:请求载体的身份标识(用啥发送的请求)
Referer：防盗链(这次请求是从哪个页面来的，反爬用到)
cookie:本地字符串数据信息(用户登录信息，反爬的token)

响应头重要内容：
cookie：
各种奇怪的字符串：(需要经验，一般是token字样，防止攻击和反爬)

请求方式：
1.GET
2.POST

# web请求过程

渲染  
1.服务器渲染  
2.客户端渲染:第一次请求只有html骨架，第二次请求拿到数据。在页面源代码中看不到数据  

使用浏览器抓包工具  
F12 检查  

Elements（元素）：显示网页的HTML结构，允许用户查看和编辑DOM元素及其属性。通过此面板，用户可以轻松地找到网页中的特定元素，并查看或修改其HTML代码和CSS样式。  
Console（控制台）：用于显示JavaScript错误、警告和日志信息。开发者可以在此面板中输入JavaScript代码进行测试或调试。  
Network（网络）：显示网页加载过程中请求的资源及其加载时间、大小等信息。这对于分析网页性能问题非常有用。  
Sources（源代码）：显示网页的源代码文件，包括HTML、CSS、JavaScript等。开发者可以在此面板中查看、编辑和调试源代码。  
其他选项卡：根据浏览器的不同，还可能包括其他选项卡，如“Application（应用）”、“Performance（性能）”、“Memory（内存）”等，用于展示和分析网页的不同方面。  

打开开发者工具：在网页上点击鼠标右键，然后选择“检查”或“查看元素”选项（具体表述取决于浏览器）。另外，也可以通过快捷键（如F12或Command+I）打开开发者工具。
选择Elements面板：在开发者工具窗口中，选择“Elements”面板以查看和编辑网页的HTML结构和CSS样式。
查找元素：在“Elements”面板中，可以使用鼠标在网页上悬停以突出显示对应的DOM元素，或者使用搜索框输入元素的标签名、类名或ID来快速定位元素。
编辑元素：找到目标元素后，可以双击其HTML代码或CSS样式进行修改。修改后，网页的显示效果会实时更新。
查看控制台信息：在“Console”面板中，可以查看网页加载过程中产生的JavaScript错误、警告和日志信息。这些信息有助于开发者定位和解决网页中的问题。
分析网络请求：在“Network”面板中，可以查看网页加载过程中请求的资源及其加载时间、大小等信息。通过分析这些信息，可以找出影响网页性能的关键因素。

# 网络爬虫库

一、HTTP请求库
urllib：这是Python标准库中的一个模块，提供了一系列用于处理URL的函数，可以方便地进行网页的下载和请求。它支持多种协议，包括HTTP、HTTPS、FTP等。
requests：这是一个基于urllib编写的HTTP库，提供了更简洁、易用的API。requests库支持GET、POST等多种HTTP请求方法，并且可以方便地设置请求头、cookies等信息。
httplib2：这是另一个Python HTTP库，提供了类似于urllib的功能，但具有更好的性能和更多的特性。
unirest：Unirest是一套可用于多种语言的轻量级的HTTP库，也支持Python。
aiohttp：这是基于asyncio实现的HTTP框架，支持异步操作。使用异步库进行数据抓取可以大大提高效率。

二、网页解析库
BeautifulSoup（bs4）：这是一个HTML和XML的解析库，可以从网页中提取信息。BeautifulSoup提供了强大的API和多种解析方式，可以方便地遍历和搜索文档树。
lxml：这是一个高效的HTML和XML解析库，支持XPath解析方式。由于它是用C语言编写的，因此解析速度非常快。
pyquery：这是jQuery的Python实现，可以以jQuery的语法来操作解析HTML文档。它提供了类似于jQuery的选择器和操作方法，使得解析HTML变得更加简单。
cssselect：这个库用于解析DOM树和CSS选择器，可以与lxml等库结合使用来提取网页中的特定元素。

三、爬虫框架
Scrapy：这是一个功能强大的爬虫框架，可以满足简单的页面爬取需求。Scrapy提供了完整的爬虫流程和各种强大的功能，包括异步处理、自动化流程控制、网页解析、数据存储等。使用Scrapy可以轻松地构建和部署爬虫程序。
pyspider：这是一个强大的爬虫系统，支持分布式爬取和多种数据库存储。pyspider提供了丰富的配置选项和可扩展的插件机制，使得定制爬虫变得更加容易。
Cola：这是一个分布式爬虫框架，但项目整体设计可能存在一些问题，模块间耦合度较高。
Portia：这是基于Scrapy的可视化爬虫工具，可以通过图形界面来配置和生成爬虫程序。

四、其他相关库
Selenium：这是一个自动化测试工具，也可以用来进行网页抓取。Selenium可以模拟浏览器的行为进行网页抓取，特别适用于处理使用JavaScript加载内容的网站。但需要注意的是，由于使用了浏览器驱动，Selenium的效率相对较低。
Tesserocr：这是一个OCR库，在遇到验证码（图形验证码为主）的时候，可以直接用OCR进行识别。
Newspaper：这个库用于新闻、文章的提取和内容分析，可以方便地提取网页中的新闻或文章内容。

此外，还有一些用于处理特定任务的库，如处理Unicode文本的ftfy、进行字符串匹配的fuzzywuzzy、进行正则表达式加速的esmre等。这些库可以根据具体需求进行选择和使用。


# NetWork

跟第二次请求有关：

fetch
定义：
fetch是一个现代JavaScript API，用于发起网络请求并获取资源。它提供了一个基于Promise的接口，用于访问和操纵HTTP管道的一部分，如请求和响应。
用途：
fetch主要用于在客户端（如浏览器）与服务器之间异步地请求和接收数据。它支持各种HTTP方法（如GET、POST等），并且可以发送和接收多种类型的数据（如JSON、文本、二进制数据等）。
优势：
简洁的API设计，使得发起请求和处理响应变得更加容易。
基于Promise的实现，支持异步操作，不会阻塞页面的其他功能。
提供了对请求和响应的细粒度控制，如设置请求头、处理响应状态等。

XHR（XMLHttpRequest）
定义：
XHR是XMLHttpRequest的缩写，它是一种在客户端和服务器之间传输数据的技术。XHR对象允许Web应用程序与服务器交换数据，而无需重新加载整个页面，从而实现了页面的局部更新或异步数据交互。
用途：
XHR主要用于在Web应用程序中实现Ajax（Asynchronous JavaScript and XML）功能。它允许Web页面在用户与页面交互时异步地请求和接收数据，从而提高了用户体验和页面性能。
工作原理：
XHR对象通过创建和发送HTTP请求来与服务器进行通信。请求可以是GET、POST、PUT、DELETE等HTTP方法。服务器接收到请求后，会处理请求并返回响应。XHR对象可以接收并处理这些响应，然后根据需要对页面进行更新。
优势：
实现了页面的异步更新，无需重新加载整个页面即可获取新的数据。
支持多种数据格式和HTTP方法，提供了灵活的数据交互方式。
被所有主流浏览器支持，具有良好的跨平台兼容性。

fetch与XHR的比较
语法和API设计：fetch提供了更简洁和现代的API设计，而XHR则相对繁琐一些。fetch基于Promise实现，使得异步操作更加直观和易于管理。
功能和灵活性：XHR提供了更多的功能和灵活性，如支持超时设置、进度事件等。而fetch则需要通过其他方式（如使用AbortController处理超时）来实现这些功能。
浏览器兼容性：虽然现代浏览器都支持fetch和XHR，但在一些老旧浏览器中可能只支持XHR。因此，在需要考虑浏览器兼容性的情况下，XHR可能是一个更稳妥的选择。

Doc（Documents文档）：
通常指的是HTML文档，它是网页的基本结构。HTML文档包含了网页的内容，如文本、图像、链接等，并通过HTML标签来定义这些内容。
在网络请求中，HTML文档通常是最先加载的，因为它定义了网页的其他资源（如JS和CSS文件）的位置和如何加载它们。

JS（JavaScript）：
JavaScript是一种用于创建动态和交互式网页的编程语言。它允许开发者在用户的浏览器上运行脚本，以改变网页内容、响应用户输入、动画效果等。
JS文件通常以.js扩展名保存，并通过<script>标签在HTML文档中引用。在现代网页开发中，JavaScript是不可或缺的一部分，用于实现网页的交互性和动态功能。

CSS（Cascading Style Sheets，层叠样式表）：
CSS用于描述HTML文档的表现样式。它允许开发者控制网页的布局、颜色、字体、动画等视觉元素。
CSS文件通常以.css扩展名保存，并通过<link>标签在HTML文档中链接。CSS的“层叠”特性意味着它可以合并来自多个来源的样式规则，并根据优先级规则应用这些样式。

font：
在网页开发中，font通常指的是字体资源。字体资源可以是本地安装的字体，也可以是网络字体（如通过@font-face规则引入的字体）。
字体资源对于网页的视觉效果至关重要，它们决定了网页中文本的外观和风格。

img：
img是HTML中的<img>标签的简写，用于在网页上嵌入和显示图片。
<img>标签通过指定图片资源的路径，使得网页能够加载并展示各类图像，如照片、图标、图表等，从而丰富网页的视觉内容和用户体验。

media：
在网页开发中，media通常指的是媒体资源，这些资源可以是音频、视频、动画等多媒体内容。
媒体资源通过HTML的<audio>、<video>等标签进行嵌入和播放，为用户提供更加丰富的视听体验。
此外，media在CSS中也被用作媒体查询的一部分，用于根据不同的设备特性和条件应用不同的样式规则。

manifest：
manifest在网页开发中，它通常与软件或应用程序的元数据文件相关联。
这些文件包含了关于应用程序、库、组件或资源的信息，如版本号、依赖项、配置设置等。
例如，在Web应用中，应用程序清单（Application Manifest）是一个XML文件，它描述了应用程序如何与操作系统交互，以及应用程序需要哪些权限才能运行。

ws：
ws作为缩写有多种含义，但在网络开发中，它可能指的是“Web Server”（网络服务器）或“WebSocket”。
Web Server是提供网页资源访问的服务器，它接收客户端的请求并返回相应的资源。
WebSocket则是一种在单个TCP连接上进行全双工通讯的协议，它允许服务器和客户端之间进行实时的双向数据传输。

wasm：
wasm是WebAssembly的缩写，它是一种为网络设计的新型代码格式，旨在提供更快的执行速度。
WebAssembly是一种低级字节码格式，可以被现代Web浏览器以接近原生性能的速度执行。
它允许开发者用多种编程语言编写代码，然后将其编译成WebAssembly格式，从而在Web上实现高效运行。
综上所述，这些术语在网页开发和网络请求中扮演着重要的角色，它们各自具有特定的含义和用途。

# 数据解析方式

## 1.re解析(运行速度快)

### 基础


```python
# 1.字符匹配：
#        . ：匹配 除换行符以外 的 任意字符
#    [...] ：匹配 方括号内的任意字符（字符集）   示例：[A-Za-z0-9]
#   [^...] ：匹配 不在方括号内的任意字符（否定字符集）
#    \d    ：匹配任意 数字          等价于[0-9]
#    \D    ：匹配任意 非数字        等价于[^0-9]
#    \w    ：匹配任意 字母数字      等价于[a-zA-Z0-9_]
#    \W    ：匹配任意 非字母数字    等价于[^a-zA-Z0-9_]
#    \s    ：匹配任意 空白字符（空格、制表符、换行符等）
#    \S    ：匹配任意 非空白字符
#    \n    ：匹配 换行符
#    \t    ：匹配 制表符
#    a|b   ：匹配 a或b

# 2. 量词：
#     *     ：匹配前面的子表达式  零次或多次
#     +     ：匹配前面的子表达式  一次或多次
#     ?     ：匹配前面的子表达式  零次或一次
#   {m,n}   ：匹配前面的子表达式  m到n次

# 3. 定位符：
#     ^     ：匹配字符串的开头  (^h开头只能是h)
#     $     ：匹配字符串的末尾  (d$结尾只能是d)
#     \b    ：匹配单词边界
#     \B    ：匹配非单词边界

# 4. 分组：
#     (exp) ：匹配exp并捕获文本到自动命名的组里。
#     (?:exp)：匹配exp但不捕获匹配的文本
#     (?<name>exp)：匹配exp并捕获文本到名称为name的组里（Python 3.6+）

# 5. 贪婪与非贪婪：
#     贪婪量词（如*、+、?、{m,n}）默认是贪婪的，会尽可能多地匹配字符
#     非贪婪量词（如*?、+?、??、{m,n}?）尽可能少地匹配字符(.*?爬虫用的多)
```


```python
import re
text="uguiioaifegxihgiohpx"
pattern=r'.*?x'#惰性
print(re.findall(pattern,text))#['uguiioaifegx', 'ihgiohpx']
pattern=r'.*x'#贪婪
print(re.findall(pattern,text))#['uguiioaifegxihgiohpx']
```

### 模块


```python
text="uguiioaifegxihgiohpx"
pattern=r'.*?x'#惰性

# 1.findall 查找所有，返回list

# 2.search 返回第一个匹配到的结果，没有返回None
it=re.search(pattern,text)
print(it.group())# uguiioaifegx

# 3.match 只从开头匹配(默认正则表达式前有^)
 
# 4.finditer 类似findall，但返回的是迭代器，效率更高(重点)(从迭代器中拿取内容用.group())
it=re.finditer(pattern,text)
for i in it:
    # print(i)
    # <re.Match object; span=(0, 12), match='uguiioaifegx'>
    # <re.Match object; span=(12, 20), match='ihgiohpx'>
    print(i.group())
    # uguiioaifegx
    # ihgiohpx
```

### 预加载(适用于表达式较长，且多次使用)


```python
pattern=re.compile(r'.*?x',re.S)#re.S:让表达式能匹配换行符
text="uguiioaifegxihgiohpx"
print(pattern.findall(text))
```

### 分组


```python
# (?P<分组命名>表达式) 单独从匹配内容中进一步提取内容
```

### csv库
以逗号分割数据并储存
便于pandas读取

## 2.bs4解析(beautiful soup 4)(写起来简单，效率不高)

### html的语法


```python
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>网页标题</title>
    <!-- 其他头部信息，如样式表链接、脚本链接等 -->
</head>
<body>
    <!-- 网页的可见内容 -->
</body>
</html>


```

<!DOCTYPE html>：声明文档类型，告知浏览器这是一个HTML5文档。
<html>：HTML文档的根元素。
<head>：包含文档的元数据（metadata），如字符集声明、标题、样式表链接等。
<meta charset="UTF-8">：指定文档的字符编码为UTF-8。
<title>：指定网页的标题，显示在浏览器的标签栏上。
<body>：包含网页的可见内容，如文本、图像、链接等。


标签
HTML标签通常由尖括号包围，例如<tagname>。大多数标签是成对出现的，有一个开始标签和一个结束标签，结束标签在标签名前加上斜杠，例如</tagname>。但是，也有一些自闭合标签，如<img/>、<br/>等，它们不需要结束标签。

属性
HTML标签可以包含属性（attributes），这些属性提供了关于标签的额外信息。属性通常写在开始标签内，以键值对的形式出现，键和值之间用等号连接，值用引号括起来。例如：
<a href="https://www.example.com">这是一个链接</a>

### bs4


```python
# 通过标签的属性来拿到标记的内容
# pip install bs4(我用的)

# pip install beautifulsoup4
# Beautiful Soup 是一个用于解析 HTML 和 XML 的库，但它本身不解析网页或文件。为了解析 HTML 或 XML 文档，Beautiful Soup 需要一个解析器。
# Python 标准库中包含了一个 HTML 解析器 html.parser，它是 Beautiful Soup 可以使用的，但它不是最快的，也不是最好的。

# 更常见的是，人们会使用第三方解析器，如 lxml 或 html5lib。
# lxml 是一个非常快速且高效的解析器，但它是一个 C 库，需要单独安装。
# html5lib 是一个纯 Python 编写的解析器，它完全遵循 HTML5 标准。
# pip install lxml
```


```python
# find(标签，属性=值)  找第一个并返回
# find_all(标签，属性=值)  所有满足的都返回
# 当属性与python中关键字冲突时，在属性后加一个下划线。或者使用字典 attrs={'属性':'值'}
```


```python
from bs4 import BeautifulSoup
# soup = BeautifulSoup(html_doc, 'lxml')
# soup.find_all()：返回所有匹配的元素，返回一个列表(注意是列表)
# soup.find()：返回第一个匹配的元素。
# soup.select()：使用 CSS 选择器语法查找元素。

# .text提取内容   .get()提取标签内容
# links = soup.find_all('a')
# for link in links:
#     print(link.get('href'))

# 使用 select() 查找所有 class 为 "sister" 的 <a> 标签
# sister_links = soup.select('a.sister')
# for sister in sister_links:
#     print(sister.get('href'))


```

## 3.xpath解析


```python
# XPath（XML Path Language）是一种在XML文档中查找信息的语言。
# 通过XPath可以定位XML文档中的节点（elements）、属性（attributes）、文本内容（text）等。
# XPath被广泛应用于XSLT（一种用于转换XML文档的语言）、XQuery（一种用于查询XML数据的语言）以及许多编程语言（如Python、Java、C#等）的XML处理库中。

# html是XML的子集
```

### 基本


```python
# pip install lxml

# 节点选择
# /：从根节点选择。
# //：从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置。
# .：选择当前节点。
# ..：选择当前节点的父节点。
# @：选择属性。
# * :任意节点，通配符

# 谓语
# 用于过滤节点，格式为[条件]。
```

### 示例


```python
<bookstore>
    <book category="cooking">
        <title lang="en">Everyday Italian</title>
        <author>Giada De Laurentiis</author>
        <year>2005</year>
        <price>30.00</price>
    </book>
    <book category="children">
        <title lang="en">Harry Potter</title>
        <author>J K. Rowling</author>
        <year>2005</year>
        <price>29.99</price>
    </book>
</bookstore>
```


```python
# 1. 选择所有book节点
# /bookstore/book

# 2. 选择所有title节点
# /bookstore/book/title

# 3. 选择第一个book节点的title
# /bookstore/book[1]/title

# 4. 选择所有category为"cooking"的book节点
# /bookstore/book[@category='cooking']

# 5. 选择所有价格低于30.00的book节点
# /bookstore/book[price<30.00]

# 6. 选择所有title节点的文本内容
# /bookstore/book/title/text()

# 7. 选择所有title节点的lang属性
# /bookstore/book/title/@lang
```


```python
from lxml import etree

# 加载XML文档
xml_data = '''
<bookstore>
    <book category="cooking">
        <title lang="en">Everyday Italian</title>
        <author>Giada De Laurentiis</author>
        <year>2005</year>
        <price>30.00</price>
    </book>
    <book category="children">
        <title lang="en">Harry Potter</title>
        <author>J K. Rowling</author>
        <year>2005</year>
        <price>29.99</price>
    </book>
</bookstore>
'''

root = etree.fromstring(xml_data)

# 使用XPath查询
books = root.xpath('/bookstore/book')
titles = root.xpath('/bookstore/book/title/text()')# /text()拿文本
cooking_books = root.xpath('/bookstore/book[@category="cooking"]')
category = root.xpath('/bookstore/book/@category')# /@拿属性

print(f"Books: {books}")
print(f"Titles: {titles}")
print(f"Cooking Books: {cooking_books}")
print(f"Category: {category}")
```

# request进阶

## cookie  
模拟浏览器登陆

使用session（会话）进行请求（可以认为是一连串的请求，这个过程中cookie不会丢失）


```python
import requests
session=requests.session()#创建session，之后使用方法和request类似
data={
    'loinName':'15873369893',
    'password':'zhl@15873369893'

}
url=''
res=session.post(url,data=data)

```

## 防盗链处理


```python

```

## 代理  
防止IP被封

# 异步提速  
进程是资源单位，线程是执行单元
进程至少包含一个线程
程序启动默认会有一个主线程

## 多线程


```python
from threading import Thread

def func():
    for i in range(10):
        print('func',i)

if __name__=='__main__':
    t=Thread(target=func)   #创建一个新线程，并告诉它执行func这个工作
    t.start()   #线程状态为可执行，具体什么时候执行由CPU决定

    for i in range(10):
        print('main',i)
```


```python
#另一个写法
from threading import Thread

class MyThread(Thread):#创建子类，继承Thread方法
    def run(self):#当线程可执行时，执行的就是run
        for i in range(10):
            print('子线程',i)

if __name__=='__main__':
    t=MyThread()
    # t.run()是错误的，这是方法调用，仍然是单线程
    t.start()
    for i in range(10):
        print('主线程',i)
```


```python
#传参
from threading import Thread

def func(name):
    for i in range(10):
        print(name,i)

if __name__=='__main__':
    t1=Thread(target=func,args=('子线程1',))#参数必须是元组,跟逗号
    t1.start()   

    t2=Thread(target=func,args=('子线程2',)) 
    t2.start()   

    for i in range(10):
        print('main',i)
```

## 多进程


```python
from multiprocessing import Process

def func():
    for i in range(10):
        print('子进程',i)

if __name__=='__main__':
    p=Process(target=func)   
    p.start()   
    for i in range(10):
        print('主进程',i)
```

## 线程池


```python
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor 
# 导入线程池和进程池
def fn(name):
    for i in range(10):
        print(i,name)

if __name__ == '__main__':
    with ThreadPoolExecutor(50) as t:
        #创建一个50个线程的线程池
        for i in range(10):
            t.submit(fn,name=f'线程{i}')#每个线程执行10次
    # 等待线程池所有线程结束
    print('over')


```

## 协程


```python
# 协程（Coroutine）是一种程序组件，用于在单个线程内进行多任务调度。与线程相比，协程提供了更轻量级的并发单元，因为它们不需要操作系统进行上下文切换，而是由程序自身控制任务的切换

# 协程通过显式的暂停（yield）和恢复（resume）操作来切换执行流程，这种切换是协作式的，也就是说，一个协程必须显式地让出控制权，其他协程才能运行

# 协程经常用于执行非阻塞I/O操作，可以在等待I/O操作完成时让出控制权，从而提高资源的利用率

# 协程比线程更加轻量级，因为它们共享同一线程的堆栈空间，并且协程的切换不需要涉及用户态与内核态之间的切换

# 协程使得异步编程更加直观和易于理解，它们允许使用顺序编程的方式来编写异步代码
```


```python
# Python 3.5+ 引入了 async 和 await 关键字，用于定义和使用协程。通过 asyncio 库，Python 支持协程的调度和事件循环。

# 格式
# import asyncio
# async def coroutine_example():#异步协程函数，执行得到的是一个协程对象
#     # 异步操作
#     await some_async_function()
    
# # 运行协程
# asyncio.run(coroutine_example())
```


```python
import asyncio
import time

async def func1():# 协程异步函数
    print('hello Amy')
    # time.sleep(3) 这是同步操作，会使异步中断
    await asyncio.sleep(3)# 挂起
    print('Amy')

async def func2():
    print('hello Mark')
    await asyncio.sleep(4)
    print('Mark')

async def func3():
    print('hello Peter')
    await asyncio.sleep(2)
    print('Peter')

async def main():
    # 创建任务列表
    tasks = [
        asyncio.create_task(func1()),
        asyncio.create_task(func2()),
        asyncio.create_task(func3())
    ]
    # 等待所有任务完成
    await asyncio.wait(tasks)

if __name__ == '__main__':
    asyncio.run(main())
```

### aiohttp


```python
# pip install aiohttp
# 基本框架

import asyncio,aiohttp

urls=[

]

async def download(url):
    # s=aiohttp.ClientSession()# 等价于request，不过是异步操作
    # s.get()
    # s.post()
    async with aiohttp.ClientSession as session:
        # session.close() with会自动关闭
        async with session.get(url) as res:
            # res.content.read() #等价于res.content
            # res.text() #等价于res.text
            # res.json()
            with open(url,mode='wb') as f:
                f.write(await res.content.read()) #异步读取内容，await挂起
    print(url,'ok')
    

async def main():
    tasks=[]
    for url in urls:
        task=asyncio.create_task(download(url))
        tasks.append(task)

if __name__=='__main__':
    asyncio.run(main())
```
