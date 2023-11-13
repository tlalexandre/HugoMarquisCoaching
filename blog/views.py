from django.shortcuts import render
from django.views import generic
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView
from .models import Post

# Create your views here.

class HomeView(TemplateView):
    template_name='index.html'

class PostList(generic.ListView):
    model=Post
    queryset=Post.objects.filter(status=1).order_by('-created_on')
    template_name='news.html'
    paginate_by=6
    
