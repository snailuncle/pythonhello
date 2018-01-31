import requests
from bs4 import BeautifulSoup
import bs4


def getHTMLText(url):  # 获得网页源码
    try:
        r = requests.get(url, timeout=30)  # get方法
        r.raise_for_status()  # 连接网页状态,404,200
        r.encoding = r.apparent_encoding  # 设置r对象的编码
        return r.text  # 返回网页字符串
    except BaseException:
        return "getHTMLText异常"


def fillUnivList(ulist, html):  # 大学列表 网页
    soup = BeautifulSoup(html, "html.parser")  # 解析网页
    for tr in soup.find("tbody").children:  # 在tbody标签中的下架标签中查找tr标签
        if isinstance(tr, bs4.element.Tag):  # 只要标签,不要文本
            tds = tr("td")  # 在tr标签下,查找所有td标签
            # 取td标签的第0,1,3个文本
            messageList = stringExtract([tds[0], tds[1], tds[2], tds[3]])
            # print(messageList)
            ulist.append(messageList)


def stringExtract(theElementList):
    tempList = []
    for i in range(len(theElementList)):
        # print ("序号：%s   值：%s" % (i + 1, list[i]))
        tempList.append(theElementList[i].string)
        # print(tempList)
    return tempList


def printUnivList(ulist, num):  # 打印大学列表
    # 排名 学校 地点 分数
    tplt = "{0:^10}\t{1:{4}^10}\t{3:^10}\t{2:^10}"  # 每列都是10个字符,居中,中间填充中国空格
    print(tplt.format("排名", "学校", "总分", "城市", chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[3], u[2], chr(12288)))


def main():
    uinfo = []  # 列表初始化,空list
    url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html"
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 100)  # 20 univs


main()
