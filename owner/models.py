from django.db import models
from django.contrib.auth.models import User as user_root

# Create your models here.
class LevelAkun(models.Model):
    name        = models.CharField(max_length=224,  unique=True)
    foto        = models.FileField(upload_to='photo/level', max_length=100, null=True, blank=True)
    keterangan  = models.CharField(max_length=224)
    nyawa       = models.IntegerField(default=0)
    biaya       = models.IntegerField(default=0)
    discount    = models.IntegerField(default=0)
    promo       = models.IntegerField(default=0)
    bestseller  = models.BooleanField(default=False)
    meeting     = models.IntegerField(default=0)
    people      = models.IntegerField(default=0)
    duration    = models.IntegerField(default=1)
    mengulang   = models.BooleanField(default=False)
    ketentuan   = models.CharField(max_length=225, blank=True, null=True)
    materi      = models.CharField(max_length=225, blank=True, null=True)
    bonus       = models.CharField(max_length=225, blank=True, null=True)
    langganan   = models.ForeignKey("owner.Langganan",blank=True, null=True,  on_delete=models.CASCADE, related_name="langganan")
    def __str__(self):
        return "{}".format(self.name)
    
    def ketentuans(self):
        return self.ketentuan.split(",")
    def materis(self):
        return self.materi.split(",")
    def bonuses(self):
        return self.bonus.split(",")

class Langganan(models.Model):
    durasi      = models.IntegerField(default=1)
    harga       = models.IntegerField(default=50000)
    diskon      = models.IntegerField(default=40000)
    def __str__(self):
        return "{} by {}".format(self.durasi, self.diskon)

class Level(models.Model):
    name        = models.CharField(max_length=224,  unique=True)
    keterangan  = models.CharField(max_length=224)
    def __str__(self):
        return "{} by {}".format(self.name, self.keterangan)

class Kategori(models.Model):
    name        = models.CharField(max_length=224,  unique=True)
    keterangan  = models.CharField(max_length=224)
    def __str__(self):
        return "{} by {}".format(self.name, self.keterangan,  unique=True)

class Master(models.Model):
    name        = models.CharField(max_length=224,  unique=True)
    keterangan  = models.CharField(max_length=224)
    def __str__(self):
        return "{} by {}".format(self.name, self.keterangan)

class QnA(models.Model):
    quest       = models.CharField(max_length=224)
    answer      = models.CharField(max_length=224)
    klik        = models.IntegerField(default=0)
    def __str__(self):
        return "{} by {}".format(self.quest, self.klik)

class Improve(models.Model):
    what        = models.CharField(max_length=224)
    why         = models.CharField(max_length=224)
    how         = models.TextField()
    def __str__(self):
        return "{}".format(self.what)

class Promo(models.Model):
    kode        = models.CharField(max_length=224)
    potongan    = models.IntegerField(default=0)
    by          = models.CharField(max_length=224)
    banner      = models.CharField(max_length=224)
    def __str__(self):
        return "{} by {}".format(self.by, self.kode)

class Event(models.Model):
    Hadiah = (
        (0,'credit'),
        (1,'barang'),
        (2,'kelas'),
        (3,'jabatan')
    )
    slug        = models.CharField(max_length=224, default="this-is-slug")
    photo       = models.FileField(upload_to='event', max_length=100, default="example.jpg")
    nama        = models.CharField(max_length=224)
    hadiah      = models.CharField(max_length=224)
    jenis       = models.IntegerField(choices=Hadiah, default=0)
    by          = models.OneToOneField(user_root,blank=True, null=True,  on_delete=models.CASCADE, related_name="user_event")
    sponsor     = models.CharField(max_length=224)
    peraturan   = models.TextField(blank=True)
    mulai       = models.DateField(blank=True, null=True)
    selesai     = models.DateField(blank=True, null=True)
    def __str__(self):
        return "{} hadiah {}".format(self.nama, self.hadiah)

    def save(self, *args, **kwargs):
        try:
            this = Event.objects.get(id=self.id)
            if this.photo != self.photo:
                this.photo.delete(save=False)
        except:
            pass  # when new photo then we do nothing, normal case
        super().save(*args, **kwargs)

