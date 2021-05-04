from django.db import models
class CovidCases(models.Model):
    state = models.CharField(max_length=100)
    district= models.CharField(max_length=100)
    active= models.CharField(max_length=100)
    confirmed = models.CharField(max_length=100)
    deceased = models.CharField(max_length=100)
    recovered = models.CharField(max_length=100)

    def __str__(self):
        return self.state