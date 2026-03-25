import requests

que=input('你想搜索人物：')
url=f'https://www.baidu.com/s?wd={que}'#地址栏里的链接全都是GET方式提交

headers={
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 SLBrowser/9.0.5.12181 SLBChan/112 SLBVPV/64-bit'
}#一个User-Agent的反爬处理
res=requests.get(url,headers=headers)
print(res)#<Response [200]>
print(res.text)#源代码  
res.close()