from random import random

import pandas as pd
from csv import writer
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import kstest, describe
from scipy.stats import normaltest
from numpy.random import poisson
# from matplotlib.pyplot import hold
df = pd.read_csv(r'C:\Users\xuyan\OneDrive\Desktop\776-777-project\csv-file-for-777-copy.csv')
vo=df.velocity_option
n=len(vo)
list_decision_time=[]
list_ori_angle=[]
list_dog_inti_position=[]
list_decision_time1=[]
list_ori_angle1=[]
list_dog_inti_position1=[]
print('velocity_option',vo[int(507*random())])
for i in range(n):
    if vo[i]==0.1:
        list_decision_time.append(df.Decision_making_time[i])
        list_ori_angle.append(df.Ori_angle[i])
        list_dog_inti_position.append(df.dog_inti_x[i])
    else:
        list_decision_time1.append(df.Decision_making_time[i])
        list_ori_angle1.append(df.Ori_angle[i])
        list_dog_inti_position1.append(df.dog_inti_x[i])
# print(df.iloc[:,2:3]) # this command is used to show the certain columns: iloc
# print(df.iloc[0:3,:])# this command is used to show the certain rows: iloc
#
# tdaveragetesttotal = df.STATISTICSIE
# averagescore=np.average(tdaveragetesttotal)
#
# fig = plt.figure(1)
plt.subplot(2,3,1)
plt.hist(list_decision_time)

plt.xlabel('Decision making time')
plt.ylabel('Frequency of decision making time')
plt.title('The frequency of decision making time', fontsize=12, color='green')
plt.ylim(0, 120)
plt.xlim(0, 20)
# legend = plt.legend([tdaveragetesttotal, p2], ["CH", "US"], facecolor='blue')
plt.legend(["Frequency"], title='Frequency of decision making time/v=0.1',loc='best',facecolor='red',fontsize=8)  # empty is also ok

plt.subplot(2,3,2)
plt.hist(list_ori_angle)

plt.xlabel('Decision making orientation angle')
plt.ylabel('Frequency of decision making orientation angle')
plt.title('The frequency of decision making orientation angle', fontsize=12, color='blue')
plt.ylim(0, 60)
plt.xlim(45, 130)
# legend = plt.legend([tdaveragetesttotal, p2], ["CH", "US"], facecolor='blue')
plt.legend(["Frequency"], title='Frequency of decision making orientation angle/v=0.1',loc='best',facecolor='red',fontsize=8)  # empty is also ok

plt.subplot(2,3,3)
plt.hist(list_dog_inti_position)

plt.xlabel('Decision making dog_inti_position')
plt.ylabel('Frequency of decision making dog_inti_position')
plt.title('The frequency of decision making dog_inti_position', fontsize=12, color='orange')
plt.ylim(0, 60)
plt.xlim(200, 1400)
# legend = plt.legend([tdaveragetesttotal, p2], ["CH", "US"], facecolor='blue')
plt.legend(["Frequency"], title='Frequency of decision making dog_inti_position/v=0.1',loc='best',facecolor='red',fontsize=8)  # empty is also ok

plt.subplot(2,3,4)
plt.hist(list_decision_time1)

plt.xlabel('Decision making time')
plt.ylabel('Frequency of decision making time')
plt.title('The frequency of decision making time', fontsize=12, color='green')
plt.ylim(0, 80)
plt.xlim(0, 8)
# legend = plt.legend([tdaveragetesttotal, p2], ["CH", "US"], facecolor='blue')
plt.legend(["Frequency"], title='Frequency of decision making time/v=0.5',loc='best',facecolor='red',fontsize=8)  # empty is also ok

plt.subplot(2,3,5)
plt.hist(list_ori_angle1)

plt.xlabel('Decision making orientation angle')
plt.ylabel('Frequency of decision making orientation angle')
plt.title('The frequency of decision making orientation angle', fontsize=12, color='blue')
plt.ylim(0, 120)
plt.xlim(20, 180)
# legend = plt.legend([tdaveragetesttotal, p2], ["CH", "US"], facecolor='blue')
plt.legend(["Frequency"], title='Frequency of decision making orientation angle/v=0.5',loc='best',facecolor='red',fontsize=8)  # empty is also ok

plt.subplot(2,3,6)
plt.hist(list_dog_inti_position1)

plt.xlabel('Decision making dog_inti_position')
plt.ylabel('Frequency of decision making dog_inti_position')
plt.title('The frequency of decision making dog_inti_position', fontsize=12, color='orange')
plt.ylim(0, 60)
plt.xlim(200, 1400)
# legend = plt.legend([tdaveragetesttotal, p2], ["CH", "US"], facecolor='blue')
plt.legend(["Frequency"], title='Frequency of decision making dog_inti_position/v=0.5',loc='best',facecolor='red',fontsize=8)  # empty is also ok

plt.show()