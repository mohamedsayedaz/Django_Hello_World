from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def homePageView(request):
    return HttpResponse("Hello World!")


def aboutPageView(request):
    return HttpResponse("About Page")


def contactPageView(request):
    return HttpResponse("Contact Page")
