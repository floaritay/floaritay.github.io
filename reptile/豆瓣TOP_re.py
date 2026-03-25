import requests,re,csv

url='https://movie.douban.com/top250'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 SLBrowser/9.0.5.12181 SLBChan/112 SLBVPV/64-bit'
}
res=requests.get(url,headers=headers)
content=res.text

pattern=re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?</p>.*?<span class="rating_num" property="v:average">(?P<rank>.*?)</span>',re.S)
result=pattern.finditer(content)

# for i in result:
#     print(i.group('name'),end=' ')
#     print(i.group('year').strip())#.strip()去除字符串的首尾空白字符（包括空格、制表符、换行符等）。
#     print(f'评分{i.group('rank')}')

with open('data.csv', mode='w', newline='', encoding='utf-8-sig') as f: #newline=''参数来避免在写入CSV文件时出现额外的空行。
    writer = csv.writer(f)#创建一个写入器对象
    for i in result:
        dic = i.groupdict()#储存到字典
        dic['year'] = dic['year'].strip()
        writer.writerow(dic.values())#写入一行

res.close()

print('over')