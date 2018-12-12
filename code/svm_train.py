
'''
to train the svm model
'''
import json
import math
from sklearn.externals import joblib
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import classification_report


#load the json data:include the lables,features,dfs,if flag=1,also load the trainning dic_sentences
def load_jsons(flag=1):
    with open("./data/train_json/features.json", "rb") as f1:
        readfeatures = f1.read()
        features = json.loads(readfeatures)
    with open("./data/train_json/dfs.json", "rb") as f1:
            readdfs = f1.read()
            dfs = json.loads(readdfs)
    if flag == 0:
        return (features,dfs)
    elif flag==1:
        with open("./data/train_json/sentences.json","rb") as f1:
            readdic_entences = f1.read()
            dic_sentences = json.loads(readdic_entences)
        with open("./data/train_json/labels.json", "rb") as f1:
            readlabels = f1.read()
            labels = json.loads(readlabels)
        return (dic_sentences,labels,features,dfs)


#make the dic_sentences mapping to the TF-IDF matrix,which is the true train_data_features
def make_train_test(dic_sentences,features,dfs,features_counts):
    x_train_test=[]
    total_count=len(dic_sentences)
    for words in dic_sentences:
        tf_idf_list=[0.0 for _ in range(features_counts) ]
        for word in words:
            try:
                index=features.index(word)
            except:
                continue
            else:
                df=dfs[index]
                tf=words[word]
                idf=math.log(total_count/df+1,10)
                tf_idf=tf*idf
                tf_idf_list[index]=tf_idf
        x_train_test.append(tf_idf_list)
    return x_train_test

#svm to class and predit
def SVM():
    dic_sentences,labels,features,dfs=load_jsons()
    labels=change_labels(labels)
    features_counts=750
    features=features[0:features_counts]
    #x_train, x_test, y_train, y_test=make_train_test(dic_sentences,labels,features,dfs,features_counts)
    x_train, x_test, y_train, y_test = train_test_split(make_train_test(dic_sentences,features,dfs,features_counts), labels, test_size=0.2, random_state=0)
    clf=svm.SVC(kernel='rbf',random_state=0,decision_function_shape="ovr",gamma=0.003,C=5)
    clf.fit(x_train,y_train)
    y_pred = clf.predict(x_test)
    print(classification_report(y_test, y_pred))
    joblib.dump(clf, "train_model.m")


#first we think we should divide four classes,howerver,the train data of label 3 is too little,so we make it to label 2
def change_labels(labels):
    for i in range(len(labels)):
        if labels[i]==3 or labels[i]==43:
            labels[i]=2
    return labels



#SVM()
