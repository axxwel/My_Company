from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test

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

def logout_user(request):
    logout(request)
    return redirect('login')

#staff authentification==================================================================
def in_group(user, group_name):
    return user.groups.filter(name=group_name).exists()

#staff administration====================================================================
@user_passes_test(lambda u: in_group(u, 'staff_admin'))
@login_required
def config_home(request):
    companys=Company.objects.filter()
    branchs=Branch.objects.filter()
    users=User.objects.filter()

    company_form = CompanyForm()
    branch_form = BranchForm()
    user_form = UserForm()

    if request.method == 'POST':
        if 'add_company' in request.POST:
            company_form = CompanyForm(request.POST)
            if company_form.is_valid():
                company_form.save()
                return redirect('config-home')
        
        if 'add_branch' in request.POST:
            branch_form = BranchForm(request.POST)
            if branch_form.is_valid():
                branch_form.save()
                return redirect('config-home')

        if 'add_user' in request.POST:
            user_form = UserForm(request.POST)
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