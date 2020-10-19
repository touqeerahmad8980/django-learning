from django.contrib import admin
from todoList.models import TodoItem
from django.utils import timezone


@admin.register(TodoItem)
class TodoListAdmin(admin.ModelAdmin):
    list_display = ('todo_name', 'start_date', 'end_date', 'user')
    # list_filter = ('name')
    # search_fields = ('name')
    ordering = ('created',)