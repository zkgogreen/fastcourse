from django.shortcuts import render, redirect
from .models import Users
from owner.models import Langganan
import datetime

context = {
    'url':'upgrade',
    'title':'upgrade',
    'icon':'static/assets/icon.png'
}

def index(request):
    user                = Users.objects.get(user=request.user)
    context['langganan']= Langganan.objects.all().order_by("diskon")
    context['user']     = user
    return render(request, 'user/upgrade/index.html', context)

def upgrade(request):
    context['user']     = Users.objects.get(user=request.user)
    context['langganan']= Langganan.objects.all().order_by("diskon")
    return render(request, 'user/upgrade/purchase.html', context)