from django.shortcuts import render
from django.http import HttpResponse

from purchases_auth.models import Datas

def hello(request):
    datas = Datas.objects.all()
    return render(request,
    'purchases_auth/hello.html',
    {'datas': datas})

def about(request):
    return HttpResponse('<h1>About apps</h1>')