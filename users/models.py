
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image

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

  def save(self):
    super().save()

    img = Image.open(self.image.path)

    if img.height > 500 or img.width > 500:
      output_size = (500,500)
      img.thumbnail(output_size)
      img.save(self.image.path)

