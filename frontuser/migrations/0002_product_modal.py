# Generated by Django 2.0.6 on 2018-07-07 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontuser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='modal',
            field=models.TextField(blank=True),
        ),
    ]
