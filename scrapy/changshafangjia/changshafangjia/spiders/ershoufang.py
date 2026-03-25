import scrapy
import re
from datetime import datetime

class ErshoufangSpider(scrapy.Spider):
    name = 'ershoufang'
    allowed_domains = ['cs.58.com']
    start_urls = [f'https://cs.58.com/ershoufang/pn{page}/' for page in range(1, 61)]
    
    def parse(self, response):
        """解析列表页"""
        self.logger.info(f"正在解析: {response.url}")
        
        # 尝试多种选择器
        houses = response.css('ul.house-list-wrap li')
        if not houses:
            houses = response.css('li[logr]')
        if not houses:
            houses = response.css('.property')
        if not houses:
            houses = response.css('.house-list-wrap > div')
        
        self.logger.info(f"找到 {len(houses)} 个房源")
        
        for house in houses:
            item = self.parse_house_item(house)
            if item:
                # 获取详情页链接
                detail_url = house.css('a::attr(href)').get()
                if not detail_url:
                    detail_url = house.css('a.property-ex::attr(href)').get()
                
                if detail_url:
                    # 处理URL
                    if detail_url.startswith('//'):
                        detail_url = 'https:' + detail_url
                    elif detail_url.startswith('/'):
                        detail_url = 'https://cs.58.com' + detail_url
                    
                    # 如果有基本信息，进入详情页
                    if item.get('district') or item.get('area'):
                        yield scrapy.Request(
                            detail_url,
                            callback=self.parse_detail,
                            meta={'item': item},
                            errback=self.handle_error
                        )
                    else:
                        # 没有基本信息，直接返回
                        item.update({
                            'build_year': None,
                            'near_subway': False,
                            'url': detail_url,
                            'crawl_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        })
                        yield item
    
    def parse_house_item(self, house):
        """从房源元素中提取基本信息"""
        item = {}
        
        # 1. 区名 - 尝试多种选择器
        district = house.css('.property-content-info-comm-name::text').get()
        if not district:
            district = house.css('.property-content-info-comm-address span::text').get()
        if not district:
            district = house.css('.property-content-info-comm-name a::text').get()
        if not district:
            # 从标题中提取
            title = house.css('h3.title a::text').get()
            if title:
                # 尝试提取区名，如 "岳麓 梅溪青秀"
                parts = title.split()
                if len(parts) > 0:
                    district = parts[0]
        
        if district:
            item['district'] = district.strip()
        
        # 2. 面积和房间数
        info_text = ''
        info_elements = house.css('.property-content-info-text::text').getall()
        if info_elements:
            info_text = ' '.join(info_elements)
        else:
            # 备用选择器
            info_text = house.css('.property-content-info-text span::text').get() or ''
        
        # 提取面积
        area_match = re.search(r'(\d+\.?\d*)\s*㎡', info_text)
        if not area_match:
            area_match = re.search(r'(\d+\.?\d*)\s*平米', info_text)
        if area_match:
            try:
                item['area'] = float(area_match.group(1))
            except:
                item['area'] = None
        
        # 提取房间数
        room_match = re.search(r'(\d+)室', info_text)
        if room_match:
            try:
                item['rooms'] = int(room_match.group(1))
            except:
                item['rooms'] = None
        
        # 3. 每平米价格
        unit_price = house.css('.property-price-average::text').get()
        if not unit_price:
            unit_price = house.css('p.unit span::text').get()
        
        if unit_price:
            # 提取数字
            price_match = re.search(r'([\d,]+)', unit_price.replace('元/平米', '').replace('元/㎡', ''))
            if price_match:
                try:
                    price_num = price_match.group(1).replace(',', '')
                    item['unit_price'] = int(price_num)
                except:
                    item['unit_price'] = None
        
        return item
    
    def parse_detail(self, response):
        """解析详情页"""
        item = response.meta['item']
        
        # 4. 建造时间
        build_year = None
        
        # 方法1：搜索页面中的年份
        year_match = re.search(r'(19\d{2}|20\d{2})', response.text)
        if year_match:
            build_year = int(year_match.group(1))
        
        # 方法2：从特定区域查找
        if not build_year:
            base_info = response.css('.general-item-left, .house-basic-item, .msg').get()
            if base_info:
                year_match = re.search(r'(19\d{2}|20\d{2})', base_info)
                if year_match:
                    build_year = int(year_match.group(1))
        
        # 方法3：从描述中查找
        if not build_year:
            desc_text = response.css('.house-desc::text, .desc::text').get()
            if desc_text:
                year_match = re.search(r'(19\d{2}|20\d{2})', desc_text)
                if year_match:
                    build_year = int(year_match.group(1))
        
        item['build_year'] = build_year
        
        # 5. 是否近地铁
        # 检查页面中是否包含地铁相关词汇
        page_text = response.text.lower()
        subway_keywords = ['地铁', '地铁站', '地铁口', '轨道交通', '地铁沿线', '地铁房']
        item['near_subway'] = any(keyword in page_text for keyword in subway_keywords)
        
        # 添加元数据
        item['url'] = response.url
        item['crawl_time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        yield item
    
    def handle_error(self, failure):
        """处理请求错误"""
        self.logger.error(f"请求失败: {failure.request.url}")
        
        # 如果详情页请求失败，返回基本数据
        if 'item' in failure.request.meta:
            item = failure.request.meta['item']
            item.update({
                'build_year': None,
                'near_subway': False,
                'url': failure.request.url,
                'crawl_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })
            yield item