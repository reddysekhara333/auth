from django.shortcuts import render

# Create your views here.
from webapp.models import movie
from .forms import fomovie
def moiveview(request):
    return render(request,'my/index.html')

def listmovies(request):
    form=movie.objects.all()
    return render(request,'my/list.html',{'form':form})

def addmovie(request):
    d=fomovie()
    if request.method=='POST':
        d=fomovie(request.POST)
        if d.is_valid():
            d.save(commit=True)
        return moiveview(request)
    return render(request,'my/add.html',{'d':d})