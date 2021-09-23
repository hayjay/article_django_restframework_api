from django.urls import path, include
# from .views import article_list, article_detail, ArticleAPIView, ArticleDetails
from .views import ArticleAPIView, ArticleDetails, GenericAPIView, ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# register out routes
router.register('article', ArticleViewSet, basename='article')

urlpatterns = [
    path('api/viewset/', include(router.urls)),
    path('api/viewset/<int:pk>/', include(router.urls)),
    path('api/articles/', ArticleAPIView.as_view()),
    # path('api/articles/', article_list),
    # path('api/article-detail/<int:pk>/', article_detail)
    path('api/article-detail/<int:id>/', ArticleDetails.as_view()),
    path('api/generic/articles/<int:id>/', GenericAPIView.as_view()),
    # path('api/generic/articles/', GenericAPIView.as_view()),

    # ArticleDetails
]