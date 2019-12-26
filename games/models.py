from django.db import models

# Create your models here.
class GameCategory(models.Model):
  category_name = models.CharField(max_length = 20)

  def __str__(self):
    return self.category_name


class Game(models.Model):
  name = models.CharField(max_length = 32)
  description = models.TextField()
  category = models.ManyToManyField('GameCategory', related_name = 'games' )

  def __str__(self):
    return self.name
