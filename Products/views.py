from django.shortcuts import render


def shopDetails(request):
    return render(request, "Products/shopDetails.html",locals())

def shopPage(request):
    return render(request, "Products/shop.html", locals())

def cartPage(request):
    return render(request, "Products/cart/cart.html", locals())

def checkoutPage(request):
    return render(request, "Products/cart/checkout.html", locals())

def notFound(request):
    return render(request, "Products/cart/404.html", locals())  

