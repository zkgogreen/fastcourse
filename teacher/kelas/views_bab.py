from teacher.models import Bab,  Kelas
from user.models import Users, UserQuestion
from ..forms import BabForm
from django.shortcuts import redirect, render

context = {
    'url':'kelas',
    'title':'kelas',
    'icon':'static/assets/icon.png'
}

def index(request, id):
    if request.method == "POST":
        bab_form = BabForm(request.POST)
        id_bab = request.POST.get('bab_id')
        if bab_form.is_valid():
            bab_form = bab_form.save(commit=False)
            if id_bab:
                bab_form.id= id_bab
            else:
                bab_form.urutan = Bab.objects.filter(kelas=Kelas(id)).count() + 1
            bab_form.kelas = Kelas.objects.get(id=id)
            bab_form.save()
            return redirect("teacher:bab", id=id)

    context['user']         = Users.objects.get(user=request.user)
    context['bab']          = Bab.objects.filter(kelas=Kelas(id)).order_by("urutan")
    context['kelas']        = Kelas.objects.get(id=id)
    context['form_bab']     = BabForm()
    return render(request, 'teacher/kelas/bab/index.html', context)

def bab_edit(request, id):
    bab                     = Bab.objects.get(id=id)
    question                = UserQuestion.objects.filter(bab_kelas=bab)
    context['benar']        = question.filter(right=True).count()
    context['salah']        = question.filter(right=False).count()
    context['user']         = Users.objects.get(user=request.user)
    context['bab']          = bab
    return render(request, 'teacher/kelas/bab/bab_edit.html', context)

def bab_hapus(request, id):
    bab_kelas   = Bab.objects.get(id=id)
    id_kelas    = bab_kelas.kelas.id
    bab_kelas.delete()
    return redirect("teacher:bab", id=id_kelas)