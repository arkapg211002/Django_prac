from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from .models import Members

# Create your views here.
def index(request):
    template=loader.get_template('myfirst.html')
    mm=Members.objects.all().values()
    #output=','.join([q['name'] for q in mm])
    #return HttpResponse("Hello, world. You're at the members index.")
    #return HttpResponse(template.render())

    ## in context 'mm' is the variable name in the template
    context={'mm':mm,}
    return HttpResponse(template.render(context,request))


def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))

'''def addrecord(request):
    template = loader.get_template('addrecord.html')
    return HttpResponse(template.render({}, request))
    '''
'''def addrecord(request):
  x = request.POST['name']
  y = request.POST['country']
  member = Members(name=x, country=y)
  member.save()
  return HttpResponseRedirect(reverse('index'))
  '''
def addrecord(request):
    x = request.POST['name']
    '''y = request.POST['email']
    z = request.POST['phone']
    a = request.POST['address']
    b = request.POST['city']
    c = request.POST['state']
    d = request.POST['zip']
    e = request.POST['country']
    f = request.POST['website']
    g = request.POST['notes']'''
    y = request.POST['country']
    #member = Members(name=x, email=y, phone=z, address=a, city=b, state=c, zip=d, country=e, website=f, notes=g)
    member=Members(name=x,country=y)
    member.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request,id):
    member = Members.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))

def update(request,id):
  template=loader.get_template('update.html')
  member=Members.objects.get(id=id)
  context={'member':member,}
  return HttpResponse(template.render(context,request))

def updaterecord(request,id):
  x = request.POST['name']
  y = request.POST['country']
  member = Members.objects.get(id=id)
  member.name = x
  member.country = y
  member.save()
  return HttpResponseRedirect(reverse('index'))