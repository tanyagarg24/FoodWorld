# Generated by Django 2.2 on 2019-08-25 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_order_orderid'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='orderid',
            field=models.CharField(default='123', max_length=50),
        ),
    ]
