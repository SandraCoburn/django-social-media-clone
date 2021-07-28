from django.db import models
from django.contrib import auth

# Create your models here.
class User(auth.models.User,auth.models.PermissionsMixin):

  def __str__(self) -> str:
      #auth.models.User will bring a form with username etc
      return "@{}".format(self.username)