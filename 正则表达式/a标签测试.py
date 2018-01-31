from bs4 import BeautifulSoup
import re
import requests
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
python href特性html前面的6位数字60092是股票编号,我要爬好多个股票,
怎样在find_all方法中写股票编号的正则


a = soup.find_all("a", target="_blank", href="http://quote.eastmoney.com/sh600292.html", limit=30) 