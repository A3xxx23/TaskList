from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('calendarTemplate/', views.calendarTemplate, name ='calendarTemplate'),
]
    
