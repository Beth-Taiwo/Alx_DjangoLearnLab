from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import TemplateView
from .form import RegisterForm, UserProfileForm, ProfileForm
from django.contrib.auth import login

# Create your views here.

def home_view(request):
    return render(request, 'blog/base.html') 

class RegisterView(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('home') # redirect to home page on success
    template_name = 'blog/base.html'
    
    def form_valid(self, form):
        form.save()
        login(self.request, user)
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Sign Up'
        return context
    

class ProfileView(TemplateView):
    template_name = 'blog/profile.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        
         # Ensure the profile exists
        if not hasattr(user, 'profile'):
            Profile.objects.create(user=user)

        context['user'] = user
        context['user_form'] = UserProfileForm(instance=user)
        context['profile_form'] = ProfileForm(instance=user.profile)
        return context
    
    def post(self, request, *args, **kwargs):
        user_form = UserProfileForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')  # Redirect to the same page or another page

        return self.render_to_response(self.get_context_data(user_form=user_form, profile_form=profile_form))
    
    
class PostView(TemplateView):
    template_name = 'blog/posts.html'
    
    
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    else:
        return redirect('home')