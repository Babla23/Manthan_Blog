from django.db import models
from django.utils.text import slugify

# Create your models here.


class Manthan(models.Model):
    pic = models.ImageField(upload_to='')
    name = models.CharField(max_length=20)
    address = models.TextField(max_length=50)
    contact = models.IntegerField()
    mail = models.EmailField(max_length=30)

    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(Manthan,self).save(*args,**kwargs)


    def __str__(self):
        return self.name
