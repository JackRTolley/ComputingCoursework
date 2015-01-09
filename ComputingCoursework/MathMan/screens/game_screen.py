import pygame
from pygame.constants import K_l,K_e
from MathMan import game_logic


pygame.init()
#Colors
white = pygame.Color(255,255,255)
black = pygame.Color(  0,  0,  0)
green = pygame.Color(  0,255,  0)
red   = pygame.Color(255,  0,  0)
grey  = pygame.Color( 50, 50, 50)


def draw(surface):
    global white,black,green,red,grey       
    #Backgroud
    pygame.draw.rect(surface,black,(0,0,772,676))    
    #Game Area
    pygame.draw.rect(surface,grey,(50,50,448,576))
    pygame.draw.rect(surface, red,(498,50,224,100))
    pygame.draw.rect(surface,green,(498,526,224,100))
    pygame.draw.rect(surface,white,(498,150,224,376)) 
    #game
    game_logic.draw_game((50,50), surface)

def game_state(event):
    if event.key == K_l:
        return "level_complete"
    elif event.key == K_e:
        return "game_over"
    else:
        return "game"