from django.template.loader import render_to_string
from django.core.mail import EmailMessage

from authentication.models import User
from purchases_auth.models import Order

class OrderAuthEmail:
    def __init__(self, id):
        self.id = id

    def send(id):
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