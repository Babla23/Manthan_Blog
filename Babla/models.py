from django.db import models

# Create your models here.
class babla(models.Model):
    pic = models.ImageField(upload_to='')
    name = models.CharField(max_length=20)
    address = models.TextField(max_length=50)
    contact = models.IntegerField()
    mail = models.EmailField(max_length=30)

    def __str__(self):
        return self.name