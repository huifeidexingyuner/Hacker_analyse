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

forums = []
users = []


def index_page():
	new = {}
	index = requests.get("http://0x00sec.org/top",headers = header)
	if(index.status_code!=200):
		print("error")
	index.encoding = index.apparent_encoding
	#print(index.text)
	soup = BeautifulSoup(index.text,'html.parser')
	for item in soup.find_all("div",attrs={'itemprop':"itemListElement"}):
		forum = item.find("a").get('href')
		forums.append(forum)
	print("[*] get forums success!")
	new[ctime()] = forums
	json_str = json.dumps(new)
	with open("formus.json", 'a') as json_file:
		json_file.write(json_str)
	#print(forums)


def get_forum(forum_url,forum_num,path):
	forum_data = {}
	text_data = []
	user_list = []
	forum = requests.get(forum_url,headers = header)
	if(forum.status_code!=200):
		print("error")
	forum.encoding = forum.apparent_encoding
	soup = BeautifulSoup(forum.text,'html.parser')
	forum_data["title"] = soup.find("title").get_text()
	print("[*] start getting forum : "+forum_data["title"])
	for user in soup.find_all("div",attrs={'class':"creator"}):
		user_url = user.find("span").find("a").get('href')
		user_url = "http://0x00sec.org"+user_url
		user_list.append(user_url)
		users.append(user_url)
	forum_data["users"] = user_list	
	for text in soup.find_all("div",attrs={"itemtype":"http://schema.org/DiscussionForumPosting"}):
		speak_item = {}
		author = text.find("div",attrs={'class':"creator"}).find("span").find("a").find("b").get_text()
		speak = text.find("div",attrs={"itemprop":"articleBody"})
		speak_data = ""
		for i in speak.contents:
			try:
				speak_data=speak_data+i.get_text()
			except:
				pass
		speak_data = speak_data.replace("\t","").replace("\n","").strip()
		speak_item["author"] = author
		speak_item["speak"] = speak_data
		text_data.append(speak_item)
	forum_data["data"]=text_data
	json_str = json.dumps(forum_data)
	name = "forum_"+str(forum_num)+".json"
	with open(path+name, 'w') as json_file:
		json_file.write(json_str)

	# path = path +"user\\"
	# user_list = list(set(user_list))
	# for u in user_list:
	# 	sleep(random.random())
	# 	try:
	# 		get_user(u,path)
	# 	except:
	# 		pass
	# get_user(user_list[0],path)



def get_user(user_url,path):
	#http://0x00sec.org/user_actions.json?offset=90&username=zsec
	#date = requests.get("http://0x00sec.org/user_actions.json?offset=90&username=zsec",headers = header)
	user_data = {}
	list_data = []
	dr = re.compile(r'<[^>]+>',re.S)
	author = user_url.split("/")[-1]
	print("[*] start getting user : "+author)
	user_data["user"] = author
	if(author=="system"):
		return 0
	count = 0
	while(True):
		#data = requests.get("http://0x00sec.org/user_actions.json?offset="+str(count)+"&username=zsec",headers = header)
		data = requests.get("http://0x00sec.org/user_actions.json?offset="+str(count)+"&username="+str(author),headers = header)
		if(data.status_code!=200):
			print("error")
		js = json.loads(data.text)
		if(len(js["user_actions"])==0):
			break
		else:
			for item in js["user_actions"]:
				text = dr.sub('',item["excerpt"]).replace("\t","").replace("\n","").strip()
				list_data.append(text)
				# print(text)
		count=count+30
	user_data["history"] = list_data
	json_str = json.dumps(user_data)
	name = user_data["user"].strip()+".json"
	with open(path+name, 'w') as json_file:
		json_file.write(json_str)
				

if __name__ == '__main__':
	index_page()
	num=0
	os.mkdir("0x00sec_forums")
	path1 = os.getcwd()
	path1 = path1 + "\\0x00sec_forums\\"
	os.mkdir(path1+"user")
	path = os.getcwd()
	for forum in forums:
		try:
			get_forum(forum,num,path1)
			num=num+1
		except:
			pass
	users = list(set(users))
	path2 = os.getcwd()
	path2 = path2 + "\\0x00sec_forums\\user\\"
	for user in users:
		try:
			get_user(user,path2)
		except:
			pass
