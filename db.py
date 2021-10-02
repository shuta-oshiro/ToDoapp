import sqlite3

DATABASE = 'database.db'

def create_tasks_table():               #データベースにtasksテーブルを作成
    con = sqlite3.connect(DATABASE)
    con.execute("CREATE TABLE IF NOT EXISTS tasks (title , priority)")
    con.close()

