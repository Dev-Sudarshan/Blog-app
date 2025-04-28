from django.shortcuts import render
from blog.models import Post


def home(request):
    context = {
        'posts': Post.objects.all()  #fetch all posts from the database and pass them to the template
        # to display them on the home page.        # The context dictionary contains the data that will be passed to the template.
        # The 'posts' key contains all the Post objects retrieved from the database.
    }
    return render(request, 'blog/home.html', context)


def about(request): 
    return render(request, 'blog/about.html', {'title': 'About'})
