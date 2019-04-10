from scrapy import cmdline
cmdline.execute('scrapy crawl panda -o test.json'.split())
# cmdline.execute('scrapy crawl douban_spider -o test.csv'.split())