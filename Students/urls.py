from django.urls import path
from .views import StudentAPI

urlpatterns = [
    path('details/', StudentAPI.as_view()),
    path('details/<int:student_id>/', StudentAPI.as_view()),
]