"""
URL configuration for B2C project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import shopDetails, shopPage, cartPage, chackoutPage, notFound



urlpatterns = [
    path("shopDetails/",shopDetails,name="shopDetails"),
    path("shop/", shopPage, name="shopPage"),
    path("cart/", cartPage, name="cartPage"),
    path("chackout/", chackoutPage, name="chackoutPage"),
    path("404/", notFound, name="notFound"),
]

