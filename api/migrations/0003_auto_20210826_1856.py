# Generated by Django 3.2.6 on 2021-08-26 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210824_1003'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='hasColors',
            new_name='hasToppings',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='colorOptions',
            new_name='sizes',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='sizeOptions',
            new_name='toppings',
        ),
    ]
