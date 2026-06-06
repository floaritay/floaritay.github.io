# 介绍


```python
# Tkinter是Python的标准GUI（Graphic User Interface）库，它提供了一组工具和组件，用于创建图形用户界面应用程序。
# Tkinter基于Tk GUI工具包，并提供了一种相对容易的方式来构建GUI应用程序。
# Tkinter应用程序通常包括一个主循环，它负责监听用户的事件，例如鼠标点击、键盘输入等，以及更新GUI界面。
# 主循环使用 mainloop() 方法启动，它会一直运行，直到用户关闭应用程序窗口。
```

# 布局容器


```python
# Tkinter提供了多种布局容器，这些容器用于组织和排列UI组件以创建更复杂的GUI布局。

# 1. Frame（框架）:
#     - Frame是Tkinter中最常用的容器，它用于分组和组织其他UI组件。你可以将其他组件放置在Frame内，以便将它们作为一个整体进行管理。

# 2. LabelFrame（标签框架）:
#     - LabelFrame是一种具有标题的容器，通常用于分组相关的控件。它可以包含其他控件，并显示一个标题标签以说明组内的内容。

# 3. PanedWindow（分割窗口）:
#     - PanedWindow允许你创建可拖动的分割窗格，以便用户可以调整窗格的大小。这对于分割视图或区域非常有用。

# 4. Toplevel（顶层窗口）:
#     - Toplevel是一个独立的顶层窗口，它不依赖于主应用程序窗口。它可以用于创建弹出式窗口、对话框或新的应用程序窗口。

# 5. Canvas（画布）:
#     - Canvas是一个可绘制图形的容器，用于创建图表、图形和绘图应用程序。你可以在画布上绘制线条、形状、文本等。

# 6. ScrolledText（滚动文本）:
#     - ScrolledText是一个带有滚动条的多行文本框，用于显示和编辑大段文本。它自动添加滚动条，以便用户可以浏览文本。

# 7. Notebook（标签页容器）:
#     - Notebook是一个选项卡式容器，TabControl，用于创建多个标签页，每个标签页可以包含不同的内容。这通常用于创建选项卡界面，例如浏览器的标签页。
```

## pack布局


```python
# pack()方法是Tkinter中用于布局管理的一个重要工具，它允许你在容器中排列和放置控件

# 1.  side （放置方向）：
#     - 用法： side  参数用于指定控件相对于容器的哪一边进行排列。
#     - 可选值： "top" （默认值）， "bottom" ， "left" ， "right" 。
#     - 示例： side="top" 表示将控件放置在容器的顶部，而 side="left" 表示将控件放置在容器的左侧。

# 2.  anchor （锚，对齐方式）：
#     - 用法： anchor  参数用于指定控件在其分配的空间内的对齐方式。
#     - 可选值： "n" （北，上边对齐）， "s" （南，下边对齐）， "e" （东，右边对齐）， "w" （西，左边对齐）， "center" （中心对齐）。
#     - 示例： anchor="n" 表示控件在其分配的空间内的上边对齐， anchor="center" 表示控件居中对齐。

# 3.  fill （填充）：
#     - 用法： fill  参数用于指定控件是否应填充分配给它的空间。
#     - 可选值： "none" （默认值，不填充）， "x" （水平方向填充）， "y" （垂直方向填充）， "both" （水平和垂直方向填充）。
#     - 示例： fill="x" 表示控件在水平方向上填充分配给它的空间。

# 4.  expand （扩展）：
#     - 用法： expand  参数用于指定是否允许控件扩展以占用额外的可用空间。
#     - 可选值： True  或  False 。
#     - 示例： expand=True 表示允许控件占用额外的可用空间。
#     -  fill  控制控件是否填充分配的空间，指定填充的方向。
#     -  expand  控制控件是否占用额外的可用空间，允许控件在可用空间增加时扩展。

# 5.  padx  和  pady （外边距）：
#     - 用法： padx  和  pady  参数分别用于指定控件的水平和垂直外边距。
#     - 示例： padx=10  表示在控件周围设置水平外边距为10像素。

# 6.  ipadx  和  ipady （内边距）：
#     - 用法： ipadx  和  ipady  参数分别用于指定控件的水平和垂直内边距。
#     - 示例： ipady=5  表示在控件内部设置垂直内边距为5像素。

# 7.  before  和  after （控件相对位置）：
#     - 用法： before  和  after  参数用于指定控件的相对位置，以确定其排列顺序。
#     - 示例： before=other_widget  表示在指定的  other_widget  控件之前排列当前控件。
```


