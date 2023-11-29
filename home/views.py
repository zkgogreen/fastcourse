from django.shortcuts import render, HttpResponse

# Create your views here.
def home(requets):
    context = {
        
    }
    return render(requets, "index.html", context)