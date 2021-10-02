from flask import Flask
app = Flask(__name__)
import ToDoapp.main

from ToDoapp import db
db.create_tasks_table()

