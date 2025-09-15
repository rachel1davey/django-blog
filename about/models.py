from django.db import models

# Create your models here.

class about(models.Model):
  title = models.CharField(max_length=300)
  content = models.TextField
  updated_on = models.DateTimeField
  
  def __str__(self):
    return self.name

