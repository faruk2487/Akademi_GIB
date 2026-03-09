class Scoring:
    def __init__(self, correct_points=10, wrong_points=0):
        self.correct_points = correct_points
        self.wrong_points = wrong_points
        self.total_score = 0
        self.correct_answers = 0
        self.wrong_answers = 0
    
    def add_correct_answer(self):
        """Doğru cevap ekle"""
        self.correct_answers += 1
        self.total_score += self.correct_points
    
    def add_wrong_answer(self):
        """Yanlış cevap ekle"""
        self.wrong_answers += 1
        self.total_score += self.wrong_points
    
    def get_score(self):
        """Toplam puanı getir"""
        return self.total_score
    
    def get_success_rate(self):
        """Başarı oranını getir (%)"""
        total = self.correct_answers + self.wrong_answers
        if total == 0:
            return 0
        return (self.correct_answers / total) * 100
    
    def reset(self):
        """Skoru sıfırla"""
        self.total_score = 0
        self.correct_answers = 0
        self.wrong_answers = 0
    
    def get_summary(self):
        """Özet bilgi getir"""
        return {
            'total_score': self.total_score,
            'correct_answers': self.correct_answers,
            'wrong_answers': self.wrong_answers,
            'success_rate': self.get_success_rate()
        }
