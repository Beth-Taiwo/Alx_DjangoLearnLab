from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name="blog/login.html"), name='login'),
    path('logout/',views.logout_view, name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('home/', views.home_view, name='home'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('posts/', views.PostView.as_view(), name='posts'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
]