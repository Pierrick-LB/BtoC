from django.shortcuts import render

# Create your views here.
def shopDetails(request):
    return render(request, "Products/shopDetails.html",locals())