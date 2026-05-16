from django.contrib import admin
from django.urls import path
from student_info import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home-page'),
    path('student/', views.student_details, name='student-details-page'),
    path('course/', views.course_details, name='course-details-page'),
]
