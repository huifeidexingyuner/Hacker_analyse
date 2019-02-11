#_*_coding:utf-8_*_
import sys
import re


reload(sys)
sys.setdefaultencoding('utf-8')

def getword():

    f = open(r'ITWord2.txt','r')
    k = open(r'ITWord1.txt', 'w')
    lines = f.readlines()
    for i in lines:
        word = i.split(' ')
        k.write(word[0])
        k.write('\n')

getword()