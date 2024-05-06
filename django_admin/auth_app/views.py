from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import User
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth import logout as django_logout

# Create your views here.


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        
        email = request.POST.get('email')
        
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request,'username already exist.')
                return redirect('register')
            
            
            
            user = User.objects.create_user(
                username=username,
                password=password,
                first_name=first_name,
                last_name =last_name,
                is_customer =True,
                # is_admin =True,
                
                
                email=email
                
            )
            user.save()
            messages.success(request,'Registered successfully and logged in.')
            return redirect('index')
        else:
            messages.error(request,'password do not match.')
            return redirect('register')
        
    return render(request,'register.html')



def customer_list(request):
    
    customers = User.objects.filter(is_customer=True)
    
    return render(request, 'customer_list.html', {'customers': customers})



def admin_list(request):
    
   admins = User.objects.filter(is_admin=True)
    
    
   return render(request, 'admin_list.html', {'admins': admins})




def login_u(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, 'Username does not exist.')
            return render(request, 'login.html')

        if user.check_password(password):
            authenticated_user = authenticate(request, username=username, password=password)
            if authenticated_user is not None:
                login(request, authenticated_user)
                messages.success(request, 'Login Successfully')
                return redirect('index')
            else:
                messages.error(request, 'Invalid login credentials.')
        else:
            messages.error(request, 'Incorrect password.')

        return render(request, 'login.html')

    return render(request, 'login.html')




def logout(request):
    django_logout(request)
    messages.success(request, 'Logged out successfully.')
    return redirect('index')
