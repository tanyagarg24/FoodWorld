# Generated by Django 2.2 on 2019-09-03 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_order_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='reviewgiven',
            field=models.BooleanField(default=False),
        ),
    ]
