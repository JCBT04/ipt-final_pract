from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .managers import UserManager
# Create your models here.


class User (AbstractUser):
      username = None
      email = models.EmailField()
      id_number = models.IntegerField(unique=True)
      is_staff = models.BooleanField(default=False)
      is_active = models.BooleanField(default=True)
      date_joined = models.DateTimeField(default=timezone.now)

      USERNAME_FIELD = 'id_number'
      REQUIRED_FIELDS = [
              'email'
      ]
      
      objects = UserManager()

      def __str__(self):
          return '{}' .format(self.id_number)