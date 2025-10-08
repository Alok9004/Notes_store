from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Note, CartItem, Category
from .forms import LoginForm, RegistrationForm

# Create your views here.

def home(request):
    obj=Category.objects.all()
    return render(request,'home.html',{'categories':obj})

def CategoryNotes(request, id):
    category=Category.objects.get(id=id)
    notes=Note.objects.filter(category=category)
    return render(request, 'notes.html', {'category':category, 'notes':notes})

def Register_view(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created Successfully!')
            return redirect("login")
        else:
            messages.error(request,'Please enter valid details.')
    form=RegistrationForm()
    return render(request,'register.html', {'form':form})

def login_view(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            user=authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                login(request,user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid Username or Password')
    form=LoginForm()
    return render(request,'login.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def AddToCart(request,id):
    obj=get_object_or_404(Note, id=id)
    CartItem.objects.get_or_create(user=request.user, note=obj)
    messages.success(request,f"{obj.title} added to your Cart.")
    return redirect("cart")

@login_required
def cart(request):
    obj= CartItem.objects.filter(user=request.user)
    total= sum(i.note.price for i in obj)
    return render(request,'cart.html',{'CItem':obj, 'total':total})


@login_required
def RemoveFromCart(request,id):
    item=get_object_or_404(CartItem, id=id, user=request.user)
    item.delete()
    messages.warning(request,"Item removed from Cart.")
    return redirect("cart")

@login_required
def payment(request):
    cart_items=CartItem.objects.filter(user=request.user)
    for i in cart_items:
        i.paid=True
        i.save()
    messages.success(request,"Payment Successful! You can now access your purchased notes.")
    return redirect('mynotes')

@login_required
def mynotes(request):
    paid_items= CartItem.objects.filter(user=request.user, paid=True)
    notes= [item.note for item in paid_items]
    return render(request,'mynotes.html',{'notes':notes})