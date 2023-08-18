import pandas as pd
import quandl,math
import numpy as np
from sklearn.model_selection import cross_validation
from sklearn import preprocessing
from sklearn.linear_model import LinearRegressoion
df = quandl.get('WIKI/GOOGL')
df = df[['Adj. Open','Adj. High','Adj. Low']]
df['HL'] =(df['Adj. High']-df['Adj. Low'])

df  = df[["Adj. High",'HL']]

forcase_col = 'Adj. High'
forcast_out = int(math.ceil(0.1*len(df)))
df['label'] = df[forcase_col].shift(-forcast_out)
df.dropna(inplace=True)
# print (df.head())

# p4

x = np.array(df.drop(['label'],1))
y = np.array(df['label'])
x=  preprocessing.scale(x)
x = x[:-forcast_out+1]
X_train,X_test,Y_train,Y_test = cross_validation.train_test_split(x,y,test_size=0.2)
clf = LinearRegressoion()
clf.fit(X_train,Y_train)
accuracy = clf.score(X_test,Y_test)
print(accuracy)

