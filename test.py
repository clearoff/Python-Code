#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
class Stack(object):
    def __init__(self):
        self._s=[]
        self.sz=0

    def Push(self,data):
        self._s.append(data)
        self.sz=self.sz+1

    def Pop(self):
        data=0
        if self.sz > 0:
            data=self._s.pop()
            self.sz=self.sz-1
        return data

    def Top(self):
        return self._s[self.sz-1]

    def IsEmpty(self):
        return self.sz==0

if __name__== "__main__":
    st=Stack()
    st.Push(1)
    st.Push(2)
    st.Push(3)
    while not st.IsEmpty():
        print st.Pop()

    print "The Stack is empty"

'''


# dict operator

#di_ct={"apple":5,"banana":3,"watermalon":9}
#for k,v in di_ct.iteritems():
#    print("%s-->%d" %(k,v))


#print di_ct["apple"]      #access dict
#print di_ct["banana"]

#print di_ct.items()     # use item opread to access

#for k in di_ct.items():
#    print k


# 字符串的格式化
#print "%s " %"hello world"

# 字符串的截取 split方法
#str="leap said: 1, 2, 3, 4, "
#print "使用空格截取：%s" %str.split()
#print "使用逗号截取：%s" %str.split(',')
#str2=str.split(',',2)
#split函数返回值为所截取的字符串列表。
#num=2表示将字符串分割两次


#for c in str2:
#   print "%s   " %c


#python中利用列表实现对字符串的翻转

#def Reverse(str):
#    ret=''
#    rlist=list(str)
#    rlist.reverse()
#    for c in rlist:
#        ret+=c
#    return ret

#print Reverse("abcdef")


#字符串的查找和替换
#str="abcabcabc"
#print str.find("abc",4,9)
# find(substr,start,end)

#replace(oldsubstr,newsubstr)
#cont="welcome to cvte,cvte"
#print cont.replace('cvte','baidu')

#正则表达式练习
#import re

#print re.findall('[1-9]',"1a2b3c4d5f")
#findall返回值为列表，找出所有匹配的字符
#['1', '2', '3', '4', '5']

#print re.findall("[abc]","abcdef")
##pattern=[m]表示匹配单个字符串


#print re.sub('[abcde]','hel',"abcedfgh")
#根据正则表达式替换string中的子串

#print re.subn('[%20]',' cvte ','we%20are%20good%friends')
#与sub函数相同，返回一个二元元组，替换后的字符串和替换次数

#node=re.match('[987]',"987abc987")
#print re.findall(r'Hello$','Hello ABC Hello',re.I)
# I参数是正则匹配忽略大小写

#print re.findall(r'\b\w+\b',"Hello World\n",re.S)


#通过python实现电话号码的匹配
#tell=['0791-1234567','010-12345678','(010)12345678']
#print re.findall(r"[\(]? \d{3} [\]-]? \d{8} | [\(]? \d{4} [\]-]? \d{7}",tell[2])

import re
s='123abc456'
p=re.compile(r"\b*\d")  #compile方法返回一个正则表达式的对象
print p.findall(s)
print p.pattern