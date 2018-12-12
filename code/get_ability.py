#coding:utf-8
#author:GuoYongyan

import pymysql


MYSQL_HOST = "localhost"
MYSQL_DBNAME = "hacker"
MYSQL_USER = 'root'
MYSQL_PASSWD = '111111'


def get_ability(score1,score2):
	connect = pymysql.connect(host=MYSQL_HOST, port=3306, db=MYSQL_DBNAME, user=MYSQL_USER, passwd=MYSQL_PASSWD,
                              charset='utf8', use_unicode=True)
	cursor = connect.cursor()
	cursor.execute("SELECT score,act_score FROM hack_user")
	data = cursor.fetchall()
	similar = 0
	for i in range(len(data)):
		temp = (data[i][0]-score1)*(data[i][0]-score1)+(data[i][1]-score2)*(data[i][1]-score2)
		if(i==0):
			similar=temp
			user=1
		if(temp<similar):
			#print("1111")
			similar = temp
			user = i+1
	cursor.execute("SELECT flag FROM hack_user WHERE user_id=%s",user)
	result = cursor.fetchone()
	print("4.黑客能力分析")
	if result[0]==1:
		print("**他是资深黑客")
	elif result[0]==0:
		print("**他是小白黑客")



#get_ability(22.076,22.076)

