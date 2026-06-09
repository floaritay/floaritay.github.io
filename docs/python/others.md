# 目录


---
# pass


```python
# 语句占位符，什么也不做
def fun1():
  pass
```

# assert


```python
# assert是一种用于调试代码的工具，它可以让你测试你的代码中的某些条件是否为真，如果不为真，就会抛出一个AssertionError异常。
# 你可以使用assert来检查你的代码中的一些假设是否成立，或者在编写测试用例时使用assert来验证结果是否符合预期。

def gcd(a, b):#计算最大公约数
  # 如果a或b不是整数，抛出TypeError异常
  if not isinstance(a, int) or not isinstance(b, int):
    raise TypeError('a and b must be integers')
  # 如果a或b是负数，抛出ValueError异常
  if a < 0 or b < 0:
    raise ValueError('a and b must be non-negative')
  # 使用辗转相除法计算最大公约数
  while b != 0:
    a, b = b, a % b
  return a


# 测试gcd函数
# 断言gcd(12, 8)等于4
assert gcd(12, 8) == 4
# 断言gcd(0, 5)等于5
assert gcd(0, 5) == 5
# 断言gcd(1.5, 3)抛出TypeError异常
try:
    gcd(1.5, 3)
except TypeError as e:
    assert str(e) == 'a and b must be integers'
else:
    assert False, "Expected TypeError not raised"
# 断言gcd(-2, 4)抛出ValueError异常
try:
    gcd(-2, 4)
except ValueError as e:
    assert str(e) == 'a and b must be non-negative'
else:
    assert False, "Expected ValueError not raised"
```

# global


```python
# 在一个模块中使用 `global` 关键字来创建一个全局变量，然后在其他模块中进行访问和修改。
import module
print(module.glb['debug'])  # 输出 False
module.glb['debug'] = True
print(module.glb['debug'])  # 输出 True

# - 这里说的global关键字与变量作用域中的global关键字不是同一个含义和作用
# - 上述代码中的glb即便不声明为global，这段代码也能访问到，但如果修改了glb，在其他文件再引用glb，是无法获得修改后的值的

```

# yield


```python
# 用来创建生成器函数。生成器函数是一种特殊的函数，它可以返回一个惰性迭代器
# 惰性迭代器是一种可以像列表一样循环遍历的对象，但是不像列表，惰性迭代器不会把它的内容存储在内存中
#  yield 的作用是让函数暂停执行，并返回一个值给调用者
# 当再次调用函数时，它会从上次暂停的地方继续执行，直到遇到下一个 yield 或者结束

def generator_function():
  yield 1
  yield 2
gen=generator_function()
for value in gen:
  print(value)

# 定义一个生成器函数，用来读取文件的每一行
def read_file(filename):
  with open(filename) as f:
    for line in f:
      yield line # 返回一行内容并暂停


```


```python
# yield 有一些配套使用的关键字

# next() 函数，它可以用来获取生成器函数的下一个返回值。
# 每次调用 next() 函数时，生成器函数都会从上次暂停的地方继续执行，直到遇到下一个 yield 语句或者结束。
def generator_function():
  yield 1
  yield 2
gen=generator_function()
print(next(gen))
print(next(gen))

# send() 方法，它可以用来向生成器函数发送一个值，并获取下一个返回值。
# send() 方法的参数是要发送的值，它会赋给 yield 表达式的结果。
# send() 方法的返回值是下一个 yield 表达式的值。
def fun_generator():
  x = yield "Hello" # x 接收 send() 方法发送的值
  y = yield x + "World" # y 接收 send() 方法发送的值
  yield y + "!"
gen = fun_generator() 
print(next(gen)) # Hello
print(gen.send("Hi ")) # Hi World
print(gen.send("Bye ")) # Bye !

# throw() 方法，它可以用来向生成器函数抛出一个异常，并获取下一个返回值。
# throw() 方法的参数是要抛出的异常类型和可选的异常信息。
# throw() 方法的返回值是下一个 yield 表达式的值。如果生成器函数没有处理异常，则 throw() 方法会抛出异常
def fun_generator():
  try:
    x = yield "Hello" # x 接收 send() 方法发送的值
    y = yield x + "World" # y 接收 send() 方法发送的值
    yield y + "!"
  except ValueError: # 处理 ValueError 异常
    yield "Error"

gen = fun_generator() 
print(next(gen)) # Hello
print(gen.send("Hi ")) # Hi World
print(gen.throw(ValueError, "Invalid value")) # Error

```

# async/await


```python
# 见async/await.py
```

# 装饰器（decorator）


```python
# 允许你在不修改原有函数或方法定义的情况下，给函数或方法添加额外的功能。装饰器本质上是一个函数，它接收一个函数作为参数，并返回一个新的函数或可调用对象。
# 使用@符号来进行注解
#  应用场景：
# •  给函数添加日志、缓存、权限检查、性能测试等功能
# •  给类添加属性、方法、元类等功能
# •  实现一些设计模式，例如单例模式、观察者模式、代理模式等

import datetime
def print_time(func):
    def wrapper():
        # 打印当前时间
        print(datetime.datetime.now())
        # 调用原始函数，并获取其返回值（即使它是None）
        result = func()
        # 返回原始函数的调用结果
        return result
    # 返回内部函数作为装饰后的函数
    return wrapper
@print_time
def print_info():
    print("This is a simple function")
# 调用print_info()函数时，会先打印当前时间，再打印信息
print_info()


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper
@my_decorator
def greet(name):
    print(f"Hello, {name}!")
greet("Alice")
```


