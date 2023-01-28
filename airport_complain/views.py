from django.shortcuts import render, redirect
from .models import *

# Create your views here.


def home(request):
     if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        date = request.POST.get("created_at")
        flight_name = request.POST.get("flight_name")
        flight_no = request.POST.get("flight_no")
        flight_date = request.POST.get("created_at")
        flight_cancellation = request.POST.get("flight")
        flight_time = request.POST.get("flight_time")
        flight_day = request.POST.get("flight_day")
        select = request.POST.get("select")

        flight = Flight(first_name = first_name, last_name = last_name, date = date, flight_name = flight_name, flight_no = flight_no, flight_date = flight_date, flight_cancellation = flight_cancellation, flight_time = flight_time, flight_day = flight_day, select = select)
        flight.save()
        return redirect('/')
     return render(request,'home.html')
    
 