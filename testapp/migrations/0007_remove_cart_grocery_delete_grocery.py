# Generated by Django 4.1 on 2022-08-10 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0006_grocery_qualities'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='grocery',
        ),
        migrations.DeleteModel(
            name='Grocery',
        ),
    ]