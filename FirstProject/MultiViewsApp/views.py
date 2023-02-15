from django.shortcuts import render
from django.http import HttpResponse;

# Create your views here.
def f1(request):
    return HttpResponse("<h2>Good Morning User..!!Have a Nice Day..</h2><hr/>");
def f2(request):
    return HttpResponse("<h2>Good Afternoon User..!!Hope you are doing Good....</h2><hr/>");
def f3(request):
    return HttpResponse("<h2>Good Evening User..!!How was your Day..</h2><hr/> ");
    