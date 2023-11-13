from .  import views
from django.urls import path

urlpatterns=[
    path('news/',views.PostList.as_view(),name='news'),
    path('',views.HomeView.as_view(),name='home')
]