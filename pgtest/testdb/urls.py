# from django.urls import path
# from . import views

# #url configuration
# urlpatterns = [
#     path('hello/', views.say_hello)
# ]
from django.urls import path, include
from .views import emp
from .views import road_form_view
from .views import road_create, road_list
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', emp, name='admin'),
    # path('addBusiness/', add_business, name='add_business_business'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('form/', road_form_view, name='road_form_view'),
    path('roads/create/', road_create, name='road_create'),
    path('roads/list/', road_list, name='road_list'),

]
