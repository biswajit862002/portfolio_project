from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Resume(models.Model):
    title = models.CharField(max_length=200)
    # image = models.ImageField(upload_to='resume/images/')  # For resume thumbnail or badge
    image = CloudinaryField('image')

    # live_link = models.FileField(upload_to='certificates/pdfs/')  # For storing PDF resume files
    live_link = CloudinaryField('raw')  # For PDF file,  raw means non-image file (PDF, DOCX, etc.)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    

    def __str__(self):
        return self.title