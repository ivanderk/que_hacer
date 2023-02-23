from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker 
from models import User, Project, Task

# Set up the database connection (NO ES IGUAL A FLASK. NO ESTAMOS EN UN PROCESO DE FLASK AHORA!!!!)
engine = create_engine('sqlite:///./instance/tasks.db')
Session = sessionmaker(bind=engine)
session = Session()

#--------------------------------------------------------------------------
print(f"SQLAlchemy example using SQL style select and not the deprecated Query interface")

# Retrieve the user with the name "John" and ID 1
john = session.execute(select(User).where((User.name == 'John') & (User.id == 1))).scalar_one()

# Retrieve all tasks for a project with ID 1 and associated with John
tasks = session.execute(select(Task.name).join(Task.project).join(Project.users).where((Project.id == 1) & (User.id == john.id)))

# Print the task names
for task in tasks:
    print(f"task: {task.name}")

#--------------------------------------------------------------------------
print(f"SQLAlchemy example more in tune with Flask ORM atterns")

john = session.execute(select(User).filter_by(id=1)).scalar_one()
tasks = john.projects[0].tasks

# Print the task names
for task in tasks:
    print(f"task: {task.name}")