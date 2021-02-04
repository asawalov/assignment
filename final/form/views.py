from django.shortcuts import render,HttpResponse,redirect
from .models import auth
from .form import authform
def home(request):
    return HttpResponse('<h1>This is hone </h1>')


def annoymous(request):
    all = auth.objects.all()
    
    return render(request,'form/annoymous.html',{'all':all})

def adminuser(request):
    all = auth.objects.all()

    return render(request,'form/adminuser.html',{'all':all})


def createuser(request):
    form = authform()

    if request.method == 'POST':
        form = authform(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/adminuser')
    context = {'form':form}
    return render(request,'form/form.html',context)


def updateuser(request,pk):
    user = auth.objects.get(id = pk)
    form = authform(instance = user)
    if request.method == 'POST':
        form = authform(request.POST,instance=user)
        if form.is_valid:
            form.save()
            return redirect('/adminuser')
    context = {'form' : form}
    return render(request,'form/form.html',context)


def deleteuser(request,pk):
    user = auth.objects.get(id = pk)
    user.delete()
    
    return redirect('/adminuser')

