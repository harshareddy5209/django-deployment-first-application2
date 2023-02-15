from django.shortcuts import render
from django.http import HttpResponse;

# Create your views here.
def f11(request):
    return HttpResponse("<h1>Hello GoodMorning User..!!Have a Nice Day..</h1><hr/>");