from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_view(*args, **kwargs):
    return HttpResponse("<h1>Chuje Muje Dżango Srango</h1>")
    
def contact_view(*args, **kwargs):
    return HttpResponse("<h1>  0-700 wypierdalaj</h1>")
