import requests
from bs4 import BeautifulSoup
import os
# 获取链接源代码
def getHTMLText(url,head):
    r = requests.get(url, headers=head)
    r.encoding = r.apparent_encoding
    return r.text
# 解析页面,储存数据
def saveText(html, filePath):
    soup = BeautifulSoup(html, "html.parser")
    allATag = soup.find("div", {"id": "mains1_l"}).find("ul", {"calss", "list_ul_1"}).find_all("a")
    print(allATag)
    for i in allATag:
        url = i.get("href")
        textTitle = i.get_text()
        listLink=["http://www.lygwoman.com/"+ url]    # 完整链接文本
        for j in listLink:
            try:
                r = requests.get(j)
                r.encoding = r.apparent_encoding
                soup = BeautifulSoup(r.text, "html.parser")
                textTag = soup.find("div", {"id": "art_text"})
                text = textTag.get_text()
                date = soup.find("span", {"class": "date_l"}) #获取公告发布日期
                d = date.get_text()
                d1 = d.split("日期：")[-1].split(" ")[0]
                d2 = d1.replace("/","-")
                textWrite = open(filePath+d2+"-"+textTitle+".txt", "w", encoding="utf-8")
                # textWrite.write(text)
                # textWrite.close()
                # print("完成")
            except:
                continue
#得到全部页码
# def getPages(url):
#     r = requests.get(url)
#     soup = BeautifulSoup(r.text, "html.parser")
#     pages = soup.find("div",{"class":"newspage"})
#     number=int(pages.get_text())
#     return number
#入口
def main():
    filePath = "D:/aaa/bb/"     # 保存地址
    if not os.path.exists(filePath):  # 判断是否有这个文件 没有就创建
        os.mkdir(filePath)
    u = "http://www.lygwoman.com/news.asp?sid=8&page=1"
    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0'}
    for n in range(7):
        url = u.replace('1',str(n+1))
        html = getHTMLText(url, head)
        saveText(html, filePath)
    print("存储完成")
main()
