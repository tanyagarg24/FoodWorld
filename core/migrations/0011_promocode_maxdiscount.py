# Generated by Django 2.2 on 2019-09-07 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_promocode'),
    ]

    operations = [
        migrations.AddField(
            model_name='promocode',
            name='maxdiscount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
