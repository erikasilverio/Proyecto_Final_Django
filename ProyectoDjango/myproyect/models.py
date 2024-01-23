from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    
    username = models.CharField(max_length=20, unique=True) 
    password = models.CharField(max_length=10)

    




'''' from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    documento = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=15)
    imagen = models.ImageField(blank=True, null=True, upload_to='perfil/')

    

    def __str__(self):
        return self.username

    
    class Meta:
        app_label = 'myproyect'

'''