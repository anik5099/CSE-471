from django.shortcuts import render

def home(request):
    return render(request, 'student_info/home.html')

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
