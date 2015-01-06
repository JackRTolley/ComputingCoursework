import pygame,sys,splashscreen
from pygame.locals import *

#Start pygame
pygame.init()

#PrimaryScreen
x_resolution = 772
y_resolution = 676
DISPLAYSURF = pygame.display.set_mode((x_resolution,y_resolution))
pygame.display.set_caption("MathMan")

#GameLogic

game_state = "splash"

#Main Game Loop
while True:
    splashscreen.draw_splashscreen(DISPLAYSURF)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()