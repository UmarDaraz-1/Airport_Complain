# Generated by Django 4.1.1 on 2023-01-28 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airport_complain', '0005_alter_flight_flight_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='flight_time',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
