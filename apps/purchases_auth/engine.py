import datetime
import logging

from django.conf import settings

from django.template.loader import render_to_string
from django.core.mail import send_mail, EmailMessage

from authentication.models import Company, Branch, User
from purchases_auth.models import Process, Order

class Engine:

    def order_temp(request_user):
        order_temp = Order()
        user = request_user

        day=datetime.datetime.now().day
        count=0
        if Order.objects.all().exists():
            parts=Order.objects.latest('order_id').order_id.split("-")
            day=int(parts[2])
            count=int(parts[3])

        if settings.GLOBAL_DAY is None:
            settings.GLOBAL_DAY=day
         
        if settings.GLOBAL_COUNT is None:                       
            settings.GLOBAL_COUNT=count + 1

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

        process=order.process
        branch=order.branch
        company=Branch.objects.get(id=branch.id).company

        controler=process.controler

        if(order.price>process.process_threshold):
            controler=branch.controler
            order.notified_controler.add(process.controler)

        if(order.price>process.branch_threshold):
            controler=company.controler
            order.notified_controler.add(branch.controler)

        if(order.price>process.company_threshold):
            controler=company.super_controler
            order.notified_controler.add(company.controler)

        if(order.payment_method.controler is not None):
            order.notified_controler.add(order.payment_method.controler)

        order.controler_login = controler
        order.save()

        logging.info("test_engine",
            order.branch.company,
            order.branch,
            order.controler_login,
            order.notified_controler,)
            
    def send_mail(id):
        order = Order.objects.get(id=id)
        
        subject = 'New Order : ' + order.order_id
        
        html_template = 'order_auth_email.html'
        context = {'order': order}
        html_content = render_to_string(html_template, context)
        
        from_email = order.asker_login.email
        to_email = [order.controler_login.email,]
        to_email_copy= [c.email for c in order.notified_controler.all()]
        
        email = EmailMessage(subject, html_content, from_email, to_email, bcc=to_email_copy)
        email.content_subtype = "html"

        email.send()
