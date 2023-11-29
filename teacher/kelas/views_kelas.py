from teacher.models import Bab,  Kelas, Pelajaran
from user.models import Users
from ..forms import BabForm, AddPelajaran
from django.db.models import F
from django.shortcuts import redirect, render
# Create your views here.

context = {
    'url':'kelas',
    'title':'kelas',
    'icon':'static/assets/icon.png'
}
def kelas(request):
    context['user']         = Users.objects.get(user=request.user)
    context["kelas"]        = Kelas.objects.all()
    return render(request, 'teacher/kelas/index.html', context)


def detail(request, id):
    kelas                   = Kelas.objects.get(id=id)
    context['bab_kelas']    = Bab.objects.filter(kelas=kelas)
    context['user']         = Users.objects.get(user=request.user)
    context['kelas']        = kelas
    return render(request, 'teacher/kelas/detail.html', context)

def soal_tambah(request, id_bab, urutan):
    bab             = Bab.objects.get(id=id_bab)

    if request.method == "POST":
        pelajaran_form = AddPelajaran(request.POST)
        pelajaran = Pelajaran.objects.filter(kelas=bab.kelas, urutan__gte=urutan)
        for p in pelajaran:
            p.urutan = p.urutan+1
            p.save()

        if pelajaran_form.is_valid():
            forms           = pelajaran_form.save(commit=False)
            forms.kelas     = bab.kelas
            forms.bab_kelas  = bab
            forms.urutan     = urutan
            forms.save()
            return redirect("teacher:bab_edit", id=bab.id)
        
    context['bab_kelas']= bab
    context['form']     = AddPelajaran()
    return render(request, 'teacher/kelas/tambah.html', context)

def soal_edit(request, id_bab, urutan):
    bab             = Bab.objects.get(id=id_bab)
    pelajaran       = Pelajaran.objects.get(bab_kelas=bab, urutan=urutan)
    if request.method == "POST":
        pelajaran_form = AddPelajaran(request.POST, instance=pelajaran)
        if pelajaran_form.is_valid():
            pelajaran_form.save()
            return redirect("teacher:bab_edit", id=bab.id)
    
    context['form']     = AddPelajaran(instance=pelajaran)
    return render(request, 'teacher/kelas/tambah.html', context)

