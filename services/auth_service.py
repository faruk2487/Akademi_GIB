from database import Database

class AuthService:

    def __init__(self):
        self.db = Database()

    def login(self, username, password):
        user = self.db.get_user(username)

        if user and user["password"] == password:
            return True

        return False

    def register(self, username, password):
        return self.db.create_user(username, password)
