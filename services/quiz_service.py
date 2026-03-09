import random

class QuizService:

    def __init__(self, questions):
        self.questions = questions
        self.current_index = 0
        self.score = 0

    def get_next_question(self):
        if self.current_index < len(self.questions):
            q = self.questions[self.current_index]
            self.current_index += 1
            return q
        return None

    def check_answer(self, question, answer):
        if question.correct_answer == answer:
            self.score += 1
            return True
        return False

    def get_score(self):
        return self.score
