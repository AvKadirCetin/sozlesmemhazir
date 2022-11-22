from django.shortcuts import render,HttpResponse
from .models import *
# Create your views here.
from xhtml2pdf import pisa
def sayfa(request):
    sozluk = {}
    sozluk["sozlesme"] = sozlesme.objects.all()
    sozlesme.objects.first()
    m = sozlesme.objects.first()
    

    return render(request ,"index.html",sozluk)
