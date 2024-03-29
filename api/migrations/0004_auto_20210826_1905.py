# Generated by Django 3.2.6 on 2021-08-26 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210826_1856'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='sizes',
        ),
        migrations.RemoveField(
            model_name='product',
            name='toppings',
        ),
        migrations.CreateModel(
            name='ToppingLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.product')),
                ('topping', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.topping')),
            ],
        ),
    ]
