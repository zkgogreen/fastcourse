from app.app import auth

# Create your views here.
def index(request):
    context = {
    }
    return auth(request, 'message', context)