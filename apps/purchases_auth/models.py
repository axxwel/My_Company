from django.db import models

class Auth_users(models.Model):
    def __str__(self):
        return f'{self.login}'

    login = models.fields.CharField(null=False, unique=True, max_length=5)
    first_name = models.fields.CharField(max_length=50)
    name = models.fields.CharField(max_length=50)
    password = models.fields.CharField(max_length=50)
    email = models.fields.EmailField(max_length=100)

class Auth_datas(models.Model):
    def __str__(self):
        return f'{self.name}'

    class auth_status(models.TextChoices):
        AUTHORIZED = 'Authorized'
        REFUSED = 'Refused'
        PENDING = 'Pending'

    name = models.fields.CharField(max_length=30, unique=True)
    date = models.fields.DateTimeField(auto_now=True)
    user_login = models.ForeignKey(Auth_users, null=True, on_delete=models.SET_NULL)
    asker_login = models.fields.CharField(max_length=30)
    controler_login = models.fields.CharField(max_length=30)
    controler_auth = models.fields.CharField(choices=auth_status.choices, default=auth_status.PENDING, max_length=10)

'''
    m_demand_id = 0 #Numero d'AA (AA2022-12-13-006)
    m_date = "2022-12-13"

    m_asker = "demandeur"
    m_branch = "branche"
    m_process = "processus"
    m_purchase_type = "type d'achat"

    m_payment_method = "methode de payment"

    m_product = "produit"
    m_price = 0 #prix

    m_asker_comment = "asker comment"

    m_vendor = "vendeur"
    m_unit_price = 0 #prix unitaire
    m_delivery_date = "2022-12-13"


    m_threshold = 0 #seuil
    m_controler = "controler"

    m_controler_auth = False
    m_controler_comment = "controler comment"
'''