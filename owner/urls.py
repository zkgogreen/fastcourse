from django.urls import path
from . import views, views_kelas, views_setting

urlpatterns = [
    path('', views.index, name="index"),

    path('kelas', views_kelas.index, name="kelas"),
    path('kelas/hapus/<str:slug>', views_kelas.hapus_kelas, name="kelashapus"),
    path('kelas/rilis/<str:slug>', views_kelas.rilis_kelas, name="kelasrilis"),
    path('kelas/<str:slug>', views_kelas.edit_kelas, name="kelasdetail"),
    path('kelas/<str:slug>/<str:input>', views_kelas.next_kelas, name="next_kelas"),

    path('pelajaran/tambah/<str:slug>/<int:id>', views_kelas.tambah_pelajaran, name="tambah_pelajaran"),
    path('pelajaran/hapus/<str:slug>/<int:id>', views_kelas.hapus_pelajaran, name="hapus_pelajaran"),
    path('pelajaran/<int:id>', views_kelas.edit_pelajaran, name="edit_pelajaran"),

    path('setting', views_setting.index, name="setting"),
]