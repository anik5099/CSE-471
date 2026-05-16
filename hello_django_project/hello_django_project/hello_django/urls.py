from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home-page'),
    path('about/', views.about, name='about-page'),
    path('contact/', views.contact, name='contact-page'),
]
