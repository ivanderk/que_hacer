# project/app.py
from flask import Flask, render_template, request, redirect, session, url_for
from models import init_app, User
from data import get_projects_by_user, get_tasks_by_project, create_task, find_task_by_id, change_task, delete_task
from middleware import authenticate_handler

app = Flask(__name__)

# The SECRET_KEY is used to encrypt session data in (persistent) cookies. 
# >>> import secrets; secrets.token_hex(32)
app.config['SECRET_KEY'] = '642918690903c342d812d16cd33a4de4c8692483462550c9ddcd4303621cc1b2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = init_app(app)

app.app_context().push()
db.create_all()

@app.before_request
def before_request():
    return authenticate_handler(None)

@app.after_request
def after_request(response):
    return authenticate_handler(response)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(name=username).first()

        if user is None or not user.check_password(password):
            error = 'Invalid username or password'
        else:
            #Note: Flask session. NOT SqlAlchemy...
            session['user_name'] = user.name
            return redirect(url_for('index'))

    return render_template('login.html', error=error)

@app.route('/logout', methods=['GET'])
def logout():
   
    #Note: Flask session. NOT SqlAlchemy...
    del session['user_name'] 
    return redirect(url_for('login'))
        
@app.route('/')
def index():
    
    projects = get_projects_by_user(session['user_name'])
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
