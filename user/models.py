from django.db import models
from django.contrib.auth.models import User as user_root
import datetime
# Create your models here.

# info user, juga primary key untuk guru
class Users(models.Model):
    getstatus = (
        (1, 'user'),
        (2, 'teacher'),
        (3, 'owner'),
    )
    user        = models.ForeignKey(user_root, blank=True, null=True ,on_delete=models.CASCADE, related_name="level_akun")
    birth       = models.DateField(null=True, blank=True)
    address     = models.CharField(max_length=224, blank=True)
    photo       = models.FileField(upload_to='photo/profile', default='photo/profile/user.jpg')
    join        = models.DateField(auto_now_add=True)                           # kapan join 
    premium_start= models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)          # akun premium
    premium_end= models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)          # akun premium
    xp          = models.IntegerField(default=0)
    nyawa       = models.IntegerField(default=0)
    game        = models.IntegerField(default=0)
    mahkota     = models.IntegerField(default=0)
    level       = models.ForeignKey('owner.Level',to_field='name', default='Beginner',on_delete=models.CASCADE, related_name="level")
    kelas       = models.IntegerField(default=1)
    testi       = models.TextField(blank=True)
    phone       = models.CharField(max_length=224, blank=True)
    status      = models.IntegerField(choices=getstatus, default=1)
    teacher     = models.BooleanField(default=False)
    promo       = models.BooleanField(default=False)
    def __str__(self):
        return "{} {}".format(self.id, self.user.username)
        
    def save(self, *args, **kwargs):
        try:
            this = Users.objects.get(id=self.id)
            if this.photo != self.photo:
                this.photo.delete(save=False)
        except:
            pass  # when new photo then we do nothing, normal case
        super().save(*args, **kwargs)

    def premium(self):
        if self.premium_end:
            return True if self.premium_end > datetime.date.today() else False
        else:
            return False

# kelas yang di ambil
class UserCourse(models.Model):
    user        = models.ForeignKey(user_root, blank=True, null=True,on_delete=models.CASCADE, related_name="user_course_user")
    kelas       = models.ForeignKey('teacher.Kelas',blank=True, null=True,on_delete=models.CASCADE, related_name="user_kelas")
    pelajaran   = models.ForeignKey('teacher.Pelajaran',blank=True, null=True,on_delete=models.CASCADE, related_name="user_history_pelajaran") #mendapat histori pelajaran
    bab_kelas   = models.ForeignKey('teacher.Bab',blank=True, null=True,on_delete=models.CASCADE, related_name="user_history")                  # mendapat histori bab
    tanggal     = models.DateField(auto_now_add=True)
    finish      = models.BooleanField(default=False)
    like        = models.IntegerField(default=0)
    feed        = models.CharField(blank=True, null=True, max_length=225)
    feedback    = models.CharField(blank=True, null=True, max_length=225)
    enroll      = models.BooleanField(default=False)
    def __str__(self):
        return "{} take {}".format(self.user, self.kelas)
    def lesson(self):
        return UserLesson.objects.filter(userCourse=self)
    def percent(self):
        lesson = UserLesson.objects.filter(userCourse=self)
        bab = UserBab.objects.filter(userCourse=self)
        return round(((lesson.filter(isdone=True).count()+bab.filter(isdone=True).count())/(lesson.count()+bab.count()))*100)

# lesson yang sudah dikerjakan
class UserLesson(models.Model):
    user        = models.ForeignKey(user_root, blank=True, null=True,on_delete=models.CASCADE, related_name="user_lesson_user")
    kelas       = models.ForeignKey('teacher.Kelas',blank=True, null=True,on_delete=models.CASCADE, related_name="user_kelas_lesson")
    bab_kelas   = models.ForeignKey('teacher.Bab',blank=True, null=True,on_delete=models.CASCADE, related_name="user_bab_kelas_lesson")
    pelajaran   = models.ForeignKey('teacher.Pelajaran',blank=True, null=True,on_delete=models.CASCADE, related_name="user_pelajaran")
    userCourse  = models.ForeignKey('user.UserCourse',blank=True, null=True,on_delete=models.CASCADE, related_name="usercourse_lesson")
    isdone      = models.BooleanField(default=False)
    question    = models.CharField(max_length=225, blank=True, null=True)
    answer      = models.CharField(max_length=225, blank=True, null=True)
    tgl         = models.DateField(auto_now_add=False, blank=True, null=True)
    def __str__(self):
        return "{} take {} by {}".format(self.id, self.user, self.pelajaran)

    def user_info(self):
        return Users.objects.get(user=self.user)
