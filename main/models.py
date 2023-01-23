from django.db import models

class Model_File(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(verbose_name=' file must be in .pkl ')
    
    def __str__(self) -> str:
        return self.name

class Features(models.Model):
    population = models.FloatField()
    gdp = models.FloatField()
    