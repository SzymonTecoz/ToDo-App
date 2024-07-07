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
    