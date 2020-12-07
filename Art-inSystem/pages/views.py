
# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import talep_detayi
from django import forms
from .forms import MyYeniTalep
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth




def index(request):
    return render(request, 'pages/index.html')



def talep(request):
    talepler = talep_detayi.objects.filter(adsoyad_id=request.user.id)
    return render(request, 'pages/talep.html', {'Taleplerim': talepler})


def yenitalep(request):
    if request.method == "POST":
        form = MyYeniTalep(request.POST)
        if form.is_valid():

            talep = form.save(commit=False)
            talep.adsoyad_id = request.user.id
            form.save()
            return redirect('talep')

    else:
        form = MyYeniTalep()
    return render(request, 'pages/yenitalep.html', {'form': form})
