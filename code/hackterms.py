#coding:utf-8
#author:GuoYongyan
import requests
from bs4 import BeautifulSoup
from time import *
import random
import json
import os
import re

header = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Cache-Control': 'max-age=0',
    'Connection': 'Keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'
}


words_list={}


def get_words():
	words = requests.get("http://www.hackterms.com/about/all",headers = header)
	if(words.status_code!=200):
		print("error!")
		return 0
	words.encoding = words.apparent_encoding
	soup = BeautifulSoup(words.text,'html.parser')
	#print(soup)
	for item in soup.find_all("a",attrs={'class':"all-terms-link"}):
		word_text = item.get_text().replace("\t","").replace("\n","").strip()
		word_mean = ""
		try:
			word_mean = get_meaning(word_text)
		except:
			pass
		print("[*] start getting word : " + word_text)
		words_list[str(word_text)] = str(word_mean)
	json_str = json.dumps(words_list)
	with open("hackterms.json", 'w') as json_file:
		json_file.write(json_str)


def get_meaning(word_text):
	data = requests.post("https://www.hackterms.com/get-definitions",data={"term":str(word_text),"user":False},headers = header)
	if(data.status_code!=200):
		print("error!")
		return 0
	data.encoding = data.apparent_encoding
	js = json.loads(data.text)
	mean = js["body"][0]["body"].strip()
	return mean



if __name__ == '__main__':
	get_words()

