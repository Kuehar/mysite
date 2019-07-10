from django.http import HttpResponse

def index(rewuest):
    return HttpResponse("Hello World!! You're at the polls index.")