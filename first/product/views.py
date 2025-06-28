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
               print('Mobile:',frm.cleaned_data['mobile'])
               print('Re_Mobile:',frm.cleaned_data['re_mobile'])
               print('laptop:',frm.cleaned_data['laptop'])
               print('email:',frm.cleaned_data['email'])
               print('about:',frm.cleaned_data['about'])
               print('textarea:',frm.cleaned_data['textarea'])
               print('checkbox:',frm.cleaned_data['checkbox'])
               print('ram:',frm.cleaned_data['ram'])
               print('ssd:',frm.cleaned_data['ssd'])
               print('youtube_chanel:',frm.cleaned_data['youtube_chanel'])
               
              
                  
               return HttpResponseRedirect('/pdc/successfully')
               
          

     else:
         frm = RecentProduct(auto_id='true',label_suffix= ' -')
         print('Get Statment')
 

     return render(request,'product/recent.html',{'form':frm})
