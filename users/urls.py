# users/url.py
from django.urls import path
from . import views

# this is where app-specific URLs go
urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]
