
from django.db import models
from django.contrib.auth.models import User

class Ticket(models.Model):
    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('IN_PROGRESS', 'In Progress'),
        ('RESOLVED', 'Resolved'),
        ('CLOSED', 'Closed'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='OPEN'
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tickets'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
