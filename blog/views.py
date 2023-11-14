
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import translation
from django.utils.translation import activate
from django.views.generic import TemplateView
from .models import Post

# Create your views here.
def set_language(request, language):
    translation.activate(language)
    print(f"Setting language to: {language}")
    print(f"Current Language in View: {request.LANGUAGE_CODE}")
    request.session['LANGUAGE_SESSION_KEY'] = language
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


class HomeView(TemplateView):
    template_name='index.html'

class PostList(generic.ListView):
    model=Post
    queryset=Post.objects.filter(status=1).order_by('-created_on')
    template_name='news.html'
    paginate_by=6
    
