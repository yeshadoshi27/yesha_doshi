from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Task
from .task_form import TaskForm
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

    

class TaskListView(ListView):
    model = Task


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task_list")


class TaskDetailView(DetailView):
    model = Task


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task_list")




class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("task_list")