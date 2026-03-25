import requests,re

url='https://dytt89.com/'
headers={
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 SLBrowser/9.0.5.12181 SLBChan/112 SLBVPV/64-bit'
}
res=requests.get(url,verify=False,headers=headers)#去掉了安全验证(verify=False,跟https有关)
res.encoding='gb2312'
# print(res.text)

pattern1=re.compile(r'2025必看热片.*?<ul>(?P<ul>.*?)</ul>',re.S)
pattern2=re.compile(r"<a href='(?P<herf>.*?)'",re.S)
pattern3=re.compile(r'◎片　　名(?P<name>.*?)<br />.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)">',re.S)

child_url_list=[]
result1=pattern1.finditer(res.text)
for i in result1:
    ul=i.group('ul')
    # print(ul)
    result2=pattern2.finditer(ul)#提取子页面链接
    for j in result2:
        herf=j.group('herf')
        # print(herf)
        child_url=url+herf.strip('/')#拼接子页面
        # print(child_url)
        child_url_list.append(child_url)#储存到列表

for child_url in child_url_list:
    res=requests.get(child_url,verify=False,headers=headers)
    res.encoding='gb2312'
    # print(res.text)
    result3=pattern3.search(res.text)
    print(result3.group('name'))
    print(result3.group('download'))
    # break#测试用
res.close()