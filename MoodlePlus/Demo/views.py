from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import UserForm
from .models import *


# Create your views here.
def index(request):
    context = {}
    return render(request, 'Demo/index.html', context)


def register(request):
    form = UserForm()
    registered= False
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            t= form.save()
            t.set_password(t.password)
            if form.cleaned_data['identity'] == UserForm.STUDENT:
                t.is_staff = False
                t.save()
                s = Student.objects.create(user=t)
                s.save()
            elif form.cleaned_data['identity'] == UserForm.PROFESSOR:
                t.is_staff = True
                t.save()
                p = Professor.objects.create(user=t)
                p.save()
            else:
                raise RuntimeError('Unknown identity. Ask Xinyu for help.')
            registered= True
        else:
            print(form.errors)
    else:
        pass
    context = {'form': form, 'registered': registered}
    return render(request, 'Demo/register.html', context)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('Demo:index'))
            else:
                return HttpResponse("Your LTC++ account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'Demo/login.html')