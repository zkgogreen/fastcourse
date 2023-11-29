from django.shortcuts import redirect
from owner.models import LevelAkun, Level, Kategori, Master, Setting
from teacher.models import Kelas, Bab, Pelajaran, Questions
from user.models import UserBab, UserCourse, UserLatihan, UserLesson
def home(request):
    return redirect("user:index")

def begin(request):
    # level akun
    levelakun1  = LevelAkun.objects.create(name='free', keterangan='belajar bahasa inggris tidak butuh biaya',  nyawa=5, biaya=0, discount=0,promo=0),
    levelakun2  = LevelAkun.objects.create(name='membersip', keterangan='belajar bahasa inggris dengan intensif',  nyawa=100, biaya=80000,discount=80000,promo=0)
    levelakun3  = LevelAkun.objects.create(name='Premium', keterangan='belajar bahasa inggris tanpa batasan', nyawa=100, biaya=120000,discount=120000,promo=0)
    
    #level
    level1      = Level.objects.create(name="Beginner", keterangan="kemampuan bahasa Inggris yang masih sangat dasar.")
    level2      = Level.objects.create(name="Elementary", keterangan="dapat berkomunikasi dengan bahasa Inggris, tetapi pembahasan hanya mencakup hal-hal tertentu yang telah dikuasai.")
    level3      = Level.objects.create(name="Intermediate", keterangan="berbahasa Inggris secara pasif dan aktif dengan topik yang lebih variatif.")
    level4      = Level.objects.create(name="Advanced", keterangan="menggunakan bahasa Inggris untuk kepentingan akademis dan profesional.")
    level5      = Level.objects.create(name="Expert", keterangan="setara dengan native speaker (penutur asli)")

    #kategori
    kategori1   = Kategori.objects.create(name="Speaking", keterangan="Kemampuan Berbicara ")
    kategori2   = Kategori.objects.create(name="Reading", keterangan="Kemampuan Membaca")
    kategori3   = Kategori.objects.create(name="Listening", keterangan="Keterampilan Menyimak")
    kategori4   = Kategori.objects.create(name="Writing", keterangan="Kemampuan Menulis")

    #master
    master1     = Master.objects.create(name="TOEFL", keterangan="Test of English as Foregn Language")
    master2     = Master.objects.create(name="Public Speaking", keterangan="Keterampilan berbicara dengan banyak orang")

    #kelas
    kelas1      = Kelas.objects.create(kelas="Kelas pertama", bahasa=1, slug="SpeakingDasar", photo="kelas/bannerexample2.png", kategori=kategori1, level=level1,
                                              keterangan="keterangan", rangkuman="rangkuman", urutan=1)
    
    k1b1        = Bab.objects.create(kelas=kelas1, bab="Bab 1", urutan=1, rangkuman="ini adalah rangkuman")
    k1b1p1      = Pelajaran.objects.create(kelas=kelas1, urutan=1, bab_kelas=k1b1, judul="judul pertama", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k1b1p1q1    = Questions.objects.create(category=kategori1, level=level1, kelas=kelas1, bab_kelas=k1b1, lesson=k1b1p1, soal="Kelas 1 bab 1 pelajaran 1 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b1p1q2    = Questions.objects.create(category=kategori1, level=level1, kelas=kelas1, bab_kelas=k1b1, lesson=k1b1p1, soal="Kelas 1 bab 1 pelajaran 1 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b1p1q3    = Questions.objects.create(category=kategori1, level=level1, kelas=kelas1, bab_kelas=k1b1, lesson=k1b1p1, soal="Kelas 1 bab 1 pelajaran 1 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)

    k1b1p2      = Pelajaran.objects.create(kelas=kelas1, urutan=2, bab_kelas=k1b1, judul="judul kedua", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k1b1p2q1    = Questions.objects.create(category=kategori1, level=level1, kelas=kelas1, bab_kelas=k1b1, lesson=k1b1p2, soal="Kelas 1 bab 1 pelajaran 2 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b1p2q2    = Questions.objects.create(category=kategori1, level=level1, kelas=kelas1, bab_kelas=k1b1, lesson=k1b1p2, soal="Kelas 1 bab 1 pelajaran 2 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b1p2q3    = Questions.objects.create(category=kategori1, level=level1, kelas=kelas1, bab_kelas=k1b1, lesson=k1b1p2, soal="Kelas 1 bab 1 pelajaran 2 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    k1b1p3      = Pelajaran.objects.create(kelas=kelas1, urutan=3, bab_kelas=k1b1, judul="judul ketiga", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k1b1p3q1    = Questions.objects.create(category=kategori1, level=level1, kelas=kelas1, bab_kelas=k1b1, lesson=k1b1p3, soal="Kelas 1 bab 1 pelajaran 3 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b1p3q2    = Questions.objects.create(category=kategori1, level=level1, kelas=kelas1, bab_kelas=k1b1, lesson=k1b1p3, soal="Kelas 1 bab 1 pelajaran 3 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b1p3q3    = Questions.objects.create(category=kategori1, level=level1, kelas=kelas1, bab_kelas=k1b1, lesson=k1b1p3, soal="Kelas 1 bab 1 pelajaran 3 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    k1b1p4      = Pelajaran.objects.create(kelas=kelas1, urutan=4, bab_kelas=k1b1, judul="judul keempat", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k1b1p4q1    = Questions.objects.create(category=kategori1, level=level1, kelas=kelas1, bab_kelas=k1b1, lesson=k1b1p4, soal="Kelas 1 bab 1 pelajaran 4 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b1p4q2    = Questions.objects.create(category=kategori1, level=level1, kelas=kelas1, bab_kelas=k1b1, lesson=k1b1p4, soal="Kelas 1 bab 1 pelajaran 4 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b1p4q3    = Questions.objects.create(category=kategori1, level=level1, kelas=kelas1, bab_kelas=k1b1, lesson=k1b1p4, soal="Kelas 1 bab 1 pelajaran 4 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    k1b1p5      = Pelajaran.objects.create(kelas=kelas1, urutan=5, bab_kelas=k1b1, judul="judul kelima", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k1b1p5q1    = Questions.objects.create(category=kategori1, level=level1, kelas=kelas1, bab_kelas=k1b1, lesson=k1b1p5, soal="Kelas 1 bab 1 pelajaran 4 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b1p5q2    = Questions.objects.create(category=kategori1, level=level1, kelas=kelas1, bab_kelas=k1b1, lesson=k1b1p5, soal="Kelas 1 bab 1 pelajaran 4 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b1p5q3    = Questions.objects.create(category=kategori1, level=level1, kelas=kelas1, bab_kelas=k1b1, lesson=k1b1p5, soal="Kelas 1 bab 1 pelajaran 4 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    
    k1b2        = Bab.objects.create(kelas=kelas1, bab="Bab 2", urutan=2, rangkuman="ini adalah rangkuman")
    
    k1b2p1      = Pelajaran.objects.create(kelas=kelas1, urutan=1, bab_kelas=k1b2, judul="judul pertama", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k1b2p1q1    = Questions.objects.create(category=kategori1, level=level2, kelas=kelas1, bab_kelas=k1b2, lesson=k1b2p1, soal="Kelas 1 bab 2 pelajaran 1 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b2p1q2    = Questions.objects.create(category=kategori1, level=level2, kelas=kelas1, bab_kelas=k1b2, lesson=k1b2p1, soal="Kelas 1 bab 2 pelajaran 1 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b2p1q3    = Questions.objects.create(category=kategori1, level=level2, kelas=kelas1, bab_kelas=k1b2, lesson=k1b2p1, soal="Kelas 1 bab 2 pelajaran 1 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)

    k1b2p2      = Pelajaran.objects.create(kelas=kelas1, urutan=2, bab_kelas=k1b2, judul="judul kedua", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k1b2p2q1    = Questions.objects.create(category=kategori1, level=level2, kelas=kelas1, bab_kelas=k1b2, lesson=k1b2p2, soal="Kelas 1 bab 2 pelajaran 2 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b2p2q2    = Questions.objects.create(category=kategori1, level=level2, kelas=kelas1, bab_kelas=k1b2, lesson=k1b2p2, soal="Kelas 1 bab 2 pelajaran 2 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b2p2q3    = Questions.objects.create(category=kategori1, level=level2, kelas=kelas1, bab_kelas=k1b2, lesson=k1b2p2, soal="Kelas 1 bab 2 pelajaran 2 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    k1b2p3      = Pelajaran.objects.create(kelas=kelas1, urutan=3, bab_kelas=k1b2, judul="judul ketiga", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k1b2p3q1    = Questions.objects.create(category=kategori1, level=level2, kelas=kelas1, bab_kelas=k1b2, lesson=k1b2p3, soal="Kelas 1 bab 2 pelajaran 3 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b2p3q2    = Questions.objects.create(category=kategori1, level=level2, kelas=kelas1, bab_kelas=k1b2, lesson=k1b2p3, soal="Kelas 1 bab 2 pelajaran 3 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b2p3q3    = Questions.objects.create(category=kategori1, level=level2, kelas=kelas1, bab_kelas=k1b2, lesson=k1b2p3, soal="Kelas 1 bab 2 pelajaran 3 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    k1b2p4      = Pelajaran.objects.create(kelas=kelas1, urutan=4, bab_kelas=k1b2, judul="judul keempat", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k1b2p4q1    = Questions.objects.create(category=kategori1, level=level2, kelas=kelas1, bab_kelas=k1b2, lesson=k1b2p4, soal="Kelas 1 bab 2 pelajaran 4 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b2p4q2    = Questions.objects.create(category=kategori1, level=level2, kelas=kelas1, bab_kelas=k1b2, lesson=k1b2p4, soal="Kelas 1 bab 2 pelajaran 4 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b2p4q3    = Questions.objects.create(category=kategori1, level=level2, kelas=kelas1, bab_kelas=k1b2, lesson=k1b2p4, soal="Kelas 1 bab 2 pelajaran 4 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    k1b2p5      = Pelajaran.objects.create(kelas=kelas1, urutan=5, bab_kelas=k1b2, judul="judul kelima", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k1b2p5q1    = Questions.objects.create(category=kategori1, level=level2, kelas=kelas1, bab_kelas=k1b2, lesson=k1b2p5, soal="Kelas 1 bab 2 pelajaran 4 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b2p5q2    = Questions.objects.create(category=kategori1, level=level2, kelas=kelas1, bab_kelas=k1b2, lesson=k1b2p5, soal="Kelas 1 bab 2 pelajaran 4 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b2p5q3    = Questions.objects.create(category=kategori1, level=level2, kelas=kelas1, bab_kelas=k1b2, lesson=k1b2p5, soal="Kelas 1 bab 2 pelajaran 4 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
        
    k1b3        = Bab.objects.create(kelas=kelas1, bab="Bab 3", urutan=3, rangkuman="ini adalah rangkuman")
    
    k1b3p1      = Pelajaran.objects.create(kelas=kelas1, urutan=1, bab_kelas=k1b3, judul="judul pertama", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k1b3p1q1    = Questions.objects.create(category=kategori1, level=level3, kelas=kelas1, bab_kelas=k1b3, lesson=k1b3p1, soal="Kelas 1 bab 3 pelajaran 1 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b3p1q2    = Questions.objects.create(category=kategori1, level=level3, kelas=kelas1, bab_kelas=k1b3, lesson=k1b3p1, soal="Kelas 1 bab 3 pelajaran 1 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b3p1q3    = Questions.objects.create(category=kategori1, level=level3, kelas=kelas1, bab_kelas=k1b3, lesson=k1b3p1, soal="Kelas 1 bab 3 pelajaran 1 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)

    k1b3p2      = Pelajaran.objects.create(kelas=kelas1, urutan=2, bab_kelas=k1b3, judul="judul kedua", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k1b3p2q1    = Questions.objects.create(category=kategori1, level=level3, kelas=kelas1, bab_kelas=k1b3, lesson=k1b3p2, soal="Kelas 1 bab 3 pelajaran 2 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b3p2q2    = Questions.objects.create(category=kategori1, level=level3, kelas=kelas1, bab_kelas=k1b3, lesson=k1b3p2, soal="Kelas 1 bab 3 pelajaran 2 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b3p2q3    = Questions.objects.create(category=kategori1, level=level3, kelas=kelas1, bab_kelas=k1b3, lesson=k1b3p2, soal="Kelas 1 bab 3 pelajaran 2 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    k1b3p3      = Pelajaran.objects.create(kelas=kelas1, urutan=3, bab_kelas=k1b3, judul="judul ketiga", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k1b3p3q1    = Questions.objects.create(category=kategori1, level=level3, kelas=kelas1, bab_kelas=k1b3, lesson=k1b3p3, soal="Kelas 1 bab 3 pelajaran 3 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b3p3q2    = Questions.objects.create(category=kategori1, level=level3, kelas=kelas1, bab_kelas=k1b3, lesson=k1b3p3, soal="Kelas 1 bab 3 pelajaran 3 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b3p3q3    = Questions.objects.create(category=kategori1, level=level3, kelas=kelas1, bab_kelas=k1b3, lesson=k1b3p3, soal="Kelas 1 bab 3 pelajaran 3 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    k1b3p4      = Pelajaran.objects.create(kelas=kelas1, urutan=4, bab_kelas=k1b3, judul="judul keempat", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k1b3p4q1    = Questions.objects.create(category=kategori1, level=level3, kelas=kelas1, bab_kelas=k1b3, lesson=k1b3p4, soal="Kelas 1 bab 3 pelajaran 4 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b3p4q2    = Questions.objects.create(category=kategori1, level=level3, kelas=kelas1, bab_kelas=k1b3, lesson=k1b3p4, soal="Kelas 1 bab 3 pelajaran 4 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b3p4q3    = Questions.objects.create(category=kategori1, level=level3, kelas=kelas1, bab_kelas=k1b3, lesson=k1b3p4, soal="Kelas 1 bab 3 pelajaran 4 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    k1b3p5      = Pelajaran.objects.create(kelas=kelas1, urutan=5, bab_kelas=k1b3, judul="judul kelima", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k1b3p5q1    = Questions.objects.create(category=kategori1, level=level3, kelas=kelas1, bab_kelas=k1b3, lesson=k1b3p5, soal="Kelas 1 bab 3 pelajaran 4 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b3p5q2    = Questions.objects.create(category=kategori1, level=level3, kelas=kelas1, bab_kelas=k1b3, lesson=k1b3p5, soal="Kelas 1 bab 3 pelajaran 4 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k1b3p5q3    = Questions.objects.create(category=kategori1, level=level3, kelas=kelas1, bab_kelas=k1b3, lesson=k1b3p5, soal="Kelas 1 bab 3 pelajaran 4 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)

    #kelas 2
    kelas2      = Kelas.objects.create(kelas="Speaking Intermediate", bahasa=1, slug="SpeakingIntermediate", photo="kelas/bannerexample1.png", kategori=kategori1, level=level3,
                                              keterangan="keterangan", rangkuman="rangkuman", urutan=2)
    
    k2b1        = Bab.objects.create(kelas=kelas2, bab="Bab 1", urutan=1, rangkuman="ini adalah rangkuman")
    k2b1p1      = Pelajaran.objects.create(kelas=kelas2, urutan=1, bab_kelas=k2b1, judul="judul pertama", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k2b1p1q1    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b1, lesson=k2b1p1, soal="Kelas 2 bab 1 pelajaran 1 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b1p1q2    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b1, lesson=k2b1p1, soal="Kelas 2 bab 1 pelajaran 1 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b1p1q3    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b1, lesson=k2b1p1, soal="Kelas 2 bab 1 pelajaran 1 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)

    k2b1p2      = Pelajaran.objects.create(kelas=kelas2, urutan=2, bab_kelas=k2b1, judul="judul kedua", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k2b1p2q1    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b1, lesson=k2b1p2, soal="Kelas 2 bab 1 pelajaran 2 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b1p2q2    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b1, lesson=k2b1p2, soal="Kelas 2 bab 1 pelajaran 2 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b1p2q3    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b1, lesson=k2b1p2, soal="Kelas 2 bab 1 pelajaran 2 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    k2b1p3      = Pelajaran.objects.create(kelas=kelas2, urutan=3, bab_kelas=k2b1, judul="judul ketiga", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k2b1p3q1    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b1, lesson=k2b1p3, soal="Kelas 2 bab 1 pelajaran 3 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b1p3q2    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b1, lesson=k2b1p3, soal="Kelas 2 bab 1 pelajaran 3 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b1p3q3    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b1, lesson=k2b1p3, soal="Kelas 2 bab 1 pelajaran 3 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    k2b1p4      = Pelajaran.objects.create(kelas=kelas2, urutan=4, bab_kelas=k2b1, judul="judul keempat", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k2b1p4q1    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b1, lesson=k2b1p4, soal="Kelas 2 bab 1 pelajaran 4 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b1p4q2    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b1, lesson=k2b1p4, soal="Kelas 2 bab 1 pelajaran 4 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b1p4q3    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b1, lesson=k2b1p4, soal="Kelas 2 bab 1 pelajaran 4 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    k2b1p5      = Pelajaran.objects.create(kelas=kelas2, urutan=5, bab_kelas=k2b1, judul="judul kelima", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k2b1p5q1    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b1, lesson=k2b1p5, soal="Kelas 2 bab 1 pelajaran 4 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b1p5q2    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b1, lesson=k2b1p5, soal="Kelas 2 bab 1 pelajaran 4 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b1p5q3    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b1, lesson=k2b1p5, soal="Kelas 2 bab 1 pelajaran 4 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    
    k2b2        = Bab.objects.create(kelas=kelas2, bab="Bab 2", urutan=2, rangkuman="ini adalah rangkuman")
    
    k2b2p1      = Pelajaran.objects.create(kelas=kelas2, urutan=1, bab_kelas=k2b2, judul="judul pertama", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k2b2p1q1    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b2, lesson=k2b2p1, soal="Kelas 2 bab 2 pelajaran 1 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b2p1q2    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b2, lesson=k2b2p1, soal="Kelas 2 bab 2 pelajaran 1 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b2p1q3    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b2, lesson=k2b2p1, soal="Kelas 2 bab 2 pelajaran 1 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)

    k2b2p2      = Pelajaran.objects.create(kelas=kelas2, urutan=2, bab_kelas=k2b2, judul="judul kedua", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k2b2p2q1    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b2, lesson=k2b2p2, soal="Kelas 2 bab 2 pelajaran 2 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b2p2q2    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b2, lesson=k2b2p2, soal="Kelas 2 bab 2 pelajaran 2 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b2p2q3    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b2, lesson=k2b2p2, soal="Kelas 2 bab 2 pelajaran 2 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    k2b2p3      = Pelajaran.objects.create(kelas=kelas2, urutan=3, bab_kelas=k2b2, judul="judul ketiga", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k2b2p3q1    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b2, lesson=k2b2p3, soal="Kelas 2 bab 2 pelajaran 3 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b2p3q2    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b2, lesson=k2b2p3, soal="Kelas 2 bab 2 pelajaran 3 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b2p3q3    = Questions.objects.create(category=kategori1, level=level4, kelas=kelas2, bab_kelas=k2b2, lesson=k2b2p3, soal="Kelas 2 bab 2 pelajaran 3 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    k2b2p4      = Pelajaran.objects.create(kelas=kelas2, urutan=4, bab_kelas=k2b2, judul="judul keempat", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k2b2p4q1    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b2, lesson=k2b2p4, soal="Kelas 2 bab 2 pelajaran 4 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b2p4q2    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b2, lesson=k2b2p4, soal="Kelas 2 bab 2 pelajaran 4 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b2p4q3    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b2, lesson=k2b2p4, soal="Kelas 2 bab 2 pelajaran 4 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    k2b2p5      = Pelajaran.objects.create(kelas=kelas2, urutan=5, bab_kelas=k2b2, judul="judul kelima", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k2b2p5q1    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b2, lesson=k2b2p5, soal="Kelas 2 bab 2 pelajaran 4 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b2p5q2    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b2, lesson=k2b2p5, soal="Kelas 2 bab 2 pelajaran 4 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b2p5q3    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b2, lesson=k2b2p5, soal="Kelas 2 bab 2 pelajaran 4 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
        
    k2b3        = Bab.objects.create(kelas=kelas2, bab="Bab 3", urutan=3, rangkuman="ini adalah rangkuman")
    
    k2b3p1      = Pelajaran.objects.create(kelas=kelas2, urutan=1, bab_kelas=k2b3, judul="judul pertama", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k2b3p1q1    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b3, lesson=k2b3p1, soal="Kelas 2 bab 3 pelajaran 1 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b3p1q2    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b3, lesson=k2b3p1, soal="Kelas 2 bab 3 pelajaran 1 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b3p1q3    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b3, lesson=k2b3p1, soal="Kelas 2 bab 3 pelajaran 1 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)

    k2b3p2      = Pelajaran.objects.create(kelas=kelas2, urutan=2, bab_kelas=k2b3, judul="judul kedua", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k2b3p2q1    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b3, lesson=k2b3p2, soal="Kelas 2 bab 3 pelajaran 2 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b3p2q2    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b3, lesson=k2b3p2, soal="Kelas 2 bab 3 pelajaran 2 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b3p2q3    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b3, lesson=k2b3p2, soal="Kelas 2 bab 3 pelajaran 2 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    k2b3p3      = Pelajaran.objects.create(kelas=kelas2, urutan=3, bab_kelas=k2b3, judul="judul ketiga", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k2b3p3q1    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b3, lesson=k2b3p3, soal="Kelas 2 bab 3 pelajaran 3 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b3p3q2    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b3, lesson=k2b3p3, soal="Kelas 2 bab 3 pelajaran 3 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b3p3q3    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b3, lesson=k2b3p3, soal="Kelas 2 bab 3 pelajaran 3 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    k2b3p4      = Pelajaran.objects.create(kelas=kelas2, urutan=4, bab_kelas=k2b3, judul="judul keempat", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k2b3p4q1    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b3, lesson=k2b3p4, soal="Kelas 2 bab 3 pelajaran 4 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b3p4q2    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b3, lesson=k2b3p4, soal="Kelas 2 bab 3 pelajaran 4 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b3p4q3    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b3, lesson=k2b3p4, soal="Kelas 2 bab 3 pelajaran 4 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    
    k2b3p5      = Pelajaran.objects.create(kelas=kelas2, urutan=5, bab_kelas=k2b3, judul="judul kelima", keterangan="ini adalah keterangan", text="ini adalah text", approve=True)
    k2b3p5q1    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b3, lesson=k2b3p5, soal="Kelas 2 bab 3 pelajaran 4 soal 1", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b3p5q2    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b3, lesson=k2b3p5, soal="Kelas 2 bab 3 pelajaran 4 soal 2", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    k2b3p5q3    = Questions.objects.create(category=kategori1, level=level5, kelas=kelas2, bab_kelas=k2b3, lesson=k2b3p5, soal="Kelas 2 bab 3 pelajaran 4 soal 3", answer="benar", wrong1="salah", wrong2="salah", wrong3="salah", penjelasan="penjelasan : ", approve=True)
    #Landing
    if not Setting.objects.all().exists():
        Setting.objects.create(title="Belajar bahasa inggris", sub="belajar bahasa inggris")
    
    return redirect("user:index")

def delall(request):
    LevelAkun.objects.all().delete()
    Level.objects.all().delete()
    Kategori.objects.all().delete()
    Master.objects.all().delete()
    Setting.objects.all().delete()


    Kelas.objects.all().delete()
    Bab.objects.all().delete()
    Pelajaran.objects.all().delete()
    Questions.objects.all().delete()

    UserBab.objects.all().delete()
    UserCourse.objects.all().delete()
    UserLatihan.objects.all().delete()
    UserLesson.objects.all().delete()
    
    return redirect("user:index")