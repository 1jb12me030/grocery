from django.urls import path
from .views import *
urlpatterns = [
    path('register/',RegistrationView.as_view()),
    path('login/',LoginView.as_view()),
    path('logout/',LogOutView.as_view()),
    path('category/',CategoryView.as_view()),
    #path('grocery/',GroceryView.as_view()),
    path('product/',ProductView.as_view()),
    path('cart/',CartView.as_view()),

    
    
    
              
 
]