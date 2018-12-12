#coding:utf-8
#author:GuoYongyan
import pymysql
import math


MYSQL_HOST = "localhost"
MYSQL_DBNAME = "hacker"
MYSQL_USER = 'root'
MYSQL_PASSWD = '123456'

area_sum = 4
text_sum = 14787
area_list = [1,2,3,4]
area_num = [941,6267,861,6715]
pt = [0.06363697842699668,0.4238182187056198,0.058226820856157435,0.45654967200919727]
ent = 0.0

def calc_ent():    #计算信息熵
    global ent
    for item in pt:
        ent += item * (math.log(item,2))
    ent = 0 - ent
    return ent


def calc_ent_grap(wid):     #计算信息增益
    connect = pymysql.connect(host=MYSQL_HOST, port=3306, db=MYSQL_DBNAME, user=MYSQL_USER, passwd=MYSQL_PASSWD,
                              charset='utf8', use_unicode=True)
    cursor = connect.cursor()
    count = 0
    try:
        cursor.execute("SELECT * from hack_df where id = %s",wid)
        df = cursor.fetchone()
        #print(df)
        pt = df[2]/text_sum     #P(t)
        pt_ = 1-pt              #P(t-1)
        # print(pt)
        # print(pt_)
        ct = 0.0
        ct_ = 0.0
        for i in range(area_sum):
            temp = (df[i + 3] / df[2])
            if (temp == 0):
                ct += 0
            else:
                ct += temp * (math.log(temp, 2))
            temp_ = ((area_num[i] - df[i + 3]) / (text_sum - df[2]))
            if (temp_ == 0):
                ct_ += 0
            else:
                ct_ += temp_ * (math.log(temp_, 2))
        # print(ct)
        # print(ct_)
        ig = ent + (pt * ct) + (pt_ * ct_)
        exec = "update hack_df set ig = %s where id = "+str(wid)
        cursor.execute(exec, ig)
        connect.commit()
        print("get id:"+str(wid)+" successful. ig="+str(ig))
    except:
        print("数据库连接失败")

calc_ent()
for i in range(17339):
    calc_ent_grap(i+1)
# calc_ent_grap(2)
