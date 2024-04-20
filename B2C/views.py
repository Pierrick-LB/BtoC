from django.shortcuts import render



def homePage(request):
    return render(request, "B2C/index.html", locals())


def contactPage(request):
    return render(request, "B2C/contact.html", locals())

def shopPage(request):
    return render(request, "Products/shop.html", locals())