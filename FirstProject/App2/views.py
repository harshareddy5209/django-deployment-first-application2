from django.shortcuts import render
from django.http import HttpResponse;
import datetime;

# Create your views here.
def f22(request):
    time=datetime.datetime.now();
    msg="<h1>Hello User..!!<br/><br/>Server Date & Time::"+str(time)+"</h1><hr/>";  
    return HttpResponse(msg);