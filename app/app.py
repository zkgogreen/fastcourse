from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from user.models import Cart, Users, UserCourse, UserLesson
from teacher.models import Pelajaran
from owner.models import Setting as land
from django.db.models import Avg

def kelas(request, many=True):
    if many == True:
        kelasarr = []
        user = Users.objects.get(user=request.user.id)
        kelas = UserCourse.objects.filter(user=user)
        for i in kelas:
            lesson =  Pelajaran.objects.filter(kelas=i.kelas).count()
            lessonDone = UserLesson.objects.filter(user=request.user.id, kelas=i.kelas).count()
            kelasarr.append({
                'name':i.kelas.kelas,
                'slug':i.kelas.slug,
                'photo':i.kelas.photo,
                'level':i.kelas.level.name,
                'kategori':i.kelas.kategori.name,
                'lesson':lesson,
                'lessondone':lessonDone,
                'percent': int(lessonDone / lesson * 100),
                'finish':i.finish,
                'history':UserCourse.objects.get(user=user, kelas=i.kelas),
                'star':UserCourse.objects.filter(kelas=i.kelas).aggregate(Avg('like'))['like__avg']
            })
    return kelasarr

def profile(request):
    return Users.objects.get_or_create(user=User(request.user.id))[0]

def auth(request, url, context):
    if not request.user.is_authenticated:
        return redirect("../accounts/login")
    path = request.path.split("/")
    gettitle = path[2] if path[2] else "dashboard"
    context.update({
        'title':gettitle,
        'user':profile(request),
        'icon':land.objects.get(id=1).icon,
        'menu':path[1]
    })
    
    if profile(request).status == 2 and path[1] != "teacher":
        return redirect("teacher:index")
    elif profile(request).status == 1 and path[1] != "user":
        return redirect("user:index")
    elif profile(request).status == 3 and path[1] != "owner":
        return redirect("owner:index")
    else:
        return render(request, 'member/'+path[1]+'/'+url+'.html', context)