class UserEvent(models.Model):
    S_name      = models.OneToOneField(user_root, on_delete=models.CASCADE, related_name="user_event_sender")
    eventname   = models.OneToOneField("owner.event", on_delete=models.CASCADE, related_name="event")
    file        = models.FileField(upload_to='file/event', max_length=100, null=True, blank=True)
    done        = models.BooleanField(default=False)
    def __str__(self):
        return "{} mengikuti {}".format(self.S_name, self.eventname)

class Setting(models.Model):
    title       = models.CharField(max_length=224)
    sub         = models.TextField()
    icon        = models.FileField(upload_to='landing', blank=True, )
    logo        = models.FileField(upload_to='landing', blank=True, )
    foto        = models.FileField(upload_to='landing', blank=True, )
    fotoadv     = models.FileField(upload_to='landing', blank=True, )
    alamat      = models.CharField(max_length=224, blank=True, )
    telp        = models.CharField(blank=True,max_length=13 )
    email       = models.EmailField(blank=True, )
    ig          = models.CharField(max_length=224, blank=True, )
    fb          = models.CharField(max_length=224, blank=True, )
    tiktok      = models.CharField(max_length=224, blank=True, )
    youtube     = models.CharField(max_length=224, blank=True, )
    komisi_teacher = models.IntegerField(default=70)
    komisi_developer = models.IntegerField(default=7)
    komisi_owner = models.IntegerField(default=23)
    def __str__(self):
        return "{}".format(self.title)
    def save(self, *args, **kwargs):
        try:
            this = Setting.objects.get(id=self.id)
            if this.icon != self.icon:
                this.icon.delete(save=False)
            if this.logo != self.logo:
                this.logo.delete(save=False)
            if this.foto != self.foto:
                this.foto.delete(save=False)
            if this.fotoadv != self.fotoadv:
                this.fotoadv.delete(save=False)
        except:
            pass  # when new photo then we do nothing, normal case
        super().save(*args, **kwargs)

class Advance(models.Model):
    icon        = models.CharField(max_length=224)
    nama        = models.CharField(max_length=224)
    ket         = models.CharField(max_length=224)
    def __str__(self):
        return "{}".format(self.nama)

class Transaksi(models.Model):
    jumlah      = models.IntegerField(default=0)
    bulan       = models.IntegerField(default=0)
    keluar      = models.BooleanField(default=False)
    def __str__(self):
        return "bulan {} = {}".format(self.bulan, self.jumlah)

class Ask(models.Model):
    nama = models.CharField(max_length=224)
    kontak = models.CharField(max_length=224)
    text = models.TextField(blank=True)
    closed = models.BooleanField(default=False)
    def __str__(self):
        return "{}".format(self.nama)


class Artikel(models.Model):
    arrjenis    = ( (0,'news'),(1,'tips'))
    slug        = models.CharField(max_length=224)
    title       = models.CharField(max_length=224)
    header      = models.CharField(max_length=224, default="this is header text of content")
    foto        = models.FileField(upload_to='article', blank=True)
    jenis       = models.IntegerField(choices=arrjenis, default=0)
    text        = models.TextField(blank=True)
    tanggal     = models.DateTimeField(auto_now_add=True)
    dibaca      = models.IntegerField(default=0)
    user        = models.ForeignKey(user_root,blank=True, null=True,  on_delete=models.CASCADE, related_name="user_artikel")
    def __str__(self):
        return "{}".format(self.slug)

class Report(models.Model):
    arrReport   = ( (0,'report'),(1,'update'))
    user        = models.ForeignKey(user_root,blank=True, null=True,  on_delete=models.CASCADE, related_name="user_report")
    jenis       = models.IntegerField(default=0, choices=arrReport)
    text        = models.TextField(blank=True)
    tanggal     = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return "{}.{}".format(self.jenis, self.user)
    
class Earn(models.Model):
    user_teacher = models.ForeignKey(user_root,blank=True, null=True, on_delete=models.CASCADE, related_name="pendapatan_user")
    teacher     = models.IntegerField(default=0)
    owner       = models.IntegerField(default=0)
    developer   = models.IntegerField(default=0)
    room        = models.ForeignKey(LevelAkun,blank=True, null=True, on_delete=models.CASCADE, related_name="pendapatan_user")
    tgl         = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return "{}.{}".format(self.user_teacher, self.tgl)
