import pygame, sys, variables
from MathMan.screens import splashscreen, options_screen, game_screen,level_complete_screen,game_over_screen
from MathMan.game_logic import reset
from pygame.locals import *

#Start pygame
pygame.init()

#PrimaryScreen

DISPLAYSURF = pygame.display.set_mode((variables.x_resolution,variables.y_resolution))
pygame.display.set_caption("MathMan")

#GameLogic



#Main Game Loop
while True:
    if pygame.time.get_ticks() % (1000 // int(variables.speed_setting))  == 0:
                   
        #Event Handling
        for event in pygame.event.get():             
            # System Events
            if event.type == QUIT:
                pygame.quit()
                sys.exit()        
            # Game State events
            elif variables.game_state == "splash":
                reset.reset(True)
                if event.type == MOUSEMOTION:
                    splashscreen.dynamic(event)
                elif event.type == MOUSEBUTTONDOWN:
                    variables.game_state = splashscreen.game_state(event)                               
            elif variables.game_state == "options":
                if event.type == MOUSEMOTION:
                    options_screen.dynamic(event)
                elif event.type == MOUSEBUTTONDOWN:
                    options_screen.change_options(event)
                    variables.game_state = options_screen.game_state(event)       
            elif variables.game_state == "game":
                if event.type == MOUSEMOTION:
                    if game_screen.question_choice != None:
                        game_screen.dynamic_question(event)
                elif event.type == MOUSEBUTTONDOWN:
                    game_screen.get_answer(event) 
                if event.type == KEYUP and not variables.paused:
                    game_screen.event_handling(event)
                elif event.type == KEYDOWN:
                    if event.key in (K_l,K_e):
                        variables.game_state = game_screen.game_state(event)
            elif variables.game_state == "level_complete":
                reset.reset(False)
                if event.type == MOUSEMOTION:
                    level_complete_screen.dynamic(event)
                elif event.type == MOUSEBUTTONDOWN:
                    variables.game_state = level_complete_screen.game_state(event)
            elif variables.game_state == "game_over":                
                if event.type == MOUSEMOTION:
                    game_over_screen.dynamic(event)                       
                elif event.type == MOUSEBUTTONDOWN:
                    variables.game_state = game_over_screen.game_state(event)
            
        
        #Draw Handling
        if variables.game_state == "splash":
            splashscreen.draw(DISPLAYSURF)
        elif variables.game_state == "options":
            options_screen.draw(DISPLAYSURF)
        elif variables.game_state == "game":
            game_screen.draw(DISPLAYSURF)
            game_screen.get_question()
            if game_screen.question_choice != None  and variables.question_displayed:
                game_screen.draw_question(DISPLAYSURF)
        elif variables.game_state == "level_complete":
            level_complete_screen.draw(DISPLAYSURF)   
        elif variables.game_state == "game_over":
            game_over_screen.draw(DISPLAYSURF)                      
        pygame.display.update()