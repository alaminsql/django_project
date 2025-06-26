from django.shortcuts import render


# Create your views here.
def pd(request):
    return render(request,'product/product.html')