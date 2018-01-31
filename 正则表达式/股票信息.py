import re
import traceback

import requests
from bs4 import BeautifulSoup


# 获取网页字符串
def getHTMLText(url):
    print("getHTMLText", url)
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding()
        return r.text
    except BaseException:
        print("getHTMLText", "异常")
        return ""


# 获取股票列表
# <a target="_blank" href="http://quote.eastmoney.com/sh500006.html">基金裕阳(500006)</a>
def getStockList(lst, stockURL):  # 股票列表
    html = getHTMLText(stockURL)  # 获取网页
    soup = BeautifulSoup(html, "html.parse")  # 解析网页为r对象
    # find_all( name , attrs , recursive , string , **kwargs )
    # find_all() 方法搜索当前tag的所有tag子节点,并判断是否符合过滤器的条件
    a = soup.find_all("a")  # 在soup对象中找所有的a标签
    for i in a:  # 遍历a标签的集合
        try:
            href = i.attrs["href"]
# 正则 re.findall  的简单用法（返回string中所有与pattern相匹配的全部字串，返回形式为数组）
# 语法：(返回列表List)=====================['th', 'wh']
# findall(pattern, string, flags=0)
            lst.append(re.findall(r"[s][hz]\d{6}", href)[0])
        except BaseException:
            continue


# 获取个股信息
def getStockInfo(lst, stockURL, fpath):  # 个股信息
    # 遍历股票列表,查询个股信息
    for stock in lst:
        # 查询网址 + 股票编号
        url = stockURL + stock + ".html"
        # 获取网页
        html = getHTMLText(url)
        try:
            if html == "":
                continue
            # 初始化个股信息,字典类,========d = {key1 : value1, key2 : value2 }
            infoDict = {}
            # 网页美味汤
            # 解析网页
            soup = BeautifulSoup(html, "html.parser")
            # 个股信息
# <div class="stock-bets">
#         <h1>
#             <a class="bets-name" href="/stock/sz000725.html">
#             京东方Ａ (<span>000725</span>)
#             </a>
#             <span class="state f-up">已收盘 2018-01-31 &nbsp;15:00:03
#             </span>
#         </h1>
#         <div class="price s-up ">
#                         <strong  class="_close">6.08</strong>
#             <span>+0.01</span>
#             <span>+0.16%</span>
#                     </div>
#         <div class="bets-content">
            
#                                             <div class="line1">
#                     <dl><dt>今开</dt><dd class="s-up">6.02</dd></dl>
#                     <dl><dt>成交量</dt><dd>563.15万手</dd></dl>
#                     <dl><dt>最高</dt><dd class="s-up">6.14</dd></dl>
#                     <dl><dt>涨停</dt><dd class="s-up">6.68</dd></dl>
#                     <dl><dt>内盘</dt><dd>267.26万手</dd></dl>
#                     <dl><dt>成交额</dt><dd>34.30亿</dd></dl>
#                     <dl><dt>委比</dt><dd>-25.56%</dd></dl>
#                     <dl><dt>流通市值</dt><dd>2058.72亿</dd></dl>
#                     <dl><dt class="mt-1">市盈率<sup>MRQ</sup></dt><dd>24.50</dd></dl>
#                     <dl><dt>每股收益</dt><dd>0.19</dd></dl>
#                     <dl><dt>总股本</dt><dd>347.98亿</dd></dl>
#                     <div class="clear"></div>
#                 </div>
#                 <div class="line2">
#                     <dl><dt>昨收</dt><dd>6.07</dd></dl>
#                     <dl><dt>换手率</dt><dd>1.66%</dd></dl>
#                     <dl><dt>最低</dt><dd class="s-down">6.01</dd>
#                     </dl>
#                     <dl><dt>跌停</dt><dd class="s-down">
#                         5.46</dd></dl>
#                     <dl><dt>外盘</dt><dd>295.90万手</dd></dl>
#                     <dl><dt>振幅</dt><dd>2.14%</dd></dl>
#                     <dl><dt>量比</dt><dd>2.97</dd></dl>
#                     <dl><dt>总市值</dt><dd>2115.74亿</dd></dl>
#                     <dl><dt>市净率</dt><dd>2.53</dd></dl>
#                     <dl><dt>每股净资产</dt><dd>2.41</dd></dl>
#                     <dl><dt>流通股本</dt><dd>338.60亿</dd></dl>
#                 </div>
#                                         <div class="clear"></div>
#         </div>
#     </div>
            stockInfo = soup.find("div", attrs={"class": "stock-bets"})

            name = stockInfo.find_all(attrs={"class": "bets-name"})[0]
            infoDict.update({"股票名称": name.text.split()[0]})
            # 提取股票综合信息
            keyList = stockInfo.find_all("dt")
            valueList = stockInfo.find_all("dd")
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val
            # 写入文件
            with open(fpath, "a", encoding="utf-8") as f:
                f.write(str(infoDict) + "\n")

        except BaseException:
            traceback.print_exc()
            continue


def main():
    # 股票列表网址
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    # 个股查询网址
    stock_info_url = 'http://gupiao.baidu.com/stock/'
    # 股票信息输出到文本
    output_file = "D:/BaiduStockInfo.txt"
    slist = []
    # 获取股票列表信息
    getStockList(slist, stock_list_url)
    # 获取个股信息,并写入文件
    getStockInfo(slist, stock_info_url, output_file)


main()