```python
class MyClassDecorator:
    def __init__(self, cls):
        self.cls = cls

    def __call__(self, *args, **kwargs):
        instance = self.cls(*args, **kwargs)
        print("Something is happening before the class instance is created.")
        # 可以在这里对实例进行额外的初始化或修改
        return instance

@MyClassDecorator
class MyClass:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, {self.name}!")

obj = MyClass("Alice")
obj.say_hello()
```

# 调用带命令行的程序


```python
# 如果你想在Python脚本b.py中调用另一个脚本a.py，并且向a.py传递命令行参数，你可以使用subprocess模块来完成这个任务。
# 假设你有一个a.py脚本，它使用argparse来解析命令行参数：

# a.py
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="Input file")
    parser.add_argument("--output", help="Output file")
    args = parser.parse_args()
    
    if args.input and args.output:
        # Do something with input and output files
        print(f"Input: {args.input}, Output: {args.output}")
    else:
        print("Missing input or output arguments.")

if __name__ == "__main__":
    main()


# b.py
import subprocess

def main():
    input_file = "input.txt"  # 设置输入文件路径
    output_file = "output.txt"  # 设置输出文件路径

    # 使用subprocess调用a.py并传递参数
    cmd = ["python", "a.py", "--input", input_file, "--output", output_file]
    
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
    else:
        print("a.py executed successfully.")

if __name__ == "__main__":
    main()
# 在这个示例中，b.py使用subprocess.run()来执行a.py，并传递了--input和--output参数。你可以在b.py中设置input_file和output_file的值，以便传递不同的文件路径。
# 运行b.py将执行a.py并传递参数，从而实现调用带有命令行参数的a.py的目标。确保在执行b.py之前，a.py位于同一目录中或在Python的模块搜索路径中。
```

# signal


```python
# signal 模块用于处理信号
# 在Python中，signal 模块允许你注册信号处理程序（信号处理函数），以便在接收到特定信号时执行自定义操作。以下是关于signal模块的一些重要知识点：

# 1. 信号的基本概念：
#     - 信号是由操作系统发出的一种异步通知，通常用于通知进程某些事件的发生，如Ctrl+C产生的中断信号（SIGINT）。
#     - 信号可以用于进程间通信（IPC），如向进程发送自定义信号以触发特定操作。
# 2. 信号常见类型：
#     - 一些常见的信号类型包括：
#         - SIGINT：中断信号，通常由Ctrl+C发送，用于终止进程。
#         - SIGTERM：终止信号，用于请求进程正常终止。
#         - SIGKILL：强制终止信号，用于强制终止进程。
#         - SIGHUP：挂起信号，通常用于通知进程重新加载配置文件。
# 3. signal模块函数：
#     - signal.signal(signum, handler)：注册信号处理程序。signum是信号的编号，handler是信号处理函数，通常是一个Python函数，当指定的信号发生时，该函数将被调用。
#     - signal.getsignal(signum)：获取指定信号的当前处理程序。
#     - signal.signal(signal.SIG_IGN, handler)：忽略指定信号，将信号处理程序设置为忽略。
# 4. 信号处理程序：
#     - 信号处理程序是用户定义的Python函数，用于在接收到特定信号时执行自定义操作。
#     - 信号处理程序接受两个参数：signum（信号编号）和frame（表示信号的堆栈帧信息）。
# 5. 注意事项：
#     - 在信号处理程序中应该尽量避免执行耗时的操作，因为信号处理是异步的，它们可能在任何时刻中断正在执行的代码。
#     - 一些信号不能被捕获、忽略或修改，例如SIGKILL。

import signal
import sys

# 信号处理函数
def signal_handler(signum, frame):
    if signum == signal.SIGINT:
        print("Received Ctrl+C. Exiting...")
        sys.exit(0)
    elif signum == signal.SIGTERM:
        print("Received SIGTERM signal.")
        # 可以执行处理SIGTERM的操作

# 注册信号处理程序
signal.signal(signal.SIGINT, signal_handler)  # 处理Ctrl+C信号
signal.signal(signal.SIGTERM, signal_handler)  # 处理SIGTERM信号

# 运行程序
print("Running...")
while True:
    pass
```

# 导入其他路径包和模块


```python
# 1. 相对导入：相对导入是一种更好的方式，它允许你相对于当前脚本的位置来导入模块

# from .. import module_to_import
# 请注意，相对导入只在包内部的模块中有效，你需要将脚本放在一个包（包含一个__init__.py文件的目录）中。


# 2. 使用 sys.path.append：

# import sys
# sys.path.append('..')  # 将上层目录添加到模块搜索路径
# import module_to_import  # 导入上层目录的模块


# 3. 使用sys.path.insert：与将上层目录添加到sys.path相似，你可以使用sys.path.insert来将上层目录添加到模块搜索路径的特定位置。
# 这种方法与添加到末尾不同，它可以让你控制模块搜索路径中的位置：

# import sys
# sys.path.insert(0, '..')  # 将上层目录添加到模块搜索路径的开头
# import module_to_import




# 最佳实践是将相关的模块放置在合适的位置，以便Python可以自动找到它们，而不需要修改模块搜索路径。
# 对于 sys.path 中的路径，不需要在其路径下包含 __init__.py 文件。sys.path 中的路径用于搜索 Python 模块，而不是包。
# 如果在 sys.path 中插入了多个路径，并且其中多个路径下都包含了同名的模块，那么在导入模块时可能会发生混淆。
# 还有一个问题要注意，比如目录是：dir1/dir2/dir1，两个dir1的情况下，就极有可能冲突。
# 还有注意，比如 dir1/dir2/a.py，你要导入 from dir2.a import xxx，则dir1需要明确的在sys.path中，dir1/dir2在sys.path中是不行的。
```
