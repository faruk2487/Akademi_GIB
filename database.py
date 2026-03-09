import sqlite3
import os
from config import DB_PATH

class Database:
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.init_db()
    
    def init_db(self):
        """Veritabanını başlat ve tabloları oluştur"""
        self.conn = sqlite3.connect(DB_PATH)
        self.cursor = self.conn.cursor()
        
        # Kullanıcılar tablosu
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Sorular tablosu
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS questions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question_text TEXT NOT NULL,
                option_a TEXT NOT NULL,
                option_b TEXT NOT NULL,
                option_c TEXT NOT NULL,
                option_d TEXT NOT NULL,
                correct_answer TEXT NOT NULL,
                category TEXT
            )
        ''')
        
        # Sınav sonuçları tablosu
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS exam_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                score INTEGER,
                total_questions INTEGER,
                correct_answers INTEGER,
                exam_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        ''')
        
        self.conn.commit()
    
    def add_user(self, username, password):
        """Yeni kullanıcı ekle"""
        try:
            self.cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)',
                              (username, password))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
    
    def get_user(self, username):
        """Kullanıcı bilgisini getir"""
        self.cursor.execute('SELECT id, username, password FROM users WHERE username = ?', 
                          (username,))
        return self.cursor.fetchone()
    
    def add_question(self, question_text, options, correct_answer, category="Genel"):
        """Soru ekle"""
        self.cursor.execute('''
            INSERT INTO questions 
            (question_text, option_a, option_b, option_c, option_d, correct_answer, category)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (question_text, options[0], options[1], options[2], options[3], correct_answer, category))
        self.conn.commit()
    
    def get_all_questions(self):
        """Tüm soruları getir"""
        self.cursor.execute('SELECT * FROM questions')
        return self.cursor.fetchall()
    
    def save_exam_result(self, user_id, score, total_questions, correct_answers):
        """Sınav sonucunu kaydet"""
        self.cursor.execute('''
            INSERT INTO exam_results (user_id, score, total_questions, correct_answers)
            VALUES (?, ?, ?, ?)
        ''', (user_id, score, total_questions, correct_answers))
        self.conn.commit()
    
    def get_user_results(self, user_id):
        """Kullanıcının sınav sonuçlarını getir"""
        self.cursor.execute('SELECT * FROM exam_results WHERE user_id = ? ORDER BY exam_date DESC',
                          (user_id,))
        return self.cursor.fetchall()
    
    def close(self):
        """Veritabanını kapat"""
        if self.conn:
            self.conn.close()
