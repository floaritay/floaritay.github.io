import csv
from datetime import datetime

class ChangshaHousePipeline:
    def open_spider(self, spider):
        self.file = open('changsha_houses.csv', 'w', newline='', encoding='utf-8-sig')
        fieldnames = ['district', 'area', 'unit_price', 'rooms', 'build_year', 'near_subway', 'url', 'crawl_time']
        self.writer = csv.DictWriter(self.file, fieldnames=fieldnames)
        self.writer.writeheader()
    
    def process_item(self, item, spider):
        # 清洗数据
        cleaned_item = {
            'district': item.get('district', ''),
            'area': item.get('area', ''),
            'unit_price': item.get('unit_price', ''),
            'rooms': item.get('rooms', ''),
            'build_year': item.get('build_year', ''),
            'near_subway': '是' if item.get('near_subway') else '否',
            'url': item.get('url', ''),
            'crawl_time': item.get('crawl_time', '')
        }
        
        # 验证数据
        if cleaned_item['area']:
            try:
                area = float(cleaned_item['area'])
                if not (10 <= area <= 500):
                    cleaned_item['area'] = ''
            except:
                cleaned_item['area'] = ''
        
        if cleaned_item['unit_price']:
            try:
                price = int(cleaned_item['unit_price'])
                if not (1000 <= price <= 50000):
                    cleaned_item['unit_price'] = ''
            except:
                cleaned_item['unit_price'] = ''
        
        # 写入CSV
        self.writer.writerow(cleaned_item)
        return item
    
    def close_spider(self, spider):
        self.file.close()
        spider.logger.info("数据已保存到 changsha_houses.csv")