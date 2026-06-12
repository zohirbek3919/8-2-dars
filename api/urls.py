from django.urls import path
from .views import CourseApiView, StudentApiView

urlpatterns = [
    path('courses/', CourseApiView.as_view()),
    path('courses/<int:pk>/', CourseApiView.as_view()),

    path('students/', StudentApiView.as_view()),
    path('students/<int:pk>/', StudentApiView.as_view()),

]