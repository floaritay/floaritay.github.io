import scrapy

class DoubanMovieItem(scrapy.Item):
    title = scrapy.Field()
    rating = scrapy.Field()
    description = scrapy.Field()
    image_url = scrapy.Field()