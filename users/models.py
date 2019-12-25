
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass
    # add additional fields in here

    def __str__(self):
        return self.username

class Profile(models.Model):
  user = models.OneToOneField(CustomUser, on_delete= models.CASCADE)
  image = models.ImageField(default= "default.jpg", upload_to="profile_pics" )

  def __str__(self):
    return f'{self.user.username} Profile'