class UserBab(models.Model):
    user        = models.ForeignKey(user_root, blank=True, null=True,on_delete=models.CASCADE, related_name="user_bab_user")
    kelas       = models.ForeignKey('teacher.Kelas',blank=True, null=True,on_delete=models.CASCADE, related_name="user_kelas_bab")
    bab_kelas   = models.ForeignKey('teacher.Bab',blank=True, null=True,on_delete=models.CASCADE, related_name="userbab_bab")
    userCourse  = models.ForeignKey('user.UserCourse',blank=True, null=True,on_delete=models.CASCADE, related_name="usercourse_bab")
    isdone      = models.BooleanField(default=False)
    tgl         = models.DateField(auto_now_add=False, blank=True, null=True)
    def __str__(self):
        return "{} take {} by {}".format(self.id, self.user, self.bab_kelas)

    def prev(self):
        return UserLesson.objects.filter(user=self.user, bab_kelas=self.bab_kelas, isdone=True).order_by("urutan")
    def next(self):
        return UserLesson.objects.filter(user=self.user, bab_kelas=self.bab_kelas, isdone=False).order_by("urutan")

    def pelajaran(self):
        return UserLesson.objects.filter(user=self.user, bab_kelas=self.bab_kelas)


#pertanyaan lesson yang sudah diselesaikan
class UserQuestion(models.Model):
    user        = models.ForeignKey(user_root, blank=True, null=True,on_delete=models.CASCADE, related_name="user_question_user")
    questions   = models.ForeignKey('teacher.Questions',blank=True, null=True,on_delete=models.CASCADE, related_name="UserQuestion_Question")
    kelas       = models.ForeignKey('teacher.Kelas',blank=True, null=True,on_delete=models.CASCADE, related_name="UserQuestion_kelas")
    bab_kelas   = models.ForeignKey('teacher.Bab',blank=True, null=True,on_delete=models.CASCADE, related_name="userbab_Question")
    latihan     = models.ForeignKey('user.UserLatihan',blank=True, null=True,on_delete=models.CASCADE, related_name="user_latihan")
    selected    = models.CharField(max_length=225, blank=True, null=True)
    right       = models.BooleanField(default=False)
    tanggal     = models.DateField(auto_now_add=True)
    def __str__(self):
        return "{} {}{}".format(self.id, self.user, self.questions)

#games yang sudah di selesaikan
class UserGames(models.Model):
    user        = models.ForeignKey(user_root, blank=True, null=True,on_delete=models.CASCADE, related_name="user_games_user")
    games       = models.ForeignKey('teacher.Games',blank=True, null=True,on_delete=models.CASCADE, related_name="Usergames_Games")
    kelas       = models.ForeignKey('teacher.Kelas',blank=True, null=True,on_delete=models.CASCADE, related_name="Usergames_kelas")
    bab_kelas   = models.ForeignKey('teacher.Bab',blank=True, null=True,on_delete=models.CASCADE, related_name="userbab_games")
    right       = models.IntegerField(default=0) #jumlah benar
    wrong       = models.IntegerField(default=0)  #jumlah salah
    failed      = models.IntegerField(default=0) #jumlah orang yg skip
    def __str__(self):
        return "{} {}{}".format(self.id, self.user, self.games)
    
class UserLatihan(models.Model):
    user        = models.ForeignKey(user_root, blank=True, null=True,on_delete=models.CASCADE, related_name="user_latihan_user")
    kelas       = models.ForeignKey('teacher.Kelas',blank=True, null=True,on_delete=models.CASCADE, related_name="user_kelas_latihan")
    pelajaran   = models.ForeignKey('teacher.Pelajaran',blank=True, null=True,on_delete=models.CASCADE, related_name="user_latihan_pelajaran")
    bab_kelas   = models.ForeignKey('teacher.Bab',blank=True, null=True,on_delete=models.CASCADE, related_name="user_latihan")
    is_last     = models.BooleanField(default=False)
    is_finish   = models.BooleanField(default=False)
    nilai       = models.IntegerField(blank=True, null=True)
    tanggal     = models.DateTimeField(auto_now_add=True)
    countdown   = models.TimeField(default="00:10:00")
    countdownNow= models.TimeField(default="00:10:00")
    def __str__(self):
        return "{}{}".format(self.user, self.nilai)

    def soal(self):
        return UserQuestion.objects.filter(latihan=self)


