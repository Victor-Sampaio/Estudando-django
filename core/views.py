from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def hello(request,nome):
    return HttpResponse('hello {}'.format(nome))

def w3scholl(request):
    return redirect('https://www.w3schools.com/')