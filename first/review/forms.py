
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm


class BuilidingAdd(UserCreationForm):
    class Meta:
        model=User
        fields=['username',"email",'first_name','last_name']

class Modifysuccessform(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','date_joined','is_staff','is_active']
