from app.app import auth, kelas as kls
from user.models import Users
from teacher.models import Teacher
from owner.models import Master
# Create your views here.
def index(request):
    user = Users.objects.get(user=request.user.id)
    teacher = Teacher.objects.get(user=user)
    if request.method == 'POST':
        teacher.api_key = request.POST["apikey"]
        teacher.secret_key = request.POST["apisec"]
        teacher.mastered = Master(request.POST["mastered"])
        teacher.desc = request.POST["about"]
        teacher.save()
    context = {
        'info':teacher,
        'master':Master.objects.all()
    }
    return auth(request, 'setting/index', context)
