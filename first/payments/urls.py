from django.urls import path
from .import views
app_name = 'payments' 
urlpatterns = [
    path('Bkash/',views.bk,name ='paymentone'),
    path('Rocket/',views.Rk, name ='paymenttwo'),
    path('pays/',views.Payment_method)

   # path('f',views.name1),
    #path('H',views.houmtoune),
    #path('love',views.like),
]