
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic, View
from django.utils import translation
from django.utils.text import slugify
from django.utils.translation import activate
from django.views.generic import TemplateView
from .models import Post
from .forms import CommentForm, NewsForm

# Create your views here.

def add_news(request):
    if request.method=='POST':
        form=NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news_item = form.save(commit=False)  # save the form without committing
            news_item.author = request.user
            news_item.save()  # save the object to generate an ID
            news_item.slug = slugify(f"{news_item.title}-{news_item.id}")  # generate a slug using the title and ID
            news_item.save()  # save the object again to save the slug
            return redirect('news')
    else:
        form=NewsForm()
    return render(request, 'add_news.html', {'form':form})


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
        comments= post.comments.order_by('created_on')
        liked=False
        if post.likes.filter(id=self.request.user.id).exists():
            liked=True
        
        return render(request, "news_details.html",{"post":post,"comments":comments,"commented":False,"liked":liked,"comment_form":CommentForm()})
    
    def post(self, request, slug, *args, **kwargs):
        queryset=Post.objects.filter(status=1)
        post= get_object_or_404(queryset,slug=slug)
        comments= post.comments.order_by('created_on')
        liked=False
        if post.likes.filter(id=self.request.user.id).exists():
            liked=True
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email=request.user.email
            comment_form.instance.name=request.user.username
            comment= comment_form.save(commit=False)
            comment.post=post
            comment.save()
        else:
            comment_form=CommentForm()

        return render(request, "news_details.html",{"post":post,"comments":comments,"commented":True,"liked":liked,"comment_form":CommentForm()})
    
