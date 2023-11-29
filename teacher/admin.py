from django.contrib import admin

# Register your models here.
from .models import Teacher, Games, Kelas, Pelajaran, Questions, Vocab, VocabGroup, Withdrow, Room, Bab, Schadule

class SlugAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("kelas",)}

admin.site.register(Teacher)
admin.site.register(Games)
admin.site.register(Kelas, SlugAdmin)
admin.site.register(Bab)
admin.site.register(Pelajaran)
admin.site.register(Questions)
admin.site.register(Vocab)
admin.site.register(VocabGroup)
admin.site.register(Withdrow)
admin.site.register(Room)
admin.site.register(Schadule)