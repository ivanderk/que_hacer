from models import db, User, Project, Task


# https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/queries/
# https://docs.sqlalchemy.org/en/20/orm/queryguide/index.html


def get_user_by_name(user_name):
    return db.session.execute(db.select(User).filter_by(name=user_name)).scalar_one()


def get_project_by_id(project_id):
    return db.session.execute(db.select(Project).filter_by(id=project_id)).scalar_one()


def get_projects_by_user(user_name):
    user = get_user_by_name(user_name)
    if user:
        return user.projects
    else:
        return []


def get_tasks_by_project(project_id):
    project = get_project_by_id(project_id)
    if project:
        return project.tasks
    else:
        return []


def create_task(project_id, task_name, description):
    task = Task(name=task_name, description=description, project_id=project_id, complete=False)
    db.session.add(task)
    db.session.commit()
    return task


def find_task_by_id(task_id):
    task = db.session.execute(db.select(Task).filter_by(id=task_id)).scalar_one()
    return task


def change_task(task, **props):
    for key in props.keys():
        setattr(task, key, props[key])

    db.session.commit()


def delete_task(task):
    db.session.delete(task)
    db.session.commit()
