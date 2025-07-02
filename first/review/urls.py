from django.urls import path
from .import views

urlpatterns = [
    path('review',views.customar, name='review'),
    path('bulid/',views.bulding_form,name='registration'),
    path('login/',views.login_from,name='login'),
    path('success/',views.login_success),
    path('logout/',views.logout_form, name='logout'),
    path('cpass/',views.pasword_change,name='passwordchange'),
    path('withoutpass/',views.change_pass_without_oldpass, name='withoutold'),
]
