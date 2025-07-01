from django.urls import path
from . import views

urlpatterns = [
    path('', views.StudentView.as_view()),
    path('students/<int:pk>/', views.StudentDetailView.as_view(), name='student-detail'),
]
