import pygame,math_man,timer_logic,checks
from MathMan import variables

my_hero = math_man.MathMan()

my_hero.get_position()

def event_handling_on_draw():
        
    
    variables.math_man_buff = my_hero.buff   
    timer_logic.handle_buff_timer()
    timer_logic.handle_fruit_timer()
    my_hero.get_position()
    my_hero.move()
    
    if variables.math_man_buff:
        my_hero.update_buff()
    if checks.level_complete():
        variables.game_state = "level_complete"
    elif checks.end_game():
        variables.game_state = "game_over"
        
    
    
def event_handling_on_action(event):
    my_hero.get_direction(event) 
    