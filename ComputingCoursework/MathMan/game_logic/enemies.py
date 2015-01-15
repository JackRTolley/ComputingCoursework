import pygame,random
from pygame.locals import *
from MathMan import variables



class Ghost():
    
    def __init__(self,starting_position):
        
        self.starting_position = starting_position
        self.position = starting_position
        self.direction = "right"
        self.dead = True
        self.out = False
        variables.grid[self.position[0]][self.position[1]] = "GHT"
        self.previous_position = "NON"
    
    def start_up(self):
        variables.grid[self.position[0]][self.position[1]] = "GHT"
        
    def spawn(self):
        
        if variables.ghost_spawn and self.dead:
            variables.ghost_spawn = False
            self.dead = False
    
    def movement(self):
        
        movement_options = 0
        direction_list = ['up','down','left','right']
        if not self.dead:    
            if self.out == False:
                if self.position[1] < 13:
                    variables.grid[self.position[0]][self.position[1] + 1] = "GHT"
                    variables.grid[self.position[0]][self.position[1]] = "NON"
                    self.position = (self.position[0],self.position[1]+1)                       
                elif self.position[1] > 14: 
                    variables.grid[self.position[0]][self.position[1]-1] = "GHT"
                    variables.grid[self.position[0]][self.position[1]] = "NON"
                    self.position = (self.position[0],self.position[1]-1)
                elif self.position[0] > 11:
                    variables.grid[self.position[0] - 1][self.position[1]] = "GHT"
                    variables.grid[self.position[0]][self.position[1]] = "NON"
                    self.position = (self.position[0] - 1,self.position[1])
                else:
                    self.out = True
            
            else:
                
                #PathFinding and Mathman Killing
                for i in (variables.grid[self.position[0] - 1][self.position[1]],
                          variables.grid[self.position[0] + 1][self.position[1]],
                          variables.grid[self.position[0]][self.position[1]-1],
                          variables.grid[self.position[0]][self.position[1]+1]):
                    if i in ('P_B','P_N','NON','FRT',"M_M"):
                        if i == "M_M":
                            if variables.math_man_buff:
                                variables.grid[self.position[0]][self.position[1]] = self.previous_position
                                self.position = self.starting_position
                                self.direction = "right"
                                self.dead = True
                                self.out = False
                                variables.grid[self.position[0]][self.position[1]] = "GHT"
                                self.previous_position = "NON"
                            else:                               
                                variables.game_state = "game_over"                                
                        else:
                            movement_options += 1
                if movement_options >= 3:
                    done = False
                    while not done:
                        if random.randint(1,4) == 1:
                            if variables.grid[self.position[0] - 1][self.position[1]] in ('P_B','P_N','NON','FRT',"M_M"):
                                variables.grid[self.position[0]][self.position[1]] = self.previous_position
                                self.previous_position = variables.grid[self.position[0] - 1][self.position[1]]                            
                                variables.grid[self.position[0] - 1][self.position[1]] = "GHT"
                                
                                self.position = (self.position[0] - 1,self.position[1])
                                done = True
                                self.direction = "up"
                        elif random.randint(1,3) == 1:        
                            if variables.grid[self.position[0] + 1][self.position[1]] in ('P_B','P_N','NON','FRT',"M_M"):
                                variables.grid[self.position[0]][self.position[1]] = self.previous_position
                                self.previous_position = variables.grid[self.position[0] + 1][self.position[1]]                             
                                variables.grid[self.position[0] + 1][self.position[1]] = "GHT"
                                
                                self.position = (self.position[0] + 1,self.position[1])
                                done = True
                                self.direction = "down"
                        elif random.randint(1,2) == 1:        
                            if variables.grid[self.position[0]][self.position[1]-1] in ('P_B','P_N','NON','FRT',"M_M"):
                                variables.grid[self.position[0]][self.position[1]] = self.previous_position 
                                self.previous_position = variables.grid[self.position[0]][self.position[1]-1]                            
                                variables.grid[self.position[0]][self.position[1]-1] = "GHT"
                                
                                self.position = (self.position[0],self.position[1]-1)
                                done = True  
                                self.direction = "left" 
                        elif random.randint(1,1) == 1:                                
                            if variables.grid[self.position[0]][self.position[1]+1] in ('P_B','P_N','NON','FRT',"M_M"):
                                variables.grid[self.position[0]][self.position[1]] = self.previous_position 
                                self.previous_position = variables.grid[self.position[0]][self.position[1]+1]                            
                                variables.grid[self.position[0]][self.position[1]+1] = "GHT"
                                
                                self.position = (self.position[0],self.position[1]+1)
                                done = True
                                self.direction = "right"  
                    
                #Normal Movement
                else:
                    if self.direction == 'up':
                        if variables.grid[self.position[0] - 1][self.position[1]] in ('P_B','P_N','NON','FRT',"M_M"):
                            variables.grid[self.position[0]][self.position[1]] = self.previous_position
                            self.previous_position = variables.grid[self.position[0] - 1][self.position[1]] 
                            variables.grid[self.position[0] - 1][self.position[1]] = "GHT"
                            
                            self.position = (self.position[0] - 1,self.position[1])
                        else:
                            self.direction = random.choice(direction_list)                   
                    elif self.direction == 'down':
                        if variables.grid[self.position[0] + 1][self.position[1]] in ('P_B','P_N','NON','FRT',"M_M"):
                            variables.grid[self.position[0]][self.position[1]] = self.previous_position  
                            self.previous_position = variables.grid[self.position[0] + 1][self.position[1]]                          
                            variables.grid[self.position[0] + 1][self.position[1]] = "GHT"
                            
                            self.position = (self.position[0] + 1,self.position[1])
                        else:
                            self.direction = random.choice(direction_list)                     
                    elif self.direction == 'left':
                        if variables.grid[self.position[0]][self.position[1]-1] in ('P_B','P_N','NON','FRT',"M_M"):
                            variables.grid[self.position[0]][self.position[1]] = self.previous_position 
                            self.previous_position = variables.grid[self.position[0]][self.position[1]-1]                            
                            variables.grid[self.position[0]][self.position[1]-1] = "GHT"
                             
                            self.position = (self.position[0],self.position[1]-1)
                        else:
                            self.direction = random.choice(direction_list) 
                    elif self.direction == 'right':
                        if variables.grid[self.position[0]][self.position[1]+1] in ('P_B','P_N','NON','FRT',"M_M"):
                            variables.grid[self.position[0]][self.position[1]] = self.previous_position  
                            self.previous_position = variables.grid[self.position[0]][self.position[1]+1]                           
                            variables.grid[self.position[0]][self.position[1]+1] = "GHT"
                            
                            self.position = (self.position[0],self.position[1]+1)
                        else:
                            self.direction = random.choice(direction_list) 

        
                            
                                
                                
                                    
                                
                        
                    
                
                
        
            
        
       
        

        
        