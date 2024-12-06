from django.urls import path
from malls.views import *

app_name='malls'

urlpatterns=[
    path('mallofasia/',mallofasia,name='mallofasia'),
]
