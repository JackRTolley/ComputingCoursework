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

#Color variables
next_level = white
main_menu  = white

def draw(surface):
    global white,black,green,red,grey
       
    #Backgroud
    pygame.draw.rect(surface,black,(0,0,772,676))
    
    #Titles
    screen_drawing.print_title(surface, "Level"    , white, 80, (220,  0))
    screen_drawing.print_title(surface, "Complete!", white, 80, (70,  90))
    screen_drawing.print_title(surface, "Score"    , white, 20, (180, 260))
    screen_drawing.print_title(surface, variables.score    , white, 30, (320, 250))
    screen_drawing.print_title(surface, "Lives"    , white, 20, (185, 380))
    screen_drawing.print_title(surface, "Live variable"    , white, 30, (320, 370))
    screen_drawing.print_title(surface, "Next"     , next_level, 30, (175,500))
    screen_drawing.print_title(surface, "level"    , next_level, 30, (170,530))
    screen_drawing.print_title(surface, "Main"     , main_menu, 30, (485,500))
    screen_drawing.print_title(surface, "Menu"     , main_menu, 30, (480,530))

def dynamic(event):
    """Handles all events related to the splash screen (colour change)"""
    global red,white,next_level,main_menu
        
    if event.type == MOUSEMOTION:
        #Difficulty
        next_level = white
        main_menu  = white  
        if (event.pos[1] >= 500) and (event.pos[1] <= 560):
            if (event.pos[0] >= 170) and (event.pos[0] <= 305):
                next_level = red               
            elif (event.pos[0] >= 480) and (event.pos[0] <= 605):
                main_menu = red 
                
def game_state(event):         
    if (event.pos[1] >= 500) and (event.pos[1] <= 560):
        if (event.pos[0] >= 170) and (event.pos[0] <= 305):
            print "game state changed to next level"
            return "game"
        elif (event.pos[0] >= 480) and (event.pos[0] <= 605):
            return "splash"
        else:
            return "level_complete" 
    else:
        return "options"  