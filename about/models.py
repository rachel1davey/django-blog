from django.db import models

# Create your models here.

class about(models.Model):
  title = models.TextField
  content = models.TextField
  updated_on = models.DateTimeField
  
    class Meta:
        verbose_name = _("")
        verbose_name_plural = _("s")

    def __str__(self):
        return self.name

