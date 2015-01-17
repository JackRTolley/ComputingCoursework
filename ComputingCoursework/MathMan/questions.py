import variables
from MathMan.game_logic import question_system


def create_questions():
    question1 = question_system.Question("Which of these is not an average?","Range","Mode","Median","Mean", "easy")
    variables.questions.append(question1)
    question2 = question_system.Question("What is 11 + 20?","31","45","4","9","easy")
    variables.questions.append(question2)