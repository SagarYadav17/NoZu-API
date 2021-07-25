# Generated by Django 3.2.5 on 2021-07-25 13:23

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='state',
        ),
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
