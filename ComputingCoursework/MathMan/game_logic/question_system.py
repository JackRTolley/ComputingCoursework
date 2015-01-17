import pygame,random
from MathMan import screens


#Colors

white = pygame.Color(255,255,255)
black = pygame.Color(  0,  0,  0)
green = pygame.Color(  0,255,  0)
red   = pygame.Color(255,  0,  0)
blue  = pygame.Color(  0,  0,255)


class Question():
    
    def __init__(self,question,correct_answer,fake_answer1,fake_answer2,fake_answer3,difficulty):
        
        self.question = question
        self.correct_answer = correct_answer       
        self.fake_answer1 = fake_answer1        
        self.fake_answer2 = fake_answer2        
        self.fake_answer3 = fake_answer3         
               
        self.difficulty        = difficulty
        
        self.correct_answer_color = white
        self.fake_answer1_color = white
        self.fake_answer2_color = white
        self.fake_answer3_color = white
        self.background_color   = black
        self.shuffled = False
        self.pos_complete = False       
        
    def draw(self,surface,starting_position): 
        
        self.x_cor = starting_position[0]
        self.y_cor = starting_position[1]
        
        if not self.pos_complete:
            self.answer_positions = [(self.x_cor +40,self.y_cor + 110),(self.x_cor +40,self.y_cor + 180),
                                     (self.x_cor +40, self.y_cor +250),(self.x_cor +40,self.y_cor + 310)]
            self.pos_complete = True
            
        
        if not self.shuffled:
            random.shuffle(self.answer_positions)
            self.shuffled = True
        
        
                      
        pygame.draw.rect(surface,self.background_color,(self.x_cor,self.y_cor ,224,376))
        
        
        if len(self.question) > 20:
            place = self.question[:19].rfind(" ")
            screens.screen_drawing.print_title(surface, self.question[:place] , white, 15, (self.x_cor + 5, self.y_cor  + 0))
            screens.screen_drawing.print_title(surface, self.question[place+1:] , white, 15, (self.x_cor + 5, self.y_cor  + 20))
        else:
            screens.screen_drawing.print_title(surface, self.question , white, 15, (self.x_cor + 0, self.y_cor  + 0))
        
        
        screens.screen_drawing.print_title(surface, self.correct_answer, self.correct_answer_color, 20, self.answer_positions[0])
        screens.screen_drawing.print_title(surface, self.fake_answer1, self.fake_answer1_color, 20, self.answer_positions[1])
        screens.screen_drawing.print_title(surface, self.fake_answer2, self.fake_answer2_color, 20, self.answer_positions[2])
        screens.screen_drawing.print_title(surface, self.fake_answer3, self.fake_answer3_color, 20, self.answer_positions[3])
    
    def dynamic(self,starting_position,event):
        
        if self.answer_positions != None:
            if event.pos[1] >= starting_position[1] and event.pos[0] >= starting_position[0]:
                self.correct_answer_color = white
                self.fake_answer1_color   = white
                self.fake_answer2_color   = white
                self.fake_answer3_color   = white
                if event.pos[1] > self.answer_positions[0][1] and event.pos[1] < self.answer_positions[0][1] + 20:
                    self.correct_answer_color = blue
                elif event.pos[1] > self.answer_positions[1][1] and event.pos[1] < self.answer_positions[1][1] + 20:
                    self.fake_answer1_color = blue
                elif event.pos[1] > self.answer_positions[2][1] and event.pos[1] < self.answer_positions[2][1] + 20:
                    self.fake_answer2_color = blue
                elif event.pos[1] > self.answer_positions[3][1] and event.pos[1] < self.answer_positions[3][1] + 20:
                    self.fake_answer3_color = blue
    
    def check_correct(self,starting_position,event):
        
        if self.answer_positions != None:
            if event.pos[1] > starting_position[1] and event.pos[0] >= starting_position[0]:
                if event.pos[1] > self.answer_positions[0][1] and event.pos[1] < self.answer_positions[0][1] + 20:
                    self.correct_answer_color = green
                    self.fake_answer1_color   = red
                    self.fake_answer2_color   = red
                    self.fake_answer3_color   = red
                    return True
                elif event.pos[1] < 520 :
                    self.correct_answer_color = green
                    self.fake_answer1_color   = red
                    self.fake_answer2_color   = red
                    self.fake_answer3_color   = red
                    return False

                
                       
        
        
        

        