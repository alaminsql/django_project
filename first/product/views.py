from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from product.froms import RecentProduct
from .models import laptop

# Create your views here.
def pd(request):
    return render(request,'product/product.html')
def send(request):
     return render(request,'product/submit.html')
def details(request):
     if request.method=='POST':
          frm= RecentProduct(request.POST)
          if frm.is_valid():
               mo=frm.cleaned_data['mobile']
               rmo=frm.cleaned_data['re_mobile']
               lb=frm.cleaned_data['laptop']
               em=frm.cleaned_data['email']
               ab=frm.cleaned_data['about']
               tx=frm.cleaned_data['textarea']
               ch=frm.cleaned_data['checkbox']
               ra=frm.cleaned_data['ram']
               ss=frm.cleaned_data['ssd']
               you=frm.cleaned_data['youtube_chanel']
               buy=laptop(mobile=mo,re_mobile=rmo,laptop=lb,email=em,about=ab,textarea=tx,checkbox=ch,ram=ra,ssd=ss,youtube_chanel=you)
               buy.save()
               
               
              
                  
               return HttpResponseRedirect('/pdc/successfully')
               
          

     else:
         frm = RecentProduct(auto_id='true',label_suffix= ' -')
         print('Get Statment')
 

     return render(request,'product/recent.html',{'form':frm})

def midd(request):
     print('1st middleware')
     return HttpResponse("this is first middleware")
