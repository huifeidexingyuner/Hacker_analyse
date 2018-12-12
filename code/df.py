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



def nltk2word(record):

    list1 = []
    list2 = []
    comma = ['!','@','#','$','%','^','*','-','+','=','[',']','?','.',',',':','(',')',';',"'",'\\',"\'",'I','1','2','3','4','5','6','7','8','9','0','O'
             ,'if','A','it','would','The','This','like','it','one','time','know','in','lot','so','we','well']
    with open("stopword.txt","rb") as f:
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

    return list2


def connect_db():

    dist = {}
    db = pymysql.connect("127.0.0.1", "root", "1011", "hacker", use_unicode=True, charset="utf8")  # 连接数据库
    cursor = db.cursor()

    sql1 = "select record from hack_record where flag=%d"   #查询数据

    sql2 = 'insert into hack_df(word,df,df1,df2,df3,df4) values("%s",%d,%d,%d,%d,%d)'   #插入数据

    for i in range(4):
        t = i + 1
        cursor.execute(sql1 % t)
        results = cursor.fetchall()
        core = nltk2word(str(results))        #进行分词
        if t == 1:
            df1list = core
        elif t == 2:
            df2list = core
        elif t == 3:
            df3list = core
        else:
            df4list = core

    word = list(set(df1list+df2list+df3list+df4list))
    for value in word:
        df1 = df1list.count(value)
        df2 = df2list.count(value)
        df3 = df3list.count(value)
        df4 = df4list.count(value)
        df = df1 + df2 + df3 +df4
        num = [df,df1,df2,df3,df4]

        dist[value] = num

        try:
            cursor.execute(sql2 % (value,df,df1,df2,df3,df4))
            db.commit()
        except pymysql.err.InternalError:
            pass
    print(dist)
    save2json(dist)    #保存到json文件

if __name__ == "__main__":


    connect_db()