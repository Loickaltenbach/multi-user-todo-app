from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Task(models.Model):
    """
    Task model for a multi-user To-Do application
    """
    
    # Priority choices
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('normal', 'Normal'),
        ('high', 'High'),
    ]
    
    # Status choices
    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    
    # Model fields
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        verbose_name="User",
        help_text="Task owner"
    )
    
    title = models.CharField(
        max_length=255,
        verbose_name="Title",
        help_text="Task title"
    )
    
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Description",
        help_text="Detailed task description (optional)"
    )
    
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='normal',
        verbose_name="Priority",
        help_text="Task priority level"
    )
    
    due_date = models.DateField(
        blank=True,
        null=True,
        verbose_name="Due Date",
        help_text="Task deadline (optional)"
    )
    
    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default='todo',
        verbose_name="Status",
        help_text="Task progress status"
    )
    
    # Metadata
    created_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created Date"
    )
    
    modified_date = models.DateTimeField(
        auto_now=True,
        verbose_name="Modified Date"
    )
    
    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        ordering = ['-created_date']
        
    def __str__(self):
        return f"{self.title} ({self.user.username})"
    
    def get_absolute_url(self):
        return reverse('task_detail', kwargs={'pk': self.pk})
