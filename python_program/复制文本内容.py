# 编写一个程序，创建一个新的文本文件，并将一些文本内容写入其中。

from pathlib import Path

file_path1=r""
file_path2=r""
# 在Python字符串中，反斜杠（\）是一个特殊字符，用于引入转义序列，如\n（换行）、\t（制表符）等。
# 当你在字符串中使用反斜杠来表示文件路径时，Python可能会尝试解释这些反斜杠后面的字符为转义序列。
# 1.使用原始字符串：在字符串前加上r来告诉Python这是一个原始字符串，不应该解释其中的反斜杠为转义字符。
# 2.使用双反斜杠
# 3.使用正斜杠
with open (file_path1,'r') as file1:
    content=file1.read()
with open(file_path2,'w') as file2:
    file2.write(content)


   
 
    
 

