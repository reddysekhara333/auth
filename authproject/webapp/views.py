from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from webapp.forms import userform


def home(request):
    return render(request,'test/home.html')
@login_required()
def java(request):
    return render(request,'test/javaexam.html')
@login_required()
def python(request):
    return render(request,'test/pythonexam.html')

@login_required()
def aptitude(request):
    return render(request,'test/Aptitudeexam.html')

def logout(request):
    return render(request,'test/logout.html')
def signup(request):
    form=userform()
    if request.method=='POST':
        form=userform(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'test/signup.html',{'form':form})