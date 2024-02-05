import sqlite3

class TaskManager:
    def __init__(self, database):
        self.database = database

    def create_table(self): 
        conn = sqlite3.connect(self.database)
        with conn:
            conn.execute("""
            CREATE TABLE IF NOT EXISTS tasks(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            description TEXT,
            user_id INTEGER NOT NULL
            )""")
            conn.commit()

    def add_task(self, user_id, name, description): #3
        conn = sqlite3.connect(self.database)
        with conn:
            conn.execute("INSERT INTO tasks (name, description, user_id) VALUES (?, ?, ?)", (name, description, user_id))
            conn.commit()

    def delete_task(self, task_name): #4
        conn = sqlite3.connect(self.database)
        with conn:
            conn.execute("DELETE FROM tasks WHERE name = ?", (task_name,))
            conn.commit()
        

