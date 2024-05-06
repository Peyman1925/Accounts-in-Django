from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    
    username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
    photo = models.ImageField(
        upload_to='photo/profile/%Y/%m/%d/', default='defaultprofil.jpg', blank=False)
    
    def __str__(self):
        return self.username