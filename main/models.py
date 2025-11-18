from django.db import models
from django.contrib.auth.models import User
from cloudinary.models  import CloudinaryField
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100)
    image=CloudinaryField('images', blank=True, null=True)

class Note(models.Model):
    category=models.ForeignKey(Category, on_delete=models.CASCADE, related_name='notes')
    title=models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField(max_digits=6, decimal_places=2)
    file=CloudinaryField('notes')
    thumbnail=CloudinaryField('thumbnails', blank=True, null=True)
    uploaded_time=models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    note=models.ForeignKey(Note, on_delete=models.CASCADE)
    added_at=models.DateTimeField(auto_now_add=True)
    paid=models.BooleanField(default=False)

    class Meta:
        unique_together=('user','note')