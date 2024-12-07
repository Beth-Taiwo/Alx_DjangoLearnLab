from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name="blog/login.html"), name='login'),
    path('logout/',views.logout_view, name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('home/', views.home_view, name='home'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('posts/', views.PostView.as_view(), name='posts')
]