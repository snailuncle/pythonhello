import requests
from bs4 import BeautifulSoup
url = "http://python123.io/ws/demo.html"
r = requests.get(url)
# print(r.text)
demo = r.text
# html.parser 解析器
soup = BeautifulSoup(demo, "html.parser")
print(soup.prettify)
