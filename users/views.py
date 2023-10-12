from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .models import CustomUser


# Create your views here.
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Autentica al usuario
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('profile')

    return render(request, 'signin.html')

def signup(request):
    
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        if request.method == 'POST':     
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            telefono = request.POST['telefono']
            username = request.POST['username']
            password1 = request.POST['password1']
            password2 = request.POST['password2']       
            
            if password1 == password2:
                 try:
                     # Crea el usuario
                     es_profesor = False
                     user = CustomUser.objects.create_user(username=username, password=password1, first_name=first_name, last_name=last_name, email=email, telefono=telefono, es_profesor=es_profesor)
                     login(request, user)  # Inicia sesión automáticamente después del registro
                     return redirect('profile')
                 except IntegrityError:
                     return render(request, 'signup.html', {"error": 'Este Usuario ya existe'})

    return render(request, 'signup.html', {"error": 'La contraseñas no coinciden'})

@login_required
def profile(request):
    return render(request, 'profile.html')

