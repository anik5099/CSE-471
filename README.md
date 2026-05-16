# Beginner Django Lab Series: Installation, Theory, and Project Workflow

## Purpose of This Guide

This README is designed for beginner students who are learning Django for the first time.

It explains:

1. How to install Django
2. How to create a Django project
3. How to create a Django app
4. Basic Django project structure
5. Important Django theory used in the five beginner projects
6. The proper learning order of the projects
7. How each project prepares students for the next one

The goal is to make students confident before they move to a larger Django blog project.

---

# 1. What is Django?

Django is a Python web framework.

A web framework helps us build websites faster by giving us ready-made tools for:

- URL routing
- HTML rendering
- form handling
- database handling
- authentication
- admin panel
- security features

Without a framework, we would need to write many things manually. Django gives us a proper structure for building web applications.

---

# 2. Basic Django Workflow

Most beginner Django projects follow this flow:

```txt
Browser Request
    ↓
urls.py
    ↓
views.py
    ↓
template.html
    ↓
Browser Response
```

Explanation:

- The user enters a URL in the browser.
- Django checks `urls.py` to find the matching route.
- The route calls a function from `views.py`.
- The view function returns an HTML page.
- The browser displays the final webpage.

---

# 3. Installing Python

Before installing Django, Python must be installed.

Check Python installation:

```bash
python --version
```

or:

```bash
py --version
```

If Python is installed correctly, you will see something like:

```txt
Python 3.x.x
```

If Python is not installed, download it from the official Python website and install it.

During installation, make sure to check:

```txt
Add Python to PATH
```

---

# 4. Installing Django

Open Command Prompt or PowerShell and run:

```bash
pip install django
```

Check Django version:

```bash
python -m django --version
```

If Django is installed correctly, you will see a version number.

Example:

```txt
5.0.6
```

or:

```txt
6.0.5
```

---

# 5. Creating a Django Project

A Django project is the main container of the website.

Command:

```bash
django-admin startproject myproject
```

Then go inside the project folder:

```bash
cd myproject
```

Run the server:

```bash
python manage.py runserver
```

Open this in browser:

```txt
http://127.0.0.1:8000/
```

If everything is correct, you will see the Django welcome page.

---

# 6. Creating a Django App

A Django app is a smaller module inside a project.

Example:

```bash
python manage.py startapp myapp
```

A project can have multiple apps.

Example:

```txt
school_project/
    students/
    teachers/
    courses/
```

Each app handles a specific part of the project.

---

# 7. Registering an App

After creating an app, add it to `INSTALLED_APPS`.

File:

```txt
settings.py
```

Example:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'myapp',
]
```

Why?

Django must know that the app exists.

---

# 8. Important Django Files

## 8.1 manage.py

This file is used to run Django commands.

Examples:

```bash
python manage.py runserver
python manage.py startapp appname
python manage.py makemigrations
python manage.py migrate
```

For these beginner projects, we mainly use:

```bash
python manage.py runserver
```

---

## 8.2 settings.py

This file contains project settings.

Important things inside `settings.py`:

- installed apps
- template settings
- database settings
- static file settings
- timezone settings

Example template setting:

```python
'DIRS': [BASE_DIR / 'templates']
```

This tells Django to look for HTML files inside the `templates` folder.

---

## 8.3 urls.py

This file controls routing.

Example:

```python
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('about/', views.about, name='about-page'),
]
```

Explanation:

- `''` means homepage
- `'about/'` means `/about/`
- `views.home` means call the `home` function from `views.py`

---

## 8.4 views.py

This file contains Python functions that handle requests.

Example:

```python
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
```

The view receives a request and returns a response.

---

## 8.5 templates folder

This folder contains HTML files.

Example:

```txt
templates/
    home.html
    about.html
```

Django uses templates to show webpages.

---

# 9. Rendering HTML Templates

To show an HTML file, use `render()`.

Example:

```python
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
```

This means:

```txt
When the home view is called, show home.html
```

---

# 10. Passing Data from View to Template

Sometimes we need to send data from Python to HTML.

Example:

```python
def student_details(request):
    student = {
        'name': 'Rahim',
        'department': 'CSE',
        'semester': '5th',
    }

    return render(request, 'student.html', {'student': student})
