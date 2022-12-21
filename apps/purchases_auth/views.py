from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from purchases_auth.models import Order
from purchases_auth.forms import Order_form

@login_required
def order_list(request):
    asker_order =Order.objects.filter(asker_login=request.user.id)
    controler_order =Order.objects.filter(controler_login=request.user.id, controler_auth="Pending")
    
    return render(request,
    'purchases_auth/order.html',
    {'asker_order': asker_order, 'controler_order': controler_order})

def order_detail(request, id):
    order = Order.objects.get(id=id)
    return render(request,
    'purchases_auth/order_detail.html',
    {'order':order})

def order_create(request):
    if request.method == 'POST':
        order_form = Order_form(request.POST)
        order_form["asker_login"]=request.user.id


        if order_form.is_valid():
            order = order_form.save()
            return redirect('order-detail', order.id)
    else:
        order_form = Order_form()

    return render(request,
    'purchases_auth/order_create.html',
    {'order_form': order_form})