from django.db import models


# Create your models here.
class User(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    Id = models.CharField(max_length=100, blank=True, default='')
    password = models.CharField(max_length=16, blank=True, default='')

    class Meta:
        ordering = 'create_time'
