from django.urls import path
from .views import StudentAPI, TaskView, TaskViewById

urlpatterns = [
    path('details/', StudentAPI.as_view()),
    path('details/<int:student_id>/', StudentAPI.as_view()),
    path('task/', TaskView.as_view()),
    path('task/<int:task_id>/', TaskViewById.as_view()),
]