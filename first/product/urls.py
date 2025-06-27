from django.urls import path
from .import views

urlpatterns = [
    path('product/',views.pd,name='Product'),
    path('recents/',views.details),
    path('successfully/',views.send),

]