```python
import tkinter as tk

app = tk.Tk()
app.title("Pack Example")

# 创建按钮控件
button1 = tk.Button(app, text="Button 1")
button2 = tk.Button(app, text="Button 2")
button3 = tk.Button(app, text="Button 3")

# 使用不同参数进行布局和排列
button1.pack(side="top", fill="x", padx=10, pady=5)
button2.pack(side="left", fill="y", padx=5, pady=10)
button3.pack(side="right", fill="both", padx=20, pady=15, expand=True)

app.mainloop()
```

## grid布局


```python
# 1. 水平布局：要实现水平布局，你可以使用 Frame 容器和 grid() 布局管理器。设置元素的 row 值相同，而 column 值递增，以便它们在同一行水平排列。


import tkinter as tk

app = tk.Tk()
frame = tk.Frame(app)
frame.grid(row=0, column=0)

label1 = tk.Label(frame, text="Label 1")
label2 = tk.Label(frame, text="Label 2")

label1.grid(row=0, column=0)
label2.grid(row=0, column=1)

app.mainloop()
```


```python
# 2. 垂直布局：要实现垂直布局，你可以设置元素的 column 值相同，而 row 值递增，以便它们在同一列垂直排列。


import tkinter as tk

app = tk.Tk()#创建程序
frame = tk.Frame(app)# 创建一个Frame
frame.grid(row=0, column=0)

label1 = tk.Label(frame, text="Label 1")#创建一个标签类型的控件
label2 = tk.Label(frame, text="Label 2")

label1.grid(row=0, column=0)#对标签进行grid布局
label2.grid(row=1, column=0)

app.mainloop()

```


```python
# 3. 自动填充容器：你可以使用 grid() 布局管理器来让元素自动填充容器，使其占据所有可用空间。
# 使用 rowconfigure 和 columnconfigure 方法来设置行和列的权重，以实现自动填充效果。


import tkinter as tk

app = tk.Tk()
frame = tk.Frame(app)# 创建一个Frame
frame.pack(fill="both", padx=15, pady=15, expand=True)# 先让frame占满APP界面全部空间

# 创建一个标签并使用grid布局，使其自动填充容器
label = tk.Button(frame, text="充满行高")
label.grid(row=0, column=0, sticky="nsew")

labe2 = tk.Button(frame, text="充满行高+列宽")
labe2.grid(row=0, column=1, sticky="nsew")

# 设置行和列的权重，使元素填充容器
frame.rowconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)

app.mainloop()


# 在上述示例中，sticky 参数设置为 "nsew" ，表示元素应该在上、下、左、右方向上填充容器。通过设置行和列的权重为1，元素将自动填充容器的可用空间。

# sticky 是Tkinter中用于控制组件在其分配的空间内对齐方式的参数。它通常与 grid() 布局管理器一起使用，以确保组件在其分配的网格单元内正确对齐。具体作用如下：
# 1. 对齐方式：sticky 参数决定了组件在其分配的网格单元内的对齐方式。你可以使用 sticky 来指定组件相对于网格单元的哪个边缘进行对齐。
# 2. 多方向对齐：sticky 可以同时指定多个方向，例如 "nsew" 表示组件在所有四个边缘上都对齐，使组件填充整个网格单元。
# 3. 灵活布局： ticky 使你能够创建更灵活的布局，确保组件在其分配的网格单元内精确对齐，无论网格单元的大小如何。

# 具体取值为：
# -  "n" ：北（上边）对齐。
# -  "s" ：南（下边）对齐。
# -  "e" ：东（右边）对齐。
# -  "w" ：西（左边）对齐。
# -  "center" ：中心对齐。

# 通过组合这些取值，你可以实现各种不同的对齐方式。例如， "nsew" 表示组件在其分配的网格单元内四个边缘上都对齐，从而填充整个单元。
#   sticky="n"  表示组件在上边对齐，  sticky="s"  表示组件在下边对齐，以此类推。
```

