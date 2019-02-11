#_*_coding:utf-8_*_
import requests
import re
import sys
from bs4 import BeautifulSoup
import os
import random
from PIL import Image
from io import BytesIO
import urllib
reload(sys)
sys.setdefaultencoding('utf-8')


def login(url,headers):

    txt = open('ITWord.txt','w')
    request = requests.get(url, headers=headers)

    if (request.status_code != 200):
        print("获取页面失败")

    html = BeautifulSoup(request.text, "html.parser")
    filtrate = re.compile(u'[a-zA-Z0-9]+')
    itword = html.find_all("span")
    for i in itword:
        word = ''
        oneword = str(i.string)
        filtered_str = filtrate.findall(oneword)
        lenword = len(filtered_str)
        if lenword == 0:
            pass
        elif lenword == 1:
            print (filtered_str[0])
            txt.write(filtered_str[0])
            txt.write('\n')
        else:
            for i in range(lenword):
                word = word + ' ' + filtered_str[i]
                word.strip()
            print (word.strip())
            txt.write(word.strip())
            txt.write('\n')

    txt.close()

def get2(url,headers):

    wordlist = []
    txt = open('ITWord3.txt', 'w')
    request = requests.get(url, headers=headers)

    if (request.status_code != 200):
        print("获取页面失败")

    html = BeautifulSoup(request.text, "html.parser")
    filtrate = re.compile(u'[a-zA-Z0-9]+')
    itword = html.find_all("h6")
    for i in itword:
        oneword = str(i.string)
        filtered_str = filtrate.findall(oneword)
        for k in filtered_str:
            wordlist.append(k)
    wordlist = list(set(wordlist))
    wordlist = sorted(wordlist)
    for i in wordlist:
        txt.write(i)
        txt.write('\n')
    txt.close()
    print (wordlist)

    # for i in itword:
    #     word = ''
    #     oneword = str(i.string)
    #     filtered_str = filtrate.findall(oneword)
    #     lenword = len(filtered_str)
    #     if lenword == 0:
    #         pass
    #     elif lenword == 1:
    #         print (filtered_str[0])
    #         txt.write(filtered_str[0])
    #         txt.write('\n')
    #     else:
    #         for i in range(lenword):
    #             word = word + ' ' + filtered_str[i]
    #             word.strip()
    #         print (word.strip())
    #         txt.write(word.strip())
    #         txt.write('\n')
    #
    # txt.close()

if __name__ == "__main__":

    # url = "http://www.cnblogs.com/anni-qianqian/p/5618693.html"
    url = 'https://blog.csdn.net/c_z_w/article/details/72953493'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }

    get2(url,headers)