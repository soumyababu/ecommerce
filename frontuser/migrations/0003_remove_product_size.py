# Generated by Django 2.0.6 on 2018-07-07 02:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontuser', '0002_product_modal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
    ]
