# project/app.py
from flask import Flask, render_template, request
from models import init_app
from data import get_projects_by_user, get_tasks_by_project, create_task, find_task_by_id, change_task, delete_task

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
    projects = get_projects_by_user(active_user_id)
    if len(projects) > 0:
        tasks = get_tasks_by_project(projects[0].id)
        return render_template('index.html', tasks=tasks, projects=projects)
    else:
        return render_template('error.html',
                               error_message="No esta asignado a un proyecto. Por favor, avisa el administrador")


@app.route('/tasks')
def tasks():
    project_id = request.args.get("project_id")
    return render_tasks(project_id)


def render_tasks(project_id):
    tasks = get_tasks_by_project(project_id)
    return render_template('tasks.html', tasks=tasks)


@app.route('/add', methods=['POST'])
def add():
    project_id = request.form['project_id']
    task_name = request.form['task_name']
    description = request.form['task_description']
    create_task(project_id, task_name, description)
    return render_tasks(project_id)


@app.route('/complete/<id>')
def complete(id):
    task = find_task_by_id(id)
    project_id = task.project_id
    newcomplete = not task.complete
    change_task(task, complete=newcomplete)
    return render_tasks(project_id)


@app.route('/delete', methods=['POST'])
def delete():
    id = int(request.form['id'])
    task = find_task_by_id(id)
    project_id = task.project_id
    delete_task(task)
    return render_tasks(project_id)


if __name__ == '__main__':
    app.run(debug=True)
