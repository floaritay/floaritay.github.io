def copy_file_contents(source_path, destination_path):
    try:
        # 打开源文件以读取模式
        with open(source_path, 'r', encoding='utf-8') as source_file:
            # 读取源文件的所有内容
            content = source_file.read()
        
        # 打开目标文件以写入模式（如果文件不存在，它将被创建）
        with open(destination_path, 'w', encoding='utf-8') as destination_file:
            # 将内容写入目标文件
            destination_file.write(content)
        
        print(f"文件内容已成功从 {source_path} 复制到 {destination_path}")
    
    except FileNotFoundError:
        print(f"错误：源文件 {source_path} 未找到。")
    
    except IOError as e:
        print(f"错误：在文件操作中发生了一个I/O错误。详情：{e}")
 
# 主程序
if __name__ == "__main__":
    # 从用户那里获取源文件和目标文件的路径
    source_path = input("请输入源文件路径(路径不要加引号)：")#
    destination_path = input("请输入目标文件路径：")#
    
    # 调用函数来复制文件内容
    copy_file_contents(source_path, destination_path)