# Lab Manual: Project 5 - To-Do List Without Database

## Project Goal

This project is the final beginner project before moving to a larger Django project.

Students will build a simple To-Do List where they can:

1. Add a task
2. View all tasks
3. Clear all tasks

This project does not use a database.

Instead, it stores tasks temporarily in a Python list.

---

## Why This Project Is Important

This project combines concepts from previous projects:

| Previous Project | Concept Used Here |
|---|---|
| Project 1 | URL, view, template |
| Project 2 | Passing data from view to template |
| Project 3 | Template loop |
| Project 4 | HTML form and POST request |

This project feels like a real mini web application, but it is still simple enough for beginners.

---

## Main Workflow

```txt
User opens add task page
    ↓
User writes a task
    ↓
User submits the form
    ↓
Django receives POST request
    ↓
views.py reads task_title
    ↓
Task is added to Python list
    ↓
User is redirected to task list page
    ↓
Template displays all tasks using loop
```

---

## What Students Will Learn

By completing this project, students will learn:

1. How to create a multi-page Django project
2. How to create a form for user input
3. How to handle POST request
4. How to read input using `request.POST.get()`
5. How to store data temporarily in a Python list
6. How to redirect after form submission
7. How to display a list using `{% for %}` loop
8. How to use `{% if %}` condition in template
9. Why database is needed in real projects

---

## Project Pages

| URL | Purpose |
|---|---|
| `/` | Home page |
| `/add-task/` | Add new task |
| `/tasks/` | Display all tasks |
| `/clear-tasks/` | Clear all tasks |
| `/about/` | Project explanation |

---

## Recommended Coding Workflow

Students should not write everything at once.

Follow this order carefully.

---

## Step 1: Create the Django Project

Command:

```bash
django-admin startproject todo_site
```

Purpose:

This creates the main Django project.

---

## Step 2: Create the App

Command:

```bash
python manage.py startapp todo
```

Purpose:

The `todo` app will contain the to-do list related views.

---

## Step 3: Register the App

File:

```txt
todo_site/settings.py
```

Add:

```python
'todo',
```

inside `INSTALLED_APPS`.

Purpose:

Django must know that the `todo` app exists.

---

## Step 4: Configure Template Folder

File:

```txt
todo_site/settings.py
```

Update:

```python
'DIRS': [BASE_DIR / 'templates'],
```

Purpose:

This tells Django where the HTML templates are stored.

---

## Step 5: Create URL Patterns

File:

```txt
todo_site/urls.py
```

Code:

```python
from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home-page'),
    path('tasks/', views.task_list, name='task-list-page'),
    path('add-task/', views.add_task, name='add-task-page'),
    path('clear-tasks/', views.clear_tasks, name='clear-tasks-page'),
    path('about/', views.about, name='about-page'),
]
```

Explanation:

- `/` opens home page
- `/add-task/` opens form page
- `/tasks/` shows all tasks
- `/clear-tasks/` clears all tasks

---

## Step 6: Create Temporary Task Storage

File:

```txt
todo/views.py
```

Code:

```python
tasks = []
```

Explanation:

This list works like temporary memory.

When a new task is submitted, it will be added to this list.

Important:

This is not permanent storage.

If the server restarts, the list becomes empty.

---

## Step 7: Create Home View

File:

```txt
todo/views.py
```

Code:

```python
from django.shortcuts import render, redirect

tasks = []

def home(request):
    context = {
        'total_tasks': len(tasks),
    }
    return render(request, 'todo/home.html', context)
```

Explanation:

`len(tasks)` counts how many tasks currently exist.

---

## Step 8: Create Home Template

File:

```txt
templates/todo/home.html
```

Code:

```html
<h1>Project 5: To-Do List Without Database</h1>

<p>Total Tasks: {{ total_tasks }}</p>

<a href="/add-task/">Add New Task</a>
<a href="/tasks/">View Task List</a>
```

Test:

```txt
http://127.0.0.1:8000/
```

---

## Step 9: Create Add Task Form

File:

```txt
templates/todo/add_task.html
```

Code:

```html
<form method="POST">
    {% csrf_token %}

    <label>Task Title:</label>
    <input type="text" name="task_title">

    <button type="submit">Add Task</button>
</form>
```

Explanation:

- `method="POST"` sends data to the backend
- `{% csrf_token %}` protects the form
- `name="task_title"` is used by Django to read the input value

---

## Step 10: Create Add Task View

File:

```txt
todo/views.py
```

Code:

