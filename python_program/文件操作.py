# 编写一个程序，复制文件,移动文件,删除文件

import os
import shutil
from pathlib import Path

file_path1=r""
file_path2=r""
file_path3=r""

def copy_file(file_path1,file_path2):
    shutil.copy2(file_path1,file_path2)
    print(f"File {file_path1} has been copied to {file_path2}.")

def move_file(file_path1,file_path2):
    shutil.move(file_path1,file_path2)
    print(f"File {file_path1} has been moved to {file_path2}.")#注意：移动后会删除源文件

def delete_file(file_path2):
    os.remove(file_path2)
    print(f"File {file_path2} has been deleted.")

#copy_file(file_path1,file_path2)
#move_file(file_path1,file_path3)
#delete_file()



   
 
    
 

