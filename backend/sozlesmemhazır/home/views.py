from django.shortcuts import render,HttpResponse
from .models import *
# Create your views here.

def sayfa(request):
    sozluk = {}
    sozluk["sozlesme"] = sozlesme.objects.all()
    return render(request ,"index.html",sozluk)
