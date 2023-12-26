from django.shortcuts import render
from .models import Posts

def list(request):
    posts = Posts.objects.all()
    return render(request, 'app1/index.html', {'posts': posts})
