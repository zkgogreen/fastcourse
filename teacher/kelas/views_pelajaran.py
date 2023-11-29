from teacher.models import Bab,  Pelajaran, Questions
from user.models import Users
from ..forms import AddPelajaran, AddSoal
from django.shortcuts import redirect, render

context = {
    'url':'kelas',
    'title':'kelas',
    'icon':'static/assets/icon.png'
}

def pelajaran_tambah(request, id_bab, urutan):
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
        
    context['user']         = Users.objects.get(user=request.user)
    context['bab_kelas']= bab
    context['form']     = AddPelajaran()
    return render(request, 'teacher/kelas/pelajaran/tambah.html', context)

def pelajaran_edit(request, id_bab, urutan):
    bab             = Bab.objects.get(id=id_bab)
    pelajaran       = Pelajaran.objects.get(bab_kelas=bab, urutan=urutan)
    if request.method == "POST":
        pelajaran_form = AddPelajaran(request.POST, instance=pelajaran)
        if pelajaran_form.is_valid():
            pelajaran_form.save()
            return redirect("teacher:bab_edit", id=bab.id)
    
    context['bab']          = bab
    context['pelajaran']    = pelajaran
    context['user']         = Users.objects.get(user=request.user)
    context['form']         = AddPelajaran(instance=pelajaran)
    return render(request, 'teacher/kelas/pelajaran/update.html', context)


def pelajaran_hapus(request, id):
    pelajaran   = Pelajaran.objects.get(id=id)
    pelajaranall = Pelajaran.objects.filter(kelas=pelajaran.kelas, urutan__gte=pelajaran.urutan)
    for p in pelajaranall:
        p.urutan = p.urutan-1
        p.save()
    id_bab      = pelajaran.bab_kelas.id
    pelajaran.delete()
    return redirect("teacher:bab_edit", id=id_bab)

def soal(request, id_bab):
    bab                     = Bab.objects.get(id=id_bab)
    context['soal']         = Questions.objects.filter(bab_kelas=bab)
    context['user']         = Users.objects.get(user=request.user)
    return render(request, 'teacher/kelas/pelajaran/soal_all.html', context)
def soal_detail(request, id_pelajaran):
    pelajaran               = Pelajaran.objects.get(id=id_pelajaran)

    if request.method == 'POST':
        soalform            = AddSoal(request.POST)
        if soalform.is_valid():
            form = soalform.save(commit=False)
            form.category   = pelajaran.kelas.kategori
            form.kelas      = pelajaran.kelas
            form.lesson     = pelajaran
            form.bab_kelas  = pelajaran.bab_kelas
            form.save()
            return redirect("teacher:soal", id_pelajaran=id_pelajaran)
    context['pelajaran']    = pelajaran
    context['soal']         = Questions.objects.filter(lesson=pelajaran)
    context['user']         = Users.objects.get(user=request.user)
    context['form']         = AddSoal()
    return render(request, 'teacher/kelas/pelajaran/soal.html', context)

def soal_edit(request, id_soal):
    soal                    = Questions.objects.get(id=id_soal)
    context['soal']         = soal
    context['form']         = AddSoal(instance=soal)
    return render(request, 'teacher/kelas/pelajaran/soal_edit.html', context)