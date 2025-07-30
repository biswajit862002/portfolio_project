from django.db import models
from datetime import timedelta
from cloudinary.models import CloudinaryField

# Create your models here.
class Blogs(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.CharField(max_length=300)
    # image = models.ImageField(upload_to='blogs_images/')
    image = CloudinaryField('image')
    github_link = models.URLField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    
