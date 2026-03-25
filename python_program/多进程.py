import multiprocessing
import os
import time

def worker(number):
    """这是一个工作进程函数,它将打印进程的PID和接收到的数字"""
    print(f'Worker: {number}, PID: {os.getpid()}')
    time.sleep(2)  # 模拟一些工作
    print(f'Worker {number} finished.')

if __name__ == '__main__':
    # 获取当前进程的PID
    print(f'Main process PID: {os.getpid()}')

    # 创建一个进程池
    processes = []

    # 创建并启动4个进程
    for i in range(4):
        p = multiprocessing.Process(target=worker, args=(i,))
        processes.append(p)
        p.start()

    # 等待所有进程完成
    for p in processes:
        p.join()

    print('All processes finished.')
