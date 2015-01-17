from MathMan import variables

def level_complete():
    
    for x in variables.grid:
        for y in x:
            if y in ('P_B','P_N','FRT'):
                return False
    return True

def end_game():
    
    if variables.lives == 0:
        return True
    return False        
    
        