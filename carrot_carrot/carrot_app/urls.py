from django.urls import path
from .views import *
app_nem = 'carrot_app'
urlpatterns = [
    path('', main, name='main'),
    path('write', write, name='write'),
    path('logout', logout, name="logout"),
]
