from django.urls import path
from Customer.views import hello_world


urlpatterns = [
    path('hello/', hello_world, name='hello_world'),
]
