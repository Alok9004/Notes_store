from django.contrib import admin
from .models import Note, CartItem, Category
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','name','image']

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display=['id','title','description','price','file','thumbnail','uploaded_time']

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display=['id','user' , 'note', 'added_at','paid']
