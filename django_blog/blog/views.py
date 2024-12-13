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
from .forms import RegisterForm, UserProfileForm, ProfileForm, PostForm
from django.contrib.auth import login
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Comment,Tag, Profile
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.


def home_view(request):
    return render(request, "blog/base.html")

class RegisterView(CreateView):

    form_class = RegisterForm
    success_url = reverse_lazy("home")  # redirect to home page on success
    template_name = "blog/register.html"

    def form_valid(self, form):
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProfileView(TemplateView):
    template_name = "blog/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user.is_authenticated:

            # Ensure the profile exists
            if not hasattr(user, "profile"):
                Profile.objects.create(user=user)

            # context["user"] = user
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

class PostCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html' 
    success_url = reverse_lazy('posts')  
    permission_classes = [IsAuthenticated]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        return self.request.user.has_perm('blog.add_post')
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['post'] = Post.objects.all()  # Add the post to the context for use in the form
        return context
      
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['post'] = Post.objects.all()  # Add the post to the context for use in the form
        return context

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
    
class CommentCreateView(CreateView):
    model = Comment
    fields = ['content']
    template_name = 'blog/comments.html'
    success_url = reverse_lazy('comments')
    permission_classes = [IsAuthenticated]
   

class CommentUpdateView(UpdateView):
    model = Comment
    fields = ['content']
    template_name = 'blog/comment_form.html'
    success_url = reverse_lazy('comments')
    permission_classes = [IsAuthenticated]
    
    
class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'
    success_url = reverse_lazy('comments')
    permission_classes = [IsAuthenticated]
    
    def search_view(request):
        queryset = Post.objects.all()
        form = SearchForm()

    # if request.method == "GET":
    #     form = SearchForm(request.GET)
    #     if form.is_valid():
    #         query = form.cleaned_data['to_search']
    #         searched_items = queryset.filter(Q(title__icontains=query)|Q(content__icontains=query))
    #     else:
    #         form = SearchForm()
    #     context = {
    #         'post_list': searched_items,
    #         'search_form': form,
    #     }
        # return render(request, 'search.html', context=context)

def tag_view(request, tag_name):
    tag = get_object_or_404(klass=Tag, name__iexact=tag_name)
    post_by_tag = Post.objects.filter(Q(tags__name__icontains=tag.name))

    context = {
        'posts':post_by_tag,
        'tag_name':tag_name
    }

    return render(request, 'tags.html', context=context)
    

class PostByTagListView():
    model = Post
    template_name = "blog/posts_by_tag.html"
    def get_queryset(self):
        tag = get_object_or_404(Tag, name__iexact=self.kwargs['tag_name'])
        return Post.objects.filter(tags__name__icontains=tag.name)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag_name'] = self.kwargs['tag_name']
        return context
    

class SearchView(ListView):
    model = Post
    template_name = "blog/search_results.html"
    def get_queryset(self):
        query = self.request.GET.get('to_search', '')
        return Post.objects.filter(Q(title__icontains=query)|Q(content__icontains=query))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('to_search', '')
        return context
    

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("login")
    else:
        return redirect("home")
