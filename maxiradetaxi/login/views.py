from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .forms import LoginUserForm
from django.urls import reverse_lazy
from django.contrib.auth import logout


def login(request):
    if request.method == 'POST':
        return redirect('operator')

    return render(request, 'login/login.html')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login/login.html'

    def get_success_url(self):
        return reverse_lazy('operator')


def logout_user(request):
    logout(request)
    return redirect('login')
