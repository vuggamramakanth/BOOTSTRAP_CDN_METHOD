from django.shortcuts import render

# Create your views here.
def bootstrap_cdn(request):
    return render(request,'bootstarp_cdn.html')
