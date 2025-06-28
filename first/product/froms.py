from django import forms
from django.core import validators
class RecentProduct(forms.Form):
    mobile= forms.CharField(label='Enter your Mobile Number:', max_length=11, widget=forms.TextInput(attrs={'type': 'tel', 'pattern': '^[0-9]{11}$', 'maxlength': '11', 'placeholder': 'e.g., 017xxxxxxxx'}))
    re_mobile= forms.CharField(label='Enter your Re_Mobile Number:', max_length=11, widget=forms.TextInput(attrs={'type': 'tel', 'pattern': '^[0-9]{11}$', 'maxlength': '11', 'placeholder': 'e.g., 017xxxxxxxx'}))
    laptop= forms.CharField(label='Enter your Laptop name:')
    email=forms.EmailField(initial='alamin88.ime@gmail.com',label_suffix='=', validators=[validators.MaxLengthValidator(25)])
    about= forms.CharField(help_text='Describe about Laptop')
    textarea=forms.CharField(widget=forms.Textarea(attrs={'rows':4,'cols':40}))
    checkbox=forms.CharField(widget=forms.CheckboxInput)
    ram=forms.IntegerField(min_value=4,max_value=12)
    ssd=forms.DecimalField(min_value=1,max_value=15,max_digits=3,decimal_places=2)
    youtube_chanel=forms.BooleanField(label='subscribe the youtube channel')
    
   # files=forms.CharField(widget=forms.FileInput)#
    def clean(self):
        cleaned_data=super().clean()
        mobile_match=self.cleaned_data['mobile']
        remobile_match=self.cleaned_data['re_mobile']
        if mobile_match !=remobile_match:
            raise forms.ValidationError('mobile number doesnot match')
        
   
   
   
  