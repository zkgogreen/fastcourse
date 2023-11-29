from app.app import auth
from teacher.models import Kelas, Pelajaran, Bab, Questions
from .models import UserCourse, UserLesson, Users, UserQuestion, UserLatihan, UserBab
from django.http import JsonResponse
from django.views import View
from django.db.models import Avg
from django.shortcuts import render, redirect
from django.contrib import messages
from user.util.pelajaran import bab_navigate
from user.forms import FormKomentar

# Create your views here.

context = {
    'url': 'kelas',
    'title': 'kelas',
    'icon': 'static/assets/icon.png'
}

class index(View):

    def get(self, request, slug=None):
        if not slug:
            context["user"] = Users.objects.get(user=request.user)
            context["kelas"] = Kelas.objects.all()
            return render(request, 'user/kelas/index.html', context)

        else:
            kelas = Kelas.objects.get(slug=slug)
            enroll = UserCourse.objects.filter(user=request.user, kelas=kelas)
            lesson = UserLesson.objects.filter(user=request.user, kelas=kelas)
            if not enroll.exists():
                UserCourse.objects.create(user=request.user, kelas=kelas)
                return redirect("user:koridor", slug=slug)
            context["user"] = Users.objects.get(user=request.user)
            context["kelas"] = kelas
            context["enroll"] = enroll[0]
            context['history'] = enroll.first() if enroll.exists() else None
            context["pelajaran"] = str(lesson.filter(isdone=True).count()) + " / " + str(Pelajaran.objects.filter(kelas=kelas).count())
            return render(request, 'user/kelas/koridor.html', context)

    def post(self, request, slug):
        kelas = Kelas.objects.get(slug=slug)
        pelajaran = Pelajaran.objects.filter(kelas=kelas).order_by("urutan")
        bab = Bab.objects.filter(kelas=kelas).order_by("urutan")

        usercourse = UserCourse.objects.filter(user=request.user, kelas=kelas)

        usercourse.update(enroll=True, user=request.user, kelas=kelas, bab_kelas=bab.first(), pelajaran=pelajaran.filter(bab_kelas=bab.first()).first())
        for i in pelajaran:
            UserLesson.objects.create(userCourse=usercourse.first(), user=request.user, kelas=kelas, pelajaran=i, bab_kelas=i.bab_kelas)
        for i in bab:
            UserBab.objects.create(userCourse=usercourse.first(), user=request.user, kelas=kelas, bab_kelas=i)
        return redirect("user:koridor", slug=slug)

class pelajaran(View):
    def get(self, request, slug , urutan_bab, urutan_pelajaran):
        context.update(bab_navigate(request, slug, urutan_bab, urutan_pelajaran))

        context['halaman'] = 'pelajaran'
        context['FormKomentar'] = FormKomentar()
        return render(request, 'user/kelas/pelajaran/pelajaran.html', context)

    def post(self, request, id_pelajaran):
        pelajaran = Pelajaran.objects.get(id=id_pelajaran)
        form = FormKomentar(request.POST)

        if form.is_valid():
            komentar = form.cleaned_data  # Create a model instance from the form data
            komentar.kelas = pelajaran.kelas
            komentar.pelajaran = pelajaran
            komentar.user = request.user
            komentar.save()  # Save the model instance to the database

        return redirect("user:pelajaran", slug=pelajaran.slug, urutan_bab=pelajaran.bab_kelas.urutan, urutan_pelajaran=pelajaran.urutan)

def rangkuman(request, slug, urutan_bab):
    kelas = Kelas.objects.get(slug=slug)
    bab = Bab.objects.filter(kelas=kelas)
    nextbab = bab.filter(urutan=urutan_bab + 1)
    jum_pelajaran = Pelajaran.objects.filter(bab_kelas=bab.get(urutan=urutan_bab)).count()
    context.update(bab_navigate(request, slug, urutan_bab, jum_pelajaran, False))
    context['halaman'] = 'rangkuman'
    context['nextbab'] = nextbab.first() if nextbab.exists() else None
    return render(request, 'user/kelas/pelajaran/rangkuman.html', context)

def rangkuman_kelas(request, slug):
    kelas  = Kelas.objects.get(slug=slug)
    bab = UserBab.objects.filter(user=request.user, kelas=kelas)
    history = UserCourse.objects.get(kelas=kelas, user=request.user)
    context['history'] = history
    context['bab'] = bab
    context['babprev'] = bab[bab.count()-1]
    context['kelas']   = kelas
    context['halaman'] = 'rangkumankelas'
    return render(request, 'user/kelas/pelajaran/rangkuman.html', context)


def koridor_soal_kelas(request, slug):
    kelas  = Kelas.objects.get(slug=slug)
    bab = UserBab.objects.filter(user=request.user, kelas=kelas)
    history = UserCourse.objects.get(kelas=kelas, user=request.user)
    babmodel = Bab.objects.filter(kelas=kelas)
    context['babprev'] = babmodel[babmodel.count()-1]
    context['history'] = history
    context['bab'] = bab
    context['kelas']   = kelas
    context['halaman'] = 'soal_kelas'
    context['nilai'] = UserLatihan.objects.filter(user=request.user, is_last=True, kelas=kelas).order_by("-id")
    return render(request, 'user/kelas/pelajaran/koridor_soal.html', context)

def koridor_soal(request, slug, urutan_bab):
    kelas = Kelas.objects.get(slug=slug)
    bab = Bab.objects.filter(kelas=kelas)
    nextbab = bab.filter(urutan=urutan_bab+1)
    jum_pelajaran = Pelajaran.objects.filter(bab_kelas=bab.get(urutan=urutan_bab)).count()
    context.update(bab_navigate(request, slug, urutan_bab, jum_pelajaran, False))
    context['halaman'] = 'soal'
    context['nextbab'] = nextbab.first() if nextbab.exists() else None
    context['nilai'] = UserLatihan.objects.filter(user=request.user, bab_kelas=bab.get(urutan=urutan_bab)).order_by(
        "-id")
    return render(request, 'user/kelas/pelajaran/koridor_soal.html', context)


