from django.shortcuts import render
from django.http import HttpResponse

from purchases_auth.models import Order
from purchases_auth.forms import Order_form


def order_list(request):
    order = Order.objects.all()
    return render(request,
    'purchases_auth/order.html',
    {'order': order})

def order_detail(request, id):
    order = Order.objects.get(id=id)
    return render(request,
    'purchases_auth/order_detail.html',
    {'order':order})

def order_create(request):
    if request.method == 'POST':
        order_form = Order_form(request.POST)
        if order_form.is_valid():
            order = order_form.save()

            #Redirection problem._____________________________________________________
            return HttpResponse('order-detail', order.id)
    else:
        order_form = Order_form()

    return render(request,
    'purchases_auth/order_create.html',
    {'order_form': order_form})

def about(request):
    return HttpResponse('<h1>About apps</h1>')