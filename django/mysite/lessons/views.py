from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Book1

def index(request):
    return HttpResponse("Hello, sworld. You're at the polls index.")

# def lessonsNo(request, id=1):
#      content = {
#              'lessonNumber': id
#          }
#      return render(request, "lessons/index.html", content)


def lessonsNo(request, id=1):
    obj = Book1.objects.get(lesson=1)
    content = {
        'lessonNumber': id,
        'data': obj.arabic
    }
    return render(request, "lessons/index.html", content)
