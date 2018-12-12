
'''
这是打标签的时候，将记录从英文转化为中文的脚本
'''

import pymysql
from urllib import request, parse
import json


MYSQL_HOST = "localhost"
MYSQL_DBNAME = "hacker"
MYSQL_USER = 'root'
MYSQL_PASSWD = '111111'

def translate(message):
	req_url = 'http://fanyi.youdao.com/translate'  # 创建连接接口
	# 创建要提交的数据
	Form_Date = {}
	Form_Date['i'] = message  # 要翻译的内容可以更改
	Form_Date['doctype'] = 'json'
	data = parse.urlencode(Form_Date).encode('utf-8') #数据转换
	response = request.urlopen(req_url, data) #提交数据并解析
	html = response.read().decode('utf-8')  #服务器返回结果读取

	# 可以看出html是一个json格式
	translate_results = json.loads(html)  #以json格式载入
	res=""
	for i in translate_results['translateResult'][0]:
		res = res+i["tgt"]
	return res

def flag():
	connect = pymysql.connect(host=MYSQL_HOST,port=3306,db=MYSQL_DBNAME,user=MYSQL_USER,passwd=MYSQL_PASSWD,charset='utf8',use_unicode=True)
	cursor = connect.cursor()
	for message_id in range(7157,7395):
		try:
			cursor.execute("select record from hack_record where message_id = %s", str(message_id))
			message = cursor.fetchone()
			message = str(message[0])
			print(translate(message))
			m_flag = str(input("自己判断:"))
			sql = "update hack_record set flag="+str(m_flag)+" where message_id="+str(message_id)
			cursor.execute(sql)
			connect.commit()
		except:
			pass


if __name__ == '__main__':
	#translate("Welcome Back to Knowing Null!This week, you voted to bring in ricksanchez! Let’s just jump right into it.First, I’d like to thank you for joining this series of course, anytime  If people really feel the urge to get toknow more about me this is the perfect chance! Can you tell me and the read&hellip;")
	flag()
