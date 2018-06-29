# -*- coding: utf-8 -*-

# Scrapy settings for SinaSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'SinaSpider'

SPIDER_MODULES = ['SinaSpider.spiders']
NEWSPIDER_MODULE = 'SinaSpider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'SinaSpider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'SinaSpider.middlewares.SinaspiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'SinaSpider.middlewares.SinaspiderDownloaderMiddleware': 543,
	'SinaSpider.middlewares.UserAgentMiddleware':500,
	# 'SinaSpider.middlewares.ProxyMiddleware': 400,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'SinaSpider.pipelines.SinaspiderPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


PROXY_IP = [
	{'ip': '106.56.102.209'},
	# {'ip': '61.135.217.7'},
	# {'ip': '175.11.213.25'},
	# {'ip': '118.190.95.35'},
	# {'ip': '118.190.95.43'},
	# {'ip': '114.231.71.41'},
]

USERAGENT = [
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
	"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
	"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
	"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
	"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
	"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
	"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
	'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)',
	'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.2)',
	'Opera/9.27 (Windows NT 5.2; U; zh-cn)',
	'Opera/8.0 (Macintosh; PPC Mac OS X; U; en)',
	'Mozilla/5.0 (Macintosh; PPC Mac OS X; U; en) Opera 8.0',
	'Mozilla/5.0 (Linux; U; Android 4.0.3; zh-cn; M032 Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
	'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13'
]

# COOKIES = {
# 	'_T_WM': '9488922b79b3a5c3466d62922c80f1b7',
# 	'MLOGIN': '0',
# 	'M_WEIBOCN_PARAMS': 'luicode%3D10000011%26lfid%3D1076032778292197',
# 	'login': '966ea0a87f4cbf4599f17efc97e14ba9'
# }

COOKIES = {'_T_WM': '9488922b79b3a5c3466d62922c80f1b7', 'SCF': 'Ar6mKqdSjw_f79qLBBjBLs6S6S6SDlWx9ze7ChlzRfJvpiaTjPwrypZTJTk2bgxV0pNfhoFQE9rmvYf49eOjRuI.', 'MLOGIN': '1', 'SUB': '_2A252MkZTDeRhGeVO6VcS9C_Fwj2IHXVV3WobrDV6PUJbkdANLWH4kW1NTT97o0S9jV9VDJZyn8Cpt-19JCDGJSnI', 'SUHB': '0D-FxxuvyDw4t1', 'SSOLoginState': '1530279427', 'M_WEIBOCN_PARAMS': 'featurecode%3D20000320%26luicode%3D20000174%26lfid%3Dhotword'}

