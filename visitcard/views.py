from django.http import HttpResponse

def hello(request):
    return HttpResponse('<h> Privet </h1>')
