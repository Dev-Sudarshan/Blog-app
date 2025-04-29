from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('',PostListView.as_view, name='blog-home'),
    path('post/<int:pk>/',PostCreateView.as_view, name='post-create'),
    path('post/new/',PostCreateView.as_view, name='post-create'),
    path('post/<int:pk>/',PostUpdateView.as_view, name='post-update'),
    path('post/<int:pk>/',PostDeleteView.as_view, name='post-delete'),
    path('about/', views.about, name='blog-about'),
]