from django.db import models

# Import the Product model from products.models

from products.models import Product

# Create Order model

class Order(models.Model):
    
    # Full name, max 50 chars, cannot be left blank
    
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    
    # Postcode, may be blank, not everywhere has one
    
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    
    # This will do an automatic date; you can add whatever date you like
    
    date = models.DateField()
    
    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.id, self.full_name)
        
        
        
class OrderLineItem(models.Model):
    
    # Although not in the video, "on_delete=models.CASCADE," need to be 
    # added to 'ForeignKey' otherwise you get a red x
    
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    quantity = models.IntegerField(blank=False)
    
    def __str__(self):
        return "{0} {1} @ {2}".format(self.quantity, self.product.name, self.product.price)
        