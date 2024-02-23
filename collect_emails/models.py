from django.db import models

class Supporter(models.Model):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)

