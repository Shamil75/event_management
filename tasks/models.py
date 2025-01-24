from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Event(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed')
    ]
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()
    time = models.TimeField(auto_now=True)
    location = models.CharField(max_length=150)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default="PENDING")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='events')
    

    def __str__(self):
        return self.name
    
class Participant(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    event = models.ManyToManyField(Event, related_name='participants')

    def __str__(self):
        return self.name
    
