from app.app import auth
from django.db.models import Avg
from teacher.models import Kelas, Pelajaran, Bab
from user.models import UserCourse
from .forms import PelajaranForm, KelasForm, BabForm
from django.shortcuts import redirect
from django.utils.text import slugify
from django.db.models import F

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = KelasForm(request.POST, request.FILES)
        if form.is_valid():
            newform = form.save(commit=False)
            newform.slug = slugify(request.POST["kelas"])
            newform.save()
    context = {
        'kelas':Kelas.objects.all().order_by("urutan"),
        'addkelas':KelasForm
    }
    return auth(request, 'kelas/index', context)

def hapus_kelas(request, slug):
    Kelas.objects.filter(slug=slug).delete()
    return redirect("owner:kelas")

def rilis_kelas(request, slug):
    print("test")
    kelas = Kelas.objects.get(slug=slug)
    kelas.rilis = not kelas.rilis
    print(kelas.rilis)
    kelas.save()
    return redirect("owner:kelas")

def edit_kelas(request, slug):
    kls         = Kelas.objects.get(slug=slug)
    bab         = Bab.objects.filter(kelas=kls)
    lessons     = []

    if request.method == 'POST':
        form = BabForm(request.POST)
        if form.is_valid():
            newform = form.save(commit=False)
            newform.kelas = kls
            newform.save()

    for i in bab:
        pelajarans = []
        for j in Pelajaran.objects.filter(bab_kelas=i):
            pelajarans.append(j)
        i.pelajaran = pelajarans
        lessons.append(i)
    context = {
        'list':lessons,
        'slug':slug,
        'form_tambah_bab':BabForm()
    }
    return auth(request, 'kelas/kelas', context)

def next_kelas(request, slug, input):
    kelas = Kelas.objects.all()
    mainkelas = kelas.filter(slug=slug)
    if input == "next":
        mainkelas.update(urutan=F('urutan') + 1)
    elif input == "prev":
        mainkelas.update(urutan=F('urutan') - 1)
    else:
        print("Perintah tidak ditemukan")
    return redirect("owner:kelas")

def tambah_pelajaran(request, slug, id):
    if request.method == "POST":
        form = PelajaranForm(request.POST)
        if form.is_valid():
            newform = form.save(commit=False)
            newform.kelas = Kelas.objects.get(slug=slug)
            newform.bab_kelas = Bab.objects.get(id=id)
            newform.save()
            return redirect("owner:kelasdetail",slug)
        else:
            # Form is invalid, provide feedback
            for field, errors in form.errors.items():
                for error in errors:
                    form.add_error(field, error)
    context = {
        'myform':PelajaranForm()
    }
    return auth(request, 'kelas/edit_pelajaran', context)

def edit_pelajaran(request, id):
    instance = Pelajaran.objects.get(id=id)
    context = {
        'myform':PelajaranForm(instance=instance)
    }
    return auth(request, 'kelas/edit_pelajaran', context)

def hapus_pelajaran(request, slug, id):
    Pelajaran.objects.filter(id=id).delete()
    return redirect("owner:kelasdetail", slug)