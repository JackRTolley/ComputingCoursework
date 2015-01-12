import pygame,screen_drawing
from MathMan import variables
from pygame.locals import *


pygame.init()
#Colors
white = pygame.Color(255,255,255)
black = pygame.Color(  0,  0,  0)
green = pygame.Color(  0,255,  0)
red   = pygame.Color(255,  0,  0)
grey  = pygame.Color( 50, 50, 50)

#Color Variables
main_menu = white


def format_score(score):
    
    score = str(score)
    zeros = 7 - len(score)
    final_return = ""
    for i in range(0,zeros):
        final_return += "0"
    final_return += score
    return final_return
        
    
def draw(surface):
    global white,black,green,red,grey
       
    #Backgroud
    pygame.draw.rect(surface,black,(0,0,772,676))
    
    #Titles
    screen_drawing.print_title(surface, "Game Over", white, 80, (45,  0))
    screen_drawing.print_title(surface, "Final Score"    , white, 40, (210, 200))
    screen_drawing.print_title(surface, format_score(variables.score)    , white, 50, (230, 330))
    screen_drawing.print_title(surface, "Main Menu"   , main_menu , 30, (270,530))

def dynamic(event):
    """Handles all events related to the splash screen (colour change)"""
    global red,white,next_level,main_menu
        
    if event.type == MOUSEMOTION:
        #Difficulty
        main_menu  = white  
        if (event.pos[1] >= 530) and (event.pos[1] <= 560):
            if (event.pos[0] >= 270) and (event.pos[0] <= 515):
                main_menu = red               
                
def game_state(event):         
    if (event.pos[1] >= 530) and (event.pos[1] <= 560):
        if (event.pos[0] >= 270) and (event.pos[0] <= 515):
            return "splash"
        else:
            return "game_over" 
    else:
        return "game_over" 