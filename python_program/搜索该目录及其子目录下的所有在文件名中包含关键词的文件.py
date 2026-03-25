# 编写一个程序，输入一个目录路径和一个关键词，搜索该目录及其子目录下的所有在文件名中包含关键词的文件，并将文件路径输出

from pathlib import Path

def search_files_with_filename_keyword(directory, keyword):
    # 将输入的目录路径转换为Path对象
    directory = Path(directory)
    
    # 检查输入的是否是一个目录
    if not directory.is_dir():
        print(f"Error: {directory} is not a directory.")
        return
    
    # 递归地遍历目录及其子目录中的文件
    for file_path in directory.rglob('*'):
        if file_path.is_file():  # 确保是一个文件
            # 检查文件名中是否包含关键词
            if keyword.lower() in file_path.name.lower():
                print(f"[F] {file_path}")

if __name__ == "__main__":
    # 输入路径
    directory_input = input("请输入要搜索的目录路径: ")#
    
    # 输入关键词
    keyword_input = input("请输入要搜索的文件名关键词: ")#quest
    
    # 调用函数并传递参数
    search_files_with_filename_keyword(directory_input, keyword_input)  # 输出文件名中包含关键词的文件路径




   
 
    
 

