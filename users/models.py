from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Agregar campos personalizados
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    is_master = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)  

    
    def __str__(self):
        return self.username