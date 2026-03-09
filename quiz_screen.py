from kivy.uix.screenmanager import Screen
from services.quiz_service import QuizService

class QuizScreen(Screen):

    def start_quiz(self, questions):

        self.quiz = QuizService(questions)
        self.load_question()

    def load_question(self):

        q = self.quiz.next_question()

        if not q:
            self.finish_exam()
            return

        self.current_question = q
