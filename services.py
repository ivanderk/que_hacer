from data import get_projects_by_user, get_tasks_by_project

def getProjects(user_id):
    projects = get_projects_by_user(user_id)
    return projects
    #return [{'id': project.id, 'name': project.name} for project in projects]

def getTasks(project_id):
    tasks = get_tasks_by_project(project_id)
    return tasks
    #return [{'id': task.id, 'name': task.name, 'complete': task.complete} for task in tasks]
