import hashlib
from models import User
import getpass
from enum import StrEnum
from crud import DatabaseManager


class Validator:
    @classmethod
    def validate_option(cls, message : str, max : int, min : int = 1):
        option = int(input(message))
        while option < min or option > max:
            print(f'ERRO: selecione uma opção válida.')
            option = int(input(message))
        return option
    
    @classmethod
    def validate_two_passwords(cls):
        password_1 = getpass.getpass('Insira a sua senha: ')
        password_2 = getpass.getpass('Confirme a sua senha: ')

        if password_1 == password_2:
            return Response(status=True, data={'password' : password_1})
        return Response(status=False, error='As senhas não correspondem')

    @classmethod
    def validate_user(cls):
        username = str(input('Insira o seu usuário: '))
        user = DatabaseManager().find_user(username)
        if user:
            return Response(status=False, error='Já existe um usuário com esse username!')
        return Response(status=True, data={'username' : username})
    
class Session:
    def __init__(self, user : User = None):
        self.user = user

class Response:
    def __init__(self, status : bool, error : str = None, data : dict = None):
        self.status = status
        self.error = error
        self.data = data

class Encryptor:
    @classmethod
    def to_hash(cls, password : str):
        password_hash = hashlib.sha256()
        password_hash.update(password.encode('utf-8'))
        return password_hash.hexdigest()
    
