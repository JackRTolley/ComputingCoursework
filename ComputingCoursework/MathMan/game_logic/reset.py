import event_handling
from MathMan import variables

def reset(new_game):
    
    
    variables.ghost_reset = True
    event_handling.my_hero.direction = None
    variables.math_man_buff = False
    variables.buff_timer = 0
    variables.fruit_timer = int(variables.speed_setting) * 60    
    variables.grid = [['BDR','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','BDL','BDR','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','BDL'],
                      ['B_V','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','B_V','B_V','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','B_V'],
                      ['B_V','P_N','BDR','B_H','B_H','BDL','P_N','BDR','B_H','B_H','B_H','BDL','P_N','B_V','B_V','P_N','BDR','B_H','B_H','B_H','BDL','P_N','BDR','B_H','B_H','BDL','P_N','B_V'],
                      ['B_V','P_B','B_V','NON','NON','B_V','P_N','B_V','NON','NON','NON','B_V','P_N','B_V','B_V','P_N','B_V','NON','NON','NON','B_V','P_N','B_V','NON','NON','B_V','P_B','B_V'],
                      ['B_V','P_N','BUR','B_H','B_H','BUL','P_N','BUR','B_H','B_H','B_H','BUL','P_N','BUR','BUL','P_N','BUR','B_H','B_H','B_H','BUL','P_N','BUR','B_H','B_H','BUL','P_N','B_V'],
                      ['B_V','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','B_V'],
                      ['B_V','P_N','BDR','B_H','B_H','BDL','P_N','BDR','BDL','P_N','BDR','B_H','B_H','B_H','B_H','B_H','B_H','BDL','P_N','BDR','BDL','P_N','BDR','B_H','B_H','BDL','P_N','B_V'],
                      ['B_V','P_N','BUR','B_H','B_H','BUL','P_N','B_V','B_V','P_N','BUR','B_H','B_H','BDL','BDR','B_H','B_H','BUL','P_N','B_V','B_V','P_N','BUR','B_H','B_H','BUL','P_N','B_V'],
                      ['B_V','P_N','P_N','P_N','P_N','P_N','P_N','B_V','B_V','P_N','P_N','P_N','P_N','B_V','B_V','P_N','P_N','P_N','P_N','B_V','B_V','P_N','P_N','P_N','P_N','P_N','P_N','B_V'],
                      ['BUR','B_H','B_H','B_H','B_H','BDL','P_N','B_V','BUR','B_H','B_H','BDL','NON','B_V','B_V','NON','BDR','B_H','B_H','BUL','B_V','P_N','BDR','B_H','B_H','B_H','B_H','BUL'],
                      ['NON','NON','NON','NON','NON','B_V','P_N','B_V','BDR','B_H','B_H','BUL','NON','BUR','BUL','NON','BUR','B_H','B_H','BDL','B_V','P_N','B_V','NON','NON','NON','NON','NON'],
                      ['NON','NON','NON','NON','NON','B_V','P_N','B_V','B_V','NON','NON','NON','NON','NON','NON','NON','NON','NON','NON','B_V','B_V','P_N','B_V','NON','NON','NON','NON','NON'],
                      ['NON','NON','NON','NON','NON','B_V','P_N','B_V','B_V','NON','BDR','B_H','B_H','NON','NON','B_H','B_H','BDL','NON','B_V','B_V','P_N','B_V','NON','NON','NON','NON','NON'],
                      ['B_H','B_H','B_H','B_H','B_H','BUL','P_N','BUR','BUL','NON','B_V','NON','NON','NON','NON','NON','NON','B_V','NON','BUR','BUL','P_N','BUR','B_H','B_H','B_H','B_H','B_H'],
                      ['NON','NON','NON','NON','NON','NON','P_N','NON','NON','NON','B_V','NON','NON','NON','NON','NON','NON','B_V','NON','NON','NON','P_N','NON','NON','NON','NON','NON','NON'],
                      ['NON','NON','NON','NON','NON','NON','P_N','NON','NON','NON','B_V','NON','NON','NON','NON','NON','NON','B_V','NON','NON','NON','P_N','NON','NON','NON','NON','NON','NON'],
                      ['B_H','B_H','B_H','B_H','B_H','BDL','P_N','BDR','BDL','NON','B_V','NON','NON','NON','NON','NON','NON','B_V','NON','BDR','BDL','P_N','BDR','B_H','B_H','B_H','B_H','B_H'],
                      ['NON','NON','NON','NON','NON','B_V','P_N','B_V','B_V','NON','BUR','B_H','B_H','B_H','B_H','B_H','B_H','BUL','NON','B_V','B_V','P_N','B_V','NON','NON','NON','NON','NON'],
                      ['NON','NON','NON','NON','NON','B_V','P_N','B_V','B_V','NON','NON','NON','NON','NON','NON','NON','NON','NON','NON','B_V','B_V','P_N','B_V','NON','NON','NON','NON','NON'],
                      ['NON','NON','NON','NON','NON','B_V','P_N','B_V','B_V','NON','BDR','B_H','B_H','B_H','B_H','B_H','B_H','BDL','NON','B_V','B_V','P_N','B_V','NON','NON','NON','NON','NON'],
                      ['BDR','B_H','B_H','B_H','B_H','BUL','P_N','BUR','BUL','NON','BUR','B_H','B_H','BDL','BDR','B_H','B_H','BUL','NON','BUR','BUL','P_N','BUR','B_H','B_H','B_H','B_H','BDL'],
                      ['B_V','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','B_V','B_V','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','B_V'],
                      ['B_V','P_N','BDR','B_H','B_H','BDL','P_N','BDR','B_H','B_H','B_H','BDL','P_N','B_V','B_V','P_N','BDR','B_H','B_H','B_H','BDL','P_N','BDR','B_H','B_H','BDL','P_N','B_V'],
                      ['B_V','P_N','BUR','B_H','BDL','B_V','P_N','BUR','B_H','B_H','B_H','BUL','P_N','BUR','BUL','P_N','BUR','B_H','B_H','B_H','BUL','P_N','B_V','BDR','B_H','BUL','P_N','B_V'],
                      ['B_V','P_B','P_N','P_N','B_V','B_V','P_N','P_N','P_N','P_N','P_N','P_N','P_N','M_M','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','B_V','B_V','P_N','P_N','P_B','B_V'],
                      ['BUR','B_H','BDL','P_N','B_V','B_V','P_N','BDR','BDL','P_N','BDR','B_H','B_H','B_H','B_H','B_H','B_H','BDL','P_N','BDR','BDL','P_N','B_V','B_V','P_N','BDR','B_H','BUL'],
                      ['BDR','B_H','BUL','P_N','BUR','BUL','P_N','B_V','B_V','P_N','BUR','B_H','B_H','BDL','BDR','B_H','B_H','BUL','P_N','B_V','B_V','P_N','BUR','BUL','P_N','BUR','B_H','BDL'],
                      ['B_V','P_N','P_N','P_N','P_N','P_N','P_N','B_V','B_V','P_N','P_N','P_N','P_N','B_V','B_V','P_N','P_N','P_N','P_N','B_V','B_V','P_N','P_N','P_N','P_N','P_N','P_N','B_V'],
                      ['B_V','P_N','BDR','B_H','B_H','B_H','B_H','BUL','BUR','B_H','B_H','BDL','P_N','B_V','B_V','P_N','BDR','B_H','B_H','BUL','BUR','B_H','B_H','B_H','B_H','BDL','P_N','B_V'],
                      ['B_V','P_N','BUR','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','BUL','P_N','BUR','BUL','P_N','BUR','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','BUL','P_N','B_V'],
                      ['B_V','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','B_V'],
                      ['BUR','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','BUL']]
    if new_game:
        variables.score = 0
        variables.lives = 3