from django.db import models
from datetime import timedelta

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.CharField(max_length=300)
    image = models.ImageField(upload_to='project_images/')
    live_link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def duration(self):
        """Returns project duration as a timedelta."""
        if self.start_date and self.end_date:
            return self.end_date - self.start_date
        return timedelta(0)
    
    def duration_in_words(self):
        delta = self.end_date - self.start_date
        days = delta.days
        if days < 30:
            return f"{days} days"
        elif days < 365:
            months = days // 30
            return f"{months} months"
        else:
            years = days // 365
            return f"{years} years"