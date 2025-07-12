from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """
    Administration interface configuration for the Task model
    """
    list_display = ['title', 'user', 'priority', 'status', 'due_date', 'created_date']
    list_filter = ['priority', 'status', 'created_date', 'due_date']
    search_fields = ['title', 'description', 'user__username']
    list_per_page = 20
    date_hierarchy = 'created_date'
    
    fieldsets = (
        ('General Information', {
            'fields': ('user', 'title', 'description')
        }),
        ('Settings', {
            'fields': ('priority', 'status', 'due_date')
        }),
        ('Metadata', {
            'fields': ('created_date', 'modified_date'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ('created_date', 'modified_date')
    
    def get_queryset(self, request):
        """
        Superusers see all tasks,
        other users see only their tasks
        """
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)