```

In HTML:

```html
<p>Name: {{ student.name }}</p>
<p>Department: {{ student.department }}</p>
<p>Semester: {{ student.semester }}</p>
```

This is called using a context dictionary.

---

# 11. Template Variables

Template variables are written using double curly braces:

```html
{{ variable_name }}
```

Example:

```html
<h1>{{ student.name }}</h1>
```

This displays the value of `student.name`.

---

# 12. Template Loop

To display multiple items, use a loop.

Example:

```python
students = [
    {'name': 'Rahim', 'department': 'CSE'},
    {'name': 'Karim', 'department': 'EEE'},
]
```

In template:

```html
{% for student in students %}
    <p>{{ student.name }} - {{ student.department }}</p>
{% endfor %}
```

This loop displays all students.

---

# 13. Template Condition

Django templates support conditions.

Example:

```html
{% if students %}
    <p>Students found.</p>
{% else %}
    <p>No students found.</p>
{% endif %}
```

This is useful when a list may be empty.

---

# 14. HTML Forms in Django

Forms are used to collect input from users.

Example:

```html
<form method="POST">
    {% csrf_token %}

    <input type="text" name="username">
    <button type="submit">Submit</button>
</form>
```

Important parts:

- `method="POST"` sends data to the backend.
- `{% csrf_token %}` protects the form.
- `name="username"` is used by Django to read the value.

---

# 15. GET vs POST

## GET Request

GET is usually used to open pages.

Example:

```txt
User opens /about/
```

## POST Request

POST is used to submit data.

Example:

```txt
User submits a form
```

In Django:

```python
if request.method == 'POST':
    # process form data
```

---

# 16. Reading Form Data

In Django, form data can be read using:

```python
request.POST.get('field_name')
```

Example:

```python
name = request.POST.get('username')
```

The `field_name` must match the HTML input name.

HTML:

```html
<input type="text" name="username">
```

View:

```python
username = request.POST.get('username')
```

If the names do not match, Django cannot read the value properly.

---

# 17. CSRF Token

CSRF means Cross-Site Request Forgery.

Django requires a CSRF token in POST forms for security.

Use this inside every POST form:

```html
{% csrf_token %}
```

Without it, Django may show:

```txt
CSRF verification failed
```

---

# 18. Redirect

After successfully submitting a form, we often redirect the user to another page.

Example:

```python
from django.shortcuts import redirect

return redirect('home-page')
```

Why use redirect?

It prevents the form from being submitted again when the browser is refreshed.

---

# 19. Temporary Data Storage Using Python List

In beginner projects without a database, we can temporarily store data in a Python list.

Example:

```python
tasks = []

tasks.append("Complete homework")
```

Important:

This data is not permanent.

If the server restarts, the list becomes empty.

This helps students understand why databases are needed in real projects.

---

# 20. The Five Beginner Django Projects

These five projects are arranged from easiest to slightly more interactive.

The order is important.

Students should not start with forms or complex projects immediately.

---

# Project 1: Hello Django

## Goal

Understand the basic Django flow:

```txt
URL → View → Template
```

## Pages

```txt
/
/about/
/contact/
```

## Main Concepts

- Creating a Django project
- Creating a Django app
- Registering the app
- Writing URL patterns
- Writing simple view functions
- Rendering HTML templates

## Why This Project Comes First

This project is the foundation.

Students learn how a URL opens a page.

No data, no form, no database.

Only routing and rendering.

## Example URL Pattern

```python
path('', views.home, name='home-page')
```

## Example View

```python
def home(request):
    return render(request, 'home.html')
