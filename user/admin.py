from django.contrib import admin

# Register your models here.
from .models import Cart, UserCourse, UserLesson, Users, UserVocab, UserQuestion, UserGames, UserMeeting, UserMentor, UserSchadule, UserLatihan, UserBab
admin.site.register(Cart)
admin.site.register(UserCourse)
admin.site.register(UserLesson)
admin.site.register(Users)
admin.site.register(UserVocab)
admin.site.register(UserQuestion)
admin.site.register(UserGames)
admin.site.register(UserMeeting)
admin.site.register(UserMentor)
admin.site.register(UserSchadule)
admin.site.register(UserLatihan)
admin.site.register(UserBab)