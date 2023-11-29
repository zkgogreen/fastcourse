from app.app import auth
from .forms import Landing
from .models import Setting
from django.contrib import messages
from django.shortcuts import redirect

def index(request):
    
    instance = Setting.objects.get(id=1)
    if request.method == "POST":
        form_landing = Landing(request.POST, request.FILES, instance=instance)
        if form_landing.is_valid():
            instance = form_landing.save()
            messages.success(request, 'Form submitted successfully!')
            return redirect("owner:setting")
        
    context = {
        'landing_form':Landing(instance=instance)
    }
    return auth(request, 'setting/index_new', context)