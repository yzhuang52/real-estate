# Generated by Django 3.2.7 on 2022-08-11 16:05

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='country',
            field=django_countries.fields.CountryField(default='AM', max_length=2, verbose_name='Country'),
        ),
    ]
