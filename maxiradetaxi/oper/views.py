from django.shortcuts import render
from django.http import HttpResponse


def operator(request):
    #return HttpResponse("<h4>Hello world</h4>")
    return render(request, 'oper/operator.html')
