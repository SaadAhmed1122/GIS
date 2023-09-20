# from django.urls import path
# from . import views

# #url configuration
# urlpatterns = [
#     path('hello/', views.say_hello)
# ]
from django.urls import path, include
from .views import emp, add_business

urlpatterns = [
    path('', emp, name='index'),
    path('addBusiness/', add_business, name='add_business_business'),
]
