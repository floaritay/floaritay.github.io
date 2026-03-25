from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
import requests
import csv

f=open('pachong/img/'+'菜价.csv',mode='w',encoding='utf-8')
csvwriter=csv.writer(f)

def download(url):
    res=requests.get(url)
    # print(res.text)
    page=BeautifulSoup(res.text,'html.parser')#指定html解析器
    table=page.find('div',class_='quotation-content-list')
    # print(table)
    trs=table.find_all('li',class_='market-list-item')
    # print(trs)
    for tr in trs:
        time = tr.find('span', class_='time').text
        product = tr.find('span', class_='product').text
        place = tr.find('span', class_='place').text
        price = tr.find('span', class_='price').text
        # print(f"时间: {time}, 品种: {product}, 产地: {place}, 价格: {price}")
        csvwriter.writerow([time, product, place, price])

    res.close()
    print(url,'提取完毕')

if __name__=='__main__':
    # download(f'https://www.cnhnb.com/hangqing/cdlist-2003191-0-18-0-0-1/')

    # for i in range(1,11):
    #     download(f'https://www.cnhnb.com/hangqing/cdlist-2003191-0-18-0-0-{i}/')
    
    
    with ThreadPoolExecutor(10) as t:
        for i in range(1,111):
            t.submit(download,f'https://www.cnhnb.com/hangqing/cdlist-2003191-0-18-0-0-{i}/')
    print('all over')
    # 这里网页需要登陆才能继续查看后面的网页，故只做示例