#keranjang untuk semua layanan
class Cart(models.Model):
    user        = models.ForeignKey(user_root, blank=True, null=True,on_delete=models.CASCADE, related_name="user_cart_user")
    kelas       = models.ForeignKey('teacher.Kelas',blank=True, null=True,on_delete=models.CASCADE, related_name="cart_kelas")
    promo       = models.ForeignKey("owner.Promo", blank=True, null=True, on_delete=models.CASCADE, related_name="cart_promo")
    bukti       = models.FileField(upload_to='media/bukti', blank=True)
    approve     = models.BooleanField(default=False)
    favorite    = models.BooleanField(default=False)
    tgl         = models.DateField(auto_now_add=True)
    def __str__(self):
        return "{} take {}".format(self.user, self.kelas)

#vocab yang sudah di kerjakan
class UserVocab(models.Model):
    user        = models.ForeignKey(user_root, blank=True, null=True,on_delete=models.CASCADE, related_name="user_vocab_user")
    vocab       = models.ForeignKey("teacher.VocabGroup", blank=True, null=True,on_delete=models.CASCADE, related_name="vocab")
    level       = models.IntegerField(default=0)
    benar       = models.IntegerField(default=0)
    salah       = models.IntegerField(default=0)
    isdone      = models.BooleanField(default=False)
    def __str__(self):
        return "{}-{}".format(self.user, self.vocab)
    
class UserMeeting(models.Model):
    mentor      = models.ForeignKey(user_root, blank=True, null=True,on_delete=models.CASCADE, related_name="mentor_meeting")
    user        = models.ForeignKey(user_root, blank=True, null=True,on_delete=models.CASCADE, related_name="user_meeting")
    room        = models.ForeignKey("teacher.Room", blank=True, null=True,on_delete=models.CASCADE, related_name="user_meeting")
    accountlevel= models.ForeignKey("owner.LevelAkun", blank=True, null=True,on_delete=models.CASCADE, related_name="user_meeting")
    start       = models.DateField(auto_now_add=True)
    end         = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    meetremain  = models.IntegerField(default=0)
    purchased   = models.BooleanField(default=False)
    trx_id      = models.IntegerField(default=0)
    via         = models.CharField(max_length=50, null=True)
    status      = models.CharField(max_length=50, null=True)
    SessionID   = models.CharField(max_length=50)
    def __str__(self):
        return "{}. {}-{}".format(self.id, self.user, self.meetremain)
    
    def meetremains(self):
        return UserSchadule.objects.filter(meeting=self, hadir=False).count()
    
    def mentorprofile(self):
        return Users.objects.get(user=self.mentor)
    
#jika sudah di mentor langsung 
class UserMentor(models.Model):
    mentor      = models.ForeignKey(user_root,blank=True, null=True,on_delete=models.CASCADE,related_name="user_teacher")
    user        = models.ForeignKey(user_root,blank=True, null=True,on_delete=models.CASCADE,related_name="user_mentor")
    isMentored  = models.BooleanField(default=False)
    start       = models.DateField(auto_now=False, auto_now_add=False)
    end         = models.DateField(auto_now=False, auto_now_add=False)
    like        = models.IntegerField(blank=True, null=True)
    message     = models.CharField(max_length=224, blank=True)
    def __str__(self):
        return "{} - {}.{}".format(self.user, self.mentor, self.like)
    def mentorprofile(self):
        return Users.objects.get(user=self.mentor)
    
#user yang mendaftar
class UserSchadule(models.Model):
    room        = models.ForeignKey("teacher.Room",blank=True, null=True,on_delete=models.CASCADE, related_name="room_room")
    schadule    = models.ForeignKey("teacher.Schadule",blank=True, null=True,on_delete=models.CASCADE, related_name="room_schadule")
    user        = models.ForeignKey(user_root,blank=True, null=True,on_delete=models.CASCADE,related_name="user_room")
    meeting     = models.ForeignKey(UserMeeting,blank=True, null=True,on_delete=models.CASCADE,related_name="user_meeting")
    hadir       = models.BooleanField(default=False)
    feedback    = models.CharField(max_length=225, blank=True, null=True)
    performance = models.IntegerField(blank=True, null=True)
    tanggal     = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    def __str__(self):
        return "{} {}".format(self.room, self.tanggal)
    
    def now(self):
        return  True if self.tanggal == datetime.datetime.now().date() else False
    def absent(self):
        return True if self.tanggal < datetime.datetime.now().date() and self.hadir == False else False
    
        
