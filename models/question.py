class Question:
    def __init__(self, id, question_text, option_a, option_b, option_c, option_d, correct_answer, category="Genel"):
        self.id = id
        self.question_text = question_text
        self.options = {
            'A': option_a,
            'B': option_b,
            'C': option_c,
            'D': option_d
        }
        self.correct_answer = correct_answer
        self.category = category
    
    def check_answer(self, user_answer):
        """Cevabı kontrol et"""
        return user_answer.upper() == self.correct_answer.upper()
    
    def to_dict(self):
        return {
            'id': self.id,
            'question_text': self.question_text,
            'options': self.options,
            'category': self.category
        }
