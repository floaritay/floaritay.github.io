BOT_NAME = 'doubantop250_spider'

SPIDER_MODULES = ['doubantop250_spider.spiders']
NEWSPIDER_MODULE = 'doubantop250_spider.spiders'

# 不遵守robots.txt规则，允许跨域请求
ROBOTSTXT_OBEY = False

# Configure user agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'

# Configure download delay
DOWNLOAD_DELAY = 2
RANDOMIZE_DOWNLOAD_DELAY = True

# Enable pipelines
ITEM_PIPELINES = {
    'doubantop250_spider.pipelines.DoubanImagePipeline': 1,
}

# Images pipeline settings
IMAGES_STORE = 'downloaded_images'

# 允许跨域请求
MEDIA_ALLOW_REDIRECTS = True

# 默认请求头
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'Referer': 'https://movie.douban.com/',
}

# 禁用offsite中间件或扩展allowed_domains
SPIDER_MIDDLEWARES = {}