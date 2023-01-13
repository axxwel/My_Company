import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from purchases_auth.models import Order
from purchases_auth.forms import Order_form, Order_auth

@login_required
def order_list(request):
    asker_order =Order.objects.filter(asker_login=request.user.id)
    controler_order =Order.objects.filter(controler_login=request.user.id, controler_auth="Pending")
    
    return render(request,
    'purchases_auth/order.html',
    {'asker_order': asker_order, 'controler_order': controler_order})

@login_required
def order_create(request):
    filled_field = Order()

    global day
    global count
    try: 
        if day is not None: pass
    except NameError: day = datetime.datetime.now().day 
    try: 
        if count is not None: pass
    except NameError: count = 0                            
    
    filled_day=day
    filled_count=count
    if(day != datetime.datetime.now().day):
        filled_day=datetime.datetime.now().day
        filled_count=1
    else:
        filled_count=count+1

    filled_field.order_id="AA"+datetime.datetime.now().strftime("%Y-%m-%d-")+f'{filled_count:03d}'
    filled_field.date=datetime.datetime.now()
    filled_field.asker_login = request.user

    if request.method == 'POST':
        order_form = Order_form(request.POST)
        if order_form.is_valid():
            
            day=filled_day
            count=filled_count

            order = order_form.save(commit=False)
            order.order_id=filled_field.order_id
            order.date=filled_field.date
            order.asker_login=filled_field.asker_login
            order.save()

            return redirect('order-detail', order.id)
    else:
        order_form = Order_form()

    return render(request,
    'purchases_auth/order_create.html',
    {'order_form': order_form, 'filled_field': filled_field})

@login_required
def order_detail(request, id):
    order = Order.objects.get(id=id)
    controler_order =Order.objects.filter(id=id, controler_login=request.user.id, controler_auth="Pending")
    auth = Order_auth(request.POST, instance=order)
    
    if request.method == 'POST':
        if auth.is_valid():
            auth.save()
            return redirect('order-detail', id=order.id)

    return render(request,
    'purchases_auth/order_detail.html',
    {'order':order, 'auth':auth, 'controler_order':controler_order})
