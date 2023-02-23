from models import db, User, Project, Task

# DEPRECATED - NO USAR!!!!

def get_user_by_id(user_id):
    return User.query.get(user_id)

def get_project_by_id(project_id):
    return Project.query.get(project_id)

def get_projects_by_user(user_id):
    user = get_user_by_id(user_id)
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

def find_task_by_id(id):
    task = Task.query.filter_by(id=int(id)).first()
    return task

def change_task(task, **props):
    for key in props.keys():
        setattr(task, key, props[key])
        
    db.session.commit()
    
def delete_task(task):
    db.session.delete(task)
    db.session.commit()