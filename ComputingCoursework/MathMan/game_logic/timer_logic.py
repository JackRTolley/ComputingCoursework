import random
from MathMan import variables



def handle_buff_timer():
    
    if variables.buff_timer > 0:
        variables.buff_timer -= 1
        
def handle_fruit_timer():
    
    if variables.fruit_timer > 0:
        variables.fruit_timer -= 1
    elif variables.fruit_timer == 0:
        variables.fruit_timer = int(variables.speed_setting) *60
        
        
        avalible_places = []
        x_place = 0
        for x in variables.grid:
            y_place = 0
            for y in x:
                if y == 'P_N':
                    avalible_places.append((x_place,y_place))
                    #y_place += 1
                y_place +=1
            x_place += 1
            
        place = random.choice(avalible_places)
        variables.grid[place[0]][place[1]] = "FRT"