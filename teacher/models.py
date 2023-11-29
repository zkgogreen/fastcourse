from django.db import models
from django.contrib.auth.models import User as user_root
from ckeditor.fields import RichTextField
from user.models import UserLesson, UserCourse, Users, UserMeeting, UserSchadule, UserQuestion
from django.db.models import Avg
from datetime import datetime, timedelta

import random
Language = [
        ('EN', 'English'),
        ('JP', 'Japan'),
        ('SA', 'Arab'),
        ('CN', 'China'),
    ]
jam = [
    (0,'07:30'),
    (1,'09:00'),
    (2,'10:30'),
    (3,'13:00'),
    (4,'14:30'),
    (5,'16:00'),
    (6,'18:30'),
    (7,'20:00'),
]
hari = [
    (0, 'minggu'),
    (1, 'senin'),
    (2, 'selasa'),
    (3, 'rabu'),
    (4, 'kamis'),
    (5, 'jumat'),
    (6, 'sabtu')
]

jadwal = [
    (0, 'senin,  rabu, jum\'at'),
    (1, 'selasa,  kamis, sabtu'),
    (2, 'jum\'at,  sabtu, minggu')
]

#info guru
class Teacher(models.Model):
    user        = models.ForeignKey(user_root,blank=True, null=True,on_delete=models.CASCADE, related_name="user_of_teacher")
    link        = models.CharField(max_length=50, null=True, default="https://zoom.us/")
    password    = models.CharField(max_length=50, null=True, blank=True)
    credits     = models.IntegerField(default=0)
    api_key     = models.CharField(max_length=50, null=True)
    secret_key  = models.CharField(max_length=50, null=True)
    mastered    = models.ForeignKey('owner.Master',blank=True, null=True,on_delete=models.CASCADE, related_name="Master_of_teacher")
    desc        = models.CharField(max_length=225, null=True)
    def __str__(self):
        return " {}".format(self.user)

# info kelas yang di buat owner
class Kelas(models.Model):
    kelas       = models.CharField(max_length=224)
    bahasa      = models.CharField(max_length=3,choices=Language, blank=True)
    slug        = models.SlugField(max_length=30, null=True)
    photo       = models.FileField(upload_to='kelas', max_length=100, default="kelas/default.jpg")
    kategori    = models.ForeignKey('owner.Kategori',blank=True, null=True,on_delete=models.CASCADE, related_name="kategori_kelas")
    level       = models.ForeignKey('owner.Level',blank=True, null=True,on_delete=models.CASCADE, related_name="level_kelas")
    keterangan  = models.CharField(blank=True,max_length=224)
    rangkuman   = RichTextField(blank=True, null=True)
    defaultget  = models.BooleanField(default=False)
    biaya       = models.IntegerField(default=0)
    discount    = models.IntegerField(default=0)
    premium     = models.BooleanField(default=False)
    mahkota     = models.IntegerField(default=0)
    dilihat     = models.IntegerField(default=0)
    certificate = models.BooleanField(default=False)
    rilis       = models.BooleanField(default=False)
    urutan      = models.IntegerField(blank=True, null=True)

    course      = UserCourse.objects.all()
    def __str__(self):
        return " {}".format(self.kelas)
    
    def ratting(self):
        return self.course.filter(kelas=self).aggregate(Avg('like'))['like__avg']
    def see(self):
        return self.course.filter(kelas=self).count()
    def subscribe(self):
        return self.course.filter(kelas=self, enroll=True).count()
    def feedback(self):
        return self.course.filter(kelas=self, feedback__isnull=False).count()
    def finish(self):
        return self.course.filter(kelas=self, finish=True).count()
    def bab(self):
        return Bab.objects.filter(kelas=self).count()
    def babmodel(self):
        return Bab.objects.filter(kelas=self)
    def pelajaran(self):
        return Pelajaran.objects.filter(kelas=self).count()
    def enroll(self, user):
        subscribe = self.course.filter(kelas=self, user=user)
        return True if subscribe.exists() else False
    def done(self, user):
        return UserLesson.objects.filter(kelas=self, user=user).count()
    def history(self, user):
        history = UserCourse.objects.filter(user=user, kelas=self)
        return history.first().pelajaran.urutan if history.exists() else 1
    def current(self, urutan):
        return Pelajaran.objects.get(kelas=self, urutan=urutan)
    
    def save(self, *args, **kwargs):
        try:
            this = Kelas.objects.get(id=self.id)
            if this.photo != self.photo:
                this.photo.delete(save=False)
        except:
            pass  # when new photo then we do nothing, normal case
        super().save(*args, **kwargs)

# perubahan kelas yang ajukan oleh guru
class Creator(models.Model):
    user        = models.ForeignKey(user_root,blank=True, null=True,on_delete=models.CASCADE, related_name="user_creator")
    Kelas       = models.ForeignKey(Kelas,blank=True, null=True,on_delete=models.CASCADE, related_name="kelas_creator")
    perubahan   = models.CharField(max_length=225)
    approve     = models.BooleanField(default=False)
    date        = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "{}-{}".format(self.user, self.Kelas)

