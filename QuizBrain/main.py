from game_data import data
from models import question_model
from models import quiz_brain


def get_questions():
    question_data = []
    for item in data.question_data:
        question_text = item["text"]
        question_answer = item["answer"]
        question = question_model.Question(question_text, question_answer)
        question_data.append(question)
    return question_data


def start_game():
    current_score = 0
    play = True
    quiz = quiz_brain.QuizBrain(get_questions())
    while quiz.still_has_questions():
        quiz.next_question()


start_game()
