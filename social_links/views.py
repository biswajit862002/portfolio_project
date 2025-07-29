from django.shortcuts import render

# Create your views here.
def social(request):
 context = {'social': 'active'}
 return render(request, 'social_links/social.html', context)