from django.urls import path
from .views import RegisterUserView, LoginView, RetrieveTokenView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/', RetrieveTokenView.as_view(), name='token'),
]