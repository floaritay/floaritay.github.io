import asyncio
import time

async def func1():
    print('hello Amy')
    await asyncio.sleep(3)
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
    t1 = time.time()
    # 等待所有任务完成
    await asyncio.wait(tasks)
    t2 = time.time()
    print(t2 - t1)

if __name__ == '__main__':
    asyncio.run(main())
