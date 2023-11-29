from django.shortcuts import render,redirect
from myportfolioHp.models import contactme

def home(request):
    return render(request,'index.html')
    data=contactme.objects.all()

def insertdata(request):
    if request.method=='POST':
        name=request.POST.GET('name')
        email=request.POST.GET('email')
        subject=request.POST.GET('subject')
        message=request.POST.GET('message')
        save=contactme(name=name, email=email,subject=subject,message=message)
        save.save()
    else:
        return render(request,'index.html')

def updateData(request,id):
    if request.method=='POST':
        name=request.POST.GET('name')
        email=request.POST.GET('email')
        subject=request.POST.GET('subject')
        message=request.POST.GET('message')
        update=contactme.objects.get(id=id)

    else:
        d=contactme.objects.get(id=id)



