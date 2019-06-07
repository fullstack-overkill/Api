from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Gerenciador de do perfil de usuario"""

    def create_user(self, email, name, password=None):
         """Criar novo perfil de usuario"""
        if not email:
            raise ValueError('Usuario deve ter um Email')

        email = self.normalize_email(email)
        user = self.models(email=email, name=name)

        user.set_password(password)
        user.save(ussing=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Cria e salva um super usuario"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user



class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for  users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrive short name of user"""
        return self.name

    def ___str___(self):
        """Return strig reoresentation of our user"""
        return self.email