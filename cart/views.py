from django.shortcuts import render, redirect, reverse

# View cart contents

def view_cart(request):
    """
    A view that renders the cart contents page
    """
    
    # We dont need to return a dictionary because the cart context is available
    # to all pages
    return render(request, 'cart.html')
    
    
def add_to_cart(request, id):
    """
    Add a quantity of the specified product to the cart
    """
        
    # This takes an integer from the form we created
    quantity = int(request.POST.get('quantity'))
    
    # This is going to the cart from the session (not from the database), 
    # and it gets a cart if one already exists, otherwise it gets an empty
    # dictionary
        
    cart = request.session.get('cart', {})
        
    # Add cart id and quantity
    
    if id in cart:
        cart[id] = int(cart[id]) + quantity
        
    else:
        cart[id] = cart.get(id, quantity)
    
        
    request.session['cart'] = cart
        
    return redirect(reverse('index'))
        

def adjust_cart(request, id):
    
    """
    Adjust the quantity of the specified product to the specified amount
    """
    
    # This takes an integer from the form we created
    
    quantity = int(request.POST.get('quantity'))
    
    # This is going to the cart from the session (not from the database), 
    # and it gets a cart if one already exists, otherwise it gets an empty
    # dictionary
        
    cart = request.session.get('cart', {})
    
    # Only adjust the cart if 'quantity' is greater than zero
    
    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    
    request.session['cart'] = cart
    
    return redirect(reverse('view_cart'))