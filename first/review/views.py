from django.shortcuts import render

# Create your views here.
def customar(request):
    return render(request,'review/review.html')

