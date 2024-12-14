from django.urls import path
from .views import RegisterUserView, LoginView, RetrieveTokenView, FollowUserView, UnfollowUserView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/', RetrieveTokenView.as_view(), name='token'),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow-user'),
]