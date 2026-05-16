from django.shortcuts import render

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
    {
        'id': 3,
        'name': 'Nusrat Jahan',
        'department': 'CSE',
        'semester': '6th',
        'cgpa': 3.92,
    },
    {
        'id': 4,
        'name': 'Sadia Islam',
        'department': 'BBA',
        'semester': '3rd',
        'cgpa': 3.30,
    },
    {
        'id': 5,
        'name': 'Tanvir Hasan',
        'department': 'CSE',
        'semester': '7th',
        'cgpa': 3.81,
    },
]

def home(request):
    total_students = len(students_data)

    context = {
        'total_students': total_students,
    }

    return render(request, 'students/home.html', context)

def student_list(request):
    context = {
        'students': students_data,
    }

    return render(request, 'students/student_list.html', context)

def top_students(request):
    selected_students = []

    for student in students_data:
        if student['cgpa'] >= 3.70:
            selected_students.append(student)

    context = {
        'students': selected_students,
    }

    return render(request, 'students/top_students.html', context)
