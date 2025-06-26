

from django.shortcuts import render
from payments.models import pay_method


# Create your views here.
def bk(request):
    Name={'friends':['alamin','tomal','tonmoy','tanpiya','tahominah']}
    
    return render(request,'payments/payments_1.html',Name)
def Rk(request):
    return render(request,'payments/payments_2.html')

def Payment_method(request):
    pay_m= pay_method.objects.all()
    return render(request,'payments/pay.html',{'pay':pay_m})

