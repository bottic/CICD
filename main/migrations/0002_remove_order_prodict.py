# Generated by Django 4.1.1 on 2022-10-13 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='prodict',
        ),
    ]