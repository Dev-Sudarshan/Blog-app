from django.shortcuts import render
from blog.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

def home(request):
    context = {
        'posts': Post.objects.all()  #fetch all posts from the database and pass them to the template
        # to display them on the home page.        # The context dictionary contains the data that will be passed to the template.
        # The 'posts' key contains all the Post objects retrieved from the database.
    }
    return render(request, 'blog/home.html', context)


def about(request): 
    return render(request, 'blog/about.html', {'title': 'About'})

class PostListView(ListView):
    model=Post #specifies that this list view will display data from the Post model.
    template_name='blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name='posts' # name of the variable to be used in the template
    ordering = ['-date_posted']# # ordering the posts by date_posted in descending order


class PostDetailView(DetailView):
    model=Post 


class PostCreateView(LoginRequiredMixin , CreateView):
    model=Post
    fields=['title','content'] # fields to be displayed in the form

    def form_valid(self, form):
        form.instance.author = self.request.user
        # This line sets the author of the post to the currently logged-in user before saving the form.
        return super().form_valid(form) # Calls the parent class's form_valid method to save the form and redirect to the success URL.

class PostUpdateView(LoginRequiredMixin , UserPassesTestMixin , UpdateView):
    model=Post
    fields=['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object() # get the current post object being updated
        if self.request.user == post.author:
            return True
        return False # This method checks if the current user is the author of the post being updated. If so, it allows the update; otherwise, it denies access.

class PostDeleteView(LoginRequiredMixin , UserPassesTestMixin , DeleteView):
    model=Post
    success_url = '/' # URL to redirect to after successful deletion
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False # This method checks if the current user is the author of the post being deleted. If so, it allows the deletion; otherwise, it denies access.