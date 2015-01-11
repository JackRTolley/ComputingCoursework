"""Stores the key variables of the game for easy editing/fetching"""


#Pygame structure
x_resolution = /NON//NON/
y_resolution = /NON//NON/

#Question system
difficulty_setting = "medium"

#Game variables
speed_setting = "/NON/"
score         = ""



# Grid
grid = [['BDR','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','BDL','BDR','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','BDL'],
        ['B_V','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','B_V','B_V','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','B_V'],
        ['B_V','P_N','BDR','B_H','B_H','BDL','P_N','BDR','B_H','B_H','B_H','BDL','P_N','B_V','B_V','P_N','BDR','B_H','B_H','B_H','BDL','P_N','BDR','B_H','B_H','BDL','P_N','B_V'],
        ['B_V','P_B','B_V',/NON/,/NON/,'B_V','P_N','B_V',/NON/,/NON/,/NON/,'B_V','P_N','B_V','B_V','P_N','B_V',/NON/,/NON/,/NON/,'B_V','P_N','B_V',/NON/,/NON/,'B_V','P_B','B_V'],
        ['B_V','P_N','BUR','B_H','B_H','BUL','P_N','BUR','B_H','B_H','B_H','BUL','P_N','BUR','BUL','P_N','BUR','B_H','B_H','B_H','BUL','P_N','BUR','B_H','B_H','BUL','P_N','B_V'],
        ['B_V','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','B_V'],
        ['B_V','P_N','BDR','B_H','B_H','BDL','P_N',/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,'P_N','BDR','B_H','B_H','BDL','P_N','B_V'],
        ['B_V','P_N','BUR','B_H','B_H','BUL','P_N',/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,'P_N','BUR','B_H','B_H','BUL','P_N','B_V'],
        ['B_V','P_N','P_N','P_N','P_N','P_N','P_N',/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,'P_N','P_N','P_N','P_N','P_N','P_N','B_V'],
        ['B_V',/NON/,/NON/,/NON/,/NON/,/NON/,'P_N',/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,'P_N',/NON/,/NON/,/NON/,/NON/,/NON/,'B_V'],
        ['B_V',/NON/,/NON/,/NON/,/NON/,/NON/,'P_N',/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,'P_N',/NON/,/NON/,/NON/,/NON/,/NON/,'B_V'],
        ['B_V',/NON/,/NON/,/NON/,/NON/,/NON/,'P_N',/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,'P_N',/NON/,/NON/,/NON/,/NON/,/NON/,'B_V'],
        ['B_V',/NON/,/NON/,/NON/,/NON/,/NON/,'P_N',/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,'P_N',/NON/,/NON/,/NON/,/NON/,/NON/,'B_V'],
        ['B_V',/NON/,/NON/,/NON/,/NON/,/NON/,'P_N',/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,'P_N',/NON/,/NON/,/NON/,/NON/,/NON/,'B_V'],
        ['B_V',/NON/,/NON/,/NON/,/NON/,/NON/,'P_N',/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,'P_N',/NON/,/NON/,/NON/,/NON/,/NON/,'B_V'],
        ['B_V',/NON/,/NON/,/NON/,/NON/,/NON/,'P_N',/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,'P_N',/NON/,/NON/,/NON/,/NON/,/NON/,'B_V'],
        ['B_V',/NON/,/NON/,/NON/,/NON/,/NON/,'P_N',/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,'P_N',/NON/,/NON/,/NON/,/NON/,/NON/,'B_V'],
        ['B_V',/NON/,/NON/,/NON/,/NON/,/NON/,'P_N',/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,'P_N',/NON/,/NON/,/NON/,/NON/,/NON/,'B_V'],
        ['B_V',/NON/,/NON/,/NON/,/NON/,/NON/,'P_N',/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,'P_N',/NON/,/NON/,/NON/,/NON/,/NON/,'B_V'],
        ['B_V',/NON/,/NON/,/NON/,/NON/,/NON/,'P_N',/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,'P_N',/NON/,/NON/,/NON/,/NON/,/NON/,'B_V'],
        ['B_V',/NON/,/NON/,/NON/,/NON/,/NON/,'P_N',/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,'P_N',/NON/,/NON/,/NON/,/NON/,/NON/,'B_V'],
        ['B_V','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N',/NON/,/NON/,'P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','B_V'],
        ['B_V','P_N',/NON/,/NON/,/NON/,/NON/,'P_N',/NON/,/NON/,/NON/,/NON/,/NON/,'P_N',/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,'P_N',/NON/,/NON/,/NON/,/NON/,'P_N','B_V'],
        ['B_V','P_N',/NON/,/NON/,/NON/,/NON/,'P_N',/NON/,/NON/,/NON/,/NON/,/NON/,'P_N',/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,'P_N',/NON/,/NON/,/NON/,/NON/,'P_N','B_V'],
        ['B_V','P_B','P_N','P_N',/NON/,/NON/,'P_N','P_N','P_N','P_N','P_N','P_N','P_N',/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,'P_N',/NON/,/NON/,'P_N','P_N','P_B','B_V'],
        ['B_V',/NON/,/NON/,'P_N',/NON/,/NON/,'P_N',/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,'P_N',/NON/,/NON/,'P_N',/NON/,/NON/,'B_V'],
        ['B_V',/NON/,/NON/,'P_N',/NON/,/NON/,'P_N',/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,'P_N',/NON/,/NON/,'P_N',/NON/,/NON/,'B_V'],
        ['B_V','P_N','P_N','P_N','P_N','P_N','P_N',/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,'P_N','P_N','P_N','P_N','P_N','P_N','B_V'],
        ['B_V','P_N',/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,'P_N','B_V'],
        ['B_V','P_N',/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,/NON/,'P_N','B_V'],
        ['B_V','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','P_N','B_V'],
        ['BUR','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','B_H','BUL']]
        
        