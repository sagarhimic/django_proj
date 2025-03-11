from django.db import models
from django.urls import reverse
class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=64)
    esal = models.FloatField()
    eaddr = models.CharField(max_length=256)

    def get_absolute_url(self):
        return reverse('list',kwargs={'pk':self.pk})
