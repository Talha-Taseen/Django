from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):  
    is_member = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
