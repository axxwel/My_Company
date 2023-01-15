from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from authentication.models import Company, Branch, User


class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=6, help_text='')
    password1 = forms.CharField(max_length=63, widget=forms.PasswordInput, label='password')
    password2 = forms.CharField(max_length=63, widget=forms.PasswordInput, label='password confirmation')

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email',)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label='username')
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='password')

class CompanyForm(forms.ModelForm):
    add_company = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = Company
        fields = [
            'name',
            'controler_login',
            'super_controler_login'
        ]

class BranchForm(forms.ModelForm):
    add_branch = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = Branch
        fields = [
            'name',
            'company',
            'controler_login',
            'members',
        ]

class UserForm(forms.ModelForm):
    add_user = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = User
        fields = [
            'username',
        ]