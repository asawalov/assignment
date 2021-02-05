from django.shortcuts import render,HttpResponse,redirect
from .models import auth
from .form import authform
from django.contrib.auth.forms import UserCreationForm
from .form import UserCreateForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user, allowed_users

def home(request):
    return HttpResponse('<h1>This is hone </h1>')

@login_required(login_url='login')
def annoymous(request):
    # all = annoymoususer.objects.all()
    all = auth.objects.all()
   
    return render(request,'form/annoymous.html',{'all':all})


@login_required(login_url='login')

def adminuser(request):
    # all = annoymoususer.objects.all()
    all = auth.objects.all()

    # all2 = adminuser1.objects.all()
    
    return render(request,'form/adminuser.html',{'all':all })

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createuser(request):
    form = authform()

    if request.method == 'POST':
        form = authform(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/adminuser')
    context = {'form':form}
    return render(request,'form/form.html',context)
# @login_required(login_url='login')
# def createadminuser(request):
#     form = adminuserform()

#     if request.method == 'POST':
#         form = adminuserform(request.POST)
#         if form.is_valid:
#             form.save()
#             return redirect('/adminuser')
#     context = {'form':form}
#     return render(request,'form/form.html',context)
# @login_required(login_url='login')
# def createannoymoususer(request):
#     form = annoymoususerform()

#     if request.method == 'POST':
#         form = annoymoususerform(request.POST)
#         if form.is_valid:
#             form.save()
#             return redirect('/adminuser')
#     context = {'form':form}
#     return render(request,'form/form.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
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

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteuser(request,pk):
    user = auth.objects.get(id = pk)
    user.delete()
    
    return redirect('/adminuser')


def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None :
            login(request, user)
            return redirect('/adminuser')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {'user1': request.user}
    return render(request, 'form/login.html', context)
@unauthenticated_user
def register(request):
    form = UserCreateForm()
    
    if request.method == 'POST' :
        form = UserCreateForm(request.POST)
        if form.is_valid:
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='auth')
            user.groups.add(group)

            messages.success(request, 'Account was created for ' + username)

            return redirect('/login')

    context = {'form':form}
    return render(request,'form/register.html',context)



def logoutUser(request):
	logout(request)
	return redirect('login')



