from django.http import HttpResponse

def home(request):
    return HttpResponse("<html><body><a href='/mopup'>Mop it up!</a>")
