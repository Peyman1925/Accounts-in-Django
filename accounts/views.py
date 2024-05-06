from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.conf import settings
from django.core.mail import send_mail
from .models import CustomUser
from .forms import *

# Create your views here.

User = CustomUser

#:::::::::::::::::::::::::::::::::::::::::::::::::
#----------------User registration----------------
#:::::::::::::::::::::::::::::::::::::::::::::::::
def register(request):
    
    if request.method == 'POST':
        
        firstname = request.POST['Firstname']
        lastname = request.POST['lastname']
        username = request.POST['Username']
        email = request.POST['Email']
        # phone = request.POST['Phone']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if not all([firstname, lastname, username, email, password, confirm_password]):
            messages.error(request, 'Please fill in all fields')
            return render(request, 'accounts/register.html')
        
        if password != confirm_password:
            messages.error(request, 'Password and confirmation do not match')
            return render(request, 'accounts/register.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already in use')
            return render(request, 'accounts/register.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already used')
            return render(request, 'accounts/register.html')
        
        user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email, password=password)
        user.save()
        subject = 'Subject'
        message = f'Hello, {username}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, email_from, recipient_list)
        auth.login(request, user)
        
        messages.success(request, 'Your registration was successful')
        return redirect('dashboard')
    else:
        return render(request, 'accounts/register.html')

#:::::::::::::::::::::::::::::::::::::::::::::::::
#----------------User login-----------------------
#:::::::::::::::::::::::::::::::::::::::::::::::::    
def login(request):
    
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return redirect('home')
    
    return render(request, 'accounts/login.html')


#:::::::::::::::::::::::::::::::::::::::::::::::::
#--------------------Dashboard--------------------
#:::::::::::::::::::::::::::::::::::::::::::::::::  
def dashboard(request):
    user = request.user    
    return render(request, 'accounts/dashboard.html', {'user': user})

#:::::::::::::::::::::::::::::::::::::::::::::::::
#-----------------Change Password-----------------
#:::::::::::::::::::::::::::::::::::::::::::::::::
def ChangePassword(request):
    user = request.user
    u = User.objects.get(username = user.username)
    
    if request.method == 'POST':
            new_password = request.POST['new_password']
            confirm_password = request.POST['confirm_password']
            if new_password == confirm_password:
                u.set_password(new_password)
                u.save()
                return redirect('logout')
 
    return render(request, 'accounts/changePassword.html')

#:::::::::::::::::::::::::::::::::::::::::::::::::
#----------------Edit Image Profile---------------
#:::::::::::::::::::::::::::::::::::::::::::::::::
def UserProfilePicture(request):
    user = request.user
    if user.is_authenticated:
        if request.method == 'POST':
            form = UserProfilePictureForm(request.POST, request.FILES, instance=user)
            if form.is_valid():
                form.save()
                return redirect('dashboard')
            else:
                print('.................Error...................')
        else:
            form = UserProfilePictureForm(instance=user)
        data = {
            'form': form,
        }
        return render(request, 'accounts/UserProfilePicture.html', data)
    else:
        print('...................You not logged in!!!!...................')
        return redirect('UserProfilePicture')

#:::::::::::::::::::::::::::::::::::::::::::::::::
#----------------------Logout---------------------
#:::::::::::::::::::::::::::::::::::::::::::::::::
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are successfully logged out.')
        return redirect('home')
    return redirect('home')