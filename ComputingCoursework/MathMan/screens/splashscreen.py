import pygame, sys,screen_drawing


#Colors
pygame.init()

white = pygame.Color(255,255,255)
black = pygame.Color(  0,  0,  0)
green = pygame.Color(  0,255,  0)
red   = pygame.Color(255,  0,  0)

#Color_variable
play_color    = white
options_color = white
exit_color    = white


def draw(surface):
    
    #Background
    pygame.draw.rect(surface,black,(0,0,772,676))
    
    #Titles
    screen_drawing.print_title(surface, "MathMan", white, 80, (85,  0))
    screen_drawing.print_title(surface, "Play"   , play_color, 30, (345,480))
    screen_drawing.print_title(surface, "Options", options_color, 30, (310,530))
    screen_drawing.print_title(surface, "Exit"   , exit_color, 30, (358,580))
    
    #Instructions
    screen_drawing.print_instructions(surface, "Guide MathMan through the maze using the WASD or Arrow keys"   , green, 20, (60,200))
    screen_drawing.print_instructions(surface, "Eat pellets and collect fruit to score points"                 , green, 20, (150,250))
    screen_drawing.print_instructions(surface, "Avoid ghosts, or eat power pellets to be able to eat them"     , green, 20, (80,300))
    screen_drawing.print_instructions(surface, "Answer questions after eating power pellets for more buff time" , green, 20, (40,350))

def dynamic(event):
    """Handles all events related to the splash screen (gamestate/colour change)"""
    global play_color, options_color,exit_color,red,white
        
    
    if (event.pos[0] > 310) and (event.pos[0] < 450):
        if (event.pos[1] > 480) and (event.pos[1] < 529):
            play_color = red
            options_color = white
            exit_color = white
        elif (event.pos[1] > 530) and (event.pos[1] < 579):
            play_color = white
            options_color = red
            exit_color = white
        elif (event.pos[1] > 580) and (event.pos[1] < 629):
            play_color = white
            options_color = white
            exit_color = red
        else:
            play_color = white
            options_color = white
            exit_color = white

            
            
def game_state(event):
           
    if (event.pos[0] > 310) and (event.pos[0] < 450):
        if (event.pos[1] > 480) and (event.pos[1] < 529):
            print "game state changed to game"
            return "game"
        elif (event.pos[1] > 530) and (event.pos[1] < 579):
            print "game state changed to options"
            return "options"
        elif (event.pos[1] > 580) and (event.pos[1] < 629):
            print "game state change to exit"
            pygame.quit()
            sys.exit()
        else:
            return "splash"
                
                  
                       
    
    