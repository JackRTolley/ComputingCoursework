import pygame
from pygame.locals import *
from MathMan import variables



class MathMan():
    
    def __init__(self):
        self.position  = None
        self.direction = None
        self.buff      = False
    
    def get_position(self):
        """Finds position by cycling through grid"""
        
        x_place = 0
        for x in variables.grid:
            y_place = 0
            for y in x:
                if y == "M_M":
                    self.position = (x_place,y_place)
                    break
                y_place += 1
            x_place += 1
    
    def get_direction(self,event):       
        if event.key == K_w:
            self.direction = "up"
        elif event.key == K_a:
            self.direction = "left"
        elif event.key == K_s:
            self.direction = "down"
        elif event.key == K_d:
            self.direction = "right"
                  
    def move(self):
              
        if self.direction == 'up':
            if variables.grid[self.position[0]-1][self.position[1]] in ('P_B','P_N','NON','FRT'):
                if variables.grid[self.position[0]-1][self.position[1]] == 'P_B':
                    self.buff = True
                    variables.buff_timer = int(variables.speed_setting) * 5 
                    variables.score += 50
                elif variables.grid[self.position[0]-1][self.position[1]] == 'P_N':
                    variables.score += 1
                elif variables.grid[self.position[0]-1][self.position[1]] == 'FRT':
                    variables.score += 50
                variables.grid[self.position[0]][self.position[1]]   = 'NON'
                variables.grid[self.position[0]-1][self.position[1]] = 'M_M'
                
        if self.direction == 'down':
            if variables.grid[self.position[0]+1][self.position[1]] in ('P_B','P_N','NON','FRT'):
                if variables.grid[self.position[0]+1][self.position[1]] == 'P_B':
                    self.buff = True
                    variables.buff_timer = int(variables.speed_setting) * 5 
                    variables.score += 50
                elif variables.grid[self.position[0]+1][self.position[1]] == 'P_N':
                    variables.score += 1
                elif variables.grid[self.position[0]+1][self.position[1]] == 'FRT':
                    variables.score += 50
                variables.grid[self.position[0]][self.position[1]]   = 'NON'
                variables.grid[self.position[0]+1][self.position[1]] = 'M_M'
                
        if self.direction == 'left':
            if self.position == (14,0) or self.position == (15,0):
                variables.grid[self.position[0]][self.position[1]]   = 'NON'
                variables.grid[self.position[0]][26]  = 'M_M'
            
            elif variables.grid[self.position[0]][self.position[1]-1] in ('P_B','P_N','NON','FRT'):
                if variables.grid[self.position[0]][self.position[1]-1] == 'P_B':
                    self.buff = True
                    variables.buff_timer = int(variables.speed_setting) * 5  
                    variables.score += 50
                elif variables.grid[self.position[0]][self.position[1]-1] == 'P_N':
                    variables.score += 1
                elif variables.grid[self.position[0]][self.position[1]-1] == 'FRT':
                    variables.score += 50
                variables.grid[self.position[0]][self.position[1]]   = 'NON'
                variables.grid[self.position[0]][self.position[1]-1] = 'M_M'
                
        if self.direction == 'right':
            if self.position == (14,26) or self.position == (15,26):
                variables.grid[self.position[0]][self.position[1]]   = 'NON'
                variables.grid[self.position[0]][0]  = 'M_M'
                
                
            elif variables.grid[self.position[0]][self.position[1]+1] in ('P_B','P_N','NON','FRT'):
                if variables.grid[self.position[0]][self.position[1]+1] == 'P_B':
                    self.buff = True
                    variables.buff_timer = int(variables.speed_setting) * 5 
                    variables.score += 50
                elif variables.grid[self.position[0]][self.position[1]+1] == 'P_N':
                    variables.score += 1
                elif variables.grid[self.position[0]][self.position[1]+1] == 'FRT':
                    variables.score += 50
                variables.grid[self.position[0]][self.position[1]]   = 'NON'
                variables.grid[self.position[0]][self.position[1]+1] = 'M_M'
                
    def update_buff(self):
        
        if variables.buff_timer == 0:
            self.buff = False
                