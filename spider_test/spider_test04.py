import requests
import time
url = 'http://www.zhihu.com/question/56483371/answer/149183021'


def getweb(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return 'success'
    except BaseException:
        return 'error'


def main():
    starttime = time.time()
    for i in range(6):
        print("爬取第", i, "次")
        getweb(url)

    endtime = time.time()
    t = str(starttime - endtime)
    print('爬取时间为: ', t, '秒')


if __name__ == '__main__':
    main()
else:
    print("__name__", "出错")
