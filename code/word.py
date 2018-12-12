import nltk
import pymysql
from nltk.book import *
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
import json
import re



def save2json(list):


    path = "//Volumes//Study//课题//代码/0x00sec_forums//user_word//1.json"

    with open(path, 'w', encoding='utf-8') as json_file:
        json.dump(list, json_file, ensure_ascii=False)

def saveflag(list):


    path = "//Volumes//Study//课题//代码/0x00sec_forums//user_word//2.json"

    with open(path, 'w', encoding='utf-8') as json_file:
        json.dump(list, json_file, ensure_ascii=False)



def nltk2word(record):

    list1 = []
    list2 = []
    dist = {}
    comma = ['!', '@', '#', '$', '%', '^', '*', '-', '+', '=', '[', ']', '?', '.', ',', ':', '(', ')', ';', "'", '\\',
             "\'", 'I', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'O'
        , 'if', 'A', 'it', 'would', 'The', 'This', 'like', 'it', 'one', 'time', 'know', 'in', 'lot', 'so', 'we', 'well']
    with open("stopword.txt", "rb") as f:
        stopword = f.readlines()
    for stop in stopword:
        vl = stop.strip()
        comma.append(vl)
    comma = list(set(comma))
    pattern = r"""(?x)                   # set flag to allow verbose regexps 
    	              (?:[A-Z]\.)+           # abbreviations, e.g. U.S.A. 
    	              |\d+(?:\.\d+)?%?       # numbers, incl. currency and percentages 
    	              |\w+(?:[-']\w+)*       # words w/ optional internal hyphens/apostrophe 
    	              |\.\.\.                # ellipsis 
    	              |(?:[.,;"'?():-_`])    # special characters with meanings 
    	            """

    word = nltk.regexp_tokenize(record, pattern)
    stopworddic = set(stopwords.words('english'))
    snowball_stemmer = SnowballStemmer("english")
    wordnet_lemmatizer = WordNetLemmatizer()
    for i in word:
        if i not in stopworddic:
            list1.append(i)
    for i in list1:
        i = snowball_stemmer.stem(i)
        i = wordnet_lemmatizer.lemmatize(i)
        if i not in comma:
            list2.append(i)
    resetlist = list(set(list2))
    for value in resetlist:
        dist[value] = list2.count(value)
    return dist


def connect_db():

    word = []
    flaglist = []
    db = pymysql.connect("127.0.0.1", "root", "1011", "hacker", use_unicode=True, charset="utf8")  # 连接数据库
    cursor = db.cursor()

    sql1 = "select record from hack_record where message_id=%d"   #查询数据
    sql2 = "select flag from hack_record where message_id=%d"
    # sql2 = 'insert into hack_df()'    #插入数据
    #update hack_record set core = "1234" where message_id=1

    for i in range(14787):
        i += 1
        cursor.execute(sql1 % i)
        results = cursor.fetchall()
        for j in results:
            # print(j[0])
            record = j[0]
        core = nltk2word(record)        #进行分词
        word.append(core)
        print(core)
        cursor.execute(sql2 % i)
        flag = cursor.fetchall()
        for k in flag:
            fl = k[0]
        flaglist.append(fl)

    save2json(word)    #保存到json文件
    print(len(word))
    saveflag(flaglist)
    print(len(flaglist))

if __name__ == "__main__":


    connect_db()
