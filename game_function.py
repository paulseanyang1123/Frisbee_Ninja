'''

make use of collide_rect(class_a,class_b)

'''

import time
import sys
from frisbee import *
import frisbee
from frisbee import Frisbee
from csv import writer
import math
import dog
from dog import Dog_Liz
from dog import *
from setting import Settings
import sympy as sp # this is used to get derivertive of function
from sympy import *
player = input('Please enter the name of the player: ')
gender = input('Please enter the gender of the player: ')
# velocity_option=input('velocity_option=') #= 0.5 #choice([0.1,0.7,0.5,0.3,0.85,1])
# velocity_option=float(velocity_option)
velocity_option=frisbee.velocity_option  # this step is very import!! gf can not direct import velocity_option from frisbee.  函数能引进，参数不能引进,要重新定义。
exp_time=time.ctime()  # 实验开始时间

parameters = Settings()
prmts = parameters
screen = pygame.display.set_mode((prmts.screen_width, prmts.screen_height)) # 设置屏幕长和宽


def check_keydown_events(event,dogliz,frisbee):
    if event.key == pygame.K_q or event.key == pygame.K_w:  # press Q or W to quit
        # 接收到退出事件后退出程序
        sys.exit()
    elif event.key == pygame.K_RIGHT:  # self.moving_right = False#self.moving_left = False
        dogliz.moving_right = True  # 我犯错这里， 用==
        #dogliz.rect.centerx += 1  # 有这一句也可以运行。但不知道速度是否加倍。
    elif event.key == pygame.K_LEFT:
        dogliz.moving_left = True
        #dogliz.rect.centerx -= 1  # 有这一句也可以运行。但不知道速度是否加倍。
    elif event.key == pygame.K_SPACE:
        frisbee.moving_frisbee = True
        frisbee.t_frisbee_moving = time.time()  # frisbee.t_frisbee_moving   and t_frisbee_moving  quite different!!!!
        print('Frisbee start moving time:', '\n', frisbee.t_frisbee_moving)

def check_keyup_events(event,dogliz,frisbee):
    if event.key == pygame.K_RIGHT:
        dogliz.moving_right = False  #True
    elif event.key == pygame.K_LEFT:
        dogliz.moving_left = False  #True
    elif event.key == pygame.K_SPACE:
        frisbee.moving_frisbee = True  #我希望 frisbee 一直动， 所以即使松开空格键， 也是TRUE。

def check_events(prmts, screen,dogliz,frisbee):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, dogliz,frisbee)  # 重建

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, dogliz,frisbee)

        elif event.type == pygame.MOUSEBUTTONDOWN:   #calculate the ori-angle
            dogliz.go_catching_frisbee = True
            dogliz.t_dogliz_moving = time.time()    # get cpu time.
            print('Dogliz start moving time:', '\n', dogliz.t_dogliz_moving)
            dogliz.decision_making_time = dogliz.t_dogliz_moving-frisbee.t_frisbee_moving
            print('Decision_making_time:', '\n', dogliz.decision_making_time)
            mouse_x, mouse_y = pygame.mouse.get_pos()
            dogliz.rect.bottom = dogliz.screen_rect.bottom  # very important, self.rect.bottom below has been a variable!
            global k
            k = (mouse_y - dogliz.rect.bottom) / (mouse_x - dogliz.slope_x)  # self.rect.x   计算斜率
            print('slope_rate in game function: ', k)  #Thanks God so much!!! Finally I set K here.
            t=dogliz.decision_making_time
            global orientation_angle
            if k>0:  # frisbee go down,dog go left
                if velocity_option==0.1:
                    slope_rate_frisbee=2*0.6483608/800*t/27.4833*1600 - 2*0.6483608 # this is the manually calculated function
                    #The derrivtive of moving function is: 0.00162090206864772*x - 1.29672165491817 by sympy
                else: slope_rate_frisbee=2*0.6483608/800*t/6.3911*1600 - 2*0.6483608
                print('slope_rate_frisbee:',slope_rate_frisbee)
                print(math.atan(-slope_rate_frisbee)/3.1415926*180,'\n')
                print(math.atan(-k)/3.1415926*180+180, '\n')
                orientation_angle=math.atan(-k)/3.1415926*180+180-math.atan(-slope_rate_frisbee)/3.1415926*180
                print('orientation_angle between frisbee and dog:', round(orientation_angle,1))
            else:  #frisbee go up  k<0, dog go right
                if velocity_option==0.1:
                    slope_rate_frisbee=2*0.6483608/800*t/27.4833*1600 - 2*0.6483608
                else: slope_rate_frisbee=2*0.6483608/800*t/6.3911*1600 - 2*0.6483608
                print('slope_rate_frisbee:',slope_rate_frisbee)
                print(math.atan(-k)/3.1415926*180, '\n')
                print(math.atan(-slope_rate_frisbee)/3.1415926*180+180, '\n')
                orientation_angle=math.atan(-slope_rate_frisbee)/3.1415926*180+180 -math.atan(-k)/3.1415926*180
                print('orientation_angle between frisbee and dog:',round(orientation_angle,1))

def frisbee_catched(prmts,screen,dogliz,frisbee):
   dogliz.update_moving(prmts)
   frisbee.frisbee_moving_update(velocity_option)
   Liz_catch = pygame.sprite.collide_rect(frisbee,dogliz)
   if Liz_catch:
      print('Frisbee Hit!')
      # j +=1
      frisbee.moving_frisbee = False
      dogliz.go_catching_frisbee = False
      list_parameter = [player, gender,exp_time, dogliz.decision_making_time,velocity_option,orientation_angle,dogliz.slope_x] #如何写入参数到CSV文件
      with open(r'C:\Users\xuyan\Desktop\776-777-project\csv-file-for-777.csv', 'a', # ‘a’ 表明是附加模式，原文件不被覆盖
                newline='') as f_target:

          writer_object = writer(f_target)
          writer_object.writerow(list_parameter)  # this is the key step #####  关键的步骤
          f_target.close()


      sleep(2)
      restart()
   elif dogliz.x >= 1553 or dogliz.x <= 0 or dogliz.y <= 0 or frisbee.x >=1600:  # find a bug, frisbee.x >=1600 is not written before.
       dogliz.go_catching_frisbee = False
       print('Liz missed frisbee this time!')
       sleep(2)
       restart()  #重新开始
def restart():
      pygame.init()
      # 初始化pygame,为使用硬件做准备
      parameters = Settings()
      prmts = parameters
      screen = pygame.display.set_mode((prmts.screen_width, prmts.screen_height))  # 设置屏幕长和宽
      # screen.fill(pts.bg_color)
      pygame.display.set_caption("Frisbee_Ninja")
      dogliz = Dog_Liz(prmts, screen)
      frisbee = Frisbee(prmts, screen)

      while True:
          check_events(prmts, screen, dogliz, frisbee)
          frisbee_catched(prmts, screen, dogliz, frisbee)
          update_screen(prmts, screen, dogliz, frisbee)


def update_screen(prmts, screen,dogliz,frisbee ):

    screen.fill(prmts.bg_color)
    dogliz.drawme()
    frisbee.blitme_frisbee()
    pygame.display.update()


