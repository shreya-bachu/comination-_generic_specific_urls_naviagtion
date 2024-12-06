from django.urls import path
from marts.views import *

app_name='marts'

urlpatterns=[
    path('dmart/',dmart,name='dmart')
]
