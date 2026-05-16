from django.contrib import admin
from django.urls import path
from students import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home-page'),
    path('students/', views.student_list, name='student-list-page'),
    path('top-students/', views.top_students, name='top-students-page'),
]
