from django.db import models
from django.contrib.auth.models import User

state = (
    ('ToDo', 'To Do'),
    ('In Progress', 'In Progress'),
    ('Done', 'Done'),
)


class project(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    projectName = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    projectName = models.ForeignKey(project, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=255)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    state = models.CharField(max_length=255, default='ToDo', choices=state)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
