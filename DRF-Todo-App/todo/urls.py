from django.urls import path
from .views import TaskListCreateView, TaskRetriveUpdateDeleteView

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>', TaskRetriveUpdateDeleteView.as_view(), name='task-detail'),
]
