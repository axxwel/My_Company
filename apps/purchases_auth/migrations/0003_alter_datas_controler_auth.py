# Generated by Django 4.1.4 on 2022-12-15 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchases_auth', '0002_datas_asker_login_datas_controler_auth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datas',
            name='controler_auth',
            field=models.IntegerField(choices=[('AUTHORIZED', 'Authorized'), ('REFUSED', 'Refused'), ('PENDING', 'Pending')], max_length=10),
        ),
    ]
