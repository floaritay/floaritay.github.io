# 编写一个程序，输入一个目录路径和文件扩展名，搜索该目录及其*子目录*下的所有指定扩展名的文件，并将文件路径输出。

from pathlib import Path

def search_files_with_extension(dir_path,extension):
    # 将输入的目录路径转换为Path对象
    directory = Path(dir_path)
    
    # 检查输入的是否是一个目录
    if not directory.is_dir():
        print(f"Error: {dir_path} is not a directory.")
        return
    
    # 遍历目录内容并打印
#    for item in directory.iterdir():   #函数目前只搜索了目录的直接子项，而没有递归地搜索子目录。为了搜索所有子目录，应该使用 rglob 而不是 iterdir。
    for item in directory.rglob(f"*{extension}"):  #rglob() 方法需要一个模式字符串来指定要搜索的文件或目录的名称模式。
        if item.is_file() and item.suffix==extension:
            print(f"[F] {item}")


if __name__ == "__main__":
    ###定义
    # 判断当前运行的脚本是否是主程序。这里的 __name__ 是一个内置变量，当Python脚本被直接运行时，__name__ 的值会被设置为 "__main__"。
    # 而如果该脚本是被其他脚本导入（作为模块使用）的，则 __name__ 的值会被设置为该脚本的模块名。
    ###作用
    # 当导入一个模块时，模块中的所有顶级代码（不在任何函数或类定义中的代码）都会被执行。但是，有时候你可能不想在导入模块时执行某些代码，而只想在模块被直接运行时执行。
    # 只有当脚本作为主程序运行时才需要执行的代码放在这个判断块里。
    # 当该脚本当作模块导入时不执行该判断块内容
    
    directory = input("请输入要搜索的目录路径: ")# 输入路径  
    ext=input("请输入要搜索的文件扩展名(包括点，例如 '.txt'): ")
    search_files_with_extension(directory,ext) # 输出该目录下的所有匹配文件





   
 
    
 

