import pygame,math_man
from MathMan import variables

my_hero = math_man.MathMan()



def event_handling_on_draw():
    
    my_hero.get_position()
    my_hero.move()
    
def event_handling_on_action(event):
    my_hero.get_direction(event) 
    