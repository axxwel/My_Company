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
    users=User.objects.filter()

    company_form = forms.CompanyForm()
    branch_form = forms.BranchForm()
    user_form = forms.UserForm()

    if request.method == 'POST':
        if 'add_company' in request.POST:
            company_form = forms.CompanyForm(request.POST)
            if company_form.is_valid():
                company_form.save()
                return redirect('config-home')
        
        if 'add_branch' in request.POST:
            branch_form = forms.BranchForm(request.POST)
            if branch_form.is_valid():
                branch_form.save()
                return redirect('config-home')

        if 'add_user' in request.POST:
            user_form = forms.UserForm(request.POST)
            if user_form.is_valid():
                user_form.save()
                return redirect('config-home')

    context={
    'companys': companys,
    'company_form': company_form,
    'branchs': branchs,
    'branch_form': branch_form,
    'users': users,
    'user_form': user_form,}

    return render(request,'authentication/config.html',context=context)