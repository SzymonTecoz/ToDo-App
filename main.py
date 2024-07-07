import tkinter as tk
from tkinter import messagebox
import sqlite3

def init_db():
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

