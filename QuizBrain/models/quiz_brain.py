from game_data import data
from models import question_model

class QuizBrain:

    def __init__(self, questions_list: []):
        self.question_number = 0
        self.game_score = 0
        self.questions_list = questions_list

    def still_has_questions(self):
        if self.question_number < len(self.questions_list):
            print("You have completed the quiz")
            print(f"Your final score is { self.game_score } / { self.question_number }")
            return False
        return True

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        correct_answer = current_question.answer
        users_answer = input(f"Q.{ self.question_number } : { current_question.text } (True/False)")
        self.check_answer(users_answer, correct_answer)

    def check_answer(self, users_answer, correct_answer):
        if users_answer.lower() == correct_answer.lower():
            self.game_score += 1
            print("That is correct")
        else:
            print("That is correct")
        print(f"The correct answer is { correct_answer.lower }")
        print(f"Your current score is { self.game_score } / { self.question_number }")
        print("\n")
