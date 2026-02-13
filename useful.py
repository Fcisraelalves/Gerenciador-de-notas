import hashlib
from models import User

class Validator:
    @classmethod
    def validate_option(cls, message : str, max : int, min : int = 1):
        option = int(input(message))
        while option < min or option > max:
            print(f'ERRO: selecione uma opção válida.')
            option = int(input(message))
        return option

class Session:
    def __init__(self, user : User = None):
        self.user = user

class Response:
    def __init__(self, status : bool, error : str = None):
        self.status = status
        self.error = error

class Encryptor:
    @classmethod
    def to_hash(cls, password : str):
        password_hash = hashlib.sha256()
        password_hash.update(password.encode('utf-8'))
        return password_hash.hexdigest()
    
