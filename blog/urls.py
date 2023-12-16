from . import views
from .views import add_news
from django.urls import path



urlpatterns = [
    path('news/', views.PostList.as_view(), name='news'),
    path('news/<slug:slug>',views.PostDetails.as_view(),name="news_details"),
    path('', views.HomeView.as_view(), name='home'),
    path('set-language/<str:language>/', views.set_language, name='set_language'),
    path('add_news/', add_news, name='add_news'),
    path('post/<int:pk>/like/', views.like_post, name='like_post'),
]

handler404 = 'blog.views.error_404_view'