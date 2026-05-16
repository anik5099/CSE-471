from django.shortcuts import render, redirect

# This list works like temporary memory.
# It will store tasks only while the server is running.
# If the server restarts, the list becomes empty again.
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
