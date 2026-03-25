# 编写一个程序，输入一个文件路径，输出文件的基本名称（文件名）和扩展名
from pathlib import Path


def file_exec(file_path):

    # 检查输入的源文件是否是一个文件
    if not file_path.is_file():
        print(f"Error: {file_path} is not a directory.")
        return
    #打印文件名
    file_name=file_path.name
    print(file_name)
    #打印文件扩展名
    file_suffix=file_path.suffix
    print(file_suffix)

if __name__ == "__main__":
    file = input("Enter the file path: ") # 输入文件路径
    file_exec(Path(file))### 将输入的文件路径转换为Path对象





   
 
    
 

