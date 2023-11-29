from django.contrib import admin

# Register your models here.
from .models import Event, Advance, Artikel, Ask, Improve, Kategori, Setting, Level, LevelAkun, Master,Promo, QnA, Report, Transaksi,UserEvent, Earn, Langganan
admin.site.register(Event)
admin.site.register(Advance)
admin.site.register(Artikel)
admin.site.register(Ask)
admin.site.register(Improve)
admin.site.register(Kategori)
admin.site.register(Setting)
admin.site.register(Level)
admin.site.register(LevelAkun)
admin.site.register(Master)
admin.site.register(Promo)
admin.site.register(QnA)
admin.site.register(Report)
admin.site.register(Transaksi)
admin.site.register(UserEvent)
admin.site.register(Earn)
admin.site.register(Langganan)