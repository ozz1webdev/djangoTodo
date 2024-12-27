from django.db import models

state = (
    ('ToDo', 'To Do'),
    ('In Progress', 'In Progress'),
    ('Done', 'Done'),
)


class Task(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    project = models.CharField(max_length=255, null=False, blank=False)
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
