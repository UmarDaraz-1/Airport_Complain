# Generated by Django 4.1.1 on 2023-01-28 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airport_complain', '0002_remove_flight_mobile_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='flight_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]