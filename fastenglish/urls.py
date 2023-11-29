from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include(('home.urls', 'home'), namespace='home')),
    path('user/', include(('user.urls', 'user'), namespace='user')),
    path('teacher/', include(('teacher.urls', 'teacher'), namespace='teacher')),
    path('owner/', include(('owner.urls', 'owner'), namespace='owner')),
    path("begin/", views.begin),
    path("delete/", views.delall),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
