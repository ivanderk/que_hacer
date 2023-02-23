# project/app.py
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import sys
from models import Task, Project, init_app
from services import getProjects, getTasks

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = init_app(app)

app.app_context().push()
db.create_all()

# id name
# 1 John
# 2 Jane
active_user_id = 1 

@app.route('/')
def index():
    projects = getProjects(active_user_id)
    if len(projects) > 0:
        tasks = getTasks(projects[0].id)
        return render_template('index.html', tasks=tasks, projects=projects)
    else:
        return render_template('error.html', error_message="No esta asignado a un proyecto. Por favor, avisa el administrador")
    # projects = Project.query.all()
    # return render_template('index.html', tasks=tasks, projects=projects)
    

@app.route('/add', methods=['POST'])
def add():
    task = Task(name=request.form['task_name'], description=request.form['task_name'], complete=False)
    db.session.add(task)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/complete/<id>')
def complete(id):
    task = Task.query.filter_by(id=int(id)).first()
    task.complete = not task.complete
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete', methods=['POST'])
def delete():
    id = int(request.form['id'])
    task = Task.query.filter_by(id=id).first()
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
