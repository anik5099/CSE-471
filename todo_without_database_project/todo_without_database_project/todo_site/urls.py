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
