import  pygame, sys 
from pygame.locals import *

import time
import Text

pygame.init()

#Display Variables
WIDTH = 1280
HEIGHT = 800
TITLE = "The Adventures of Filipino Man!"
display = pygame.display.set_mode((int(WIDTH),int(HEIGHT)))
pygame.display.set_caption(TITLE)
bg = pygame.image.load("TitleScreen.png")
fpsClock = pygame.time.Clock()

#sprite variables
fManL = pygame.image.load("fmL.png") #filiman left sprite
fManR = pygame.image.load("fmR.png") #filiman right sprite
fManB = pygame.image.load("fmB.png") #filiman back sprite
fManNL = pygame.image.load("fmNL.png") #filiman left sprite
fManNR = pygame.image.load("fmNR.png") #filiman right sprite
fManNB = pygame.image.load("fmNB.png") #filiman back sprite


x = 640
y = 400
movspeedx = 0
movspeedy = 0


left = False
right = False
back = False
nakedEasterEgg = False

#INTRO slide1
while True:
    
    if x > 1280: #exit intro when codypus is off screen
        x = 1280
    if y > 800:
        y = 800
    if x < 0:
        x = 0
    if y < 0:
        y = 0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                movspeedx = -5
                left = True
                right = False
                back = False
            if event.key == pygame.K_d:
                movspeedx = 5
                left = False
                right = True
                back = False
            if event.key == pygame.K_w:
                movspeedy = -5
                left = False
                right = False
                back = True
            if event.key == pygame.K_s:
                movspeedy = 5
                left = True
                right = False
                back = False
                
            if event.key == pygame.K_n: #naked easter egg
                nakedEasterEgg = True
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                movspeedx = 0
            if event.key == pygame.K_d:
                movspeedx = 0
            if event.key == pygame.K_w:
                movspeedy = 0
            if event.key == pygame.K_s:
                movspeedy = 0

    
    display.blit(bg, (0,0))
    
    x += movspeedx
    y += movspeedy
    
    if nakedEasterEgg == False:
        if left:
            display.blit(fManL, (x, y))
        if right:
            display.blit(fManR, (x, y))
        if back:
            display.blit(fManB, (x, y))
    else: 
        if left:
            display.blit(fManNL, (x, y))
        if right:
            display.blit(fManNR, (x, y))
        if back:
            display.blit(fManNB, (x, y))
        


    fpsClock.tick(30)
    
    pygame.display.update()
    