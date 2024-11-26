import pygame
from pygame.sprite import Sprite
from dog import Dog_Liz
from frisbee import Frisbee
from setting import Settings
parameters = Settings()
prmts = parameters
screen = pygame.display.set_mode((prmts.screen_width, prmts.screen_height)) # 设置屏幕长和宽
dogliz = Dog_Liz(prmts, screen)
frisbee = Frisbee(prmts, screen)
# spirte_1 = MySprite("sprite_1.png",200,200,1)
# sprite_2 = MySprite("sprite_2.png",50,50,1)
result = pygame.sprite.collide_rect(dogliz,frisbee)
if result:
    print ("Collision occurred")