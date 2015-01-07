import pygame,sys,splashscreen,options_screen
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
    #Draw Handling
    if game_state == "splash":
        splashscreen.draw(DISPLAYSURF)
    elif game_state == "options":
        options_screen.draw(DISPLAYSURF)
    
    #Event Handling
    for event in pygame.event.get():
        #Dynamic User Feedback
        if event.type == MOUSEMOTION:
            if game_state == "splash": 
                splashscreen.dynamic(event)
            elif game_state == "options":
                options_screen.dynamic(event)
        #Game State changing options
        elif event.type == MOUSEBUTTONDOWN:
            if game_state == "splash": 
                game_state = splashscreen.game_state(event)
            elif game_state == "options":
                options_screen.change_options(event)
                game_state = options_screen.game_state(event)

                
        elif event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()