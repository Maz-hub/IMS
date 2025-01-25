from django.shortcuts import render
from .models import Product


# Create your views here.

def index(request):
    products = Product.objects.all()  # Fetch all products
    context = {'products': products}  # Use 'products' as the context key
    return render(request, 'inventory/index.html', context)
