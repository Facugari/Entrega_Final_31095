from django.urls import path
from .views import render_items

app_name= "podcasts"
urlpatterns = [

    path('', render_items, name='items'),
    
]