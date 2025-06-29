from django.contrib import admin
from .models import laptop
# Register your models here.
@admin.register(laptop)
class laptopAdmin(admin.ModelAdmin):
    list_display=('mobile','re_mobile','laptop','email','about','textarea','checkbox','ram','ssd','youtube_chanel')
