import requests
import time


def getweb(url):
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return "成功"
    except BaseException:
        return "异常"


url = "http://www.usj.co.jp/ticket/expresspass/expr.html"
t1 = time.time()
for i in range(100):
    print("爬取第", i+1, "次", getweb(url))
t2 = time.time()
t = t2 - t1
print("爬取网页100次时间花费了", t, "秒")
