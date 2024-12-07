from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name="blog/login.html")),
    path('logout/', auth_views.LogoutView.as_view(template_name="blog/logout.html")),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('home/', views.home_view, name='home'),
]