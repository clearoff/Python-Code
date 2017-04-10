#-*- coding:utf-8 -*-

import urllib
import urllib2
import re
import os
import tool
import requests

"""
filename="taobaomm.txt"

# 抓取MM
class Spider:
    # 页面初始化
    def __init__(self):
        self.siteURL = 'http://mm.taobao.com/json/request_top_list.htm'
        self.tool = tool.Tool()

    # 获取索引页面的内容
    def getPage(self, pageIndex):
        url = self.siteURL + "?page=" + str(pageIndex)
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        return response.read().decode('gbk')

    # 获取索引界面所有MM的信息，list格式
    def getContents(self, pageIndex):
        page = self.getPage(pageIndex)
        #item[0]:头像连接
        #item[1]:个人主页连接
        #item[2]:姓名
        #item[3]:年龄
        #item[4]:城市
        pattern = re.compile(
            '<div class="list-item".*?pic-word.*?<a href=".*?".*?<img src="(.*?)".*?<a class="lady-name" href="(.*?)".*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>',
            re.S)
        items = re.findall(pattern, page)
        contents = []
        for item in items:
            contents.append([item[0], item[1], item[2], item[3], item[4]])
        return contents

    # 获取MM个人详情页面
    #def getDetailPage(self, infoURL):
    #    response = urllib2.urlopen(infoURL)
    #    return response.read().decode('gbk')

    # 获取页面所有图片
    #def getAllImg(self, page):
    #    pattern = re.compile('<div class="mm-aixiu-content".*?>(.*?)<!--', re.S)
    #    # 个人信息页面所有代码
    #    content = re.search(pattern, page)
    #    # 从代码中提取图片
    #    patternImg = re.compile('<img.*?src="(.*?)"', re.S)
    #    images = re.findall(patternImg, content.group(1))
    #   return images

    # 保存多张写真图片
    #def saveImgs(self, images, name):
    #    number = 1
    #    print u"发现", name, u"共有", len(images), u"张照片"
    #    for imageURL in images:
    #        splitPath = imageURL.split('.')
    #        fTail = splitPath.pop()
    #        if len(fTail) > 3:
    #            fTail = "jpg"
    #        fileName = name + "/" + str(number) + "." + fTail
    #        self.saveImg(imageURL, fileName)
    #        number += 1

    # 保存头像
    def saveIcon(self, iconURL, name):
        splitPath = iconURL.split('.')
        fTail = splitPath.pop()
        fileName = name + "/icon." + fTail
        self.saveImg(iconURL, fileName)

    # 保存个人简介
    def saveBrief(self, content, name):
        fileName = name + "/" + name + ".txt"
        f = open(fileName, "w+")
        print u"正在偷偷保存她的个人信息为", fileName
        f.write(content.encode('utf-8'))

    # 传入图片地址，文件名，保存单张图片
    def saveImg(self, imageURL, fileName):
        u = urllib.urlopen(imageURL)
        data = u.read()
        f = open(fileName, 'wb')
        f.write(data)
        print u"正在悄悄保存她的一张图片为", fileName
        f.close()

    def SaveMM(self,item):
        '''
        #item[0]:头像连接
        #item[1]:个人主页连接
        #item[2]:姓名
        #item[3]:年龄
        #item[4]:城市
        '''
        name=item[2]
        age=item[3]
        city=item[4]
        brieflink="http:%s" %str(item[1])
        mmfile.write("name:%s\n" %str(name))
        mmfile.write("age:%s\n" %str(age))
        mmfile.write("city:%s\n" %str(city))
        mmfile.write("Personal brief:%s\n" %brieflink)
        mmfile.write("-----------------------------------------\n")

    # 将一页淘宝MM的信息保存起来
    def savePageInfo(self, pageIndex):
        # 获取第一页淘宝MM列表
        contents = self.getContents(pageIndex)
        for item in contents:
            print u"发现一位模特,名字叫", item[2], u"芳龄", item[3], u",她在", item[4]
            print u"正在偷偷地保存", item[2], "的信息"
            self.SaveMM(item)
            print u"保存%s信息完毕" %item[2]
            #path=item[2]
            #detailURL = "http:%s" %item[1]



    # 传入起止页码，获取MM图片
    def savePagesInfo(self, start, end):
        for i in range(start, end + 1):
            print u"正在偷偷寻找第", i, u"个地方，看看MM们在不在"
            self.savePageInfo(i)


# 传入起止页码即可，在此传入了2,10,表示抓取第2到10页的MM
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
mmfile=file(filename,'w')
spider = Spider()
spider.savePagesInfo(2, 10)
mmfile.close()
"""

