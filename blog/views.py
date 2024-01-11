
from django.shortcuts import (render,
                              HttpResponseRedirect,
                              get_object_or_404,
                              redirect)
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.views import generic, View
from django.utils import translation
from django.utils.text import slugify
from django.utils.translation import activate, gettext
from django.views.generic import TemplateView
from .models import Post
from .forms import CommentForm, NewsForm

# Create your views here.


def error_404_view(request, exception):
    """ Renders the 404 page """
    return render(request, '404.html', {}, status=404)


def add_news(request):
    """ View to add news items """
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            # save the form without committing
            news_item = form.save(commit=False)
            news_item.author = request.user
            news_item.save()  # save the object to generate an ID
            # generate a slug using the title and ID
            news_item.slug = slugify(f"{news_item.title}-{news_item.id}")
            news_item.save()  # save the object again to save the slug
            messages.success(request, gettext(
                'Your news item was successfully added.'))
            return redirect('news')
    else:
        form = NewsForm()
    return render(request, 'add_news.html', {'form': form})


def set_language(request, language):
    """ Sets the language for the site """
    translation.activate(language)
    print(f"Setting language to: {language}")
    print(f"Current Language in View: {request.LANGUAGE_CODE}")
    request.session['LANGUAGE_SESSION_KEY'] = language
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def like_post(request, pk):
    """ View to like a post """
    post = get_object_or_404(Post, pk=pk)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    if post:
        return redirect('news_details', slug=post.slug)
    else:
        return redirect('news')


class HomeView(TemplateView):
    """ View for the home page """
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['last_post'] = Post.objects.filter(
            status=1).order_by('-created_on').first()
        return context


class PostList(generic.ListView):
    """ View for the news page"""
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'news.html'
    paginate_by = 6


class PostDetails(View):
    """ View for the news details page """
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        context = {
            "post": post,
            "comments": comments,
            "commented": False,
            "liked": liked,
            "comment_form": CommentForm()
        }
        return render(request, "news_details.html", context)

    def post(self, request, slug, *args, **kwargs):
        """ View for posting comments """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request, 'Your comment was posted successfully.')
        else:
            comment_form = CommentForm()

            context = {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            }
        return render(request, "news_details.html", context)
