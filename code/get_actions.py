'''
to create the interface of make the actions of the new user_json
'''

from svm_train import *
import nltk
import json
from sklearn.externals import joblib


'''
the data format:
string_sentences:[string1,string2,...]
dic_sentences:[{word1:count1,word2:count2,...},{...},...]
words:{word1:count1,word2：count2，...}
'''

# load a user json ; output:[string1,string2.....,]
def load_user_json(jsonname):
    with open(jsonname,"rb") as f1:
        readuserdata = f1.read()
        string_sentences = list(json.loads(readuserdata)["history"])
    return string_sentences


#input:string_sentences;output:dic_sentences
def div_all(string_sentences):
    return list(map(div_onesentence, string_sentences))


#input:string    output:words,the count is the num of the word in the  input string
def div_onesentence(record):
    div_words = {}
    pattern = r"""(?x)                   # set flag to allow verbose regexps 
    	              (?:[A-Z]\.)+           # abbreviations, e.g. U.S.A. 
    	              |\d+(?:\.\d+)?%?       # numbers, incl. currency and percentages 
    	              |\w+(?:[-']\w+)*       # words w/ optional internal hyphens/apostrophe 
    	              |\.\.\.                # ellipsis 
    	              |(?:[.,;"'?():-_`])    # special characters with meanings 
    	            """

    words_list = nltk.regexp_tokenize(record, pattern)
    unique_words=set(words_list)
    for word in unique_words:
        div_words[word] = words_list.count(word)
    return div_words


#make the dic_sentences mapping to the TF-IDF matrix,which is the true train_data_features
def make_x_user(dic_sentences):
    features, dfs = load_jsons(flag=0)
    features_counts = 750
    features = features[0:features_counts]
    x_train=make_train_test(dic_sentences, features, dfs, features_counts)
    return x_train


#predict the user
def predit_user(x_user):
    scores=[0 for i in range(0,5)]
    count_labels1=[0 for i in range(0,5)]
    count_labels2={0:0,1:0,2:0}
    clf = joblib.load("train_model.m")
    y_pred=clf.predict(x_user)
    unique_y=set(y_pred)
    for y in unique_y:
        count_labels1[y]=list(y_pred).count(y)
    count_labels2[0]=count_labels1[1]
    count_labels2[1] = count_labels1[2]
    count_labels2[2] = count_labels1[4]
    scores[1]= 60*count_labels1[1]
    scores[2] =80 * count_labels1[2]
    scores[4] = 80 * count_labels1[4]
    score=(scores[1]+scores[2]+scores[4])/10000
    print_actions(count_labels2)
    return score


def print_actions(count_labels):
    print("3. 黑客行为活动分析：")
    actions={0:"传播黑客工具的活动",1:"传播攻击源代码或传播黑客教程的活动",2:"正常行为活动"}
    sorted_labels=sorted(count_labels.items(),key=lambda k:k[1],reverse=True)
    if sorted_labels[0][1]!=0 :
        #print(indexs[0])
        print("**他主要在做", actions[sorted_labels[0][0]])
    if sorted_labels[1][1] != 0:
        #print(indexs[1])
        print("**除此之外，他还做了一些",actions[sorted_labels[1][0]])
    if sorted_labels[2][1] != 0:
        #print(indexs[2])
        print("**最后，他还做了少量的",actions[sorted_labels[2][0]])

def get_actions(jsonname):
    string_sentences=load_user_json(jsonname)
    #print(len(string_sentences))
    dic_sentences=div_all(string_sentences)
    x_user=make_x_user(dic_sentences)
    return(predit_user(x_user))

#print(get_actions("C:\\Users\\孙鹏\\Desktop\\威胁情报分析\\user\\user\\Evalion.json"))
