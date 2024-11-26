'''
Accuracy:

 CFM:
 [[245  52]
 [111  99]]

 Classification report:
               precision    recall  f1-score   support

           f       0.69      0.82      0.75       297
           m       0.66      0.47      0.55       210

    accuracy                           0.68       507
   macro avg       0.67      0.65      0.65       507
weighted avg       0.67      0.68      0.67       507

'''


import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df = pd.read_csv(r'C:\Users\xuyan\OneDrive\Desktop\776-777-project\csv-file-for-777-copy.csv')
a=df.shape
print('Total rows and columns are:  ',a)
a=df.shape
print('Total rows and columns are:  ',a)
X_train=df.iloc[:,3:7]
# print('X_train',X_train)
Y_train=np.array(df.iloc[:,1])
# Y_train=df.iloc[:,3]
# print(Y_train)
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier(max_leaf_nodes = 5)  #, criterion = “entropy”
# clf.tree_.impurity # get entropy or gini of each node
clf.fit(X_train, Y_train)
prediction=clf.predict(X_train) #yhat   25
print('Predict of X_test as yhat:  ','\n', prediction)
# Answer for question 2:
from sklearn.metrics import classification_report,confusion_matrix, accuracy_score
Y_test=pd.DataFrame(Y_train, dtype=str) # 25
print('Y_test',Y_test)
# Y_test=tumortypeTest
# confusion_matrix(Y,yhat)
confusion_matrix(Y_test,prediction)
# acc_score = accuracy_score(Y, yhat) #Yh
acc_score = accuracy_score(Y_test,prediction)
print("\n", "Accuracy: ".format(format(acc_score,'.3f')))
print("\n", "CFM: \n", confusion_matrix(Y_test,prediction))
print("\n", "Classification report: \n", classification_report(Y_test,prediction))