from django.shortcuts import render,redirect,HttpResponse
from myportfolioHp.models import contactme

def home(request):
    return render(request,'index.html')

def contact_update(request):
    data = contactme.objects.all()
    context = {"data": data}
    return render(request, "contact_update.html", context)



def insertdata(request):
    if request.method=='POST':
        name=request.POST.GET('name')
        email=request.POST.GET('email')
        subject=request.POST.GET('subject')
        message=request.POST.GET('message')
        save=contactme(name=name, email=email,subject=subject,message=message)
        save.save()
    else:
        return render(request,'contact_update.html')

def updateData(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message= request.POST.get('message')

        edit = contactme.objects.get(id=id)
        edit.name = name
        edit.email = email
        edit.subject = subject
        edit.message= message
        edit.save()
        return redirect("/")

    d = Student.objects.get(id=id)
    context = {"d": d}
    return render(request, "contact_edit.html", context)
def deleteData(request, id):
    d = contactme.objects.get(id=id)
    d.delete()
    return redirect("/")

    return render(request, "contact_update.html")




