import scrapy

class ChangshafangjiaItem(scrapy.Item):
    # 定义数据字段
    title = scrapy.Field()          # 标题
    district = scrapy.Field()       # 区名
    area = scrapy.Field()           # 面积（平方米）
    unit_price = scrapy.Field()     # 每平米价格
    total_price = scrapy.Field()    # 总价
    rooms = scrapy.Field()          # 房间数
    build_year = scrapy.Field()     # 建造时间
    near_subway = scrapy.Field()    # 是否近地铁
    detail_url = scrapy.Field()     # 详情页URL
    crawl_time = scrapy.Field()     # 爬取时间