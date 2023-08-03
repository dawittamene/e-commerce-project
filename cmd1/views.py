from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *
from .forms import OrderForm, CreationUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def registrationpage(request):
    form = CreationUserForm()
    if request.method == 'POST':
        form = CreationUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'registration.html', context)

def loginpage(request):
    form = CreationUserForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user =authenticate(request, username=username, password=password)
        if user is not None:
            login(request, username)
            return redirect('home')
    context = {'form': form}
    return render(request, 'login.html', context)
def logoutpage(request):
    logout(request)
    return redirect('login')


def home(request):
    customers = Customer.objects.all()      
    orders = Order.objects.all()
    context = {'customers': customers, 'orders': orders}
    return render(request, 'home.html',context) 
def products(request):
    
    products = Product.objects.all()
    context = {'products':products}
    return render(request, "products.html", context)
def customer(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    
    context = {'customers': customers, 'orders': orders}
    return render(request, "customer.html", context)


def createorder(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'order_form.html', context)
def updateorder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'order_form.html', context)

def deleteorder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('home')
    context = {'order': order}
    return render(request, 'delete.html', context)
    