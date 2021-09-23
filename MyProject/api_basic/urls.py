from django.urls import path, include
from .views import article_list, article_detail

urlpatterns = [
    path('api/articles/', article_list),
    path('api/article-detail/<int:pk>/', article_detail)
]