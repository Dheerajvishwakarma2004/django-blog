from django.urls import path
from .views import HomeView, BlogDetail , create_post

urlpatterns = [
    path('', HomeView.as_view(), name = "home"),
    path('article/<int:pk>', BlogDetail.as_view(), name = "blog-detail"),
    path('create/', create_post, name='create_post'),
]
