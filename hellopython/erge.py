#-*-coding=utf-8-*-
import sys,os  #导入库  系统操作,文件读写等功能
import requests # URL请求
from lxml import etree  # 网页提取
import subprocess   # 子进程执行外部指令 返回信息
session = requests.Session()
def getContent(url):
    # url='http://www.iqiyi.com/v_19rrkwcx6w.html'
    try:
        ret = requests.get(url)  # get  URL 内容
        ret.encoding='utf-8'  # 设置响应编码
    # except Exception,e:
    except: 
        # print e
        return None
    if ret.status_code==200:    # 判断响应状态码
        return ret.text
    else:
        return None

def getUrl():
    url='http://www.iqiyi.com/v_19rrkwcx6w.html'  
    url2='http://www.iqiyi.com/v_19rrl2td7g.html' # 31-61
    content = getContent(url)
    if not content:
        print "network issue, retry"
        exit(0) # 退出exit(0)
    root = etree.HTML(content,parser=etree.HTMLParser(encoding='utf-8')) # 解析方法  etree.HTMLParse
    elements=root.xpath('//div[@data-current-count="1"]//li')   # xpah方法提取元素,   div标签 特性data-current-count=1  li标签
    for items in elements:
        url_item=items.xpath('.//a/@href')[0]   # 提取href链接列表的头一个
        song_url = url_item.replace('//','')    #  把双斜杆替换为空
        song_url=song_url.strip()   #去掉两边的空格
        print(song_url)  #  打印儿歌URL信息
        # name=items.xpath('.//span[@class="item-num"]/text()')[0]
        name=items.xpath('.//span[@class="item-num"]/text()')[0].encode('utf-8').strip()+\
             ' '+items.xpath('.//span[@class="item-txt"]/text()')[0].encode('utf-8').strip()+'.mp4'
        name= '儿歌多多 '+name
        name=name.decode('utf-8')
        filename=os.path.join(os.getcwd(),name)
        print filename
        if os.path.exists(filename):
            continue
        p=subprocess.Popen('python you-get -d --format=HD {}'.format(song_url),stderr=subprocess.PIPE,stdout=subprocess.PIPE,shell=True)
        output,error = p.communicate()
        print(output)
        print(error)
        p.wait()


def main():
    getUrl()

if __name__ == '__main__':
    main()
