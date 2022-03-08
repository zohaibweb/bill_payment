from django.shortcuts import render, redirect
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
            Bnda.objects.create(name= fm.cleaned_data['name'], bill = form.cleaned_data['bill'], paidDate= fm.cleaned_data['paidDate'])
    else:
        fm = PersonRegistration()        
    return render(request, 'bill/newcon.html', {'form':fm})    