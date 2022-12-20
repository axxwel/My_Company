from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from purchases_auth.models import Order
from purchases_auth.forms import Order_form

from authentication.models import User

@login_required
def order_list(request):
    order_asker = Order.objects.filter(asker_login__exact=User.username)
    #order_control = Order.objects.filter(controler_login=User.username)
    return render(request,
    'purchases_auth/order.html',
    {'order_asker': order_asker})

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