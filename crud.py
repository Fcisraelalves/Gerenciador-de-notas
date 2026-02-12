from database import DBConnector
from useful import Encryptor
from models import Note, User

class DatabaseManager:

    def new_note(self, user_id : int, text : str):
        with DBConnector.get_connection() as conn:
            cursor = conn.cursor()
            
            cursor.execute(
                """
                INSERT INTO note (user_id, text)
                VALUES (?, ?);
                """, [user_id, text]
            )

            conn.commit()

    def new_user(self, username : str, password : str):
        password_hash = Encryptor.to_hash(password)

        with DBConnector.get_connection() as conn:
            cursor = conn.cursor()

            cursor.execute(
                """
                INSERT INTO user (username, password_hash)
                VALUES (?, ?);
                """, [username, password_hash]
            )
        
    def list_notes(self, user_id : int):

        with DBConnector.get_connection() as conn:
            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT * FROM note WHERE user_id = ?;
                """, [user_id]
            )

            results = cursor.fetchall()
        if results:
            return [Note.from_row(row) for row in results]
        return results
    
    def find_user(self, username : str):
        with DBConnector.get_connection() as conn:
            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT * FROM user WHERE username = ?;
                """, [username]
            )
        
            result = cursor.fetchone()
        if result:
            return User.from_row(result)
        return result
    