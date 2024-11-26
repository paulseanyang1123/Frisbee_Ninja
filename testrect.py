import pygame
from  pygame.sprite import Sprite
from time import sleep
pygame.init()
screen = pygame.display.set_mode((1500,700))
pygame.display.set_caption('c语言中文网')
image_surface = pygame.image.load('frisbee1.jpg')
print(image_surface.get_size())  #(465, 369)
image_resize = pygame.transform.scale(image_surface, (47, 47))
rect1 = pygame.Rect(65,69,400,300)
rect0 = pygame.Rect(0,0,47,47)
# 在原图的基础上创建一个新的子图（surface对象）
image_child= image_surface.subsurface(rect1)
image_child2= image_resize.subsurface(rect0)
rect2 = image_child.get_rect()
#输出的矩形大小为 100*100
print(rect2)
# rect1 = rect1.move((65,69))
rect1 = rect1.move((0,0))
# rect1 = image_child.get_rect()
# print(rect1)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    #在屏幕上显示子图的区域
    # for i in range(1,365,50):
    #      screen.blit(image_child,pygame.Rect(i,360,100,100))
    #      sleep(1)
    #      pygame.display.update()

    screen.blit(image_child2, rect0)
    screen.blit(image_child,rect1)
    screen.blit(image_child, (500,300))

    screen.blit(image_child2, (800, 600))
    screen.blit(image_surface,(1000,200))
    #Liz_catch = pygame.sprite.collide_rect(rect2, rect1)
    # Liz_catch = pygame.sprite.collide_rect(image_child, image_child2)
    # print(Liz_catch)
    # screen.blit(image_child, pygame.Rect(65,69,400,300))
    #      sleep(1)
    pygame.display.update()