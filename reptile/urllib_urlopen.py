from urllib.request import urlopen


url='http://www.baidu.com'
res=urlopen(url)
# print(res.read().decode('utf-8'))

with open('baidu.html',mode='w',encoding='utf-8') as f:
    f.write(res.read().decode('utf-8'))
print('已保存源代码')

res.close






