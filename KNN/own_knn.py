from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from collections import Counter
import pandas as pd
import random
style.use('fivethirtyeight')
dataset = {'k':[[1,2],[2,3],[3,1]],'r':[[6,5],[7,7],[8,6]]}
new_features = [3,7]
def knn(data,predict,k = 3):
    if len(data)>=k:
        warnings.warn('k is less than total voting group')
    distances = []
    for group in data:
        for features in data[group]:
            euclidean_distance = np.sqrt(np.sum(np.array(features)-np.array(predict))**2)
            distances.append([euclidean_distance,group])
    vote = [i[1] for i in sorted(distances)[:k]]
    # print(Counter(vote).most_common(1))
    vote_result=Counter(vote).most_common(1)[0][0]
    return vote_result
# result = knn(dataset,new_features,k=3)
# print(result)
# [[plt.scatter(ii[0],ii[1],s=100,color=i) for ii in dataset[i]] for i in dataset]
# plt.scatter(new_features[0],new_features[1],s=100,color=result)
# plt.show()
df  = pd.read_csv('D:\Tutorial\ML\sentdex\KNN\wdbc.data')
df.drop('id',axis=1,inplace=True)
# print (df.head())
full_data = df.astype(float).values.tolist()
# print (full_data[:5])
random.shuffle(full_data)
# print(full_data[:5])

test_size = 0.2
train_set= {2:[],4:[]}
test_set = {2:[],4:[]}
train_data = full_data[:-int(test_size*len(full_data))]
test_data = full_data[-int(test_size*len(full_data)):]
for i in train_data:
    train_set[4].append(i[:-1])
for i in test_data:
    test_set[4].append(i[:-1])
    
correct = 0
total = 0
for group in test_set:
    for data in test_set[group]:
        vote = knn(train_set,data,k=5)
        if(group ==vote):
            correct +=1
        total+=1
print(correct/total)