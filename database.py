import sqlite3

class DBConnector:
    
    @classmethod
    def get_connection(cls):
        return sqlite3.connect("notes.db")
    

class DBLauncher:

    @classmethod
    def create_tables(cls):
        with DBConnector.get_connection() as conn:
            cursor = conn.cursor()

            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS user (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username VARCHAR(150) UNIQUE NOT NULL,
                password_hash VARCHAR(100) NOT NULL
                )
                """
            )

            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS note (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                content TEXT,
                FOREIGN KEY (user_id) REFERENCES user(id)
                ON DELETE CASCADE
                )
                """
            )
            
                        
