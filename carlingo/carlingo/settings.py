# -*- coding: utf-8 -*-
#from scrapy.settings.default_settings import ITEM_PIPELINES
# Scrapy settings for carlingo project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
import sys
import MySQLdb
import redis

BOT_NAME = 'carlingo'
BOT_VERSION = '1.0'

# SCRAPY SETTING
SPIDER_MODULES = ['carlingo.spiders']
NEWSPIDER_MODULE = 'carlingo.spiders'
#IMAGES_STORE= '/Users/codehi/Documents/github_project/carlingo/output'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

# SQL DATABASE SETTING
#MYSQL_DB = 'scrapyDB'
#MYSQL_TABLE = 'carlingo'
#MYSQL_HOST = 'localhost'
#MYSQL_USER = 'root'
#MYSQL_PASSWD = '12345'

# connect to the MySQL server
#try:
#    CONN = MySQLdb.connect(host = MYSQL_HOST,
#                           user = MYSQL_USER,
#                           passwd = MYSQL_PASSWD,
#                           db = SQL_DB)
#except MySQLdb.Error, e:
#    print "Error %d: %s" % (e.args[0], e.args[1])
#    sys.exit(1)

ITEM_PIPELINES = {
     'carlingo.pipelines.CarlingoPipeline': 0
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'carlingo (+http://www.yourdomain.com)'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS=32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY=3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN=16
#CONCURRENT_REQUESTS_PER_IP=16

# Disable cookies (enabled by default)
#COOKIES_ENABLED=False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED=False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'carlingo.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'carlingo.middlewares.MyCustomDownloaderMiddleware': 543,
   'carlingo.random_useragent.RandomUserAgentMiddleware': 400,
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'carlingo.pipelines.SomePipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# NOTE: AutoThrottle will honour the standard settings for concurrency and delay
#AUTOTHROTTLE_ENABLED=True
# The initial download delay
#AUTOTHROTTLE_START_DELAY=5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY=60
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG=False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED=True
#HTTPCACHE_EXPIRATION_SECS=0
#HTTPCACHE_DIR='httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES=[]
#HTTPCACHE_STORAGE='scrapy.extensions.httpcache.FilesystemCacheStorage'
