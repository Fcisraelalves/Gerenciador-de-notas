import hashlib
from crud import DatabaseManager
from models import User
from useful import Response, Encryptor

class Auth:

    
    @classmethod
    def check_password(cls, password : str, password_hash : str):
        return Encryptor.to_hash(password) == password_hash

    @classmethod
    def login(cls, db_manager : DatabaseManager, username : str, password : str):
        user = db_manager.find_user(username)
        if not user:
            return Response(status=False, error='Usuário não encontrado')
        
        if cls.check_password(password, user.password_hash):
            return Response(status=True)
        
        return Response(status=False, error='A senha está incorreta')
        
    
