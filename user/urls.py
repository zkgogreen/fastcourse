from django.urls import path
from . import views, views_message, view_kelas, view_bootcamp, views_upgrade, views_pdf

urlpatterns = [
    path('', views.index, name="index"),
    path('checkuser', views.checkuser, name="checkuser"),
    path('changeteacher', views.teacher, name="changeteacher"),

    #message
    path('message', views_message.index, name="message"),

    #kelas
    path('kelas', view_kelas.index.as_view(), name="kelas"),
    path('kelas/<str:slug>', view_kelas.index.as_view(), name="koridor"),
    path('kelas/subscribe/<str:slug>', view_kelas.index.as_view(), name="subscribe"),

    path('kelas/<str:slug>/<int:urutan_bab>/<int:urutan_pelajaran>', view_kelas.pelajaran.as_view(), name="pelajaran"),
    path('kelas/<int:id_pelajaran>', view_kelas.pelajaran.as_view(), name="komentar"),
    path('kelas/soal/pembahasan/<int:id>', view_kelas.pembahasan, name="pembahasan"),
    path('kelas/soal/waktu', view_kelas.waktu, name="waktu"),
    path('kelas/soal/select', view_kelas.select, name="select"),
    path('kelas/soal/<str:slug>/<int:urutan_bab>', view_kelas.soal, name="soal"),
    path('kelas/soal/<str:slug>', view_kelas.soal_kelas, name="soal_kelas"),
    path('kelas/rangkuman/<str:slug>/<int:urutan_bab>', view_kelas.rangkuman, name="rangkuman"),
    path('kelas/rangkuman/<str:slug>', view_kelas.rangkuman_kelas, name="rangkuman_kelas"),
    path('kelas/koridor-soal/<str:slug>/<int:urutan_bab>', view_kelas.koridor_soal, name="koridor_soal"),
    path('kelas/koridor-soal-kelas/<str:slug>', view_kelas.koridor_soal_kelas, name="koridor_soal_kelas"),

    #bootcamp
    path('bootcamp', view_bootcamp.index, name="bootcamp"),
    path('bootcamp/jadwal', view_bootcamp.jadwal, name="jadwal"),
    path('bootcamp/coming', view_bootcamp.coming, name="coming_bootcamp"),
    path('bootcamp/purchase', view_bootcamp.purchase_bootcamp, name="purchase_bootcamp"),
    path('bootcamp/confirm/<int:id>', view_bootcamp.confirm, name="confirm_bootcamp"),
    path('bootcamp/confirm/thank', view_bootcamp.thank, name="thank"),
    path('bootcamp/confirm/callback/<int:ref_id>', view_bootcamp.notify, name="notify"),

    # upgrade
    path('upgrade', views_upgrade.index, name="upgrade"),
    path('upgrade/purchase', views_upgrade.upgrade, name="purchase_upgrade"),

    path('pdf', views_pdf.generate_english_certificate, name="pdf")
]