from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Catagory(models.Model):
    name = models.CharField(max_length=255)


    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Catagories'

    def __str__(self):
        return self.name

class Item(models.Model):
    catagory = models.ForeignKey(Catagory,related_name = 'items', on_delete= models.CASCADE)

    name = models.CharField(max_length=255) 
    description = models.TextField(blank=True, null= True)
    price = models.FloatField()
    created_at = models.DateField(auto_now_add=True)
    image=models.ImageField(upload_to = 'product_images', blank=True,null=True)  
    created_by = models.ForeignKey(User, related_name='items',on_delete=models.CASCADE)
    is_sold = models.BooleanField(default=False)

    def __str__(self):
        return self.name        