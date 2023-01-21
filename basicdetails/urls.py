from django.urls import path, include 
from basicdetails import views

app_name = 'basicdetails'
urlpatterns = [
    path('', views.index, name="index"),
]
