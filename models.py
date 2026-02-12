from enum import StrEnum

class Note:
    FIELDS = ['id', 'user_id', 'text']
    def __init__(self, id : int, user_id : int, text : str):
        self.id = id
        self.user_id = user_id
        self.text = text

    @classmethod
    def from_row(cls, row):
        kwargs = {field : value for field, value in zip(Note.FIELDS, row)}
        return cls(**kwargs)
    
class User:
    FIELDS = ['id', 'username', 'password_hash']
    def __init__(self, id : int, username : str, password_hash : str):
        self.id = id
        self.username = username
        self.password_hash = password_hash

    @classmethod
    def from_row(cls, row):
        kwargs = {field : value for field, value in zip(User.FIELDS, row)}
        return cls(**kwargs)
    
