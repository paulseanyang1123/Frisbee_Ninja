import sympy as sp # this is used to get derivertive of function
from sympy import *
import math
x=symbols('x')
y =118 + math.tan(10)/800*(x-800)**2  #The moving function of frisbee.
dy=diff(y,x)
print('The derrivtive of moving function is:','\n',dy)  # 0.00162090206864772*x - 1.29672165491817
fy1=integrate(y,(x,-1,4))  #求定积分
fy2=integrate(y,(x,-10,40))  #求定积分
print('定积分 fy1=',fy1,'\n','定积分 fy2=',round(fy2))
originalfunc=integrate((dy),x) # 求原函数
print('original function: ','\n',originalfunc)
'''
The derrivtive of moving function is: 
 0.00162090206864772*x - 1.29672165491817
定积分 fy1= 3173.73545719687 
 定积分 fy2= 30879.4516295852
original function:  
 0.000810451034323858*x**2 - 1.29672165491817*x

'''