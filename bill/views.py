from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Bnda
from .forms import PersonRegistration


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        # Redirect to a success page.
            return redirect('home')
        else:
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html')

@login_required
def index(request):
    persons = Bnda.objects.all()
    content = {'persons': persons}
    return render(request, 'bill/index.html', content)


def newuser(request):
    if request.method=='POST':
        fm = PersonRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            bil = fm.cleaned_data['bill']
            pd = fm.cleaned_data['paidDate']
            reg = Bnda(name=nm, bill=bil, paidDate=pd)
            reg.save()
    else:
        fm = PersonRegistration()        
    return render(request, 'bill/newcon.html', {'form':fm})  



def delete_data(request, id):
    if request.method == 'POST':
        bo = Bnda.objects.get(pk=id)
        bo.delete()
        return redirect('home')


def update_data(request, id):
   if request.method == 'POST':
       pi = Bnda.objects.get(pk=id)
       fm = PersonRegistration(request.POST, instance=pi)
       if fm.is_valid():
           fm.save()
   else:
        pi = Bnda.objects.get(pk=id)
        fm = PersonRegistration(instance=pi)        
   return render(request, 'bill/update.html', {'form':fm})
