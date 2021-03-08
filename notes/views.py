from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from .models import Note

# Create your views here.
def home_view(request,*args,**kwarg):
    return HttpResponse('<h1>Hello world</h1>')

