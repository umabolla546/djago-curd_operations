from django.db import models

# Create your models here.
class emp(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=50)
    eaddres=models.CharField(max_length=50)