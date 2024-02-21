import pygame
import random
import time
from pygame.locals import *
import random


pygame.init()


s=[1,-1]
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)
black=(0,0,0)

white=(255,255,255)
width=640
height=480

screen=pygame.display.set_mode((width,height))
pygame.display.set_caption('Pong Game')
font=pygame.font.SysFont(None,25)


do=True
x=300
y=300
flag, count = 0 ,1
while do:
    #print(flag, count)
    pygame.display.update()
    screen.fill(black)
    
    if flag %2==0:
        pygame.draw.circle(screen,green, (x,y),20)
       
        
        
        
   
        

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            do=False
   
        if event.type==pygame.MOUSEBUTTONDOWN:
            x,y=event.pos
            flag += 1
            
            
            
            
