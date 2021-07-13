from django.shortcuts import render


# Create your views here.
def login(request): #หน้า index.html
  
    return render(request, 'login.html')

# def good(request): #หน้า good.html
  
#     return render(request, 'good.html')
