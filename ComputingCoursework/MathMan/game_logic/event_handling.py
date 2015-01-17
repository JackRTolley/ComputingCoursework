import pygame,math_man,timer_logic,checks,enemies
from MathMan import variables

my_hero = math_man.MathMan()
ghosts  = [enemies.Ghost((13,11)),enemies.Ghost((16,11)),enemies.Ghost((13,16)),enemies.Ghost((16,16))]
my_hero.get_position()

def event_handling_on_draw():
    
    if variables.ghost_reset:
        for i in ghosts:
            i.dead = True
            i.position = i.starting_position
            i.out = False
        variables.ghost_reset = False
    for i in ghosts:
        i.start_up()
        i.spawn()
        i.movement()
    
        
    
    variables.math_man_buff = my_hero.buff   
    timer_logic.handle_buff_timer()
    timer_logic.handle_fruit_timer()
    timer_logic.handle_ghost_timer()
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
    