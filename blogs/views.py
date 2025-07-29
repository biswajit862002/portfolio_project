from django.shortcuts import render, get_object_or_404
from .models import Blogs

# Create your views here.
def blogs(request):
    all_blogs = Blogs.objects.all().order_by('-created_at')  # Fetch all projects, newest first
    context = {
        'blogs': all_blogs,
        'blogs_active': 'active',  # for navbar highlighting, if needed
    }
    return render(request, 'blogs/blogs.html', context)


def blog_detail(request, id):
    blog = get_object_or_404(Blogs, id=id)
    context = {
        'blog': blog,
        'blogs_active': 'active',
    }
    return render(request, 'blogs/blog_detail.html', context)