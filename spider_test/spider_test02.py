import requests
import time


def getHTML(url):
    try:
        r = requests.get(url, timeout=5)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return "爬取成功"
    except BaseException:
        return "爬取异常"


def main():
    url = "http://www.sit.edu.cn/97/t/297/main.htm"
    print("请输入爬取次数")
    n = int(input())
    t1 = time.time()
    for i in range(n):
        getHTML(url)

    t2 = time.time()
    sumtime = t2-t1
    print("共爬取", n, "个页面,所需时间为:", sumtime)


main()
