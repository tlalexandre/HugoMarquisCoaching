from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class NewsForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'featured_image', 'excerpt', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'w-50 rounded '})
        self.fields['content'].widget.attrs.update({'class': 'w-50 rounded '})
        self.fields['featured_image'].widget.attrs.update(
            {'class': 'w-50 rounded '})
