#-*- coding:utf-8 -*-

import urllib2
import urllib
import requests
import re
import os
import sys
from bs4 import BeautifulSoup

'''
class QSBK():
    def __init__(self):
        self.url = 'http://www.qiushibaike.com/hot/page/'  # 基础网址
        self.user_agent = 'Mozilla/4.0(cpmpatible;MSIE 5.5;Windows NT)'  # 要添加的headers
        self.headers = {'User-Agent': self.user_agent}
        self.item_joke = []  # 用来保存段子的列表

    # 请求函数
    def request(self, page):
        request = urllib2.Request(self.url + str(page), headers=self.headers)
        response = urllib2.urlopen(request)
        return response.read().decode('utf-8')  # 将源代码进行编码转换为HTML格式

    # 将获取到的网页和正则表达式进行匹配并返回匹配到的每个段子的信息列表
    def get_joke(self, num):
        try:
            page=self.request(num)
            pattern = re.compile(
                '<.*?class="author.*?>.*?<a.*?<h2>(.*?)</h2>.*?<div.*?class="content".*?<span>(.*?)</span>(.*?)<div class="stats.*?class="number">(.*?)</i>',
                re.S|re.M)
            items=re.findall(pattern, page)
            for item in items:
                print item[0],item[1],item[2],item[3]
                print "#######################################"
            #self.item_joke.append(re.findall(pattern, content))  # 将获取到的每一页的段子追加到存储列表中
        except urllib.error.URLError as e:
            if hasattr(e, "code"):
                print(e.code)
            if hasattr(e, "reason"):
                print(e.reason)

sp=QSBK()
sp.get_joke(1)
'''




class Spider:
    def __init__(self):
        self.root_url="http://www.weather.com.cn/weather/101110101.shtml"
        self.Link=[]

    #获取一页html
    def GetPage(self,url):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 "}
        if url:
            request=urllib2.Request(url,headers=headers)
            response=urllib2.urlopen(request)
            print u"获取html成功...正在写入文件"
            page=response.read().decode('utf-8')
            print u"写入文件成功..."
            return page
        else :
            return None


    def getContents(self,page):
        pattern1 = re.compile(
            '<.*?class="con.*?today.*?>.*?<a.*?href.*?>(.*?)</a>.*?<a.*?href.*?>(.*?)</a>.*?<span>.*?</span>.*?<span>(.*?)</span>',
            re.S)
        pattern2 = re.compile(
            '<li.*?class="sky.*?<h1>(.*?)</h1>.*?<p.*?>(.*?)</p>.*?<p.*?class="tem.*?<span>(.*?)</span>.*?<i>(.*?)</i>',
            re.S | re.M)
        if page==None:
            return
        else:
            print u"开始进行提取..."
            items = re.findall(pattern1, page)
            print u"debug1"
            for item in items:
                proc = item[0]
                city = item[1]
                sqre = item[2]
            print u"for end"
            items = re.findall(pattern2, page)
            print u"debug2"
            print proc, city, sqre
            print "-----近期天气状况如下-----"
            print items
            for item in items:
                print item[0], "-", item[1], "-", item[2], "-", item[3]
                print "#######################################################"

    #获取一个html下的url
    def GetLink(self,page):
        #pattern=re.compile('<li>.*?<a.*?href="(.*?)".*?>',re.S)
        soup=BeautifulSoup(page)
        node=soup.find_all('a',href=re.compile(r"^/weather.*?/\d+.shtml",re.S))
        #print soup.prettify()
        for link in node:
            pattern=re.compile('<a.*?href="(.*?)">')
            newUrl=re.findall(pattern,str(link))
            url="http://www.weather.com.cn/"+str(newUrl[0])
            self.Link.append(url)
        print u"Get all link End"

    def Start(self):
        print u"爬取天气信息开始"
        page=self.GetPage(self.root_url)
        self.GetLink(page)
        for url in self.Link:
            print url
            page=self.GetPage(url)
            self.getContents(page)
        print u"爬取天气信息结束"


reload(sys)
sys.setdefaultencoding('utf-8')
wea=Spider()
wea.Start()




