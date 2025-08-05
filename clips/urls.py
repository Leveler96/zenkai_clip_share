from django.urls import path
from . import views

urlpatterns = [
    path('',views.clip_list,name='clip_list'),
]