```

## Example Template

```html
<h1>Hello Django</h1>
<p>This is my first Django page.</p>
```

---

# Project 2: Student Information Display

## Goal

Learn how to send data from `views.py` to an HTML template.

Main workflow:

```txt
URL → View → Context Dictionary → Template
```

## Pages

```txt
/
/student/
/course/
```

## Main Concepts

- Context dictionary
- Template variables
- Displaying dynamic data
- Passing Python dictionary to HTML

## Example View

```python
def student_details(request):
    student = {
        'name': 'Rahim Uddin',
        'department': 'CSE',
        'semester': '5th',
        'cgpa': 3.75,
    }

    return render(request, 'student_details.html', {'student': student})
```

## Example Template

```html
<p>Name: {{ student.name }}</p>
<p>Department: {{ student.department }}</p>
<p>Semester: {{ student.semester }}</p>
<p>CGPA: {{ student.cgpa }}</p>
```

## Why This Project Is Important

Students learn that webpages do not need to be static.

Data can come from Python and be displayed in HTML.

---

# Project 3: Student List

## Goal

Learn how to display multiple records.

Main workflow:

```txt
URL → View → List of Dictionaries → Template Loop
```

## Pages

```txt
/
/students/
/top-students/
```

## Main Concepts

- Python list
- Dictionary inside list
- Template loop
- HTML table
- Template condition
- Basic filtering logic

## Example Data

```python
students = [
    {'name': 'Rahim', 'department': 'CSE', 'cgpa': 3.75},
    {'name': 'Karim', 'department': 'EEE', 'cgpa': 3.45},
]
```

## Example Template Loop

```html
{% for student in students %}
    <p>{{ student.name }} - {{ student.department }} - {{ student.cgpa }}</p>
{% endfor %}
```

## Example Filtering

```python
top_students = []

for student in students:
    if student['cgpa'] >= 3.70:
        top_students.append(student)
```

## Why This Project Is Important

Most real websites show lists:

- student lists
- product lists
- blog post lists
- task lists
- user lists

This project teaches how to display repeated data.

---

# Project 4: Simple Calculator

## Goal

Learn how to collect user input using an HTML form.

Main workflow:

```txt
User Input → POST Request → View Logic → Result → Template
```

## Pages

```txt
/
/calculator/
/about/
```

## Main Concepts

- HTML form
- POST request
- CSRF token
- `request.POST.get()`
- String to number conversion
- Conditional logic
- Error handling
- Displaying result

## Example Form

```html
<form method="POST">
    {% csrf_token %}

    <input type="text" name="number1">
    <input type="text" name="number2">

    <select name="operation">
        <option value="add">Addition</option>
        <option value="subtract">Subtraction</option>
    </select>

    <button type="submit">Calculate</button>
</form>
```

## Example View Logic

```python
if request.method == 'POST':
    number1 = request.POST.get('number1')
    number2 = request.POST.get('number2')

    number1 = float(number1)
    number2 = float(number2)

    result = number1 + number2
```

## Why This Project Is Important

This is the first interactive project.

The user gives input, Django processes it, and the webpage shows the output.

This prepares students for real web applications.

---

# Project 5: To-Do List Without Database

## Goal

Build a small interactive app without using a database.

Main workflow:

```txt
Form Submit → POST Request → Add to Python List → Redirect → Display List
```

## Pages

```txt
/
/add-task/
/tasks/
/clear-tasks/
/about/
```

## Main Concepts

- HTML form
- POST request
- CSRF token
- Reading form data
- Python list as temporary storage
- Redirect
- Template loop
- Template condition
- Clearing list data

## Example Temporary Storage

```python
tasks = []
```

## Example Add Task View

```python
def add_task(request):
    if request.method == 'POST':
        task_title = request.POST.get('task_title')
        tasks.append(task_title)
        return redirect('task-list-page')

    return render(request, 'add_task.html')
