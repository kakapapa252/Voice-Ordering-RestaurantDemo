# Generated by Django 3.2.6 on 2021-09-08 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='isSpecial',
            field=models.BooleanField(default=False),
        ),
    ]
