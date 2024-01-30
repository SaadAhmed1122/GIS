# from django.urls import path
# from . import views

# #url configuration
# urlpatterns = [
#     path('hello/', views.say_hello)
# ]
from django.urls import path, include
from .views import emp, add_business
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', emp, name='admin'),
    path('addBusiness/', add_business, name='add_business_business'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
