from user.models import Users, UserSchadule
from app.mydate import fetchday
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import RoomForm
from .models import Room, Schadule, Teacher
# Create your views here.

context = {
    'url':'bootcamp',
    'title':'bootcamp',
    'icon':'static/assets/icon.png'
}

def index(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.mentor = request.user
            form.save()
            for day in fetchday(form.mulai, form.jadwal):
                Schadule.objects.create(room=form, mentor=request.user, tanggal=day, level=form.level)
            return redirect("teacher:bootcamp")
    else:
        form = RoomForm()
    context['form']         = form
    context['teacher']      = Teacher.objects.get(user=request.user)
    context['user']         = Users.objects.get(user=request.user)
    context['jadwal']       = Room.objects.filter(mentor=request.user)
    context['events']        = Schadule.objects.filter(mentor=request.user)
    return render(request, 'teacher/bootcamp/index.html', context)

def reschadule(request):
    if request.method == 'POST':
        sch = Schadule.objects.filter(id=request.POST['id'])
        UserSchadule.objects.filter(schadule=sch.first()).update(tanggal=request.POST['tanggal'])
        sch.update(time=request.POST['time'], tanggal=request.POST['tanggal'])
    return redirect("teacher:bootcamp")
