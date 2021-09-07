from django.db import models

# Create your models here.
class Highscore(models.Model):
  name = models.CharField(max_length=50)
  highscore = models.IntegerField()

  def __str__(self):
    return self.name