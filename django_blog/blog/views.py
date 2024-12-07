from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.base import TemplateView as BaseView
from .form import RegisterForm
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
    
    
class ProfileView(BaseView):
    template_name = 'blog/profile.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
    
    