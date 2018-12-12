# -*- coding: utf-8 -*-  
import os
import json
import pymysql
import sys

#   获取当前路径下的所有json文件
def listdir(path, list_name):  # 传入存储的list
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            listdir(file_path, list_name)
        else:
            list_name.append(file_path)

        #print(file_path)
    return list_name

#   读取json文件写入到sql数据库中
def readjson(list_name):

    db = pymysql.connect("127.0.0.1","root","1011","hacker",use_unicode=True, charset="utf8")   #   连接数据库
    cursor = db.cursor()
    sql1 = "INSERT INTO hack_user(username)\
             VALUES ('%s')"
    sql2 = "INSERT INTO hack_record(record)\
                 VALUES ('%s')"
    count = 0
    row = 0
    for i in list_name:
        print(i)
        f = open(i,"rb")
        readcontent = f.read()
        content = json.loads(readcontent)
        user = content['user']
        print(user)
        cursor.execute(sql1 % (user))
        history = list(set(content['history']))
        for x in range(len(history)):
            print(history[x])
            row += 1
            try:
                if(history[x] != ''):
                    cursor.execute(sql2 %(history[x]))
            except pymysql.err.ProgrammingError:
                pass
        count = count + 1
    print(count)
    print(row)



if __name__ == '__main__':

    filename_list = []
    path = "//Volumes//Study//课题//代码/0x00sec_forums//user//"
    filelist = listdir(path,filename_list)
    print(filelist)
    # readjson(filelist)