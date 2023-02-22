-- Insert sample users
INSERT INTO "user" (id, name)
VALUES (1, 'John'),
       (2, 'Jane');

-- Insert sample projects
INSERT INTO project (id, name)
VALUES (1, 'Project 1'),
       (2, 'Project 2'),
       (3, 'Project 3');

-- Associate projects with users
INSERT INTO user_project (user_id, project_id)
VALUES (1, 1),
       (1, 2),
       (2, 2),
       (2, 3);

-- Insert sample tasks
INSERT INTO task (id, name, complete, project_id)
VALUES (1, 'Task 1', false, 1),
       (2, 'Task 2', true, 1),
       (3, 'Task 3', false, 2),
       (4, 'Task 4', false, 2),
       (5, 'Task 5', true, 3);

-- Get all projects with tasks for a particular user

SELECT p.name AS project_name, t.name AS task_name, t.complete
FROM "user" u
JOIN user_project up ON u.id = up.user_id
JOIN project p ON up.project_id = p.id
JOIN task t ON p.id = t.project_id
WHERE u.name = 'John'