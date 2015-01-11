import pygame,math_man
from MathMan import variables

my_hero = math_man.MathMan()



def event_handling():
    
    my_hero.get_position()
    print my_hero.position
    my_hero.move()
    
    
    