from django.db import models

# Create your models here.

class patient(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    mobile = models.CharField(max_length=50, blank=False, null=False)
    address = models.TextField(blank=False, null=False)
    age = models.CharField(max_length=50, blank=False, null=False)
    gender = models.CharField(max_length=50, blank=False, null=False)
    def __str__(self):
        return "{0}_{1}".format(self.id, self.name)