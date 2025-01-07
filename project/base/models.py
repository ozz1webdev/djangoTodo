from django.db import models
from django.contrib.auth.models import User

state = (
    ('ToDo', 'To Do'),
    ('In Progress', 'In Progress'),
    ('Done', 'Done'),
)

priority = (
    (1, 'Low'),
    (2, 'Medium'),
    (3, 'High'),
)


class Project(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    projectName = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    projectName = models.ForeignKey(Project, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=255)
    description = models.TextField()
    priority = models.IntegerField(default=1, choices=priority)
    state = models.CharField(max_length=255, default='ToDo', choices=state)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
