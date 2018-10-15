from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from emaillist.models import Emaillist


def index(request):
   # results = models.fetchall()
   # order_by('id) = asc ('-id') = desc

   results = Emaillist.objects.all().order_by('-id')
   data = {'emaillist_list': results}

   return render(request, 'emaillist/index.html', data)

def form(request):
    return render(request, 'emaillist/form.html')


def add(request):

    emaillist = Emaillist()

    #form.html에가서 각 name을 확인해서 넣어준다.
    emaillist.first_name = request.POST['fn']
    emaillist.last_name = request.POST['ln']
    emaillist.email = request.POST['email']

   # models.insert((first_name, last_name, email))
    emaillist.save()
    #  save는 insert


    return HttpResponseRedirect("/emaillist")