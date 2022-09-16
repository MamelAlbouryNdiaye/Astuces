from django.shortcuts import render
from .models import Projet #+
"from django.http import HttpResponse"
# Create your views here.

#def FirstView(request):
   #return HttpResponse('Hi Amma Mbaye!!')

def index(request):
    projet = Projet.objects.all()
    return render(request,'index.html',{'projet':projet})
