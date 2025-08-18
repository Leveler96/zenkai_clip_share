from django.urls import path
from . import views
from .views import ClipCreateView

urlpatterns = [
    path('home/',views.clip_list,name='clip-list'),
    path('create/', ClipCreateView.as_view(), name='clip-create'),

]