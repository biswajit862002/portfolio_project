from django.shortcuts import render
from .models import Certification

# Create your views here.
def certifications(request):
    all_certifications = Certification.objects.all().order_by('created_at')  # Fetch all projects, newest first
    context = {
        'certifications': all_certifications,
        'certificates_active': 'active',  # for navbar highlighting, if needed
    }
    return render(request, 'certifications/certificates.html', context)