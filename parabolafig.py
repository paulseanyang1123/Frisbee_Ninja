import pandas as pd
from csv import writer
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import kstest, describe
from scipy.stats import normaltest

x=np.linspace(0,1600,10000)
y=118-0.6484/800*(x-800)**2
fig=plt.figure()
plt.ylim(-200, 200)
plt.xlim(400, 1200)
plt.plot(x,y)
plt.axhline(y=-50,ls="-.",c="red")#添加水平直线
plt.title('Decision making task trajectory for frisbee and dog', fontsize=22, color='r')
plt.legend(["Frisbee trajectory"], loc='best',facecolor='g',fontsize=16) # title='Decision making task for frisbee and dog',
plt.show()