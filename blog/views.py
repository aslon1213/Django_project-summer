# blog/views.py
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView# new
from .models import Post
from django.urls import reverse_lazy
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
class BlogCreateView(CreateView): # new
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'delete_blog.html'
    success_url = reverse_lazy('home')