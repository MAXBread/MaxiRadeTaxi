from django.shortcuts import render, redirect
from django.http import HttpResponse


def login(request):
    if request.method == 'POST':
        return redirect('operator')


    #return HttpResponse("<h4>Hello world</h4>")
    return render(request, 'login/login.html')

