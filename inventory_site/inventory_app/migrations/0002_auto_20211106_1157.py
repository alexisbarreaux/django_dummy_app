# Generated by Django 3.2.9 on 2021-11-06 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Store name')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='GTIN',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='product',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=40, verbose_name='First name')),
                ('lastname', models.CharField(max_length=40, unique=True, verbose_name='Last name')),
                ('current_store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory_app.store')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='current_store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory_app.store'),
        ),
    ]