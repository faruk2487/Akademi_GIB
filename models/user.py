import bcrypt

class User:
    def __init__(self, username, password=None, user_id=None):
        self.user_id = user_id
        self.username = username
        self.password = password
    
    @staticmethod
    def hash_password(password):
        """Şifreyi şifrele"""
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    @staticmethod
    def verify_password(password, hashed_password):
        """Şifreyi doğrula"""
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
    
    def to_dict(self):
        return {
            'id': self.user_id,
            'username': self.username
        }
