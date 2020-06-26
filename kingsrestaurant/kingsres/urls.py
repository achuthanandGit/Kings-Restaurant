from django.urls import  path

from . import views

app_name = "kingsres"

urlpatterns = [
    path('', views.home, name='home'),
]