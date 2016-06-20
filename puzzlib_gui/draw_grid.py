
# coding: utf-8

# In[1]:

import pygame
import os
os.chdir( "C:\Users\Shathra\Desktop\puzzlib_gui")

white = (180,180,180)
black = (120,120,120)
red = (255, 0, 0)

box_image = pygame.image.load("box.png")
box_image = pygame.transform.scale( box_image, (50, 50))
box_rect = box_image.get_rect()
box_rect = box_rect.move( 100, 100)

pygame.init()

game_display = pygame.display.set_mode( (400, 400))
pygame.display.set_caption( "Title")

game_exit = False

while( not game_exit):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True
            
    game_display.fill( white)
    for i in xrange( 8):
        for j in xrange( 8):
            if( (i+j)%2 == 0):
                game_display.fill( white, rect=[i * 50, j * 50, 50, 50])
            else:
                game_display.fill( black, rect=[i * 50, j * 50, 50, 50])
    
    game_display.blit( box_image, box_rect)
    game_display.blit( box_image, box_rect.move(100,100))
    game_display.blit( box_image, box_rect.move(150,0))

    pygame.display.update()

pygame.quit()
quit()

