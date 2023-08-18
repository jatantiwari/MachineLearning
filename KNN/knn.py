import numpy as np
from sklearn import preprocessing, neighbors
from sklearn.model_selection import train_test_split
import pandas as pd
df  = pd.read_csv('KNN/wdbc.data')
df.drop(['id'],axis=1,inplace = True)

x  = np.array(df.drop(['diagnosis'],axis=1))
y= np.array(df['diagnosis'])
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
clf = neighbors.KNeighborsClassifier()
clf.fit(X_train, y_train)
accuracy=  clf.score(X_test,y_test)
print (accuracy)