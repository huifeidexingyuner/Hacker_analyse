源代码和数据集全在code文件夹下，进入code文件夹前须知：

1. 需要额外安装的库文件
requests库，BeautifulSoup 库，scrapy库，nltk库，pymysql库,skleaarn库，flashtext库
2. 文件结构
(1) data文件夹存放着实验中所用到的数据。其中，forums文件夹存放论坛50个帖子的json数据，user文件夹存放论坛130个黑客近期说过的话的json数据，
train_json里面存放着训练SVM模型所要用到的4个json文件，hackterms.json存放着爬取下来的黑客术语集，hack.sql则存放着实验过程中用到的所有表
(2) x0xxsec.py是爬取0x00sec网站的爬虫
(3) flag.py 是打标签用的文件
(4) generate_actions_score是临时文件，可以忽略
(5) get_ability是通过类似于KNN的相似度分析，得到黑客能力的文件
(6) get_actions是通过已经训练好的SVM模型，预测黑客行为的文件
(7) get_area 是通过flashtext库，通过术语集匹配黑客研究领域
(8) get_active.py 是实现黑客活跃度的文件
(9) hackterms.py是爬取黑客术语集的文件
(10) info_gain.py是实现信息增益的文件
(11) svm_train.py是训练svm模型的文件
(12) test.py 如其名，测试文件，无用
(13) df.py,计算df的文件
(14) json2sql.py 临时处理文件，现在无用
(15) word.py,分词去停词文件
(16) main.py,主函数文件，集合了其他文件，可打印黑客画像

3. train_modle.m是已经训练好的svm模型
4. 数据库名为hacker,用户为root,密码111111