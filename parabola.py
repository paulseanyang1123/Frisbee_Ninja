import pygame
import sys
imgx0 = 10
imgy0 = 570
imgx = imgx0
imgy = imgy0
Red = (255,0,0)
Blue = (0,0,255)
WHITE = (255,255,255)
screen = pygame.display.set_mode((1180, 570)) # 设置屏幕长和宽
i=1
direction = 'right'
image = pygame.image.load('frisbee1.jpg')
image = pygame.transform.scale(image, (47, 47))
while True:
    screen.fill(WHITE) # if no this verse, black screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    if direction == 'right':
        imgx = imgx0 + 4.6*i
        imgy = imgy0 - 4.6*i + 0.02*i**2
        if imgx >=1180:
            imgx = imgx0
            imgy = imgy0
            i=1
        if imgy >= 570:
            imgx = imgx0
            imgy = imgy0
            i=1
    i = i + 1
    screen.blit(image, (imgx,imgy))

    pygame.draw.ellipse(screen,Red,[1000,500,60,60],20)
    pygame.draw.rect(screen, Blue, [600, 290, 60, 60], 1)

    pygame.display.update()
    #fpsClock.tick(FPS)