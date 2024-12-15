from django.urls import path, include
from . import views
from rest_framework import routers

post_router = routers.DefaultRouter()
post_router.register(r'posts', views.PostViewSet, basename='post')
post_router.register(r'comments', views.CommentViewSet, basename='comment')


urlpatterns = [
    path('', include(post_router.urls)),
    path('feed/', views.FeedView.as_view(), name='feed'),
]