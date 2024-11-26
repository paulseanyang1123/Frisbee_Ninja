'''
CFM:
 [[276  21]
 [ 92 118]]

 Classification report:
               precision    recall  f1-score   support

           f       0.75      0.93      0.83       297
           m       0.85      0.56      0.68       210

    accuracy                           0.78       507
   macro avg       0.80      0.75      0.75       507
weighted avg       0.79      0.78      0.77       507
'''


import numpy as np
import pandas as pd
from sklearn import preprocessing # sklearn 是 ML 的预测工具
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report,confusion_matrix, accuracy_score
# Answer for question 1:
df = pd.read_csv(r'C:\Users\xuyan\OneDrive\Desktop\776-777-project\csv-file-for-777-copy.csv')
a=df.shape
print('Total rows and columns are:  ',a)
X_train=df.iloc[:,3:7]
# print('X_train',X_train)
Y_train=np.array(df.iloc[:,1])
Y=Y_train
arraynewdata=np.array(X_train)  #newdata
print(arraynewdata)

arraynewdata = preprocessing.scale(arraynewdata)# 预处理 X 训练数据
# print(arraynewdata)
X=arraynewdata
from sklearn.svm import SVC
# clf=SVC(C=0.01, kernel = 'rbf',probability=True, gamma = 30) # 这个方法参数不好，精度小。
clf=SVC(C=1, kernel = 'rbf',probability=True, gamma = 3) # gamma = inverse of Sigma
# 2. What is the accuracy, Precision, and Recall for each class prediction under each
# of your above experiments?
clf.fit(X, Y)  #_CAT
yhat = clf.predict(X) # yhat = prob.
# Classes = np.argmax(yhat, axis=1)
confusion_matrix(Y,yhat)
acc_score = accuracy_score(Y, yhat) #Yh
print("\n", "Accuracy: ".format(format(acc_score,'.3f')))
print("\n", "CFM: \n", confusion_matrix(Y, yhat))
print("\n", "Classification report: \n", classification_report(Y, yhat))


# 5. Create a ROC Curve for **EACH** of the two classes.
# Compute ROC curve and ROC area for each class
from sklearn.metrics import roc_curve, roc_auc_score, precision_recall_curve, confusion_matrix, auc, accuracy_score

C = 1.0 # SVM regularization parameter
clf = SVC(kernel = 'rbf', C = C,probability=True,gamma=3)
clf.fit(X, Y)
yhat = clf.predict_proba(X) # probability
print('yhat', '\n',yhat)
y_pred = clf.predict(X) # class label

# class 0,f
fpr_0, tpr_0, _ = roc_curve(Y, yhat[:, 0], pos_label='f')
# roc_auc_0 = roc_auc_score (Y, yhat[:, 0])
roc_auc_0 = roc_auc_score (Y, yhat[:, 0])
# class 1,m
fpr_1, tpr_1, _ = roc_curve(Y, yhat[:, 1], pos_label='m')
roc_auc_1 = roc_auc_score(Y, yhat[:, 1])
# plot ROC curves
print('roc_auc_0: ', roc_auc_0)
print('roc_auc_1: ', roc_auc_1, '\n')
fig = plt.figure(1)
# plt.subplot(1,2,1)
plt.plot(fpr_0, tpr_0, marker='.', label='Class f', color='b')
# plt.subplot(1,2,2)
plt.plot(fpr_1, tpr_1, marker='.', label='Class m', color='r')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.legend()
plt.show()