## place布局


```python
# Tkinter支持绝对定位，但它通常不被推荐使用，因为它会导致界面不适应不同屏幕尺寸和分辨率。
# 你可以使用place()方法来实现绝对定位，但要小心确保你的应用程序只在固定分辨率的情况下使用时才使用它。

import tkinter as tk

app = tk.Tk()
frame = tk.Frame(app, width=200, height=100)
frame.place(x=50, y=50)  # 设置左上角坐标

label1 = tk.Label(frame, text="Label 1")
label1.place(x=10, y=10)  # 在容器内设置元素的坐标

app.mainloop()
```

## 布局示例


```python
# 这是app界面        



        #框架的左上角坐标 x=50, y=50
        #------------------------------->X (width=250)    #在app中创建一个 Frame框架，参数 width=200, height=100
        #|   
        #|  # (x=60, y=60) 元素的坐标  x=10, y=10
        #|
        #|                                     
        #|
        #|
        #|
        #y (height=150)
```

# 常见元素


```python
# 以下是一些Tkinter中常见的GUI元素以及它们的说明：

# 1. Label（标签）：
#     - 用途：用于在界面上显示文本或标签。
#     - 示例代码：label = tk.Label(app, text="Hello, World!")

# 2. Button（按钮）：
#     - 用途：用于创建可点击的按钮，通常用于触发操作。
#     - 示例代码：button = tk.Button(app, text="Click me", command=callback_function)

# 3. Entry（输入框）：
#     - 用途：用于允许用户输入文本。
#     - 示例代码：entry = tk.Entry(app)

# 4. Text（文本框）：
#     - 用途：用于多行文本的输入和显示。
#     - 示例代码：text = tk.Text(app)

# 5. Frame（框架）：
#     - 用途：用于组织和包含其他GUI元素，常用于创建布局结构。
#     - 示例代码：frame = tk.Frame(app)

# 6. Canvas（画布）：
#     - 用途：用于绘制图形、图像和自定义绘图。
#     - 示例代码：canvas = tk.Canvas(app)

# 7. Checkbutton（复选框）：
#     - 用途：用于允许用户选择一个或多个选项。
#     - 示例代码：checkbutton = tk.Checkbutton(app, text="Check me")

# 8. Radiobutton（单选按钮）：
#     - 用途：用于在一组互斥选项中选择一个。
#     - 示例代码：radiobutton = tk.Radiobutton(app, text="Option 1", value=1, variable=selected_option)

# 9. Listbox（列表框）：
#     - 用途：用于显示列表或选项，用户可以从中选择。
#     - 示例代码：listbox = tk.Listbox(app)

# 10. Menu（菜单）：
#     - 用途：用于创建菜单栏和弹出菜单。
#     - 示例代码：menu = tk.Menu(app)

# 11. Scrollbar（滚动条）：
#     - 用途：用于支持滚动视图，通常与其他可滚动的元素一起使用。
#     - 示例代码：scrollbar = tk.Scrollbar(app)

# 12. Scale（滑块）：
#     - 用途：用于选择一个值，通常用于调整参数。
#     - 示例代码：scale = tk.Scale(app, from_=0, to=100, orient="horizontal")

# 13. LabelFrame（标签框架）：
#     - 用途：用于创建带有标题的框架，用于分组相关元素。
#     - 示例代码：labelframe = tk.LabelFrame(app, text="Group")

# 14. Toplevel（顶级窗口）：
#     - 用途：用于创建新的独立窗口。
#     - 示例代码：top_window = tk.Toplevel(app)

# 15. MessageBox（消息框）：
#     - 用途：用于显示提示、警告和错误消息给用户。
#     - 示例代码：tk.messagebox.showinfo("Info", "This is an information message.")

# 这些是Tkinter中常见的GUI元素，它们用于构建各种类型的图形用户界面，包括按钮、文本框、复选框、菜单等，以满足不同的应用程序需求。
```


