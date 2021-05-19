from django.db import models
class CovidDistrict(models.Model):
    state = models.CharField(max_length=100)
    district= models.CharField(max_length=100)
    active= models.IntegerField()
    confirmed = models.IntegerField()
    deceased = models.IntegerField()
    recovered = models.IntegerField()
    published_date=models.DateField(auto_now_add=True)


    def __str__(self):
        return self.state