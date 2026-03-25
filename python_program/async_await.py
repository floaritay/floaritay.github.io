# Python 3.4 引入了 asyncio 模块，增加了异步编程，跟 JavaScript 的async/await 极为类似，大大方便了异步任务的处理。
# 为什么要异步？因为很多处理是需要大量时间，如果一直等待，则可能导致界面卡死等问题。
# 异步的基本思想是处理自己去做，等做完了再来通知我。而异步编程通常比较复杂，可能导致回调地狱（callback hell）的问题（回调函数嵌套在其他回调函数中，导致代码难以阅读和维护）
# 但python为了简单，将异步改为了同步呈现，这就是 async/await 的作用。

# async 关键字用来定义一个协程函数，协程函数是一种可以暂停和恢复执行的特殊函数，它可以在遇到耗时的操作时让出控制权，让其他协程或代码继续运行。
# await 关键字用来暂停一个协程函数的执行，并等待一个可等待对象（如另一个协程函数）完成后返回结果。await 关键字只能在 async 定义的协程函数中使用。

import asyncio
async def hello_world():
  print("hello")
  await asyncio.sleep(1) # 暂停 1 秒
  print("world")
asyncio.run(hello_world()) # 运行协程函数

# 调用协程函数会返回一个协程对象，但是这并不会立即执行协程函数内部的代码，而是需要将协程对象交给一个事件循环来处理

# async/await 是一种让异步编程看起来像同步编程的语法糖。
# 它可以让我们用更简洁和直观的方式来处理异步操作，而不需要使用回调函数。
# 你可以把 await 理解为等待一个异步操作的完成，然后继续执行后面的代码。

import asyncio

async def task1():
  print('Task 1 started')
  await asyncio.sleep(3) # 模拟一个耗时3秒的异步操作
  print('Task 1 finished')

async def task2():
  print('Task 2 started')
  await asyncio.sleep(1) # 模拟一个耗时1秒的异步操作
  print('Task 2 finished')

async def main():
  await asyncio.gather(task1(), task2()) # 并发执行两个异步函数

asyncio.run(main()) # 启动事件循环

# 输出：
# Task 1 started
# Task 2 started
# Task 2 finished
# Task 1 finished
