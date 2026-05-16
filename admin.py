from django.contrib import admin
from django.urls import path
from calculator import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home-page'),
    path('calculator/', views.calculator, name='calculator-page'),
    path('about/', views.about, name='about-page'),
]
