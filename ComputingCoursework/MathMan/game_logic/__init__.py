import pygame,random,os
from MathMan import variables

#Tiles

test_tile  = pygame.image.load('assets/test_tile.png')
horizontal_border = pygame.image.load('assets/horizontal_border.png')
vertical_border = pygame.image.load('assets/vertical_border.png')
corner_down_right = pygame.image.load('assets/border_corner_DR.png')
corner_up_left = pygame.image.load('assets/border_corner_UL.png')
corner_down_left = pygame.image.load('assets/border_corner_DL.png')
corner_up_right = pygame.image.load('assets/border_corner_UR.png')

#tile = tile_surface.convert()

def draw_game(start_pos,surface):
    global random_color,tile_surface
    row_number = 0
    column_number = 0
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
            else:
                surface.blit(test_tile,pos)
                
        column_number = 0
    row_number = 0        
                