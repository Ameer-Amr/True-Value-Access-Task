from django.db import models

# Create your models here.
class accounts(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip = models.CharField(max_length=8)
    email = models.EmailField(max_length=100,unique=True)
    web = models.URLField(max_length=200)
    age = models.IntegerField()
    
    
    def __str__(self):
        return self.first_name