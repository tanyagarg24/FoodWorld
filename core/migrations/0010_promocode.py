# Generated by Django 2.2 on 2019-09-07 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_order_reviewgiven'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promocode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('discountpercent', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
