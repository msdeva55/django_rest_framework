from django.urls import path
from .views import *
from .models import *

urlpatterns = [
    path('details/', StudentAPI.as_view()),
    path('details/<int:student_id>/', StudentAPI.as_view()),


    path('task/', TaskView.as_view()),
    path('task/<int:task_id>/', TaskView.as_view(), name="task-detail"),

    path('rank/', RankSheet),
    path('rank/<int:id>/', RankSheet),

    path('task/list/create/', task_list_create),
    path('task/update/delete/<int:id>/',task_update_delete),

]