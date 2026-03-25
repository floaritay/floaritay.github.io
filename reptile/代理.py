import requests

url='https://www.baidu.com/index.htm'
headers={
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 SLBrowser/9.0.5.12181 SLBChan/112 SLBVPV/64-bit'
}
# res=requests.get(url,headers=headers)
# print(res.text)
#准备的代理 ：你的代理地址
proxies={
    # 'https':'https://代理'      #看你的网站是哪个
    'http':'http://' #百度不太一样，是http
}
res=requests.get(url,headers=headers,proxies=proxies)
print(res.text)
res.close()