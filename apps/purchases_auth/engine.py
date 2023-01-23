import datetime

from django.template.loader import render_to_string
from django.core.mail import EmailMessage

from authentication.models import Company, Branch, User
from purchases_auth.models import Process, Order

class Engine:
    def order_temp(request_user):
        order_temp = Order()
        user = request_user

        global day
        global count
        
        try: 
            if day is not None: pass
        except NameError: day = datetime.datetime.now().day 
        try: 
            if count is not None: pass
        except NameError: count = 1                            
    
        day_temp=day
        count_temp=count
        if(day_temp != datetime.datetime.now().day):
            day_temp=datetime.datetime.now().day
            count_temp=1
        else:
            count_temp+=1

        order_temp.order_id="AA"+datetime.datetime.now().strftime("%Y-%m-%d-")+f'{count_temp:03d}'
        order_temp.date=datetime.datetime.now()

        order_temp.asker_login = user

        return order_temp

    def define_controler(id):
        order = Order.objects.get(id=id)
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
