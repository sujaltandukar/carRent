from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from accounts.forms import EditProfileForm

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,'Username or Password Not Matching')
            return redirect('login')

    else:
        return render(request, 'login.html')

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email  Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save();
                print('User Created')
                return redirect('login')
        else:
            messages.info(request,'Password Not Matching!')
            return redirect('register')

        return redirect('/')

    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required(login_url="accounts/login")
def editprofile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = EditProfileForm(instance=request.user)
        args={'form':form}
        return render(request,"edit_profile.html", args)

@login_required
def changepw(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect("profile")
    else:
        form = PasswordChangeForm(user=request.user)
        args={'form':form}
        return render(request,"change_password.html", args)
