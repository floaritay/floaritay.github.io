import requests
from bs4 import BeautifulSoup
import csv
f=open('菜价.csv',mode='w')
csvwriter=csv.writer(f)

url='http://www.xinfadi.com.cn/priceDetail.html'
res=requests.post(url)
res.close()

page=BeautifulSoup(res.text,'html.parser')#指定html解析器
table=page.find('table',class_='hq_table')#class时关键字，后面加下划线
table=page.find('table',attrs={'class':'hq_table'})#跟上一行一个意思
#进一步提取
trs=table.find_all('td')[1:]#切片
for tr in trs:
    tds=tr.find_all('td')
    name=tds[0].text#拿到被标记的内容
    low=tds[1].text
    avg=tds[2].text
    high=tds[3].text
    gui=tds[4].text
    kind=tds[5].text
    date=tds[6].text
    # print(name,low,avg,high,gui,kind,date)
    csvwriter.writerow(name,low,avg,high,gui,kind,date)
f.close()
print('over')