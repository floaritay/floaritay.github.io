import requests

url='https://www.pearvideo.com/video_1730587'#网页链接
count_id=url.split('_')[1]# 拿到视频的id 1730587
#Element: https://video.pearvideo.com/mp4/short/20210528/cont-1730587-15683024-hd.mp4   真正的视频地址
#Preview: https://video.pearvideo.com/mp4/short/20210528/1737865782007-15683024-hd.mp4  解密前地址
#Headers：https://www.pearvideo.com/videoStatus.jsp?contId=1730587&mrd=0.6816886482032432 #网页二次加工拿到视频链接所访问的链接
vedio_url=f'https://www.pearvideo.com/videoStatus.jsp?contId={count_id}&mrd=0.6816886482032432'# 把id加到视频链接
headers={
    #防盗链 referer（引用页） 会溯源是哪个页面的请求，一定是他的上一级页面
    'Referer':'https://www.pearvideo.com/video_1730587'
}
#拿vedio_url的json
res=requests.get(vedio_url,headers=headers)
# print(res.text)
# {
#         "resultCode":"5",
#         "resultMsg":"该文章已经下线！",
#         "systemTime": "1737867605076"
# }防盗链反爬

#通过字典的方式找到srcUrl和systemTime
dic=res.json()
srcUrl=dic['videoInfo']['videos']['srcUrl']
systemTime=dic['systemTime']
#替换
srcUrl=srcUrl.replace(systemTime,f'cont-{count_id}')
# print(srcUrl) #ok

#下载视频，准备文件
with open('pachong/img/a.mp4',mode='wb') as f:
    f.write(requests.get(srcUrl).content)
print('ok')

res.close()