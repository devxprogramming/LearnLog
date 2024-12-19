from django.db import models
from uuid import uuid4

class LearnLog(models.Model):

    PRIORITY_CHOICES = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]

    PROGRESS_CHOICES = [
        ('New', 'New'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    unique = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    progress = models.CharField(max_length=20, choices=PROGRESS_CHOICES, default='New')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)