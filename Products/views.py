from django.shortcuts import render


def shopDetails(request):
    return render(request, "Products/shopDetails.html",locals())

def shopPage(request):
              return render(request, "Products/shop.html", locals())

