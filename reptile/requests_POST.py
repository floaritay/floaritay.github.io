import requests

url='https://fanyi.baidu.com/sug'#network，sug中

s=input('请输入你要翻译的内容:')
data={
    'kw':s
}
#POST发送的数据必须放在字典，通过data参数传递
res=requests.post(url,data=data)
# print(res.text)
print(res.json())#将返回的内容处理为json，python里的字典
res.close()