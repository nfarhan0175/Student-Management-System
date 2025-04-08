from django.contrib import admin
from django.urls import path 
from . import views
urlpatterns = [
    path('addStudents/', views.addStudent,name='addStudents'),
    path('showStudent/', views.showStudent,name='showStudent'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
]