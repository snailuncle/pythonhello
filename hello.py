import requests
r = requests.get("http://www.baidu.com")
s = r.status_code
print(s)
r.encoding = "utf-8"
s = r.text
print(s)
print(type(r))
print(r.headers)
