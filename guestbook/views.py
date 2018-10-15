from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from guestbook.models import Guestbook


def index(request):
    results = Guestbook.objects.all().order_by('-id')
    data = {'messages': results}

    return render(request, 'guestbook/index1.html', data)

def add(request):

    guestbook =Guestbook()

    guestbook.name = request.POST['name']
    guestbook.password = request.POST['pass']
    guestbook.content = request.POST['content']

    guestbook.save()

    return HttpResponseRedirect('/guestbook')

def delete(request):

    password= request.POST['password']
    id = request.POST['id']

    Guestbook.objects.filter(id=int(id)).filter(password=password).delete()


    return HttpResponseRedirect('/guestbook')

def deleteform(request):
    id = request.GET['id']
    data = {"id": id}
    return render(request, "guestbook/deleteform.html", data)