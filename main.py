from ToDoapp import app
from flask import render_template,request,redirect,url_for
import sqlite3,cgi
DATABASE = 'database.db'


@app.route('/')
def index():
    con = sqlite3.connect(DATABASE)
    db_tasks = con.execute('SELECT *,ROWID FROM tasks ').fetchall()     #テーブル行のIDとしてROWIDを取得
    con.close()

    tasks = []
    for row in db_tasks:
        tasks.append({'title': row[0], 'priority': row[1], 'rowid':row[2]})

    return render_template(
        'index.html',
        tasks=tasks
    )

@app.route('/form')
def form():
    return render_template(
        'form.html'
    )

@app.route('/register', methods=['POST'])       #タスク追加
def register():
    title = request.form['title']
    priority = request.form['priority']
    
    con = sqlite3.connect(DATABASE)
    con.execute('INSERT INTO tasks VALUES(?, ?)',[title,priority])
    con.commit()
    con.close()

    return redirect(url_for('index'))

@app.route('/eraser', methods=['POST','GET'])       #タスク完了
def eraser():
    param = request.form.getlist("kanryou")
    sql=('DELETE FROM tasks WHERE rowid=?')

    con = sqlite3.connect(DATABASE)
    con.execute(sql,param)
    con.commit()
    con.close()

    return redirect(url_for('index'))