# bab pada lesson
class Bab(models.Model):
    kelas       = models.ForeignKey(Kelas,blank=True, null=True,on_delete=models.CASCADE, related_name="kelas_bab")
    bab         = models.CharField(max_length=50)
    urutan      = models.IntegerField(blank=True, null=True)
    rangkuman   = RichTextField(blank=True, null=True)
    premium     = models.BooleanField(default=False)
    def __str__(self):
        return "{}-{}".format(self.kelas, self.bab)
    
    def pelajaran(self, user):
        return [i.finish(user=user) for i in Pelajaran.objects.filter(bab_kelas=self)]
    def pelajaranModel(self):
        return Pelajaran.objects.filter(bab_kelas=self).order_by("urutan")
    def soalModel(self):
        return Questions.objects.filter(bab_kelas=self)
    def benar(self):
        return UserQuestion.objects.filter(bab_kelas=self, right=True).count()
    def salah(self):
        return UserQuestion.objects.filter(bab_kelas=self, right=False).count()
            

#materi pelajaran
class Pelajaran(models.Model):
    kelas       = models.ForeignKey(Kelas,blank=True, null=True,on_delete=models.CASCADE, related_name="kelas_pelajaran")
    urutan      = models.IntegerField(blank=True, null=True)
    bab_kelas   = models.ForeignKey(Bab,blank=True, null=True,on_delete=models.CASCADE, related_name="bab_kelas")
    judul       = models.CharField(max_length=224)
    keterangan  = models.CharField(max_length=224, default="belum ada keterangan")
    vidio       = models.URLField(max_length=200, null=True, blank=True)
    text        = RichTextField()
    date        = models.DateField(auto_now_add=True, blank=True)
    approve     = models.BooleanField(default=False)
    def __str__(self):
        return "{}-{}".format(self.id, self.judul)
    
    def prev(self, isPelajaran):
        pelajaran = Pelajaran.objects.filter(kelas=self.kelas, bab_kelas=self.bab_kelas)
        pelajaran = pelajaran.filter(urutan=self.urutan-1) if isPelajaran else pelajaran.filter(urutan=pelajaran.count())
        pelajaran = pelajaran.first() if pelajaran.exists() else None
        return pelajaran
    def next(self, isPelajaran):
        pelajaran = Pelajaran.objects.filter(kelas=self.kelas, urutan=self.urutan+1, bab_kelas=self.bab_kelas)
        return pelajaran.first() if pelajaran.exists() else None
    
    def soal(self):
        # pelajaran = Pelajaran.objects.filter(kelas=self.kelas, urutan=self.urutan+1)
        return Questions.objects.filter(bab_kelas=self.bab_kelas)
    
    def question(self):
        question = Questions.objects.filter(lesson=self).order_by("?")
        return question.first() if question.exists() else None
        
    
    def komentar(self):
        return UserLesson.objects.filter(pelajaran=self).exclude(question__isnull=True)
    
    def finish(self, user):
        return UserLesson.objects.filter(user=user).first().isdone

# soal yang dibuat pada lesson
class Questions(models.Model):
    category    = models.ForeignKey('owner.Kategori',blank=True, null=True,on_delete=models.CASCADE, related_name="quest_kategori")
    level       = models.ForeignKey('owner.Level',blank=True, null=True,on_delete=models.CASCADE, related_name="quest_level")
    kelas       = models.ForeignKey(Kelas,blank=True, null=True,on_delete=models.CASCADE, related_name="quest_kelas")
    bab_kelas   = models.ForeignKey(Bab,blank=True, null=True,on_delete=models.CASCADE, related_name="bab_question")
    lesson      = models.ForeignKey(Pelajaran,blank=True, null=True,on_delete=models.CASCADE, related_name="quest_pelajaran")
    soal        = models.CharField(max_length=224)
    answer      = models.CharField(max_length=224)
    wrong1      = models.CharField(max_length=224)
    wrong2      = models.CharField(max_length=224)
    wrong3      = models.CharField(max_length=224)
    penjelasan  = models.TextField(default="Belum ada penjelasan")
    user        = models.ForeignKey(user_root,blank=True, null=True,on_delete=models.CASCADE, related_name="user_question")
    approve     = models.BooleanField(default=False)

    question    = UserQuestion.objects.all()
    def __str__(self):
        return "{}.{}".format(self.soal, self.lesson)
    
    def questionList(self):
        choices = [self.answer, self.wrong1, self.wrong2, self.wrong3]
        random.shuffle(choices)
        return choices
    def userquestion(self):
        return self.question.filter(questions=self)[:20]
    def userquestionRight(self):
        return self.question.filter(questions=self, right=True).count()
    def userquestionWrong(self):
        return self.question.filter(questions=self, right=False).count()

