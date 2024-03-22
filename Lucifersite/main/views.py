from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h4>Test server</4>")

def about(request):
    return HttpResponse("<h4>Site about us</4>")