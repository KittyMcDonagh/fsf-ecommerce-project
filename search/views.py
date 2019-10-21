from django.shortcuts import render

from products.models import Product

# Search view

def do_search(request):
    
    # Get whatever is returned on the form. Form name = 'q'. Whatever is typed
    # into this form will be used to filter the products
    
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, 'products.html', {'products': products})

