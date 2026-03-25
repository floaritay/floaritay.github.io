# 1.提取子页面地址
# 2.找到子页面图片下载地址
# 3.下载

import requests
from bs4 import BeautifulSoup
import time

url='https://www.umei.cc/bizhitupian/weimeibizhi/'
res=requests.get(url)
res.encoding='utf-8'

page=BeautifulSoup(res.text,'html.parser')
# print(page)
alist=page.find('div',class_="item_list infinite_scroll").find_all('a')
# print(alist)
for a in alist:
    # print(a.get('href'))#通过get拿到属性的值
    href=a.get('href')
    # /bizhitupian/weimeibizhi/317404.htm
    hrefs=url+href.strip('/bizhitupian/weimeibizhi/')+'htm'
    # 提取的子页面链接
    # print(hrefs)
    child_res=requests.get(hrefs)
    child_res.encoding='utf-8'
    child_page=BeautifulSoup(child_res.text,'html.parser')
    img=child_page.find('div',class_="big-pic").find('img')
    # print(img)
    img_src=img.get('src')
    # print(img_src)
    # 下载图片                          #以下内容报错，找不到地址，网页也加载不出
    img_res=requests.get(img_src)
    # img_res.content # 这里拿到的是字节
    img_name=img_src.split('/')[-1]# 以斜杠最后一部分取名

    with open('img/'+img_name,mode='wb') as f:
        f.write(img_res.content)# 图片内容写入文件夹
    print('over!!',img_name)

    time.sleep(1)

    # break



res.close()
print('all over!!')
