from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from uuid import uuid4
import random
from django.db.models.signals import post_save
from django.dispatch import receiver


# Get the current user model

class CustomBaseModel(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        first_name = extra_fields.get('first_name').strip().capitalize()
        last_name = extra_fields.get('last_name').strip().capitalize()
        if first_name and last_name:
            user.full_name = f"{first_name} {last_name}"
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password=None,  *args, **kwargs):
        user = self.create_user(email, username, password, *args, **kwargs)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    




class CustomUser(AbstractUser):
    unique_user_id = models.UUIDField(default=uuid4, editable=False)
    fullname = models.CharField(max_length=200, blank=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    biography = models.TextField()
    

    objects = CustomBaseModel()

    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']
    USERNAME_FIELD = "username"
    



@receiver(post_save, sender=CustomUser)
def set_fullname(sender, instance, created, **kwargs):
    if created:
        new_first_name = instance.first_name.strip().capitalize()
        new_last_name = instance.last_name.strip().capitalize()
        
        if new_first_name and new_last_name:
            instance.fullname = f"{new_first_name} {new_last_name}"
            instance.save()

    