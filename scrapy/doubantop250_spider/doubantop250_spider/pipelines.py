import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request
import re

class DoubanImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if item.get('image_url'):
            # 添加Referer头部防止防盗链
            yield Request(
                url=item['image_url'], 
                meta={'item': item},
                headers={'Referer': 'https://movie.douban.com/'}
            )

    def file_path(self, request, response=None, info=None, *, item=None):
        item_data = request.meta.get('item')
        if item_data:
            # 清理标题中的非法字符
            title = item_data.get('title', 'unknown')
            title = re.sub(r'[^\w\s-]', '', title).strip()
            if not title:
                title = 'unknown'
            return f'{title}.jpg'
        else:
            return 'unknown.jpg'