from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request,nome):
    return HttpResponse(f'<h1>Hello {nome}!</h1>')
def soma(request, n1, n2):
    new_n1 = int(n1)
    new_n2 = int(n2)
    soma = new_n1+new_n2
    return HttpResponse(f'<h1>O total é {soma}</h1>')
def sub(request, n1, n2):
    new_n1 = int(n1)
    new_n2 = int(n2)
    sub = new_n1-new_n2
    return HttpResponse(f'<h1>O total é {sub}</h1>')
def divi(request, n1, n2):
    new_n1 = int(n1)
    new_n2 = int(n2)
    divi = new_n1/new_n2
    return HttpResponse(f'<h1>O total é {divi}</h1>')
def mult(request, n1, n2):
    new_n1 = int(n1)
    new_n2 = int(n2)
    mult = new_n1*new_n2
    return HttpResponse(f'<h1>O total é {mult}</h1>')
