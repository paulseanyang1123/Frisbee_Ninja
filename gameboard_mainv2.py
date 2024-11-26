'''
main function including setting,dog,frisbee, gamfunction,gamboard_main2
key is make rect movable rect.x = x,rect.y  = y,
splope k calculation, make sure you use constance not variable

24/12/2021

这是正式版本！！！！
'''

# __author__ (xu yang)
import sys
import pygame
from setting import Settings
from  pygame.sprite import Sprite
import game_function as gf
from dog import Dog_Liz
from frisbee import Frisbee
from time import sleep
from pygame.sprite import Group
import pandas as pd
# import xlsxwriter as xw
def main():
    pygame.init()
    # 初始化pygame,为使用硬件做准备
    parameters = Settings()
    prmts = parameters
    screen = pygame.display.set_mode((prmts.screen_width, prmts.screen_height)) # 设置屏幕长和宽
    #screen.fill(pts.bg_color)
    pygame.display.set_caption("Frisbee_Ninja")
    dogliz = Dog_Liz(prmts,screen)
    frisbee = Frisbee(prmts,screen)

    while True:
        gf.check_events(prmts, screen,dogliz,frisbee)
        # 下面的4行可有可无。因为frisbee_catched已经写过了。不然一定要写。
        # dogliz.update_moving(prmts)
        # frisbee.frisbee_moving_update(frisbee.velocity_option)
        # event = pygame.event.get()
        # gf.check_keydown_events(event,dogliz,frisbee)
        gf.frisbee_catched(prmts,screen,dogliz, frisbee)
        gf.update_screen(prmts, screen,dogliz,frisbee)

main()
