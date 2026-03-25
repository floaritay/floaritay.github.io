import requests
from lxml import etree
import time

url='https://www.zbj.com/fw/?k=saas'
headers={
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 SLBrowser/9.0.5.12181 SLBChan/112 SLBVPV/64-bit',
    'Cookie':'你的Cookie'
}
res=requests.get(url,headers=headers)
# print(res.text)

html=etree.HTML(res.text)#加载html源码
divs=html.xpath('/html/body/div[2]/div/div/div[3]/div[1]/div[4]/div/div[2]/div/div[2]/div')
for div in divs:#每一个服务商
    price=div.xpath('./div/div[3]/div[1]/span/text()')[0]#从列表里拿出来
    # print(price)
    title='saas'.join(div.xpath('./div/div[3]/div[2]/a/span/text()'))
    # print(title)
    # location=div.xpath('./div/div[4]/div/span[2]/text()')
    # print(location)
    company=div.xpath('./div/div[5]/div/div/div/text()')[0]
    print(company)
   
    
    time.sleep(1)
    # break
res.close()