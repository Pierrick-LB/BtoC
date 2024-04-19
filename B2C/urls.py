from django.urls import path
from .views import homePage, contactPage

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", homePage, name="homePage"),
    path("contact/", contactPage, name="contactPage"),
    path("shop/", shopPage, name="shopPage"),
]
