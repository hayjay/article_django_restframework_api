from django.urls import path, include
# from .views import article_list, article_detail, ArticleAPIView, ArticleDetails
from .views import ArticleAPIView, ArticleDetails, GenericAPIView

urlpatterns = [
    path('api/articles/', ArticleAPIView.as_view()),
    # path('api/articles/', article_list),
    # path('api/article-detail/<int:pk>/', article_detail)
    path('api/article-detail/<int:id>/', ArticleDetails.as_view()),
    path('api/generic/articles/<int:id>/', GenericAPIView.as_view()),
    # path('api/generic/articles/', GenericAPIView.as_view()),

    # ArticleDetails
]