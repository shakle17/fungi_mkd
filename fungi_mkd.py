background_image_filename = 'main_pics/funga.jpg'
deni_file = 'main_pics/deno.png'

alex_file='alex_pics/a1.png'
a1='alex_pics/a1.png'
a2='alex_pics/a2.png'
a3='alex_pics/a3.png'
a4='alex_pics/a4.png'
a5='alex_pics/a5.png'
alexx=[a1,a2,a3,a4,a5]

petre_file='petre_pics/p1.png'
p1='petre_pics/p1.png'
p2='petre_pics/p2.png'
p3='petre_pics/p3.png'
p4='petre_pics/p4.png'
p5='petre_pics/p5.png'
petree=[p1,p2,p3,p4,p5]

goka_file='goka_pics/g1.png'
g1='goka_pics/g1.png'
g2='goka_pics/g2.png'
g3='goka_pics/g3.png'
g4='goka_pics/g4.png'
g5='goka_pics/g5.png'
gokaa=[g1,g2,g3,g4,g5]

kiro_file='kiro_pics/k1.png'
k1='kiro_pics/k1.png'
k2='kiro_pics/k2.png'
k3='kiro_pics/k3.png'
k4='kiro_pics/k4.png'
k5='kiro_pics/k5.png'
kiroo=[k1,k2,k3,k4,k5]

cursor='main_pics/shroom.png'
shoot='sound/shoot.wav'

start_x=60
start_y=150


import pygame
import random
from random import randrange
from pygame.locals import *
from sys import exit
from gameobjects.vector2 import Vector2
import math
xx = 300
yy = 120
import os
import time

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (xx,yy)

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)

gun=pygame.mixer.Sound(shoot)
background = pygame.image.load(background_image_filename).convert()
background=pygame.transform.scale(background,(640,480))
speed=700
speed_color=200
speed_deni=800
deni = pygame.image.load(deni_file).convert_alpha()
deni=pygame.transform.scale(deni,(550,600))
deni_pos = Vector2(-250,-150)

alex_move=pygame.USEREVENT + 1
color_change=pygame.USEREVENT +2
deni_move=pygame.USEREVENT +3



cursor_shroom=pygame.image.load(cursor).convert_alpha()
cursor_shroom=pygame.transform.scale(cursor_shroom,(30,30))
cursor_shroom=pygame.transform.flip(cursor_shroom,1,0)
cursor_pos=Vector2(0,250)

a_x=random.randint(100,590) 
a_y=random.randint(0,430)
k_x=random.randint(100,590)
k_y=random.randint(0,430)
g_x=random.randint(100,590) 
g_y=random.randint(0,430)
p_x=random.randint(100,590)
p_y=random.randint(0,430)


pygame.mouse.set_visible(False)
pygame.event.set_grab(True)

pygame.time.set_timer(alex_move,speed)
pygame.time.set_timer(color_change,speed_color)
pygame.time.set_timer(deni_move,speed_deni)

while True:
  
  screen.blit(background, (0,0))
  for event in pygame.event.get():
   if event.type == QUIT:
     exit()
   if event.type == KEYDOWN:
     if event.key == K_ESCAPE:
       exit()
   if event.type == alex_move:
   
    alex_file=random.choice(alexx)
    kiro_file=random.choice(kiroo)
    goka_file=random.choice(gokaa)
    petre_file=random.choice(petree)
    a_x=random.randint(100,590) 
    a_y=random.randint(0,430)
    k_x=random.randint(100,590)
    k_y=random.randint(0,430)
    g_x=random.randint(100,590) 
    g_y=random.randint(0,430)
    p_x=random.randint(100,590)
    p_y=random.randint(0,430)
   
   if event.type == deni_move:
     deni_pos[0]=deni_pos[0]-1
     start_x=start_x-1  
     if deni_pos[0]==-265:  
      deni_pos[0]=deni_pos[0]+1
      start_x=start_x+1
  
   
   
  alex=pygame.image.load(alex_file).convert_alpha()
  alex=pygame.transform.scale(alex,(50,60))
  alex_pos=Vector2(220,160)
  
  kiro=pygame.image.load(kiro_file).convert_alpha()
  kiro=pygame.transform.scale(kiro,(50,50))
  kiro_pos=Vector2(300,50)

  goka=pygame.image.load(goka_file).convert_alpha()
  goka=pygame.transform.scale(goka,(50,50))
  goka_pos=Vector2(400,10)

  petre=pygame.image.load(petre_file).convert_alpha()
  petre=pygame.transform.scale(petre,(50,50))
  petre_pos=Vector2(300,250)   
  cursor_pos=pygame.mouse.get_pos()
  
  screen.blit(deni,deni_pos)
  screen.blit(alex,(a_x,a_y))
  screen.blit(kiro,(k_x,k_y))
  screen.blit(goka,(g_x,g_y))
  screen.blit(petre,(p_x,p_y))
  screen.blit(cursor_shroom,cursor_pos)
 
  pressed_mouse = pygame.mouse.get_pressed()
  
  
  if(pressed_mouse[0]):
   
   end_x=cursor_pos[0]+23
   end_y=cursor_pos[1]
   c1=random.randint(0,255) 
   c2=random.randint(0,255) 
   c3=random.randint(0,255) 
 
   for event in pygame.event.get():
     if event.type == color_change:
      c1=random.randint(0,255) 
      c2=random.randint(0,255) 
      c3=random.randint(0,255) 
     
   
   pygame.draw.line(screen,(c1,c2,c3),(start_x,start_y),(end_x,end_y),2)
   pygame.draw.line(screen,(c2,c1,c3),(start_x+2,start_y+2),(end_x,end_y+2),2)
   pygame.draw.line(screen,(c3,c1,c3),(start_x+2,start_y-2),(end_x,end_y-2),2)
   pygame.draw.line(screen,(c2,c2,c1),(end_x,end_y),(end_x-13,end_y-13),4)
   pygame.draw.line(screen,(c3,c2,c3),(end_x,end_y),(end_x-13,end_y+13),4)
   
    
   gun.play()  
  pygame.display.update() 
       
    
    
   
     
  
  
  
  
 
