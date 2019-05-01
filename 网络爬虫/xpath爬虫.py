import requests
from scrapy import Selector

head = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"}
url = 'http://www.atobo.com.cn/Companys/'
r = requests.get(url, headers=head)
r.encoding = 'GB2312'
url1 = Selector(text=r.text).xpath("//div[@class='filterlist']/ul/li[@class='alist']//li/a/@href").extract()  #获取url
for k in url1:
    for i in range(1,3):
        try:
            url2 = 'https://www.atobo.com.cn'+k + '-y' +str(i)
            a = requests.get(url2, headers=head)
            a.encoding = 'GB2312'
            txt = Selector(text=a.text).xpath("//div/ul/li[@class='p_name']//a[@class='CompanyName']/text()").extract()  #获取url
            for j in txt:
                f= open("D:/aaa/a1.txt",'a+',encoding="utf-8")
                f.write(j+'\n')
        except:
            continue
