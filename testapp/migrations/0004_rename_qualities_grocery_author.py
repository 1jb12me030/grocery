# Generated by Django 4.1 on 2022-08-10 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_rename_quantiles_grocery_qualities'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grocery',
            old_name='qualities',
            new_name='author',
        ),
    ]
