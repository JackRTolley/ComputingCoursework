import pygame,screen_drawing


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
    
    #Titles
    screen_drawing.print_title(surface, "Game Over", white, 80, (130,  0))
    screen_drawing.print_title(surface, "Main Menu"   , white , 30, (400,530))
    screen_drawing.print_title(surface, "Score", white, 20, (180, 150))
