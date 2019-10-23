from django.contrib import admin

# We need to add the models we've created otherwise we wont be ablce to access
# them via the admin panel.

from .models import Order, OrderLineItem

# We're creating a class here, OrderLineAdmin.
# And that inherits from the TabularInline within admin.
# TabularInline subclass defines the template used to render the Order in the
# admin interface. StackedInline is another option

class OrderLineAdminInline(admin.TabularInline):
    
    # And it uses the OrderLineItem as a model
    model = OrderLineItem

# And then we're creating a class, OrderAdmin, which inherits from the 
# ModelAdmin of the admin Django. That just takes inlines, which is the 
# OrderLineAdmin inline that we created above.
# The admin interface has the ability to edit more than one model on a single
# page. This is known as inlines.

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInline, )


admin.site.register(Order, OrderAdmin)
    
    
