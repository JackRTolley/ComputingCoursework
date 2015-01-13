import variables
from MathMan.game_logic import question_system


def create_questions():
    question1 = question_system.Question("Which of these is not an average?","Range","Mode","Median","Mean", "easy")
    variables.questions.append(question1)