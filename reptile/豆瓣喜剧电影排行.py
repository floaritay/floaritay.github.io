import requests

# url='https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=20'
# 问号后面是参数，前面是url
# url过长，后面的参数可以去掉
url='https://movie.douban.com/j/chart/top_list'

#参数封装
#payload
params={
    'type': '24',
    'interval_id': '100:90',
    'action': '',
    'start': 0,
    'limit': 20,
}

# res=requests.get(url=url,params=params)
# print(res.text)
# 没有内容，被反爬了，考虑以下情况
# 1.User-Agent
# print(res.request.headers)#查找程序默认的User-Agent
# {'User-Agent': 'python-requests/2.32.3', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 SLBrowser/9.0.5.12181 SLBChan/112 SLBVPV/64-bit'
}
res=requests.get(url=url,params=params,headers=headers)
print(res.json())
res.close #关闭，防止访问过多
