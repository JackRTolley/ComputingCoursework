import pygame,math_man,timer_logic
from MathMan import variables

my_hero = math_man.MathMan()

my_hero.get_position()

def event_handling_on_draw():
    
    my_hero.get_position()
    my_hero.move()
    variables.math_man_buff = my_hero.buff
    my_hero.update_buff()
    timer_logic.handle_buff_timer()
    timer_logic.handle_fruit_timer()
    
def event_handling_on_action(event):
    my_hero.get_direction(event) 
    