def soal(request, slug, urutan_bab):
    kelas = Kelas.objects.get(slug=slug)
    bab = Bab.objects.get(kelas=kelas, urutan=urutan_bab)
    latihan = UserLatihan.objects.filter(user=request.user, kelas=kelas, bab_kelas=bab, is_finish=False)
    latih = UserQuestion.objects.filter(latihan=latihan.first())
    if not latihan.exists():
        question = Questions.objects.filter(kelas=kelas, bab_kelas=bab).order_by("?")
        latih = UserLatihan.objects.create(user=request.user, kelas=kelas, bab_kelas=bab, is_finish=False)
        for i in range(10):
            UserQuestion.objects.create(user=request.user, kelas=kelas, bab_kelas=bab, questions=question[i],
                                        latihan=latih)
        return redirect("user:soal", slug=slug, urutan_bab=urutan_bab)

    if request.method == "POST":
        benar = 0
        nextbab = Bab.objects.filter(kelas=kelas, urutan=bab.urutan + 1)
        for l in latih:
            selected_value = request.POST.get(str(l.id))
            if l.questions.answer == selected_value:
                benar = benar + 10
                l.right = True
                l.save()
        if nextbab.exists():
            pelajaran = Pelajaran.objects.get(kelas=kelas, bab_kelas=nextbab.first(), urutan=1)
            UserCourse.objects.filter(kelas=kelas, user=request.user).update(bab_kelas=nextbab.first(), pelajaran=pelajaran)
        UserBab.objects.filter(bab_kelas=bab).update(isdone=True)
        latihan.update(is_finish=True, nilai=benar)
        return redirect("user:koridor_soal", slug=slug, urutan_bab=urutan_bab)
    context['latih'] = latih
    return render(request, 'user/kelas/soal.html', context)

def soal_kelas(request, slug):
    kelas = Kelas.objects.get(slug=slug)
    latihan = UserLatihan.objects.filter(user=request.user, kelas=kelas, is_finish=False, is_last=True)
    latih = UserQuestion.objects.filter(latihan=latihan.first())
    if not latihan.exists():
        question = Questions.objects.filter(kelas=kelas).order_by("?")
        latih = UserLatihan.objects.create(user=request.user, is_last=True,countdownNow='00:30:00', countdown='00:30:00', kelas=kelas, is_finish=False)
        for i in range(30):
            UserQuestion.objects.create(user=request.user, kelas=kelas, questions=question[i], latihan=latih)
        return redirect("user:soal_kelas", slug=slug)

    if request.method == "POST":
        benar = 0
        for l in latih:
            selected_value = request.POST.get(str(l.id))
            if l.questions.answer == selected_value:
                benar = benar + 10
                l.right = True
                l.save()
        benar = benar/3
        latihan.update(is_finish=True, nilai=benar)
        return redirect("user:koridor_soal_kelas", slug=slug)
    context['latih'] = latih
    return render(request, 'user/kelas/soal.html', context)

def pembahasan(request, id):
    context['latih'] = UserLatihan.objects.get(id=id)
    return render(request, 'user/kelas/pembahasan.html', context)


def waktu(request):
    if request.method == "GET":
        id = request.GET['id']
        minutes = request.GET['minutes']
        seconds = request.GET['seconds']
        latihan = UserLatihan.objects.get(id=id)
        latihan.countdownNow = "00:{}:{}".format(minutes, seconds)
        latihan.is_finish = True if minutes == 0 and seconds <= 2 else False
        latihan.save()
    return JsonResponse({'status': 'success'})


def select(request):
    if request.method == "GET":
        UserQuestion.objects.filter(id=request.GET['id']).update(selected=request.GET['selected'])
    return JsonResponse({'status': 'success'})


def cari(request):
    listkelas = []
    kelas = Kelas.objects.filter(defaultget=False)
    for i in kelas:
        enroll = UserCourse.objects.filter(kelas=i)
        pelajaran = Pelajaran.objects.filter(kelas=i)
        i.ratting = 0 if enroll.count() == 0 else enroll.aggregate(Avg('like'))['like__avg']
        i.see = enroll.count()
        i.enroll = enroll.filter(enroll=True).count()
        i.done = enroll.filter(finish=True).count()
        i.feed = enroll.filter(feed__isnull=False).count()
        i.pelajaran = pelajaran
        i.count = pelajaran.count()
        listkelas.append(i)
    context = {
        'kelas': listkelas
    }
    return auth(request, 'kelas/kelas', context)


def jsonkelas(request, id):
    kelas = Kelas.objects.get(id=id)
    jum = UserCourse.objects.filter(kelas=kelas)
    lesson = Pelajaran.objects.filter(kelas=kelas).values()
    return JsonResponse({
        'photo': str(kelas.photo),
        'ratting': 0 if jum.count() == 0 else jum.aggregate(Avg('like'))['like__avg'],
        'views': jum.count(),
        'enroll': jum.filter(enroll=True).count(),
        'done': jum.filter(finish=True).count(),
        'judul': kelas.kelas,
        'feed': jum.filter(feed__isnull=False).count(),
        'keterangan': kelas.keterangan,
        'kategori': kelas.kategori.name,
        'kelas': list(lesson)
    }, safe=False)


def games(request, slug, bab):
    context = {

    }
    return auth(request, 'kelas/pelajaran', context)
