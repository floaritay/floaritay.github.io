BOT_NAME = 'changshafangjia'

SPIDER_MODULES = ['changshafangjia.spiders']
NEWSPIDER_MODULE = 'changshafangjia.spiders'

# 启用管道
ITEM_PIPELINES = {
   'changshafangjia.pipelines.ChangshaHousePipeline': 300,
}

# 下载设置
DOWNLOAD_DELAY = 1.5

# 用户代理
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'

# 自动限速
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 1.0
AUTOTHROTTLE_MAX_DELAY = 30.0

# 日志
LOG_LEVEL = 'INFO'