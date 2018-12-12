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


def count(filelist):

    dist = {}
    numletter = 0
    numrecord = 0
    for i in filelist:
        num = []
        f = open(i,"rb")
        readcontent = f.read()
        content = json.loads(readcontent)
        user = content['user']
        history = list(set(content['history']))
        numrecordone = len(history)
        numrecord += numrecordone
        num.append(numrecordone)
        numletterone = 0
        for k in history:
            numletterone = len(k) + numletterone
        numletter += numletterone
        num.append(numletterone)
        dist[user] = num

    return numrecord,numletter

def get_active(listpath):
    numrecord = 15566
    numletter = 3118639



    f = open(listpath, "rb")
    readcontent = f.read()
    content = json.loads(readcontent)
    history = list(set(content['history']))
    numrecordone = len(history)
    numletterone = 0
    for k in history:
        numletterone = len(k) + numletterone
    score1 = (numrecordone/numrecord)*100
    score2 = (numletterone/numletter)*100
    score = score1+score2
    print("2.黑客的活跃度分析")
    if(score > 0.75453329482544):
        print("**活跃")
    if(score <0.05094360318596063):
        print("**不活跃")
    if(score<=0.75453329482544 and score >=0.05094360318596063 ):
        print("**普通")
        # print(score)
    return score