# games yang dibuat pada lesson
class Games(models.Model):
    level       = models.IntegerField()
    soal        = models.CharField(max_length=224)
    answer      = models.CharField(max_length=224)
    dummy       = models.CharField(max_length=224)
    penjelasan  = models.TextField(default="Belum ada penjelasan")
    pelajaran   = models.ForeignKey(Pelajaran,blank=True, null=True,on_delete=models.CASCADE, related_name="games_pelajaran")
    kelas       = models.ForeignKey(Kelas,blank=True, null=True,on_delete=models.CASCADE, related_name="Games_kelas")
    bab_kelas   = models.ForeignKey(Bab,blank=True, null=True,on_delete=models.CASCADE, related_name="bab_games")
    user        = models.ForeignKey(user_root,blank=True, null=True,on_delete=models.CASCADE, related_name="user_games")
    approve     = models.BooleanField(default=False)
    def __str__(self):
        return "level {} - {}".format(self.level, self.soal)
    

#grup vocabulary seperti nama buah, pekerjaan, part of speech
class VocabGroup(models.Model):
    english     = models.CharField(max_length=50)
    indo        = models.CharField(max_length=50)
    level       = models.ForeignKey("owner.Level",blank=True, null=True, on_delete=models.CASCADE, related_name="vocab_group_level")
    img         = models.FileField(upload_to='media/vocabgroup', max_length=100, default="media/vocabgroup/default.jpg")
    def __str__(self):
        return "{}.{}-{}".format(self.id, self.english, self.indo)

#penjabaran dari vocab grup seperti buah = anggur, jeruk dll
class Vocab(models.Model):
    group       = models.ForeignKey("teacher.VocabGroup",blank=True, null=True, on_delete=models.CASCADE, related_name="vocab_group")
    english     = models.CharField(max_length=50)
    indo        = models.CharField(max_length=50)
    success     = models.IntegerField(default=0)
    failed      = models.IntegerField(default=0)
    def __str__(self):
        return "{}.{}-{}".format(self.id, self.english, self.indo)


#link pada zoom
class Room(models.Model):
    mentor      = models.ForeignKey(user_root,blank=True, null=True,on_delete=models.CASCADE,related_name="teacher_room")
    bahasa      = models.CharField(choices=Language, blank=True, max_length=3, default=1)
    level       = models.ForeignKey('owner.LevelAkun',blank=True, null=True,on_delete=models.CASCADE, related_name="level_akun_room")
    time        = models.IntegerField(choices=jam, blank=True, default=1)
    mulai       = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    jadwal      = models.IntegerField(choices=jadwal, blank=True, default=1)

    def __str__(self):
        return "{} - {}".format(self.mentor, self.time)
    def usermentor(self):
        return Users.objects.get(user=self.mentor)
    def teacher(self):
        return Teacher.objects.get(user=self.mentor)
    def jumlah(self):
        return UserSchadule.objects.filter(room=self).count()
    def kuota(self):
        return UserMeeting.objects.filter(room=self).count()
    def schadule(self):
        return Schadule.objects.filter(room=self).order_by("tanggal")
    def now(self):
        return True if Schadule.objects.filter(room=self, tanggal=datetime.now().date()).exists() else Schadule.objects.filter(room=self, tanggal__gt=datetime.now().date()).first()
    def end(self):
        return self.mulai + timedelta(days=90)
    
class Schadule(models.Model):
    room        = models.ForeignKey("teacher.Room",blank=True, null=True,on_delete=models.CASCADE, related_name="teacher_schadule_room")
    mentor      = models.ForeignKey(user_root,blank=True, null=True,on_delete=models.CASCADE,related_name="mentor_schadule")
    terlaksana  = models.BooleanField(default=False)
    time        = models.IntegerField(choices=jam, blank=True, default=1)
    level       = models.ForeignKey('owner.LevelAkun',blank=True, null=True,on_delete=models.CASCADE, related_name="level_akun_schadule")
    tanggal     = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    def __str__(self):
        return "{} {}".format(self.room, self.tanggal)
    
    def now(self):
        return  True if self.tanggal == datetime.now().date() else False
    
    def peserta(self):
        return UserSchadule.objects.filter(schadule=self).count()
    
    def link(self):
        # user = Users.objects.get(user=self.mentor).user
        return Teacher.objects.get(user=self.mentor).link

# narik duit
class Withdrow(models.Model):
    user        = models.ForeignKey(user_root,blank=True, null=True, on_delete=models.CASCADE, related_name="user_withdrow")
    jumlah      = models.IntegerField(default=0)
    bank        = models.CharField(max_length=30)
    no_bank     = models.CharField(max_length=18)
    penerima    = models.CharField(max_length=50)
    tgl         = models.DateField(auto_now_add=True)
    approve     = models.BooleanField(default=False)
    
    def __str__(self):
        return "{}.{}".format(self.T_name, self.jumlah)