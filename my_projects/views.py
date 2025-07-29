from django.shortcuts import render, get_object_or_404
from .models import Project

# Create your views here.
def projects(request):
    all_projects = Project.objects.all().order_by('-created_at')  # Fetch all projects, newest first
    context = {
        'projects': all_projects,
        'projects_active': 'active',  # for navbar highlighting, if needed
    }
    return render(request, 'my_projects/project.html', context)


def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    context = {
        'project': project,
        'projects_active': 'active',
    }
    return render(request, 'my_projects/project_detail.html', context)