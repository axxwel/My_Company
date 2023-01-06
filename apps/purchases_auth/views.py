import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from purchases_auth.models import Order
from authentication.models import User
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
        if order_form.is_valid():
            global day
            global count
            try: 
                if day is not None: pass
            except NameError: day = datetime.datetime.now().day 
            try: 
                if count is not None: pass
            except NameError: count = 0

            day = datetime.datetime.now().day
            if(day != datetime.datetime.now().day):
                day=datetime.datetime.now().day
                count=1
            else:
                count+=1

            order = order_form.save(commit=False)
            order.order_id="AA"+datetime.datetime.now().strftime("%Y-%m-%d-")+f'{count:03d}'
            order.asker_login=request.user
            order.save()

            return redirect('order-detail', order.id)
    else:
        order_form = Order_form()

    return render(request,
    'purchases_auth/order_create.html',
    {'order_form': order_form})
