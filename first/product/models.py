from django.db import models

# Create your models here.
class laptop(models.Model):
    mobile=models.CharField(max_length=20)
    re_mobile=models.CharField(max_length=20)
    laptop=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    about=models.CharField(max_length=20)
    textarea=models.CharField(max_length=20)
    checkbox=models.CharField(max_length=20)
    ram=models.IntegerField()
    ssd=models.CharField(max_length=20)
    youtube_chanel=models.BooleanField()
  
    
