from django.contrib import admin

# Import the model we have created in products/models.py
from .models import Product

# Register our model so that we can add products via the admin panel.

admin.site.register(Product)

