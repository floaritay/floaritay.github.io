# 编写一个程序，输入一个目录路径，列出该目录下的所有文件和子目录

from pathlib import Path

def list_directory_contents(directory_path):
    # 将输入的目录路径转换为Path对象
    directory = Path(directory_path)
    
    # 检查输入的是否是一个目录
    if not directory.is_dir():
        print(f"Error: {directory_path} is not a directory.")
        return
    
    # 遍历目录内容并打印
    for item in directory.iterdir():
        if item.is_dir():
            print(f"[D] {item}")
        elif item.is_file():
            print(f"[F] {item}")
        else:
            # 通常这里不会有其他类型的文件系统条目，但理论上可以处理符号链接等
            print(f"[?] {item}")

if __name__ == "__main__":
    ###定义
    # 判断当前运行的脚本是否是主程序。这里的 __name__ 是一个内置变量，当Python脚本被直接运行时，__name__ 的值会被设置为 "__main__"。
    # 而如果该脚本是被其他脚本导入（作为模块使用）的，则 __name__ 的值会被设置为该脚本的模块名。
    ###作用
    # 当导入一个模块时，模块中的所有顶级代码（不在任何函数或类定义中的代码）都会被执行。但是，有时候你可能不想在导入模块时执行某些代码，而只想在模块被直接运行时执行。
    # 只有当脚本作为主程序运行时才需要执行的代码放在这个判断块里。
    # 当该脚本当作模块导入时不执行该判断块内容
    
    directory_to_list = input("Enter the directory path to list: ")# 输入路径  
    list_directory_contents(directory_to_list) # 输出该目录下的所有文件和子目录