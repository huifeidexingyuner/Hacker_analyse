import math
#print(math.log1p(500))
'''
list1=[1,2,3,4]
for i in range(1,10):
    try:
        a=list1.index(i)
    except ValueError:
        print("xxx")
        continue
    else:
        print(list1[a])

tf_idf_list=[0.0 for _ in range(10) ]
print(tf_idf_list)
'''
list1=[1,2,3,4]
list2=[1,2,3,4]
list1.append(list2)
print(list1)