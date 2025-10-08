from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('register/',Register_view,name='register'),
    path('login/',login_view, name='login'),
    path('logout/',logout_view, name='logout'),
    path('add-to-cart/<int:id>/',AddToCart,name='add-to-cart'),
    path('cart/',cart,name='cart'),
    path('remove/<int:id>/',RemoveFromCart,name='remove'),
    path('payment',payment, name='payment-success'),
    path('mynotes/',mynotes,name='mynotes'),
    path('category/<int:id>',CategoryNotes, name='category-notes'),
]
