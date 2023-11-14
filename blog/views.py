
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse
from django.views import generic, View
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
    
class PostDetails(View):
    
    def get(self, request, slug, *args, **kwargs):
        queryset=Post.objects.filter(status=1)
        post= get_object_or_404(queryset,slug=slug)
        comments= post.comments.filter(approved=True).order_by('created_on')
        liked=False
        if post.likes.filter(id=self.request.user.id).exists():
            liked=True
        
        return render(request, "news_details.html",{"post":post,"comments":comments,"liked":liked})