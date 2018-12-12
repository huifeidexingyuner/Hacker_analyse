'''
to create the scores of action scores for the train of buding hacker ability
'''

from get_actions import get_actions
import pymysql

MYSQL_HOST = "localhost"
MYSQL_DBNAME = "hacker"
MYSQL_USER = 'root'
MYSQL_PASSWD = '111111'
MYSQL_PORT=3306


def generate_actions_score():
    db= pymysql.connect(host=MYSQL_HOST, port=MYSQL_PORT, db=MYSQL_DBNAME, user=MYSQL_USER, passwd=MYSQL_PASSWD,
                              charset='utf8', use_unicode=True)
    cursor1 = db.cursor()
    cursor2 = db.cursor()
    sql="select user_id,username from hack_user "
    cursor1.execute(sql)
    results=cursor1.fetchall()
    #print(results)
    for result in results:
        user_id=result[0]
        username=result[1]
        print("the userid and name is ",user_id,username)
        jsonname = "C:\\Users\\孙鹏\\Desktop\\威胁情报分析\\user\\user\\"+username+".json"
        score = get_actions(jsonname)
        #这里的username的%s要加‘’，否则插入数据库就是x0xxfe，而不是‘0xffes'
        '''
        sql="insert into action_scores(user_id,username,action_scores) values(%s,'%s',%s)" %(user_id,username,score)
        print(sql)
        cursor1.execute(sql)
        db.commit()
        '''

generate_actions_score()
# 0x00pf Bowlslaw dtm Evalion exploit fraq fxbg Joe_schmoe Leeky Ninja243 Nitrax oaktree pryooc