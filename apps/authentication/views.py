from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from django.views.generic import View

from authentication.forms import LoginForm, CompanyForm, BranchForm, UserForm
from authentication.models import Company, Branch, User

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
def config_home(request):
    companys=Company.objects.filter()
    branchs=Branch.objects.filter()

    new_company = CompanyForm()
    new_branch = BranchForm()

    if request.method == 'POST':
        if 'new_company' in request.POST:
            new_company = forms.CompanyForm(request.POST)
            if new_company.is_valid():
                new_company.save()
                return redirect('config-home')
        
        if 'new_branch' in request.POST:
            new_branch = forms.CompanyForm(request.POST)
            if new_branch.is_valid():
                new_branch.save()
                return redirect('config-home')

    context={
    'companys': companys, 'new_company': new_company,
    'branchs': branchs, 'new_branch': new_branch}

    return render(request,'authentication/config.html',context=context)


""" def config_home(request):
    companys=Company.objects.filter()
    branchs=Branch.objects.filter()
    users=User.objects.filter()

    new_company = CompanyForm()
    new_branch = BranchForm()
    new_user = UserForm()

    if request.method == 'POST':
        if 'new_company' in request.POST:
            new_company = forms.CompanyForm(request.POST)
            if new_company.is_valid():
                new_company.save()
                return redirect('config-home')

        if 'new_branch' in request.POST:
            new_branch = forms.BranchForm(request.POST)
            if new_branch.is_valid():
                new_branch.save()
                return redirect('config-home')

        if 'new_user' in request.POST:
            new_user = forms.UserForm(request.POST)
            if new_user.is_valid():
                new_user.save()
                return redirect('config-home')

    return render(request,
    'authentication/config.html',
    {'companys': companys, 'new_company': new_company,
    'branchs': branchs, 'new_branch': new_branch,
    'users': users, 'new_user': new_user}) """