```python
import tkinter as tk
app = tk.Tk()

label1 = tk.Label(app, text="Label 1")
label1.pack()

btn1 = tk.Button(app, text="Button 1")
btn1.pack()

txt1 = tk.Entry(app)
txt1.pack()

checkbutton1 = tk.Checkbutton(app, text="Check me")
checkbutton1.pack()

selected_option=tk.IntVar(value=1)
radiobutton1 = tk.Radiobutton(app, text="Option 1", value=1, variable=selected_option)
radiobutton2 = tk.Radiobutton(app, text="Option 2", value=2, variable=selected_option)
radiobutton1.pack()
radiobutton2.pack()

labelframe1 = tk.LabelFrame(app, text="Group 1")
txt2 = tk.Entry(labelframe1)
txt2.pack()
txt3 = tk.Entry(labelframe1)
txt3.pack()
labelframe1.pack()

lst1 = tk.Listbox(app)
lst1.pack()
items=['apple','banana','cherry']
for item in items:
    lst1.insert(tk.END,item)

app.mainloop()
```

# 边框


```python
# 要在Tkinter中的元素或容器上显示边框，你可以使用relief和borderwidth属性来配置

# 1. 使用 relief 属性： relief 属性用于指定元素或容器的边框风格。它可以设置为以下值之一：
#     -  "flat" ：没有边框（默认值）。
#     -  "sunken" ：下沉式边框，表示元素或容器的内容处于边框之下。
#     -  "raised" ：凸出式边框，表示元素或容器的内容凸出在边框之上。
#     -  "ridge" ：槽式边框，类似于  "sunken" ，但带有更强的立体感。
#     -  "solid" ：实线边框。

#     例如，你可以使用以下代码为一个Frame添加一个凸出式边框：


import tkinter as tk

app = tk.Tk()

frame = tk.Frame(app, relief="raised", borderwidth=2)
frame.pack()

label = tk.Label(frame, text="This is a frame with a border")
label.pack()

app.mainloop()

```


```python

# 2. 使用 borderwidth 属性： borderwidth 属性用于指定边框的宽度（以像素为单位）。你可以通过设置这个属性来控制边框的厚度。


import tkinter as tk

app = tk.Tk()

label = tk.Label(app, text="This is a label with a thick border")
label.config(borderwidth=3, relief="solid")
label.pack()

app.mainloop()


# 在这个示例中， borderwidth 设置为3， relief 设置为 "solid" ，从而创建了一个有3像素宽的实线边框的标签。
```

# 菜单


```python
import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        print(f"打开的文件路径为：{file_path}")

def save_file():
    file_path = filedialog.asksaveasfilename()
    if file_path:
        print(f"保存的文件路径为：{file_path}")

def copy_text():
    print("执行复制操作")

def paste_text():
    print("执行粘贴操作")

root = tk.Tk()
# 创建菜单栏
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# 创建文件菜单
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="文件", menu=file_menu)
file_menu.add_command(label="打开文件", command=open_file)
file_menu.add_command(label="保存文件", command=save_file)

# 创建编辑菜单
# 当tearoff=True时（这是默认值），菜单可以被 “撕下”，即用户可以将菜单从菜单栏中拖出成为一个独立的窗口。
# 这个独立的窗口可以在屏幕上任意移动，方便用户在进行一些操作时不受菜单栏位置的限制。
edit_menu = tk.Menu(menu_bar, tearoff=1)
menu_bar.add_cascade(label="编辑", menu=edit_menu)
edit_menu.add_command(label="复制", command=copy_text)
edit_menu.add_command(label="粘贴", command=paste_text)

root.mainloop()
```

# 事件绑定

## 常见与使用方法 


