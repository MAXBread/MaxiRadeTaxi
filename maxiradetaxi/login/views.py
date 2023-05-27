from django.shortcuts import render
from django.http import HttpResponse


def login(request):
    #return HttpResponse("<h4>Hello world</h4>")
    return render(request, 'login/login.html')

