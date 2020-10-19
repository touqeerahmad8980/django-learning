from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class TodoItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users")
    todo_name = models.CharField(max_length=200)
    start_date= models.DateField()
    end_date= models.DateField()
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('created',)
