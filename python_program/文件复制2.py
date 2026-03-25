# 编写一个程序，输入两个文件路径，将第一个文件的内容复制到第二个文件中。
from pathlib import Path


def file_copy(file1_path,file2_path):
    # # 将输入的文件路径转换为Path对象(函数调用时转换成Path对象更简洁)
    # file1_path=Path(file1)
    # file2_path=Path(file2)

    # 检查输入的源文件是否是一个文件
    if not file1_path.is_file():
        print(f"Error: {file1_path} is not a directory.")
        return
   # 读取源文件内容
    try:
        content = file1_path.read_text(encoding='utf-8')  # 可以指定编码，默认是utf-8
    except UnicodeDecodeError:
        print(f"Error: Cannot decode {file1_path} as UTF-8 text.")
        return
    # 写入到目标文件
    try:
        file2_path.write_text(content, encoding='utf-8')  # 保持编码一致
    except Exception as e:
        print(f"Error: Failed to write to {file2_path}. Details: {e}")

if __name__ == "__main__":
    file1 = input("Enter the source file path: ") # 输入文件路径
    file2 = input("Enter the destination file path: ")
    file_copy(Path(file1),Path(file2))### 将输入的文件路径转换为Path对象





   
 
    
 

