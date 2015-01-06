import pygame,os

pygame.init()

title_font = os.path.join(os.path.dirname(__file__), 'resources\\fonts\ETHNOCENTRIC RG.TTF')
word_font  = os.path.join(os.path.dirname(__file__), 'resources\\fonts\SQUARED DISPLAY.TTF')

def print_title(surface,text,color,size,position):
    my_font =  pygame.font.Font(title_font,size)
    text_box = my_font.render(text,0,color)
    return surface.blit(text_box,position)
    

def print_instructions(surface,text,color,size,position):        
    my_font =  pygame.font.Font(word_font,size)
    text_box = my_font.render(text,0,color)
    return surface.blit(text_box,position)
    
    
    


