from django.shortcuts import render
from django.http import HttpResponse

from purchases_auth.models import Auth_datas
from purchases_auth.forms import Order_form

def order_list(request):
    auth_datas = Auth_datas.objects.all()
    return render(request,
    'purchases_auth/order.html',
    {'auth_datas': auth_datas})

def order_detail(request, id):
    auth_datas = Auth_datas.objects.get(id=id)
    return render(request,
    'purchases_auth/order_detail.html',
    {'auth_datas':auth_datas})

def order_create(request):
    if request.method == 'POST':
        order_form = Order_form(request.POST)
        if order_form.is_valid():
            auth_datas = order_form.save()

            #Redirection problem._____________________________________________________
            return HttpResponse('order-detail', auth_datas.id)
    else:
        order_form = Order_form()

    return render(request,
    'purchases_auth/order_create.html',
    {'order_form': order_form})

def about(request):
    return HttpResponse('<h1>About apps</h1>')