from django.db import models

class Deparment(models.Model):
  name = models.CharField(max_length=50,unique=True)
  def __str__(self) -> str:
    return self.name
