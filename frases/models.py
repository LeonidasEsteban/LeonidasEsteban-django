from django.db import models

# Create your models here.

class Frase(models.Model):
    frase     = models.CharField(max_length=1000)
    autor     = models.CharField(max_length=150)
    fecha     = models.DateField()
    link      = models.CharField(max_length=1000, blank=True)
    slug      = models.CharField(max_length=300, blank=True)
    activa    = models.BooleanField(default=True)
    destacada = models.BooleanField(default=False)

    def __unicode__(self):
        return self.frase

