from django.conf.urls import url, include

# Import the All Products view from views.py

from .views import index


# These urls will be linked to the top level urls in fsf-ecommerce-project
urlpatterns =  [
    url(r'^$', index, name="home"),
    
    ]
