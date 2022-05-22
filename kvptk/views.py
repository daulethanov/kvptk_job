from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import Group
from django.views.generic import CreateView, ListView, TemplateView, DetailView

from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout

from .forms import CustomUserCreationForm
from .models import CustomUser


class HomepageView(TemplateView):
    template_name = 'pages/homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Главная'
        return context


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('homepage')
    template_name = 'users/signup.html'


class LoginView(LoginView):
    template_name = 'users/login.html'

    # Redirect from login page in case user already authenticated and loggedin
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('homepage')
        return self.render_to_response(self.get_context_data())


class ProfileView(DetailView):
    model = CustomUser
    template_name = 'base.html'
    context_object_name = 'profile'

