from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Task


class TaskListView(LoginRequiredMixin, ListView):
    """
    List view filtered by logged-in user
    """
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    paginate_by = 10
    login_url = reverse_lazy('login')
    
    def get_queryset(self):
        """
        Filter tasks to show only those belonging to the logged-in user
        """
        return Task.objects.filter(user=self.request.user).order_by('-created_date')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Statistics for the user
        user_tasks = Task.objects.filter(user=self.request.user)
        context['total_tasks'] = user_tasks.count()
        context['completed_tasks'] = user_tasks.filter(status='completed').count()
        context['pending_tasks'] = user_tasks.exclude(status='completed').count()
        return context


class TaskDetailView(LoginRequiredMixin, DetailView):
    """
    Detail view for a task
    """
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'
    login_url = reverse_lazy('login')
    
    def get_queryset(self):
        """
        Ensure user can only see their own tasks
        """
        return Task.objects.filter(user=self.request.user)


class TaskCreateView(LoginRequiredMixin, CreateView):
    """
    View to add a task
    """
    model = Task
    template_name = 'tasks/task_form.html'
    fields = ['title', 'description', 'priority', 'due_date', 'status']
    success_url = reverse_lazy('task_list')
    login_url = reverse_lazy('login')
    
    def form_valid(self, form):
        """
        Automatically associate the task with the logged-in user
        """
        form.instance.user = self.request.user
        messages.success(self.request, 'Task created successfully!')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create New Task'
        context['button_text'] = 'Create'
        return context


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    """
    View to update a task
    """
    model = Task
    template_name = 'tasks/task_form.html'
    fields = ['title', 'description', 'priority', 'due_date', 'status']
    success_url = reverse_lazy('task_list')
    login_url = reverse_lazy('login')
    
    def get_queryset(self):
        """
        Ensure user can only update their own tasks
        """
        return Task.objects.filter(user=self.request.user)
    
    def form_valid(self, form):
        messages.success(self.request, 'Task updated successfully!')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Task'
        context['button_text'] = 'Update'
        return context


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    """
    View to delete a task
    """
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('task_list')
    login_url = reverse_lazy('login')
    
    def get_queryset(self):
        """
        Ensure user can only delete their own tasks
        """
        return Task.objects.filter(user=self.request.user)
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Task deleted successfully!')
        return super().delete(request, *args, **kwargs)


# Custom authentication views
class CustomLoginView(auth_views.LoginView):
    """
    Custom login view
    """
    template_name = 'registration/login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('task_list')


class CustomLogoutView(auth_views.LogoutView):
    """
    Custom logout view
    """
    next_page = reverse_lazy('login')
