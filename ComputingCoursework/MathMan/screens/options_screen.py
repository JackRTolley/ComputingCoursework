import pygame, screen_drawing
from MathMan import variables
from pygame.constants import MOUSEMOTION


pygame.init()
#Colors
white = pygame.Color(255,255,255)
black = pygame.Color(  0,  0,  0)
green = pygame.Color(  0,255,  0)
red   = pygame.Color(255,  0,  0)

#Color_variable
back_color = white
easy_color = white
easy_picked = False
medium_color = white
medium_picked = True
hard_color = white
hard_picked = False

# Speed setting functions
""" 0 = Not picked / white
    1 = hovered over / red
    2 = picked
    """

speed = [0,0,0,2,0,0,0,0]

#Screen handling

def draw(surface):
    global easy_color,medium_color,hard_color,green,black,white,back_color,easy_picked,medium_picked,hard_picked,speed
    
    #Picked Check
    if easy_picked:
        easy_color = green
    elif medium_picked:
        medium_color = green
    elif hard_picked:
        hard_color = green
        
    #Backgroud
    pygame.draw.rect(surface,black,(0,0,772,676))
                     
    #Difficulty boxes
    pygame.draw.rect(surface,easy_color,(180,180,150,50))
    pygame.draw.rect(surface,medium_color,(340,180,150,50))
    pygame.draw.rect(surface,hard_color,(500,180,150,50))
    
    #Titles
    screen_drawing.print_title(surface, "Options", white, 80, (130,  0))
    screen_drawing.print_title(surface, "Back"   , back_color, 30, (345,530))
    screen_drawing.print_title(surface, "Difficulty", white, 20, (180, 150))
    screen_drawing.print_title(surface, "Speed", white, 20, (180, 350))
    
    #Difficulties
    screen_drawing.print_instructions(surface, "EASY"   , black, 40, (215,185))
    screen_drawing.print_instructions(surface, "MEDIUM"   , black, 40, (355,185))
    screen_drawing.print_instructions(surface, "HARD"   , black, 40, (535,185))
    
    # Speed settings
    turns = 0
    for i in speed:
        if i == 0:
            pygame.draw.rect(surface,white,(180 + turns* 60,380, 50, 50))
            screen_drawing.print_instructions(surface, str(turns + 1) , black, 40, (195 + turns* 60, 385))   
        elif i == 1:
            pygame.draw.rect(surface,red  ,(180 + turns* 60,380, 50, 50))
            screen_drawing.print_instructions(surface, str(turns + 1) ,black, 40, (195 + turns* 60, 385))          
        elif i == 2:
            pygame.draw.rect(surface,green,(180 + turns* 60,380, 50, 50))
            screen_drawing.print_instructions(surface, str(turns + 1) , black, 40, (195 + turns* 60, 385))
        turns += 1
        
    
def dynamic(event):
    """Handles all events related to the splash screen (gamestate/colour change)"""
    global back_color,red,white,green,easy_color,medium_color,hard_color,speed
        
    if event.type == MOUSEMOTION:
        #Difficulty
        if (event.pos[1] >= 180) and (event.pos[1] <= 230):
            if (event.pos[0] >= 180) and (event.pos[0] <= 330):
                easy_color = red
                medium_color = white
                hard_color = white
            elif (event.pos[0] >= 340) and (event.pos[0] <= 490):
                easy_color = white
                medium_color = red
                hard_color = white
            elif (event.pos[0] >= 500) and (event.pos[0] <= 650):
                easy_color = white
                medium_color = white
                hard_color = red           
            else:
                if easy_color != green:
                    easy_color = white
                elif medium_color != green:
                    medium_color = white
                elif hard_color != green:
                    hard_color = white
        #Speed                             
        elif (event.pos[1] >= 380) and (event.pos[1] <= 430):
            if (event.pos[0] > 175) and (event.pos[0] < 655):
                place = ((event.pos[0] - 175) // 60)
                #Resets speed
                new_speed = []
                for i in speed:
                    if i != 1:
                        new_speed.append(i)
                    else:
                        new_speed.append(0)                    
                speed = new_speed
                if speed[place] != 2:
                    speed[place] = 1
                   
        elif (event.pos[0] > 345) and (event.pos[0] < 420):
            if (event.pos[1] >= 530) and (event.pos[1] <= 560):
                back_color = red
            else:
                back_color = white
        
        else:
            back_color = white
            easy_color = white
            medium_color = white
            hard_color = white
            
            
def change_options(event):
    global easy_picked,medium_picked,hard_picked,speed
    
    # Event handling for the difficulty 
    if (event.pos[1] >= 180) and (event.pos[1] <= 230):
            if (event.pos[0] >= 180) and (event.pos[0] <= 330):
                easy_picked = True
                medium_picked = False
                hard_picked = False
                print "difficulty changed to easy"
                variables.difficulty = "easy"
            elif (event.pos[0] >= 340) and (event.pos[0] <= 490):
                easy_picked = False
                medium_picked = True
                hard_picked = False
                print "difficulty changed to medium"
                variables.difficulty = "medium"
            elif (event.pos[0] >= 500) and (event.pos[0] <= 650):
                easy_picked = False
                medium_picked = False
                hard_picked = True
                print "difficulty changed to hard"
                variables.difficulty = "hard"
    # Event handling for the speed 
    elif (event.pos[1] >= 380) and (event.pos[1] <= 430):           
        if (event.pos[0] > 175) and (event.pos[0] < 655):
                    place = ((event.pos[0] - 175) // 60)
                    new_speed = []
                    for i in speed:
                        new_speed.append(0)                    
                    speed = new_speed
                    speed[place] = 2
                    variables.speed = place         
            
def game_state(event):         
    if (event.pos[1] >= 530) and (event.pos[1] <= 560):
        if (event.pos[0] > 345) and (event.pos[0] < 420):
            print "game state changed to splash"
            return "splash"
        else:
            return "options"
    else:
        return "options"
             
            
