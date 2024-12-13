from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name="blog/login.html"), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name="blog/logout.html"), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('home/', views.home_view, name='home'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('posts/', views.PostListView.as_view(), name='posts'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/update/', views.update_post, name='post_update'),
    path('post/<int:pk>/delete/', views.delete_post, name='post_delete'),
    path('post/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='comment_create'),
    path('post/<int:post_pk>/comment/<int:pk>/update/', views.CommentUpdateView.as_view(),name='comment_update'),
    path('post/<int:post_pk>/comment/<int:pk>/delete/', views.CommentDeleteView.as_view(),name='comment_delete'),
    path('tags/<tag_name>/', views.tag_view, name='post-tag'),
    # path('tags/<slug:tag_slug>/', views.PostByTagListView.as_view(), name='post-tag_list'),
    path('search/', views.SearchView.as_view(), name='post-search'),

]