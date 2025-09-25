from django.urls import path
from . import views

urlpatterns = [
    path('create_event', views.create_event, name='create_event'),
    path('view_event', views.view_event, name='view_event'),
    ]