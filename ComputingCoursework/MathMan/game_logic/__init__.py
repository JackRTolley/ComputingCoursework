import pygame,random,os,event_handling
from MathMan import variables

#Tiles

point_normal      = pygame.image.load('assets/point_normal.png')
point_buff        = pygame.image.load('assets/point_buff.png')
horizontal_border = pygame.image.load('assets/horizontal_border.png')
vertical_border   = pygame.image.load('assets/vertical_border.png')
corner_down_right = pygame.image.load('assets/border_corner_DR.png')
corner_up_left    = pygame.image.load('assets/border_corner_UL.png')
corner_down_left  = pygame.image.load('assets/border_corner_DL.png')
corner_up_right   = pygame.image.load('assets/border_corner_UR.png')
math_man          = pygame.image.load('assets/math_man.png')
math_man_buff     = pygame.image.load('assets/math_man_buff.png')
fruit             = pygame.image.load('assets/fruit.png')

#tile = tile_surface.convert()

def draw_game(start_pos,surface):
    global random_color,tile_surface
    row_number = 0
    column_number = 0
    event_handling.event_handling_on_draw() 
    for x in variables.grid:
        row_number += 1
        for y in x:                    
            column_number += 1
            pos = ([(-16 + start_pos[1])+(column_number*16),(-18+start_pos[0]) +(row_number*18)])
            if y == 'B_H':
                surface.blit(horizontal_border,pos)
            elif y == 'B_V':
                surface.blit(vertical_border,pos)
            elif y == 'BDR':
                surface.blit(corner_down_right,pos)
            elif y == 'BUL':
                surface.blit(corner_up_left,pos)
            elif y == 'BDL':
                surface.blit(corner_down_left,pos)
            elif y == 'BUR':
                surface.blit(corner_up_right,pos)
            elif y == "P_N":
                surface.blit(point_normal,pos)
            elif y == "P_B":
                surface.blit(point_buff,pos)
            elif y == "NON":
                pygame.draw.rect(surface,pygame.Color(0,0,0),(pos[0],pos[1],16,18))
            elif y == "M_M":
                if variables.math_man_buff:
                    surface.blit(math_man_buff,pos)
                else:
                    surface.blit(math_man,pos) 
            elif y == "FRT":
                surface.blit(fruit,pos)         
        column_number = 0
        
    row_number = 0      

def game_event_handling(event):
    event_handling.event_handling_on_action(event)              