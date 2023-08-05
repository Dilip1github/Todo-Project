from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import course
from django.db.models import Q
# Create your views here.

def create_task(request):
    return render(request,'myapp/createcourse.html')

def task_form(request):
    if request.method == 'POST':
        x = request.POST['cname']
        y = request.POST['cdur']
        z = request.POST['cprice']
        s = course.objects.create(cname=x,cdur=y,cprice=z)
        s.save()
    return redirect('/')

def get_task(request):
    dis = {}
    dis ['data'] = course.objects.all()
    print(dis)
    return render(request,'myapp/dashboard.html',dis)

def delete(request,rid):
    x = course.objects.get(id = rid)
    x.delete()
    return redirect('/')

def edit(request,rid):
    if request.method == "POST":
        x = request.POST['cname']
        y = request.POST['cdur']
        z = request.POST['cprice']
        c = course.objects.filter(id = rid)
        c.update(cname=x,cdur=y,cprice=z)
        return redirect('/')
    else:
        display = {}
        display ['data'] = course.objects.get(id = rid)
        return render(request,'myapp/course_edit.html',display)
    