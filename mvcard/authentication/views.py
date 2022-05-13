from django.contrib.auth import authenticate, login
from django.contrib.auth.views import *
from django.shortcuts import render, redirect

from django.views import View

from authentication.forms import UserCreationForm


class LoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True


class RegisterView(View):
    template_name = 'registration/signin.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('account')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


class PasswordResetView(PasswordResetView):
    template_name = 'registration/recover.html'


class PasswordResetDoneView(PasswordResetDoneView):
    template_name = 'registration/recover-send.html'


