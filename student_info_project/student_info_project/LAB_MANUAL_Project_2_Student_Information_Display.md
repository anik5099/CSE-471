# Lab Manual: Project 2 - Student Information Display

## Project Goal

In Project 1, students learned the basic Django flow:

URL → View → Template

In this project, students will learn the next important concept:

URL → View → Data/Context → Template

This means the view will not only open an HTML page, but it will also send data to that page.

---

## What Students Will Learn

By completing this project, students will learn:

1. How to create multiple pages in Django
2. How to send data from `views.py` to an HTML template
3. How to use a Python dictionary as template data
4. How to display dynamic values using `{{ variable }}`
5. How to display list items using `{% for %}` loop
6. How Django connects URL, view, context, and template

---

## Project Pages

This project has three pages:

| URL | Purpose |
|---|---|
| `/` | Home page |
| `/student/` | Shows student information |
| `/course/` | Shows course information and topic list |

---

## Recommended Coding Workflow

Do not write the whole project at once. Code and test step by step.

### Step 1: Create the Django Project

Command:

```bash
django-admin startproject student_info_site
```

Purpose:

This creates the main Django project folder. The project folder contains settings, main URLs, ASGI, and WSGI files.

---

### Step 2: Create the App

Command:

```bash
python manage.py startapp student_info
```

Purpose:

The app contains the actual project logic such as views, models, admin file, and app configuration.

---

### Step 3: Register the App

File:

```txt
student_info_site/settings.py
```

Add:

```python
'student_info',
```

inside `INSTALLED_APPS`.

Purpose:

Django must know that the `student_info` app exists.

---

### Step 4: Configure Template Folder

File:

```txt
student_info_site/settings.py
```

Update:

```python
'DIRS': [BASE_DIR / 'templates'],
```

Purpose:

This tells Django to search for HTML files inside the `templates` folder.

---

### Step 5: Create URLs

File:

```txt
student_info_site/urls.py
```

Code:

```python
from django.contrib import admin
from django.urls import path
from student_info import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home-page'),
    path('student/', views.student_details, name='student-details-page'),
    path('course/', views.course_details, name='course-details-page'),
]
```

Explanation:

- `/` opens the home page
- `/student/` opens the student details page
- `/course/` opens the course details page

---

### Step 6: Create Simple Views First

File:

```txt
student_info/views.py
```

First write only:

```python
from django.shortcuts import render

def home(request):
    return render(request, 'student_info/home.html')
```

Purpose:

Before adding data, students should confirm that the home page works.

---

### Step 7: Create the Home Template

File:

```txt
templates/student_info/home.html
```

Code:

```html
<h1>Project 2: Student Information Display</h1>
<a href="/student/">View Student Details</a>
<a href="/course/">View Course Details</a>
```

Purpose:

The home page gives links to other pages.

Test:

```txt
http://127.0.0.1:8000/
```

---

### Step 8: Create Student Data in the View

File:

```txt
student_info/views.py
```

Code:

```python
def student_details(request):
    student = {
        'name': 'Rahim Uddin',
        'department': 'Computer Science and Engineering',
        'semester': '5th',
        'university': 'Example University',
        'email': 'rahim@example.com',
        'cgpa': 3.75,
    }

    return render(request, 'student_info/student_details.html', {'student': student})
```

Explanation:

Here, `student` is a Python dictionary.

This line sends the dictionary to HTML:

```python
{'student': student}
```

The first `student` is the template variable name.
The second `student` is the Python dictionary.

---

### Step 9: Display Student Data in Template

File:

```txt
templates/student_info/student_details.html
```

Code:

```html
<p>Name: {{ student.name }}</p>
<p>Department: {{ student.department }}</p>
<p>Semester: {{ student.semester }}</p>
<p>CGPA: {{ student.cgpa }}</p>
```

Explanation:

`{{ student.name }}` means Django will take the value of `name` from the `student` dictionary.

Test:

```txt
http://127.0.0.1:8000/student/
```

---

### Step 10: Create Course Data with a List

File:

```txt
student_info/views.py
```

Code:

```python
def course_details(request):
    course = {
        'title': 'Introduction to Django',
        'teacher': 'Anik Shanto',
        'duration': '1 hour',
        'topics': [
            'URL routing',
            'View function',
            'Context dictionary',
            'Template variable',
            'Dynamic HTML rendering',
        ],
    }

    return render(request, 'student_info/course_details.html', {'course': course})
```

Purpose:

This introduces students to list data inside a dictionary.

---

### Step 11: Display a List Using Template Loop

File:

```txt
templates/student_info/course_details.html
```

Code:

```html
<ul>
    {% for topic in course.topics %}
        <li>{{ topic }}</li>
    {% endfor %}
</ul>
```

Explanation:

- `{% for topic in course.topics %}` starts the loop
- `{{ topic }}` prints each topic
- `{% endfor %}` ends the loop

Test:

```txt
http://127.0.0.1:8000/course/
```

---

## Final Testing Checklist

Test these URLs:

```txt
http://127.0.0.1:8000/
http://127.0.0.1:8000/student/
http://127.0.0.1:8000/course/
```

Expected output:

- Home page opens
- Student details page shows dynamic student data
- Course page shows course data and topic list

---

## Important Teaching Explanation

In this project, students should understand that HTML files do not have fixed content only.

Django views can send data to HTML.

The full workflow is:

```txt
Browser URL
    ↓
urls.py
    ↓
views.py
    ↓
context dictionary
    ↓
HTML template
    ↓
final webpage
```

---

## Common Student Mistakes

### Mistake 1: TemplateDoesNotExist

Cause:

Wrong template path.

Fix:

Make sure the file is inside:

```txt
templates/student_info/
```

and the render path is:

```python
return render(request, 'student_info/home.html')
```

---

### Mistake 2: Page Not Found 404

Cause:

URL not added in `urls.py`.

Fix:

Check:

```python
path('student/', views.student_details, name='student-details-page')
```

---

### Mistake 3: Variable Not Showing

Cause:

Context variable name mismatch.

Example mistake:

```python
{'students': student}
```

but template uses:

```html
{{ student.name }}
```

Fix:

Use the same variable name in view and template.

---

## Why This Project Comes Before Form Projects

Before students learn forms, POST requests, and user input, they should first understand how backend data is displayed in frontend templates.

This project builds confidence because it has no database and no complex logic.
