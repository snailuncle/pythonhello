import requests
import re


def getHTMLText(url):  # 获取页面
    print("getHTMLText", url)
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except BaseException:
        return ""


def parsePage(ilt, html):  # 解析页面
    # print("parsePage", ilt)
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        for i in range(len(plt)):
            price = eval(plt[i].split(":")[1])
            title = eval(tlt[i].split(":")[1])
            ilt.append([price, title])
    except BaseException:
        print("parsePage异常")


def printGoodsList(ilt):  # 打印商品信息
    # print("printGoodsList", ilt)
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))


def main():
    print("main")
    goods = "书包"
    depth = 10
    start_url = "http://s.taobao.com/search?q=" + goods
    print("start_url", start_url)
    infoList = []
    # 不同页面url不一样
    for i in range(depth):
        try:
            url = start_url + "&s=" + str(44*i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except BaseException:
            continue
    printGoodsList(infoList)


main()
