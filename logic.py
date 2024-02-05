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

    def add_task(self, user_id, name, description): 
        conn = sqlite3.connect(self.database)
        with conn:
            conn.execute("INSERT INTO tasks (name, description, user_id) VALUES (?, ?, ?)", (name, description, user_id))
            conn.commit()

    def delete_task(self, task_name, user_id): 
        conn = sqlite3.connect(self.database)
        with conn:
            conn.execute("DELETE FROM tasks WHERE name = ? AND user_id = ?", (task_name, user_id))
            conn.commit()

    def show_task(self, user_id):
        conn = sqlite3.connect(self.database)
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT name FROM tasks WHERE user_id = ?", (user_id,))
            return cur.fetchall()
            

