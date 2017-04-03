#-*- coding:utf-8 -*-

import urllib2
import re
import os

class Spider(object):
    '''
        内涵段子爬虫
    '''
    def load_page(self,url,page):
        '''
            发送url请求
            得到html
            并且用正则表达式对html进行处理，只保留段子内容
        '''
        url=url+str(page)+".html"
        print url
        user_agent="Mozilla/5.0"
        #print "debug 1"
        headers={"User-Agent":user_agent}
        #print "debug 2"
        req = urllib2.Request(url, headers=headers)
        #print "debug 3"
        response = urllib2.urlopen(req)
        #print "debug 4"
        html=response.read()
        html=html.decode("gbk").encode("utf-8")
        pattern=re.compile(r'<div.*?class="f18 mb20">(.*?)</div>',re.S)
        duanzi_list=pattern.findall(html)
        return duanzi_list

    def Write_file(self,duzi,page):
        '''
            将爬虫的文本写入文件当中
        '''
        filename="duanzi"+str(page)+".txt"
        fwrite=file(filename,"wb")
        for item in duzi:
            fwrite.write(item.replace("<p>"," ").replace("</p>"," ").replace("<br />"," "))
        fwrite.close()


if __name__ == "__main__":
    tieba=Spider()
    root_url="http://www.neihan8.com/article/list_5_"
    page_begin = int(raw_input("请输入开始页码："))
    page_end = int(raw_input("请输入结束页码："))
    for page in range(page_begin,page_end):
        duzi=tieba.load_page(root_url,page)
        tieba.Write_file(duzi,page)
    #for item in duzi:
    #   print item.replace("<p>","").replace("</p>"," ")
