from django.contrib import auth
from django.db import models
from django.utils import timezone

# Create your models here.from django.contrib import auth


class User(auth.models.User, auth.models.PermissionsMixin):
    
    def __str__(self):
        return "@{}".format(self.username)

