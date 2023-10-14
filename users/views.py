from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .models import CustomUser


# Create your views here.

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html')

    else:

        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, "signin.html", {'error': 'username of password incorret'})
        else:
            login(request,user)
            return redirect('profile')



def signup(request):
    
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        if request.method == 'POST':     
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            phone = request.POST['phone']
            username = request.POST['username']
            password1 = request.POST['password1']
            password2 = request.POST['password2']       
            
            if password1 == password2:
                 try:
                     # Crea el usuario
                     is_master = False
                     user = CustomUser.objects.create_user(username=username, password=password1, first_name=first_name, last_name=last_name, email=email, phone=phone, is_master=is_master)
                     login(request, user)  # Inicia sesión automáticamente después del registro
                     return redirect('profile')
                 except IntegrityError:
                     return render(request, 'signup.html', {"error": 'Este Usuario ya existe'})

    return render(request, 'signup.html', {"error": 'La contraseñas no coinciden'})

def profile(request):
    user = request.user  # Obtiene el usuario autenticado
    
    # Ahora puedes acceder a los datos del usuario
    username = user.username
    first_name = user.first_name
    last_name = user.last_name
    email = user.email
    phone = user.phone
    is_master = user.is_master  # Puedes usar esto para determinar si el usuario es profesor o no

    return render(request, 'profile.html', {
        'username': username,
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'phone': phone,
        'is_master': is_master,
    })

