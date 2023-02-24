-- Insert sample users
INSERT INTO "user" (id, name)
VALUES (1, 'John'),
       (2, 'Jane');

-- Insert sample projects
INSERT INTO project (id, name)
VALUES (1, 'Asociación de vecinos'),
       (2, 'Club de deporte'),
       (3, 'Pilates club');

-- Associate projects with users
INSERT INTO user_project (user_id, project_id)
VALUES (1, 1),
       (1, 2),
       (2, 2),
       (2, 3);

-- Insert sample tasks
INSERT INTO task (id, name, complete, project_id)
VALUES (1, 'Reconstruir piscina', false, 1),
       (2, 'Limpieza de aparcamiento', true, 1),
       (3, 'Event Madrid Agosto 2023', false, 2),
       (4, 'Publicidad por Instragram', false, 2),
       (5, 'Cambiar sala', true, 3);

-- Get all projects with tasks for a particular user

SELECT p.name AS project_name, t.name AS task_name, t.complete
FROM "user" u
JOIN user_project up ON u.id = up.user_id
JOIN project p ON up.project_id = p.id
JOIN task t ON p.id = t.project_id
WHERE u.name = 'John'