```

## Example Display Template

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

## Important Limitation

Since there is no database, tasks disappear when the server restarts.

This is normal.

This limitation helps students understand why databases are needed in larger projects.

---

# 21. Recommended Teaching Order

Use this order in class:

```txt
1. Hello Django
2. Student Information Display
3. Student List
4. Simple Calculator
5. To-Do List Without Database
6. Blog Project
```

Do not skip the early projects.

Each project introduces one or two new ideas.

---

# 22. How the Projects Build Confidence

## Project 1

Students learn:

```txt
How a URL opens an HTML page
```

## Project 2

Students learn:

```txt
How Python data appears in HTML
```

## Project 3

Students learn:

```txt
How to display multiple records
```

## Project 4

Students learn:

```txt
How to collect input from users
```

## Project 5

Students learn:

```txt
How to build a small interactive app
```

After these five projects, students are more prepared for a blog project.

---

# 23. How These Projects Prepare Students for the Blog Project

| Beginner Project Concept | Blog Project Concept |
|---|---|
| URL routing | Blog URLs |
| Views | Signup, login, home, post views |
| Templates | Signup page, login page, home page |
| Context dictionary | Sending posts to templates |
| Template loop | Displaying all blog posts |
| HTML form | Signup, login, create post |
| POST request | User registration, login, post creation |
| Redirect | Redirect after signup/login/post creation |
| Temporary list | Database model |
| Task list | Blog post list |

---

# 24. Common Errors and Fixes

## Error 1: Page Not Found 404

Cause:

URL is not added correctly in `urls.py`.

Fix:

Check URL pattern:

```python
path('about/', views.about, name='about-page')
```

Then visit:

```txt
http://127.0.0.1:8000/about/
```

---

## Error 2: TemplateDoesNotExist

Cause:

Template file is missing or path is wrong.

Fix:

Check template folder:

```txt
templates/app_name/file.html
```

Check render function:

```python
return render(request, 'app_name/file.html')
```

---

## Error 3: App Not Found

Cause:

App is not registered in `INSTALLED_APPS`.

Fix:

Add app name in `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'myapp',
]
```

---

## Error 4: CSRF Verification Failed

Cause:

The form does not contain CSRF token.

Fix:

Add this inside the form:

```html
{% csrf_token %}
```

---

## Error 5: Form Data Not Coming

Cause:

Input field name and `request.POST.get()` name do not match.

Wrong:

```html
<input name="num1">
```

```python
number1 = request.POST.get('number1')
```

Correct:

```html
<input name="number1">
```

```python
number1 = request.POST.get('number1')
```

---

## Error 6: Server Not Running

Run:

```bash
python manage.py runserver
```

Then open:

```txt
http://127.0.0.1:8000/
```

---

# 25. Basic Commands Summary

## Create Project

```bash
django-admin startproject project_name
```

## Go Inside Project

```bash
cd project_name
```

## Create App

```bash
python manage.py startapp app_name
```

## Run Server

```bash
python manage.py runserver
```

## Stop Server

Press:

```txt
CTRL + C
```

## Install Django

```bash
pip install django
```

## Check Django Version

```bash
python -m django --version
```

---

# 26. Suggested Lab Teaching Strategy

For each project, follow this teaching pattern:

```txt
1. Explain the goal of the project
2. Draw the workflow
3. Create project and app
4. Configure settings.py
5. Write urls.py
6. Write simple views.py
7. Create templates
8. Run and test
9. Add one feature
10. Test again
11. Discuss common errors
```

Students should test after every small step.

Do not write the full project at once.

---

# 27. Final Advice for Students

Django may feel confusing at first because many files work together.

But every beginner should remember this simple flow:

```txt
URL → View → Template
```

When data is involved:

```txt
URL → View → Context → Template
```

When forms are involved:

```txt
Form → POST Request → View → Process Data → Template or Redirect
```

If students understand these three flows, they can understand most beginner Django projects.

---

# 28. Final Learning Outcome

After completing these five projects, students should be able to:

- create a Django project
- create and register an app
- configure templates
- write URL patterns
- write view functions
- render HTML pages
- pass data from views to templates
- use template variables
- use template loops
- use template conditions
- create HTML forms
- handle POST requests
- read form input
- redirect users
- build a small interactive Django app without database

This foundation is enough to confidently start a larger Django blog project.
