# Generated by Django 3.2.9 on 2021-11-06 10:22

from django.db import migrations, models
import inventory_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_store', models.CharField(max_length=200, verbose_name='Shop')),
                ('product_name', models.CharField(max_length=200, verbose_name='Name')),
                ('GTIN', models.CharField(max_length=14, verbose_name='Name')),
                ('shortest_expiry_date', models.DateField(default=inventory_app.models.Product.current_date, verbose_name='Products expire at')),
                ('last_modified', models.DateField(auto_now=True)),
            ],
        ),
    ]
