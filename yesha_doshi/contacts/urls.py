# contacts/urls.py

from django.urls import path

from .views import TaskCreateView, TaskDeleteView, TaskDetailView, TaskListView, TaskUpdateView

urlpatterns = [
    path("contacts/<int:pk>/delete/", TaskDeleteView.as_view(), name="task_confirm_list"),
    path("contacts/<int:pk>/update/", TaskUpdateView.as_view(), name="task_update"),
    path("contacts/<int:pk>/", TaskDetailView.as_view(), name="task_detail"),
    path("create/", TaskCreateView.as_view(), name="task_create"),
    path("", TaskListView.as_view(), name="task_list"),
]
