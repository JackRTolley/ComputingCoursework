import pygame,screen_drawing,random
from pygame.constants import K_l,K_e
from MathMan import game_logic,variables,questions


pygame.init()
questions.create_questions()
#Colors
white = pygame.Color(255,255,255)
black = pygame.Color(  0,  0,  0)
green = pygame.Color(  0,255,  0)
red   = pygame.Color(255,  0,  0)
grey  = pygame.Color( 50, 50, 50)

question_choice = None
question_timer = 0
primed = False


def draw(surface):
    global white,black,green,red,grey      
    #Backgroud
    pygame.draw.rect(surface,black,(0,0,772,676))    
    
    #Game Area
    pygame.draw.rect(surface,grey,(50,50,448,576))
    screen_drawing.print_title(surface, "Score", white, 30, (530,50))
    screen_drawing.print_title(surface, str(variables.score), white, 30, (530,90))
    screen_drawing.print_title(surface, "Lives", white, 30, (530,540))
    screen_drawing.print_title(surface, str(variables.lives), white, 30, (610,590))     
    #game
    game_logic.draw_game((50,50), surface)
    
def get_question():
    global question_choice  
    #Question choosing
    if len(variables.questions) > 0:
        random.shuffle(variables.questions)
        if question_choice == None:    
            for i in variables.questions:
                if i.difficulty == variables.difficulty_setting:
                    question_choice = i
    else:
        question_choice = None
        
        
def draw_question(surface):       
    global question_choice,question_timer,primed
    
    if variables.question_displayed:  
        question_choice.draw(surface,(498,150))
        question_timer = int(variables.speed_setting) * 3
        primed = True
    elif question_timer > 0:
        question_timer -= 1
        question_choice.draw(surface,(498,150))
    elif primed:       
        variables.questions.remove(question_choice)
        question_choice = None
        primed = False    
    
def event_handling(event):
    game_logic.game_event_handling(event)

def dynamic_question(event):
    if variables.question_displayed:
        question_choice.dynamic((498,150), event)
    
def get_answer(event):
    global question_choice
    
    if event.pos[0] > 498 and event.pos[1] > 150 and event.pos[1] < 520 and variables.question_displayed:
        if question_choice.check_correct((498,150),event):
            print "Answered correctly"
            variables.paused = False
            variables.buff_timer = int(variables.speed_setting) * 15
            variables.score += 50
            variables.question_displayed = False
        else:
            print "not answered correctly"
            variables.paused = False
            variables.buff_timer = int(variables.speed_setting) * 5
            variables.question_displayed = False
             
           

def game_state(event):
    if event.key == K_l:
        return "level_complete"
    elif event.key == K_e:
        return "game_over"
    else:
        return "game"