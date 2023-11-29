from app.app import auth, kelas
from app.ipaymu import pay, transaksi
from app.mydate import fetchday
from .models import  Users, UserMeeting, UserSchadule, UserMentor
from teacher.models import Room, Teacher, Schadule
from owner.models import LevelAkun, Setting, Earn
from datetime import datetime
from django.shortcuts import redirect, HttpResponse, render
from django.db.models import Sum, F
from django.contrib import messages


import datetime
x = datetime.datetime.now()


context = {
    'url':'bootcamp',
    'title':'bootcamp',
    'icon':'static/assets/icon.png'
}
# Create your views here.
def index(request):
    meeting                 = UserMeeting.objects.filter(user=request.user, purchased=True)
    room                    = UserSchadule.objects.filter(user=request.user)
    if not meeting.exists():
        return redirect("user:purchase_bootcamp")
    if not meeting.exclude(room__isnull=True).exists():
        return redirect("user:jadwal")
    
    if request.method == 'POST':
        sch =  Schadule.objects.filter(level=meeting.first().accountlevel, time=request.POST["time"], tanggal=request.POST["date"]).order_by("?")
        if sch.exists():
            sch_first = sch.first()
            room.filter(id=request.POST['id']).update(schadule=sch_first, room=sch_first.room, tanggal=sch_first.tanggal)
            messages.success(request, 'Anda akan belajar dengan {} pada tangal {} jam {}'.format(sch_first.mentor.first_name+" "+sch_first.mentor.last_name, sch_first.tanggal, sch_first.get_time_display()))
            return redirect("user:bootcamp")
        else:
            messages.error(request, 'Kelas tidak ditemukan, coba ganti tanggal lain atau jam lain')
            return redirect("user:bootcamp")
    context["user"]         = Users.objects.get(user=request.user)
    context['yet']          = room.filter(hadir=False).order_by("tanggal")[:5]
    context['done']         = room.filter(tanggal__lt=x)[:5]
    context['meeting']      = meeting.first()
    return render(request, "user/bootcamp/index.html", context)

def coming(request):
    context["user"]         = Users.objects.get(user=request.user)
    context['jadwal']       = UserSchadule.objects.filter(user=request.user).order_by("tanggal")
    return render(request, "user/bootcamp/coming.html", context)

def jadwal(request):
    meeting                 = UserMeeting.objects.filter(user=request.user, purchased=True).first()
    if request.method == 'POST':
        room    = Room.objects.get(id=request.POST["id"])
        meeting.room    = room
        meeting.mentor  = room.mentor
        meeting.save()
        UserMentor.objects.create(mentor=room.mentor, user=request.user, isMentored=True, start=room.mulai, end=(room.mulai + datetime.timedelta(days=90)))
        for i in Schadule.objects.filter(room=room):
            UserSchadule.objects.create(room=room, schadule=i, user=request.user, tanggal = i.tanggal)
        return redirect("user:bootcamp")

    context["user"]         = Users.objects.get(user=request.user)
    context['mentor']       = Room.objects.filter(level=meeting.accountlevel)
    context['meeting']      = meeting
    return render(request, "user/bootcamp/jadwal.html", context)
    
def purchase_bootcamp(request):
    context["user"]     = Users.objects.get(user=request.user)
    context['paket'] = LevelAkun.objects.all().order_by("biaya")
    return render(request, "user/bootcamp/purchase.html", context)

def confirm(request,id):
    account = LevelAkun.objects.get(id=id)
    nextmonth = x.replace(month=x.month+account.duration)
    if nextmonth.month == 1:
        nextmonth = nextmonth.replace(year=nextmonth.year+1)

    meeting = UserMeeting.objects.create(user=request.user, accountlevel=account, end=nextmonth, meetremain=account.meeting)
    product = account.name
    price = account.biaya
    ref_id = meeting.id
    url, SessionID = pay(request, product, price, ref_id)
    meeting.SessionID = SessionID
    meeting.save()
    return redirect(url)


def thank(request):
    id = request.GET.get('trx_id')
    trans = transaksi(id)
    if request.GET.get('status') == "berhasil":
        meeting = UserMeeting.objects.get(SessionID=trans["Data"]["SessionId"])
        meeting.purchased = True
        meeting.trx_id = id
        meeting.via = trans["Data"]["Sender"]
        meeting.status = trans["Message"]
        meeting.save()
        return auth(request, 'bootcamp/thank', context={})
    else:
        UserMeeting.objects.filter(SessionID=trans["Data"]["SessionId"]).delete()
        return redirect('user:purchase_bootcamp')


def notify(request, ref_id):
    print("terpanggil")
    ref = UserMeeting.objects.get(id=ref_id)
    ref.purchased = True
    ref.save()
    return HttpResponse("Success")
