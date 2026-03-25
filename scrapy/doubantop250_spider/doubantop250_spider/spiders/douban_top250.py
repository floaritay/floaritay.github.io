# 不仅爬取图片链接，还通过管道下载图片

import scrapy
from doubantop250_spider.items import DoubanMovieItem

class DoubanSpider(scrapy.Spider):
    name = 'douban_top250'
    # 添加豆瓣图片域名到allowed_domains
    allowed_domains = ['movie.douban.com', 'img1.doubanio.com', 'img2.doubanio.com', 'img3.doubanio.com', 
                      'img4.doubanio.com', 'img5.doubanio.com', 'img6.doubanio.com', 'img7.doubanio.com', 
                      'img8.doubanio.com', 'img9.doubanio.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        # 提取所有电影链接
        movie_links = response.css('div.hd > a::attr(href)').getall()
        
        for link in movie_links:
            yield response.follow(link, callback=self.parse_movie)
            
        # 获取下一页链接并继续爬取
        next_page = response.css('span.next > a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def parse_movie(self, response):
        item = DoubanMovieItem()
        
        # 电影标题
        title = response.css('h1 span[property="v:itemreviewed"]::text').get()
        if title:
            item['title'] = title.strip()
        else:
            item['title'] = 'Unknown Title'
        
        # 评分
        rating = response.css('strong[property="v:average"]::text').get()
        if rating:
            try:
                item['rating'] = float(rating)
            except ValueError:
                item['rating'] = 0.0
        else:
            item['rating'] = 0.0
        
        # 描述
        description = response.css('span[property="v:summary"]::text').getall()
        if description:
            item['description'] = ''.join(description).strip()
        else:
            item['description'] = 'No description available'
        
        # 图片链接
        image_url = response.css('div#mainpic img::attr(src)').get()
        if image_url:
            item['image_url'] = image_url
        else:
            item['image_url'] = None
        
        yield item


# 运行此爬虫：
#  创建一个Scrapy项目: 
#  cd D:\VSCodepythonprogram\scrapy
#  scrapy startproject doubantop250_spider
# 
#  将此代码复制到项目中的spiders文件夹下
#
#  在项目根目录（D:\VSCodepythonprogram\scrapy\doubantop250_spider）下，手动创建名为 download_images 的文件夹（用于存放下载的图片）。
#  根目录：有scrapy.cfg文件的那一个目录
#
#  在项目根目录执行: scrapy crawl douban_top250 -o movies.json
#  图片将会下载到 doubantop250_spider\downloaded_images 文件夹中，以电影标题命名

# 对应修改
# settings.py 
# items.py     
# pipelines.py 