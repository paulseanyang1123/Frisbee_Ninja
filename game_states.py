#from gameboard_main import main  #this results circular import  这个导致循环引用，import.
import pygame
from setting import Settings
import game_function as gf
from dog import Dog_Liz
from frisbee import Frisbee
from pygame.sprite import Group
class GameStats():
    def __init__(self,prmts):  #,history_high_score
        #self.prameters = prameters
        #self.reset_stats()
        self.game_active = True

        #self.history_high_score =  history_high_score #
    def reset_stats(self):
        # self.ships_left = self.ai_settings.ship_limit
        #
        # self.score = 0
        # self.level = 1
        pygame.init()
        # 初始化pygame,为使用硬件做准备
        parameters = Settings()
        prmts = parameters
        screen = pygame.display.set_mode((prmts.screen_width, prmts.screen_height))  # 设置屏幕长和宽
        # screen.fill(pts.bg_color)
        pygame.display.set_caption("Frisbee_Ninja")
        dogliz = Dog_Liz(prmts, screen)
        frisbee = Frisbee(prmts, screen)
        doglizgroup = Group()
        doglizgroup.add(dogliz)
        frisbeegroup = Group()
        frisbeegroup.add(frisbee)
        gf.check_events()
        gf.check_keydown_events()
        gf.check_keyup_events()
        #main()