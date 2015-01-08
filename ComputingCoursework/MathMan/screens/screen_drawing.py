import pygame

pygame.init()

title_font = pygame.font.match_font('ethnocentricrgregular')
word_font = pygame.font.match_font('squared display')


def print_title(surface,text,color,size,position):
    my_font =  pygame.font.Font(title_font,size)
    text_box = my_font.render(text,0,color)
    return surface.blit(text_box,position)
    

def print_instructions(surface,text,color,size,position):        
    my_font =  pygame.font.Font(word_font,size)
    text_box = my_font.render(text,0,color)
    return surface.blit(text_box,position)
    
    
    


