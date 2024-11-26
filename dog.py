import pygame
from pygame.sprite import Sprite
import random
from random import choice
from setting import Settings

# k=0.07

class Dog_Liz(Sprite):
    def __init__(self,prmts,screen):
        super().__init__()  #you can also super(Dog_Liz,self).__init__() ,python 2.7
        # self.k = k
        parameters = Settings()
        prmts = parameters
        screen = pygame.display.set_mode((prmts.screen_width, prmts.screen_height))  # 设置屏幕长和宽
        self.screen = screen
        self.prmts = prmts
        l = [1, 2]
        if choice(l)==1:
            self.image = pygame.image.load('dogliz.jpg')
        else:
            self.image = pygame.image.load('liz2.jpg')
        # self.image.resize(40,50)
        self.image = pygame.transform.scale(self.image, (47, 47))
        self.rect = self.image.get_rect()   # get the rect of dog
        self.screen_rect = self.screen.get_rect()
        self.slope_x = random.randint(250, 1350)   # dog appears randomly between 250 to 1350
        print('self.slope_x ', self.slope_x)
        self.rect.x = self.slope_x
        self.rect.bottom = self.screen_rect.bottom
        print('self.rect.bottom ',self.rect.bottom)
        # self.moving_right = False
        # self.moving_left = False
        self.go_catching_frisbee = False
        self.x = self.rect.x
        self.y = self.rect.bottom    #self.rect.y
        # print('current rect position: ', self.rect)
    def update_moving(self,prmts):
            if  self.go_catching_frisbee:                      #calculate the ori-angle
                self.image.set_alpha(50)
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # self.k=k
                self.rect.bottom = self.screen_rect.bottom # very important, self.rect.bottom below has been a variable!
                # global k
                k = (mouse_y - self.rect.bottom) / (mouse_x - self.slope_x)  # self.rect.x   计算斜率
                # print('self.rect.bottom  ', self.rect.bottom)
                # print('self.slope_x  ', self.slope_x)
                # print('slope_rate in class dog: ', k)

                if k <0:
                    self.x += 1
                    self.y = k * self.x - k * self.slope_x + self.rect.bottom
                    # self.location = (self.x, self.y)

                    self.rect.topleft = (int(self.x), int(self.y)) # self.rect.x = self.rect.y =  also works the same.
                    # print('current dog moving rect position: ', self.rect)  # return the position of dog rect
                    # print((self.x, self.y))
                    # print(self.rect.topleft)

                else:
                    self.x -= 1
                    self.y = k * self.x - k * self.slope_x + self.rect.bottom

                    # self.location = (self.x, self.y)
                    # self.rect.topleft = (int(self.x), int(self.y))  #self.location
                    self.rect.topleft = (int(self.x), int(self.y))
                    # print('current dog moving rect position: ', self.rect)
                    # print((self.x, self.y))
                    # print(self.rect.topleft)


                if self.x >= 1553 or self.x <= 0 or self.y <= 0:
                   self.go_catching_frisbee = False

                # return k


    def drawme(self):
        # self.screen.blit(self.image, (self.x, self.y))
        self.screen.blit(self.image, self.rect)