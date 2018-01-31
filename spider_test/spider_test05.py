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


url = "http://www.baidu.com"
n = 10
t1 = time.time()
for i in range(n):
    print("爬取第", i+1, "次")
    print(getweb(url))
t2 = time.time()
t = t2 - t1
print("爬去网页时间花费了", t, "秒")
