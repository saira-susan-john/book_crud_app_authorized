from repositories.user_repository import UserRepository
import bcrypt
import jwt
from datetime import datetime, timedelta


JWT_SECRET = 'your_secret_key'
JWT_ALGORITHM = 'HS256'

class UserService:
    def __init__(self, db_config):
        self.user_repository = UserRepository(**db_config)

    def register_user(self, username, password):
    
        if self.user_repository.get_user_by_username(username):
            print("Username already exists.")
            return False

        
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        self.user_repository.add_user(username, hashed_password)
        return True

    def login_user(self, username, password):
        
        user = self.user_repository.get_user_by_username(username)
        if not user:
            print("User not found.")
            return None

        
        if not bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):

            print("Incorrect password.")
            return None

        
        payload = {
            'username': user['username'],

            'exp': datetime.utcnow() + timedelta(hours=1)
        }
        token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
        return token
