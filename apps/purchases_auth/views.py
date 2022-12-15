from django.shortcuts import render
from django.http import HttpResponse

from purchases_auth.models import Auth_datas

def hello(request):
    auth_datas = Auth_datas.objects.all()
    return render(request,
    'purchases_auth/hello.html',
    {'auth_datas': auth_datas})

def about(request):
    return HttpResponse('<h1>About apps</h1>')