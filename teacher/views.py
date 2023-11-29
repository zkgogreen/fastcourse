from app.app import auth, kelas as kls
from app.zoom import createMeeting
from teacher.models import Schadule, Room, Teacher
from user.models import Users
from owner.models import Level
from django.contrib.auth.models import User
from django.shortcuts import render
# Create your views here.

context = {
    'url':'index',
    'title':'index',
    'icon':'static/assets/icon.png'
}

def index(request):
    teacher                 = Teacher.objects.get_or_create(user=request.user)
    room                    = Schadule.objects.filter(mentor=request.user).count()
    context['jadwal']       = Schadule.objects.filter(mentor=request.user)
    context['orang']        = room
    context['info']         = teacher[0]
    context['user']         = Users.objects.get(user=request.user)
    return render(request, 'teacher/index.html', context)
