# Generated by Django 4.1.1 on 2023-01-28 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('airport_complain', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flight',
            name='mobile_no',
        ),
    ]
