import pygame,math_man
from MathMan import variables

my_hero = math_man.MathMan()

my_hero.get_position()

def event_handling_on_draw():
    
    my_hero.get_position()
    my_hero.move()
    print my_hero.position
    variables.math_man_buff = my_hero.buff
    
def event_handling_on_action(event):
    my_hero.get_direction(event) 
    