from django.shortcuts import render, redirect
from django.views import View, generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy, reverse
from django.contrib.auth import logout

from .forms import SignUpForm, EditProfileForm

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeView
    success_url = reverse_lazy('home')

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
    
    class UserLogoutView(View):
        def get(self, request):
            logout(request)
            return redirect(reverse_lazy('login'))
