from Blogapp import models
from django.shortcuts import render
from django.views import generic
# Create your views here.

class PostList(generic.ListView):
    queryset = models.Post.objects.filter(status = 1).order_by('-created_on')

class DetailView(generic.DetailView):
    model = models.Post
    template_name = 'post_detail.html'