```python
# 以下是一些常见的Tkinter事件以及它们的使用方法：

# 1. Button Click（按钮点击事件）：
#     - 事件名称： <Button-1> （鼠标左键点击）
#     - 使用方法：你可以绑定按钮的点击事件，当用户单击按钮时触发相应的函数。

# button = tk.Button(app, text="Click me")
# button.bind("<Button-1>", click_handler)



# 2. KeyPress（键盘按键事件）：
#     - 事件名称： <Key> ，通常跟随具体的按键（例如， <KeyPress-a> 表示按下键盘上的字母"A"）。
#     - 使用方法：你可以绑定键盘按键事件，以便在按下特定键时触发相应的函数。

# app.bind("<KeyPress-a>", key_a_handler)



# 3. Mouse Hover (Enter/Leave)（鼠标悬停事件）：
#     - 事件名称： <Enter> （鼠标进入元素区域）、 <Leave> （鼠标离开元素区域）。
#     - 使用方法：你可以绑定这些事件，以在鼠标进入或离开元素时触发相应的函数。

# button.bind("<Enter>", mouse_enter_handler)
# button.bind("<Leave>", mouse_leave_handler)



# 4. Mouse Double Click（鼠标双击事件）：
#     - 事件名称： <Double-1> （鼠标左键双击）。
#     - 使用方法：你可以绑定双击事件，以在用户双击鼠标左键时触发相应的函数。

# button.bind("<Double-1>", double_click_handler)



# 5. Focus In/Out（焦点事件）：
#     - 事件名称： <FocusIn> （焦点进入元素）和  <FocusOut> （焦点离开元素）。
#     - 使用方法：你可以绑定这些事件，以在元素获得或失去焦点时触发相应的函数。

# entry.bind("<FocusIn>", focus_in_handler)
# entry.bind("<FocusOut>", focus_out_handler)



# 6. Window Close (Closing)（窗口关闭事件）：
#     - 事件名称： <Destroy> （窗口被关闭）。
#     - 使用方法：你可以绑定窗口的关闭事件，以在用户关闭窗口时触发相应的函数。

# app.bind("<Destroy>", window_close_handler)


# 这些是一些常见的Tkinter事件示例，你可以根据具体的应用需求绑定相应的事件和函数，以实现用户交互和响应。通过处理这些事件，可以GUI程序更加交互和功能丰富。
```

## 与command的区别


```python
# 在 Python 的 Tkinter 中， command 与事件既有联系又有区别。

# 联系：
# 两者都是用于响应用户操作以触发特定功能的机制。
# 无论是通过按钮的 command 属性指定的函数，还是通过绑定事件处理函数来响应的事件，最终目的都是在用户进行某些操作时执行特定的代码逻辑，以实现程序的交互功能。

# 区别：
# - 触发范围：
#     -  command ：通常主要用于特定小部件的特定触发动作，比如按钮被点击、菜单选项被选择等。触发较为局限，只针对与之关联的特定小部件的特定操作。
#     - 事件：可以响应各种不同类型的用户交互行为，触发范围更广。包括鼠标点击、按键按下、窗口大小改变等多种事件，涵盖了整个应用程序的交互场景。
# - 参数传递：
#     -  command ：一般情况下不能直接传递参数给关联的函数，通常需要通过其他方式（如使用 lambda 表达式或设置全局变量）来间接传递参数。
#     - 事件：事件处理函数会自动接收一个事件对象作为参数，这个事件对象包含了关于该事件的详细信息，比如鼠标的坐标、按下的键等。在处理事件时可以方便地获取到与事件相关的具体数据
# - 灵活性：
#     -  command ：相对较为简单直接，适合处理一些简单的、特定小部件的触发行为。
#     - 事件：由于可以绑定不同类型的事件，并且可以根据事件对象进行更复杂的处理，因此更加灵活。可以根据具体的需求对不同的事件进行不同的处理，实现更精细的交互控制。


```


```python
import tkinter as tk

def on_key_press(event):
    # 判断按下的键是否是回车键
    if event.keysym == 'Return':
        print(f"你在窗口中按下了回车键，输入的内容是：{entry.get()}")
    else:
        print(f"你按下了键：{event.char}")

def on_mouse_click(event):
    print(f"鼠标在 ({event.x}, {event.y}) 处被点击。")

root = tk.Tk()
entry = tk.Entry(root)
entry.pack()

# 绑定键盘按下事件到窗口
root.bind('<KeyPress>', on_key_press)
# 创建一个标签用于展示鼠标点击位置
label = tk.Label(root, text="")
label.pack()
# 绑定鼠标点击事件到标签
label.bind('<Button-1>', on_mouse_click)

root.mainloop()
```
