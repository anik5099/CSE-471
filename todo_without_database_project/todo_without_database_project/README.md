# Project 5: To-Do List Without Database

A beginner-friendly Django project that teaches form submission and temporary data handling without using a database.

## Run

```bash
cd todo_without_database_project
python manage.py runserver
```

Open:

```txt
http://127.0.0.1:8000/
```

## Pages

- `/` - Home page
- `/add-task/` - Add task form
- `/tasks/` - View task list
- `/clear-tasks/` - Clear all tasks
- `/about/` - Project explanation

## Database

No database is used.

## Important Note

Tasks are stored in a Python list. They remain available only while the server is running.
If the server restarts, the list becomes empty.
