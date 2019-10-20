from django.shortcuts import render

# Import our Product from models.py

from .models import Product


# View - All Products

def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})