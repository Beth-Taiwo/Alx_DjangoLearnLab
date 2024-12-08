from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    CreateView,
    ListView,
    DeleteView,
    UpdateView,
    DetailView,
)
from .forms import RegisterForm, UserProfileForm, ProfileForm
from django.contrib.auth import login
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.


def home_view(request):
    return render(request, "blog/base.html")


class RegisterView(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy("home")  # redirect to home page on success
    template_name = "blog/base.html"

    def form_valid(self, form):
        form.save()
        login(self.request, user)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Sign Up"
        return context


class ProfileView(TemplateView):
    template_name = "blog/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user

        # Ensure the profile exists
        if not hasattr(user, "profile"):
            Profile.objects.create(user=user)

        context["user"] = user
        context["user_form"] = UserProfileForm(instance=user)
        context["profile_form"] = ProfileForm(instance=user.profile)
        return context

    def post(self, request, *args, **kwargs):
        user_form = UserProfileForm(request.POST, instance=request.user)
        profile_form = ProfileForm(
            request.POST, request.FILES, instance=request.user.profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("profile")  # Redirect to the same page or another page

        return self.render_to_response(
            self.get_context_data(user_form=user_form, profile_form=profile_form)
        )


class PostView(TemplateView):
    template_name = "blog/posts.html"

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html' 
    success_url = reverse_lazy('posts')  
    permission_classes = [IsAuthenticated]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

@login_required
def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form, 'message': "Post updated successfully"})

@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect(reverse_lazy('posts'))  
    return render(request, 'blog/post_confirm_delete.html', {'post': post})


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get(self, request):
        return Response({"message": "Post details retrieved successfully"})


class PostListView(ListView):
    model = Post
    template_name = "blog/posts.html"
    permission_classes = [IsAuthenticatedOrReadOnly]
   

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("login")
    else:
        return redirect("home")
