import threading
import time

# 定义线程要执行的任务
def worker(thread_id):
    print(f"线程 {thread_id} 开始工作")
    time.sleep(2)  # 模拟一个耗时操作
    print(f"线程 {thread_id} 完成工作")

# 创建线程列表
threads = []

# 创建并启动多个线程
for i in range(5):
    thread = threading.Thread(target=worker, args=(i,))
    threads.append(thread)
    thread.start()

# 等待所有线程完成
for thread in threads:
    thread.join()#使用 join() 方法等待每个线程完成。这会阻塞主线程，直到所有子线程都执行完毕。

print("所有线程已完成")
