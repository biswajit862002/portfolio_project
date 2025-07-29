from django.shortcuts import render
from .models import Resume

# Create your views here.
def resume(request):
    my_resume = Resume.objects.all().order_by('-created_at')  # Fetch all projects, newest first
    context = {
        'resume': my_resume,
        'resume_active': 'active',  # for navbar highlighting, if needed
    }
    return render(request, 'my_resume/resume.html', context)