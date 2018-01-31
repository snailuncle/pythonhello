import requests
kv = {"key1": "value1", "key2": "value2"}
r = requests.request("post","http://python123.io/ws", data=kv)
body = "主题内容"
r = requests.request("post", "http://python123.io/ws", data=body)
# headers
hd = {"user-agent": "Chrome/10}
r = requests.request("POST", "http://python123.io/ws",headers=hd)
# files
fs = {"file": open("data.xls", "rb")}
r = requests.request("POST", "http://python123.io/ws", files=fs)
# timeout
r = requests.request("GET", "http://www.baidu.com", timeout=10)
# proxies 设定访问代理服务器
pxs = {"http":"http://user:pass@10.10.10.1:1234"
       "https": "https://10.10.10.1:4321" }
r = requests.request("GET","http://www.baidu.com",proxies=pxs)

