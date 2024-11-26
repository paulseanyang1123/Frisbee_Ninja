import time

import pygame
from  pygame.sprite import Sprite
from random import choice
import random
from time import sleep
from pygame import Rect
# import game_function as gf     # this is circular import ,errror
import math
velocity_option=input('velocity_option=') #= 0.5 #choice([0.1,0.7,0.5,0.3,0.85,1])
velocity_option=float(velocity_option)
# v = [1, 2]
# if choice(v) == 1:
#     velocity_option = 0.1
# else:
#     velocity_option = 0.5

class Frisbee(Sprite):    #  class NeuralNetwork(nn.Module): # 神经网络被定义为类

    def __init__(self, prmts, screen):
        super().__init__()
        self.screen = screen
        self.prmts = prmts
        l = [1, 2, 3]
        if choice(l) == 1:
            self.image = pygame.image.load('frisbee1.jpg')  # .convert()
        elif choice(l) == 2:
            self.image = pygame.image.load('frisbee2.jpg')  # .convert()
        else:
            self.image = pygame.image.load('frisbee3.jpg')

        self.image = pygame.transform.scale(self.image, (47, 47))
        self.rect = self.image.get_rect()  #pygame.Rect(left, top, width, height)
        self.rect.x = 0 #random.randint(1,1350)   #10   #self.rect.width   # 40
        self.rect.y = 1000   # 1000，故意设置到屏幕以下。
        self.x = self.rect.x
        self.y = self.rect.y
        self.moving_frisbee = False
        self.location = (self.x, self.y)
        self.rect.topleft = self.location

    def frisbee_moving_update(self,velocity_option):
        if self.moving_frisbee and self.x < 1600:
            # t_frisbee_moving= time.time()
            # print('frisbee start moving time:','\n',t_frisbee_moving)
            self.x += velocity_option
            self.y =118 + math.tan(10)/800*(self.x-800)**2 # 118 is based on experience! ****
            if self.x >= 1600:
                self.moving_frisbee = False
            self.location = (self.x, self.y)
            self.rect.topleft = self.location
        # return velocity_option

    def blitme_frisbee(self):
        self.screen.blit(self.image, (self.x, self.y))
