import pygame
from setting import Settings
import game_function as gf
#from dog import Dog_Liz
import dog
from frisbee import Frisbee
from pygame.sprite import Group
import numpy as np
kk=np.zeros(1)

class Slope():
    def __init__(self,prmts):  #,history_high_score
        parameters = Settings()
        prmts = parameters
        screen = pygame.display.set_mode((prmts.screen_width, prmts.screen_height))  # 设置屏幕长和宽
        dogliz = dog.Dog_Liz(prmts, screen)

        mouse_x, mouse_y = pygame.mouse.get_pos()
        print( mouse_x, mouse_y)
        self.k = (mouse_y-dogliz.rect.bottom)/(mouse_x-dogliz.rect.x)  # k is slope of the line #self.rect.x
        #self.k = (mouse_y-self.rect.bottom)/(mouse_x-self.rect.x)
        kkk = self.k      #gf.kself.k = (mouse_y-self.rect.bottom)/(mouse_x-self.rect.x)
        #

        print('kk = ', kkk)
        kk[0] = kkk
        # kkk=kk[0]
        # k = (mouse_y - self.y) / (mouse_x - self.x)    # 用这个将会出现被 0 除的现象。
        #return kk