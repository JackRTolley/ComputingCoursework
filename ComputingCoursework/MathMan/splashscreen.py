import pygame,screen_drawing

#Colors
pygame.init()

white = pygame.Color(255,255,255)
black = pygame.Color(  0,  0,  0)
green  = pygame.Color(  0,255,  0)


def draw_splashscreen(surface):
    
    #Background
    pygame.draw.rect(surface,black,(0,0,772,676))
    
    #Titles
    screen_drawing.print_title(surface, "MathMan", white, 80, (85,  0))
    screen_drawing.print_title(surface, "Play"   , white, 30, (345,480))
    screen_drawing.print_title(surface, "Options", white, 30, (310,530))
    screen_drawing.print_title(surface, "Exit"   , white, 30, (358,580))
    
    #Instructions
    screen_drawing.print_instructions(surface, "Guide MathMan through the maze using the WASD or Arrow keys"   , green, 20, (60,200))
    screen_drawing.print_instructions(surface, "Eat pellets and collect fruit to score points"                 , green, 20, (150,250))
    screen_drawing.print_instructions(surface, "Avoid ghosts, or eat power pellets to be able to eat them"     , green, 20, (80,300))
    screen_drawing.print_instructions(surface, "Answer questions after eating power pellets for more buff time" , green, 20, (40,350))
    
    
    