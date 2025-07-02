from django.shortcuts import render,HttpResponseRedirect
from .forms import BuilidingAdd,Modifysuccessform
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm,UserChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash

# Create your views here.
def customar(request):
    return render(request,'review/review.html')

def bulding_form(request):
    if request.method=='POST':
        frm=BuilidingAdd(request.POST)
        if frm.is_valid():
            frm.save()
    else:
        frm = BuilidingAdd
    return render(request,'review/building.html',{'form':frm})
    
    
 #login 
  
def login_from(request):
    if request.method == 'POST':
        variable = AuthenticationForm(request=request, data=request.POST)
        if variable.is_valid():
            usern = variable.cleaned_data['username']
            userp = variable.cleaned_data['password']
            user = authenticate(username=usern, password=userp)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/Rv/success/')  # ✅ সফল হলে success পেইজে যাবে
        # ⛔ Login ব্যর্থ হলে নিচে গিয়ে আবার form রেন্ডার করবে
    else:
        variable = AuthenticationForm()  # ✅ GET হলে ফর্ম তৈরি হবে

    return render(request, 'review/login.html', {'form': variable}) 

            


#successfully login
def login_success(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            frm=Modifysuccessform(request.POST,instance=request.user)
            if frm.is_valid():
                frm.save()
        else:
            frm=Modifysuccessform(instance=request.user)
        return render(request,'review/success.html',{'form':frm})
        
    else:
        return HttpResponseRedirect('/login/')

        

def logout_form(request):
    logout(request)
    return HttpResponseRedirect('/Rv/login')
#Changepassword

def pasword_change(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            frm=PasswordChangeForm(user= request.user,data=request.POST)
            if frm.is_valid():
                frm.save()
                update_session_auth_hash(request,frm.user)
                return HttpResponseRedirect('/Rv/success/')
        else:
            frm=PasswordChangeForm(user= request.user)
        return render(request,'review/cpass.html',{'form':frm})
    else:
        return HttpResponseRedirect('/Rv/login')
    
#change without old pass
def change_pass_without_oldpass(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            frm=SetPasswordForm(user= request.user,data=request.POST)
            if frm.is_valid():
                frm.save()
                update_session_auth_hash(request,frm.user)
                return HttpResponseRedirect('/Rv/success/')
        else:
            frm=SetPasswordForm(user= request.user)
        return render(request,'review/withoutoldpass.html',{'form':frm})
    else:
        return HttpResponseRedirect('/Rv/login')


