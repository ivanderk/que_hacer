from models import db, User, Project, Task

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
