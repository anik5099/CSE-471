# Lab Manual: Project 4 - Simple Calculator

## Project Goal

In the previous projects, students learned:

1. URL routing
2. View functions
3. Template rendering
4. Passing data from views to templates
5. Displaying lists using template loops

In this project, students will learn how to collect data from users using an HTML form.

The main workflow is:

```txt
User fills form
    ↓
Browser sends POST request
    ↓
urls.py sends request to view
    ↓
views.py reads form data
    ↓
views.py performs calculation
    ↓
result is sent back to template
    ↓
result is displayed on webpage
```

---

## What Students Will Learn

By completing this project, students will learn:

1. How to create an HTML form
2. Difference between GET and POST request
3. Why `{% csrf_token %}` is needed
4. How to read form input using `request.POST.get()`
5. How to convert string input to numbers
6. How to use conditional logic in views.py
7. How to display result or error messages in templates

---

## Project Pages

| URL | Purpose |
|---|---|
| `/` | Home page |
| `/calculator/` | Calculator form |
| `/about/` | Explanation page |

---

## Recommended Coding Workflow

Do not build everything at once. Follow the order below.

---

## Step 1: Create the Django Project

Command:

```bash
django-admin startproject calculator_site
```

Purpose:

This creates the main Django project.

---

## Step 2: Create the App

Command:

```bash
python manage.py startapp calculator
```

Purpose:

The `calculator` app will contain the calculator-related views.

---

## Step 3: Register the App

File:

```txt
calculator_site/settings.py
```

Add:

```python
'calculator',
```

inside `INSTALLED_APPS`.

Purpose:

Django must know that the calculator app exists.

---

## Step 4: Configure Template Folder

File:

```txt
calculator_site/settings.py
```

Update:

```python
'DIRS': [BASE_DIR / 'templates'],
```

Purpose:

This tells Django where to find HTML files.

---

## Step 5: Create URL Patterns

File:

```txt
calculator_site/urls.py
```

Code:

```python
from django.contrib import admin
from django.urls import path
from calculator import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home-page'),
    path('calculator/', views.calculator, name='calculator-page'),
    path('about/', views.about, name='about-page'),
]
```

Explanation:

- `/` opens the home page
- `/calculator/` opens the calculator
- `/about/` opens the explanation page

---

## Step 6: Create Basic Views First

File:

```txt
calculator/views.py
```

Code:

```python
from django.shortcuts import render

def home(request):
    return render(request, 'calculator/home.html')

def about(request):
    return render(request, 'calculator/about.html')
```

Purpose:

First confirm that basic pages load correctly.

---

## Step 7: Create Home Template

File:

```txt
templates/calculator/home.html
```

Code:

```html
<h1>Project 4: Simple Calculator</h1>
<a href="/calculator/">Open Calculator</a>
<a href="/about/">About This Project</a>
```

Test:

```txt
http://127.0.0.1:8000/
```

---

## Step 8: Create the Calculator Form

File:

```txt
templates/calculator/calculator.html
```

Code:

```html
<form method="POST">
    {% csrf_token %}

    <input type="text" name="number1">
    <input type="text" name="number2">

    <select name="operation">
        <option value="add">Addition</option>
        <option value="subtract">Subtraction</option>
        <option value="multiply">Multiplication</option>
        <option value="divide">Division</option>
    </select>

    <button type="submit">Calculate</button>
</form>
```

Explanation:

- `method="POST"` means form data will be sent securely to the server
- `name="number1"` is important because Django uses this name to read the value
- `{% csrf_token %}` protects the form from CSRF attacks

---

## Step 9: Create Calculator View

File:

```txt
calculator/views.py
```

Code:

```python
def calculator(request):
    result = None
    error = None

    if request.method == 'POST':
        number1 = request.POST.get('number1')
        number2 = request.POST.get('number2')
        operation = request.POST.get('operation')

    return render(request, 'calculator/calculator.html')
```

Explanation:

