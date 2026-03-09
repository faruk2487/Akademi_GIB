from datetime import datetime

class ExamResult:
    def __init__(self, user_id, score, total_questions, correct_answers, exam_date=None):
        self.user_id = user_id
        self.score = score
        self.total_questions = total_questions
        self.correct_answers = correct_answers
        self.exam_date = exam_date or datetime.now()
        self.success_rate = (correct_answers / total_questions * 100) if total_questions > 0 else 0
    
    def to_dict(self):
        return {
            'user_id': self.user_id,
            'score': self.score,
            'total_questions': self.total_questions,
            'correct_answers': self.correct_answers,
            'success_rate': self.success_rate,
            'exam_date': self.exam_date.strftime('%Y-%m-%d %H:%M:%S')
        }