```python
def add_task(request):
    error = None

    if request.method == 'POST':
        task_title = request.POST.get('task_title')

        if task_title == '' or task_title is None:
            error = 'Task title cannot be empty.'
        else:
            tasks.append(task_title)
            return redirect('task-list-page')

    context = {
        'error': error,
    }
    return render(request, 'todo/add_task.html', context)
```

Explanation:

1. First, Django checks whether the request is POST.
2. Then it reads `task_title` from the submitted form.
3. If the task is empty, it shows an error.
4. If the task is valid, it adds the task to the `tasks` list.
5. Then it redirects the user to the task list page.

---

## Step 11: Create Task List View

File:

```txt
todo/views.py
```

Code:

```python
def task_list(request):
    context = {
        'tasks': tasks,
    }
    return render(request, 'todo/task_list.html', context)
```

Explanation:

This sends the full task list to the template.

---

## Step 12: Display Tasks Using Template Loop

File:

```txt
templates/todo/task_list.html
```

Code:

```html
{% if tasks %}
    <ol>
        {% for task in tasks %}
            <li>{{ task }}</li>
        {% endfor %}
    </ol>
{% else %}
    <p>No tasks added yet.</p>
{% endif %}
```

Explanation:

- `{% if tasks %}` checks whether the list has tasks
- `{% for task in tasks %}` loops through all tasks
- `{{ task }}` displays each task
- `{% else %}` shows a message if no task exists

---

## Step 13: Add Clear Task Feature

File:

```txt
todo/views.py
```

Code:

```python
def clear_tasks(request):
    tasks.clear()
    return redirect('task-list-page')
```

Explanation:

`tasks.clear()` removes all items from the list.

Then the user is redirected to the task list page.

---

## Step 14: Add About Page

File:

```txt
todo/views.py
```

Code:

```python
def about(request):
    return render(request, 'todo/about.html')
```

Purpose:

The about page explains what students are learning from the project.

---

## Final Full views.py

```python
from django.shortcuts import render, redirect

tasks = []

def home(request):
    context = {
        'total_tasks': len(tasks),
    }
    return render(request, 'todo/home.html', context)

def task_list(request):
    context = {
        'tasks': tasks,
    }
    return render(request, 'todo/task_list.html', context)

def add_task(request):
    error = None

    if request.method == 'POST':
        task_title = request.POST.get('task_title')

        if task_title == '' or task_title is None:
            error = 'Task title cannot be empty.'
        else:
            tasks.append(task_title)
            return redirect('task-list-page')

    context = {
        'error': error,
    }
    return render(request, 'todo/add_task.html', context)

def clear_tasks(request):
    tasks.clear()
    return redirect('task-list-page')

def about(request):
    return render(request, 'todo/about.html')
```

---

## Final Testing Checklist

Test these URLs:

```txt
http://127.0.0.1:8000/
http://127.0.0.1:8000/add-task/
http://127.0.0.1:8000/tasks/
http://127.0.0.1:8000/about/
```

Test these actions:

1. Open home page
2. Click Add New Task
3. Submit an empty task
4. Check whether error appears
5. Submit a valid task
6. Check whether the task appears in task list
7. Add multiple tasks
8. Click Clear All Tasks
9. Confirm that task list becomes empty

---

## Important Teaching Explanation

This project does not use a database.

So where are tasks stored?

Answer:

```python
tasks = []
```

This is a normal Python list.

It exists only while the Django server is running.

If the server is stopped and started again, the list becomes empty.

This limitation is useful for teaching.

It helps students understand why databases are needed in real projects.

---

## Common Student Mistakes

### Mistake 1: Forgetting CSRF Token

Error:

```txt
CSRF verification failed
```

Fix:

```html
{% csrf_token %}
```

inside the form.

---

### Mistake 2: Form Field Name Mismatch

If the input is:

```html
<input name="title">
```

but the view uses:

```python
request.POST.get('task_title')
```

Django will not get the value.

The names must match.

---

### Mistake 3: Forgetting Redirect

After adding a task, use:

```python
return redirect('task-list-page')
```

This prevents repeated form submission when the browser is refreshed.

---

### Mistake 4: Thinking the List Is Permanent

The task list is temporary.

It is not saved in a database.

This is expected behavior for this beginner project.

---

## How This Project Prepares Students for the Blog Project

The blog project will use similar ideas:

| To-Do Project | Blog Project |
|---|---|
| Add task | Create post |
| View task list | View blog posts |
| Form input | Post form input |
| Python list | Database model |
| Template loop | Display posts |
| Redirect | Redirect after creating post |

So this project is a very good bridge before the blog project.
