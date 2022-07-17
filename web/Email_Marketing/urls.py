from unicodedata import name
from django.urls import include , path
from .views import Marital_Customer , monthly_customer_purchase, Product_Purchase, Countries_Purchase, Conversion_Age_Marital,Top_5_Products, Age_Distribution, Gender_Conversion


urlpatterns = [
    path('Marital_Customer' , Marital_Customer ,name = 'Marital_Customer'),
    path('monthly_customer_purchase' , monthly_customer_purchase ,name = 'monthly_customer_purchase'),
    path('Product_Purchase' , Product_Purchase ,name = 'Product_Purchase'),
    path('Countries_Purchase' , Countries_Purchase ,name = 'Countries_Purchase'),
    path('Conversion_Age_Marital' , Conversion_Age_Marital ,name = 'Conversion_Age_Marital'),
    path('Top_end_Products' , Top_5_Products ,name = 'Top_end_Products'),
    path('Age_Distribution' , Age_Distribution ,name = 'Age_Distribution'),
    path('Gender_Conversion' , Gender_Conversion ,name = 'Gender_Conversion'),
    

    
    
]