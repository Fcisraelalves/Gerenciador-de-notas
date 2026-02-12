from app import App
from crud import DatabaseManager

app = App(DatabaseManager())
app.run()