from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from django.views.generic import View

from authentication.forms import LoginForm
from authentication.models import Company, Branch

from . import forms

#user authetification===================================================
class LoginPageView(View):
    form_class = LoginForm
    template_name = 'authentication/login.html'
    def get(self, request):
        form = self.form_class()
        message = 'connexion'
        return render(request, self.template_name, context={'form': form, 'message': message})

    def post(self, request):
        form = self.form_class(request.POST)
        message = ''
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('order-list')
        message = 'Identifiants invalides.'
        return render(request, self.template_name, context={'form': form, 'message': message})

def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'authentication/signup.html', context={'form': form})

def logout_user(request):
    logout(request)
    return redirect('login')

#staff administration====================================================================

@login_required
def group_admin(request):
    company=Company.objects.filter()
    branch =Branch.objects.filter()
    
    return render(request,
    'authentication/group.html',
    {'company': company, 'branch': branch})
