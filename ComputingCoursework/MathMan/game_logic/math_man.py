import pygame
from pygame.locals import *
from MathMan import variables



class MathMan():
    
    def __init__(self):
        self.position  = None
        self.direction = None
        self.buff      = None
    
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
            variables.grid[self.position[0]][self.position[1]]   = 'NON'
            variables.grid[self.position[0]-1][self.position[1]] = 'M_M'
        if self.direction == 'down':
            variables.grid[self.position[0]][self.position[1]]   = 'NON'
            variables.grid[self.position[0]+1][self.position[1]] = 'M_M'
        if self.direction == 'left':
            variables.grid[self.position[0]][self.position[1]]   = 'NON'
            variables.grid[self.position[0]][self.position[1]-1] = 'M_M'
        if self.direction == 'right':
            variables.grid[self.position[0]][self.position[1]]   = 'NON'
            variables.grid[self.position[0]][self.position[1]+1] = 'M_M'
