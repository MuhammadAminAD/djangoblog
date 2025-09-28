from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy


# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = "home.html"


class BlogDetailView(DetailView):
    model = Post
    template_name = "post_item.html"


class BlogCreateView(CreateView):
    model = Post
    template_name = "create_item.html"
    fields = ["title", "body", "author"]


class BlogUpdateView(UpdateView):
    model = Post
    template_name = "edit_item.html"

    fields = ["title", "body"]


class BlogDeleteView(DeleteView):
    model = Post
    template_name = "delete_item.html"
    success_url = reverse_lazy("home")
