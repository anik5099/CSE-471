# Lab Manual: Project 3 - Student List

## Project Goal

In Project 2, students learned how to pass one dictionary from `views.py` to an HTML template.

In this project, students will learn how to pass multiple records using a list of dictionaries.

The main workflow is:

```txt
URL → View → List of Dictionaries → Template Loop → Webpage
```

---

## What Students Will Learn

By completing this project, students will learn:

1. How to store multiple records in a Python list
2. How to use dictionaries inside a list
3. How to pass a list from `views.py` to a template
4. How to use `{% for %}` loop in Django templates
5. How to show data in an HTML table
6. How to use `{% if %}` condition in templates
7. How to filter data using basic Python logic

---

## Pages in This Project

| URL | Purpose |
|---|---|
| `/` | Home page |
| `/students/` | Displays all students |
| `/top-students/` | Displays students with CGPA 3.70 or above |

---

## Recommended Coding Workflow

Students should code and test step by step.

---

## Step 1: Create the Django Project

Command:

```bash
django-admin startproject student_list_site
```

Purpose:

This creates the main Django project.

---

## Step 2: Create the App

Command:

```bash
python manage.py startapp students
```

Purpose:

The `students` app will contain the views for student-related pages.

---

## Step 3: Register the App

File:

```txt
student_list_site/settings.py
```

Add:

```python
'students',
```

inside `INSTALLED_APPS`.

Purpose:

This tells Django that the `students` app is part of the project.

---

## Step 4: Configure Template Directory

File:

```txt
student_list_site/settings.py
```

Update:

```python
'DIRS': [BASE_DIR / 'templates'],
```

Purpose:

This allows Django to find HTML files inside the `templates` folder.

---

## Step 5: Create URL Patterns

File:

```txt
student_list_site/urls.py
```

Code:

```python
from django.contrib import admin
from django.urls import path
from students import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home-page'),
    path('students/', views.student_list, name='student-list-page'),
    path('top-students/', views.top_students, name='top-students-page'),
]
```

Explanation:

- `/` opens the home page
- `/students/` opens the full student list
- `/top-students/` opens the filtered student list

---

## Step 6: Create Student Data

File:

```txt
students/views.py
```

Code:

```python
students_data = [
    {
        'id': 1,
        'name': 'Rahim Uddin',
        'department': 'CSE',
        'semester': '5th',
        'cgpa': 3.75,
    },
    {
        'id': 2,
        'name': 'Karim Ahmed',
        'department': 'EEE',
        'semester': '4th',
        'cgpa': 3.45,
    },
]
```

Explanation:

`students_data` is a list.

Each item inside the list is a dictionary.

Each dictionary represents one student.

---

## Step 7: Create the Home View

File:

```txt
students/views.py
```

Code:

```python
def home(request):
    total_students = len(students_data)

    context = {
        'total_students': total_students,
    }

    return render(request, 'students/home.html', context)
```

Explanation:

`len(students_data)` counts the total number of students.

The value is passed to the home page.

---

## Step 8: Create the Home Template

File:

```txt
templates/students/home.html
```

Code:

```html
<h1>Project 3: Student List</h1>

<p>Total Students: {{ total_students }}</p>

<a href="/students/">View All Students</a>
<a href="/top-students/">View Top Students</a>
```

Test:

```txt
http://127.0.0.1:8000/
```

---

## Step 9: Create the Student List View

File:

```txt
students/views.py
```

Code:

```python
def student_list(request):
    context = {
        'students': students_data,
    }

    return render(request, 'students/student_list.html', context)
```

Explanation:

The complete list is sent to the template using the variable name `students`.

---

## Step 10: Display Students Using Template Loop

File:

```txt
templates/students/student_list.html
```

Code:

```html
{% for student in students %}
    <p>{{ student.name }} - {{ student.department }} - {{ student.cgpa }}</p>
{% endfor %}
```

Explanation:

- `students` is the list sent from views.py
- `student` represents one item from that list
- `student.name` prints the name of one student

Test:

```txt
http://127.0.0.1:8000/students/
```

---

## Step 11: Show Students in a Table

Instead of showing student data as simple paragraphs, students can display it in a table.

Code:

```html
<table border="1">
    <tr>
        <th>ID</th>
        <th>Name</th>
        <th>Department</th>
        <th>Semester</th>
        <th>CGPA</th>
    </tr>

    {% for student in students %}
    <tr>
        <td>{{ student.id }}</td>
        <td>{{ student.name }}</td>
        <td>{{ student.department }}</td>
        <td>{{ student.semester }}</td>
        <td>{{ student.cgpa }}</td>
    </tr>
    {% endfor %}
</table>
```

Purpose:

Students learn how Django template loops can be combined with normal HTML table structure.

---

## Step 12: Create a Filtered Student List

File:

```txt
students/views.py
```

Code:

```python
def top_students(request):
    selected_students = []

    for student in students_data:
        if student['cgpa'] >= 3.70:
            selected_students.append(student)

    context = {
        'students': selected_students,
    }

    return render(request, 'students/top_students.html', context)
```

Explanation:

This is normal Python logic.

It checks each student's CGPA.

If CGPA is 3.70 or above, that student is added to `selected_students`.

---

## Step 13: Use If Condition in Template

File:

```txt
templates/students/top_students.html
```

Code:

```html
{% if students %}
    <ul>
        {% for student in students %}
            <li>{{ student.name }} - CGPA: {{ student.cgpa }}</li>
        {% endfor %}
    </ul>
{% else %}
    <p>No top students found.</p>
{% endif %}
```

Explanation:

- `{% if students %}` checks whether the list contains data
- If the list is not empty, it displays students
- If the list is empty, it displays a message

---

## Final Testing Checklist

Test these URLs:

```txt
http://127.0.0.1:8000/
http://127.0.0.1:8000/students/
http://127.0.0.1:8000/top-students/
```

Expected result:

- Home page shows total students
- Student list page shows all students in a table
- Top students page shows only students with CGPA 3.70 or above

---

## Important Concept

This project prepares students for future database projects.

In a real database project, data will come from the database.

But in this beginner project, data comes from a Python list.

So students can understand the display logic first without worrying about database complexity.

---

## Common Mistakes

### Mistake 1: Forgetting to pass context

Wrong:

```python
return render(request, 'students/student_list.html')
```

Correct:

```python
return render(request, 'students/student_list.html', {'students': students_data})
```

---

### Mistake 2: Wrong variable name in template

If the view sends:

```python
{'students': students_data}
```

then the template must use:

```html
{% for student in students %}
```

not:

```html
{% for student in student_list %}
```

---

### Mistake 3: Wrong dictionary key

If the dictionary has:

```python
'department': 'CSE'
```

then use:

```html
{{ student.department }}
```

not:

```html
{{ student.dept }}
```
