from django.shortcuts import render
from django.http import HttpResponseRedirect
from product.froms import RecentProduct

# Create your views here.
def pd(request):
    return render(request,'product/product.html')
def send(request):
     return render(request,'product/submit.html')
def details(request):
     if request.method=='POST':
          frm= RecentProduct(request.POST)
          if frm.is_valid():
               print('valid form')
               print('POST Statment')
               print(frm.cleaned_data)
               return HttpResponseRedirect('/pdc/successfully')
               
          

     else:
         frm = RecentProduct(auto_id='true',label_suffix= ' -')
         print('Get Statment')
 

     return render(request,'product/recent.html',{'form':frm})
