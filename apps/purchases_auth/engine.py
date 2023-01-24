import datetime
import logging

from django.conf import settings

from django.template.loader import render_to_string
from django.core.mail import EmailMessage

from authentication.models import Company, Branch, User
from purchases_auth.models import Process, Order

class Engine:

    def order_temp(request_user):
        order_temp = Order()
        user = request_user

        logging.warning("test_engine_orderTemp",settings.GLOBAL_DAY,settings.GLOBAL_COUNT)

        if settings.GLOBAL_DAY is None:
            settings.GLOBAL_DAY=datetime.datetime.now().day
         
        if settings.GLOBAL_COUNT is None:                       
            settings.GLOBAL_COUNT = 1

        if(settings.GLOBAL_DAY != datetime.datetime.now().day):
            settings.GLOBAL_DAY=datetime.datetime.now().day
            settings.GLOBAL_COUNT = 1

        order_temp.order_id="AA"+datetime.datetime.now().strftime("%Y-%m-")+f'{settings.GLOBAL_DAY}-{settings.GLOBAL_COUNT:03d}'
        order_temp.date=datetime.datetime.now()

        order_temp.asker_login = user
        order_temp.branch = user.branch

        return order_temp
        
    def define_controler(id):
        order = Order.objects.get(id=id)

        logging.warning("test_engine",order.branch.company,order.branch)

        process=order.process
        branch=order.branch
        company=Branch.objects.get(id=branch.id).company

        controler=process.controler
        controler_copy=[]

        if(order.price>process.process_threshold):
            controler=branch.controler
            order.notified_controler.add(process.controler)

        if(order.price>process.branch_threshold):
            controler=company.controler
            order.notified_controler.add(branch.controler)

        if(order.price>process.company_threshold):
            controler=company.super_controler
            order.notified_controler.add(company.controler)

        if(order.payment_method=='Card'):
            order.notified_controler.add(company.controler)

        order.controler_login = controler
            
    def send_mail(id):
        order = Order.objects.get(id=id)

        controler_login = order.controler_login
        controler = User.objects.get(username=order.controler_login)

        subject = 'New Order: ' + order.order_id
        html_template = 'order_auth_email.html'
        context = {'order': order}
        from_email = 'from@example.com'
        to_list = [controler.email]

        html_content = render_to_string(html_template, context)

        email = EmailMessage(subject, html_content, from_email, to_list)
        email.content_subtype = "html"
        email.send()
