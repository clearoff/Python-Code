#!/usr/bin/python

#import os
#fread=open("file.txt","r")
#str=fread.read();
#print("%s %d" %('The file.txt have ? :',len(str)))
#
#print str.split()

# find rise many words

import os
fread=open("file.txt","r")
str=fread.read()
print str
print normalize(str)
Map={}
for ch in words:
	Map.setdefault(ch,words.count(ch))
print Map
