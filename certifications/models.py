from django.db import models

# Create your models here.

class Certification(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='certificates/images/')  # For certificate thumbnail or badge
    live_link = models.FileField(upload_to='certificates/pdfs/')  # For storing PDF certificate files
    organization_name = models.CharField(max_length=200)
    issue_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title