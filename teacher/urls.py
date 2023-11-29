from django.urls import path

from .kelas import views_kelas, views_bab, views_pelajaran
from . import views, views_setting, views_bootcamp

urlpatterns = [
    path('', views.index, name="index"),
    path('bootcamp', views_bootcamp.index, name="bootcamp"),
    path('reschadule', views_bootcamp.reschadule, name="reschadule"),

    # kelas 
    path('kelas', views_kelas.kelas, name="kelas"),
    path('kelas/<int:id>', views_kelas.detail, name="kelas_detail"),
    # kelas | bab
    path('kelas/bab/<int:id>', views_bab.index, name="bab"),
    path('kelas/bab/edit/<int:id>', views_bab.bab_edit, name="bab_edit"),
    path('kelas/bab/hapus/<int:id>', views_bab.bab_hapus, name="bab_hapus"),
    # kelas | pelajaran
    path('kelas/pelajaran/tambah/<int:id_bab>/<int:urutan>', views_pelajaran.pelajaran_tambah, name="pelajaran_tambah"),
    path('kelas/pelajaran/edit/<int:id_bab>/<int:urutan>', views_pelajaran.pelajaran_edit, name="pelajaran_edit"),
    path('kelas/pelajaran/hapus/<int:id>', views_pelajaran.pelajaran_hapus, name="pelajaran_hapus"),
    #kelas  | soal
    path('kelas/soal/<int:id_bab>', views_pelajaran.soal, name="soal_all"),
    path('kelas/soal/detail/<int:id_pelajaran>', views_pelajaran.soal_detail, name="soal"),
    path('kelas/soal/edit/<int:id_soal>', views_pelajaran.soal_edit, name="soal_edit"),
    
    # path('kelas/hapus/<int:id>', views_kelas.kelas_hapus, name="kelas_hapus"),
    path('setting', views_setting.index, name="setting"),
]