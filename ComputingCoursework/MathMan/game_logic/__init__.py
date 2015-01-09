import pygame,random
from MathMan import variables

#Colours
random_color = pygame.Color(random.randint(0,256),random.randint(0,256),random.randint(0,256)) 

def draw_game(start_pos,surface):
    global random_color
    row_number = 0
    column_number = 0
    for x in variables.grid:
        row_number += 1
        random_color = pygame.Color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        for y in x:             
            column_number += 1
            if y > 0:
                pygame.draw.rect(surface,random_color,((-16 + start_pos[1])+(column_number*16),(-18+start_pos[0]) +(row_number*18),16,18))
        column_number = 0
    row_number = 0        
                