This reads the values submitted from the form.

At this stage, students should print values in the terminal for testing:

```python
print(number1, number2, operation)
```

---

## Step 10: Convert Input to Numbers

Form input always comes as text/string.

So we need to convert:

```python
number1 = float(number1)
number2 = float(number2)
```

Why?

Without conversion:

```python
"10" + "20" = "1020"
```

With conversion:

```python
10 + 20 = 30
```

---

## Step 11: Add Calculation Logic

Code:

```python
if operation == 'add':
    result = number1 + number2
elif operation == 'subtract':
    result = number1 - number2
elif operation == 'multiply':
    result = number1 * number2
elif operation == 'divide':
    result = number1 / number2
```

Purpose:

This performs different calculations based on the selected operation.

---

## Step 12: Handle Errors

Use `try-except` to handle invalid input.

Code:

```python
try:
    number1 = float(number1)
    number2 = float(number2)
except ValueError:
    error = 'Please enter valid numbers.'
```

Also handle division by zero:

```python
if number2 == 0:
    error = 'Cannot divide by zero.'
```

Purpose:

Students learn that user input must be validated.

---

## Step 13: Send Result Back to Template

Code:

```python
context = {
    'result': result,
    'error': error,
}

return render(request, 'calculator/calculator.html', context)
```

Purpose:

The result and error message are sent to HTML.

---

## Step 14: Display Result in Template

File:

```txt
templates/calculator/calculator.html
```

Code:

```html
{% if result is not None %}
    <h2>Result: {{ result }}</h2>
{% endif %}

{% if error %}
    <h2>Error: {{ error }}</h2>
{% endif %}
```

Explanation:

- If result exists, show the result
- If error exists, show the error

---

## Final Calculator View Code

```python
from django.shortcuts import render

def calculator(request):
    result = None
    error = None

    if request.method == 'POST':
        number1 = request.POST.get('number1')
        number2 = request.POST.get('number2')
        operation = request.POST.get('operation')

        try:
            number1 = float(number1)
            number2 = float(number2)

            if operation == 'add':
                result = number1 + number2
            elif operation == 'subtract':
                result = number1 - number2
            elif operation == 'multiply':
                result = number1 * number2
            elif operation == 'divide':
                if number2 == 0:
                    error = 'Cannot divide by zero.'
                else:
                    result = number1 / number2
            else:
                error = 'Invalid operation selected.'

        except ValueError:
            error = 'Please enter valid numbers.'

    context = {
        'result': result,
        'error': error,
    }

    return render(request, 'calculator/calculator.html', context)
```

---

## Final Testing Checklist

Test these URLs:

```txt
http://127.0.0.1:8000/
http://127.0.0.1:8000/calculator/
http://127.0.0.1:8000/about/
```

Test these calculations:

| Input | Operation | Expected Output |
|---|---|---|
| 10, 5 | Addition | 15 |
| 10, 5 | Subtraction | 5 |
| 10, 5 | Multiplication | 50 |
| 10, 5 | Division | 2 |
| 10, 0 | Division | Error message |
| abc, 5 | Any | Error message |

---

## Common Student Mistakes

### Mistake 1: Forgetting CSRF Token

Error:

```txt
CSRF verification failed
```

Fix:

Add inside form:

```html
{% csrf_token %}
```

---

### Mistake 2: Wrong Input Name

If HTML has:

```html
<input name="num1">
```

but view has:

```python
request.POST.get('number1')
```

Django will not find the value.

The names must match.

---

### Mistake 3: Not Converting String to Number

Form input is always string.

Use:

```python
float(number1)
```

---

### Mistake 4: Division by Zero

Always check:

```python
if number2 == 0:
    error = 'Cannot divide by zero.'
```

---

## Why This Project Is Important

This project is the first step toward interactive web applications.

Previous projects only displayed data.

This project collects input from the user, processes it on the backend, and returns an output.

This idea is very important before students move to larger Django projects.
