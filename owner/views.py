from django.shortcuts import redirect, render

context = {
    'url':'index',
    'title':'index',
    'icon':'static/assets/icon.png'
}
def index(request):
    return render(request, 'user/index.html', context)