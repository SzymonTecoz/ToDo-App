import tkinter as tk
from tkinter import messagebox
import sqlite3

def init_db(): #inicjalizacja bazy danych
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        task NEXT NOT NULL,
        status INTEGER NOT NULL DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

def add_task(task): #dodawanie nowego taska
    conn = sqlite3. connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
    conn.commit()
    conn.close()

def get_task():
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, task, status FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def complete_task(task_id): #do kompletowania tasków
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET status = 1 WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id =?", (task_id,))
    conn.commit()
    conn.close()

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do App")
        self.task_var = tk.StringVar()

        self.task_entry = tk.Entry(self.root, textvariable=self.task_var)
        self.task_entry.pack(pady=5)

        self.add_button = tk.Button(self.root, text="Add task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.tasks_frame = tk.Frame(self.root)
        self.tasks_frame.pack(pady=10)

        self.load_tasks()

    def add_task(self):
        task = self.task_var.get()
        if task:
            add_task(task)
            self.task_var.set("")
            self.load_tasks()
        else:
            messagebox.showwarning("Warning", "Task can't be empty!")

    def load_tasks(self):
        for widget in self.tasks_frame.winfo_children():
            widget.destroy()

        tasks = get_task()
        for task_id, task, status in tasks:
            task_frame = tk.Frame(self.tasks_frame)
            task_frame.pack( fill="x", pady=5)

            task_label = tk.Label(task_frame, text = task, anchor="w")
            task_label.pack(side="left", expand=True, fill = "x")

            complete_button = tk.Button(task_frame, text="Complete", command=lambda id = task_id: self.complete_task(id))
            complete_button.pack(side="right")

            delete_button = tk.Button(task_frame, text = "Delete", command=lambda  id = task_id: self.delete_task(id))
            delete_button.pack(side="right")


            if status:
                task_label.config(fg="gray")

    def complete_task(self, task_id):
        complete_task(task_id)
        self.load_tasks()

    def delete_task(self, task_id):
        delete_task(task_id)
        self.load_tasks()

if __name__ == "main":
    init_db()
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()