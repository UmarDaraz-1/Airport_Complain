from django.db import models

# Create your models here.
class Flight(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date = models.DateTimeField(max_length=255,auto_now_add=True)
    flight_name = models.CharField(max_length=255, blank=True, null=True)
    flight_no = models.CharField(max_length=255, blank=True, null=True)
    flight_day = models.CharField(max_length=255, blank=True, null=True)
    flight_date = models.DateTimeField(max_length=255,auto_now_add=True)
    flight_cancellation = models.CharField(max_length=255)
    flight_time = models.CharField(max_length=255, blank=True, null=True)
    select = models.CharField(max_length=255, blank=True, null=True)
    

    def __str__(self):
        return self.first_name