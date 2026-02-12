# views.py
from django.shortcuts import redirect, render
from .models import Measurement

# Create your views here.

def index(request):
    mem=Measurement.objects.all()
    return render(request,'index.html',{'mem':mem})

def add(request):
    return render(request,'add.html')

def addrec(request):
    x=request.POST['Temperature']
    y=request.POST['Humidity']
    mem=Measurement(Temperature=x, Humidity=y)
    mem.save()
    return redirect("/")

def delete(request,id):
    mem=Measurement.objects.get(id=id)
    mem.delete()
    return redirect("/")

def update(request,id):
    mem=Measurement.objects.get(id=id)
    return render(request,'update.html',{'mem':mem})

def uprec(request,id):
    x=request.POST['Temperature']
    y=request.POST['Humidity']
    mem=Measurement.objects.get(id=id)
    mem.Temperature=x
    mem.Humidity=y
    mem.save()
    return redirect("/")