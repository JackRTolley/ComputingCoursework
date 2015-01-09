import pygame, sys, variables
from MathMan.screens import splashscreen, options_screen, game_screen,level_complete_screen,game_over_screen
from pygame.locals import *

#Start pygame
pygame.init()

#PrimaryScreen

DISPLAYSURF = pygame.display.set_mode((variables.x_resolution,variables.y_resolution))
pygame.display.set_caption("MathMan")

#GameLogic

game_state = "game"

#Main Game Loop
while True:
    if pygame.time.get_ticks() % 500 == 0:
        #Draw Handling
        if game_state == "splash":
            splashscreen.draw(DISPLAYSURF)
        elif game_state == "options":
            options_screen.draw(DISPLAYSURF)
        elif game_state == "game":
                    game_screen.draw(DISPLAYSURF)
        elif game_state == "level_complete":
            level_complete_screen.draw(DISPLAYSURF)   
        elif game_state == "game_over":
            game_over_screen.draw(DISPLAYSURF)
            
        #Event Handling
        for event in pygame.event.get():             
            # System Events
            if event.type == QUIT:
                pygame.quit()
                sys.exit()        
            # Game State events
            elif game_state == "splash":
                if event.type == MOUSEMOTION:
                    splashscreen.dynamic(event)
                elif event.type == MOUSEBUTTONDOWN:
                    game_state = splashscreen.game_state(event)                               
            elif game_state == "options":
                if event.type == MOUSEMOTION:
                    options_screen.dynamic(event)
                elif event.type == MOUSEBUTTONDOWN:
                    options_screen.change_options(event)
                    game_state = options_screen.game_state(event)       
            elif game_state == "game":
                if event.type == KEYDOWN:
                    if event.key in (K_l,K_e):
                        game_state = game_screen.game_state(event)
            elif game_state == "level_complete":
                if event.type == MOUSEMOTION:
                    level_complete_screen.dynamic(event)
                elif event.type == MOUSEBUTTONDOWN:
                    game_state = level_complete_screen.game_state(event)
            elif game_state == "game_over":
                if event.type == MOUSEMOTION:
                    game_over_screen.dynamic(event)
                elif event.type == MOUSEBUTTONDOWN:
                    game_state = game_over_screen.game_state(event)
                                
        pygame.display.update()