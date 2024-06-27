from django.urls import path
from .views import HomeView, BlogDetail

urlpatterns = [
    path('', HomeView.as_view(), name = "home"),
    path('article/<int:pk>', BlogDetail.as_view(), name = "blog-detail"),
]
