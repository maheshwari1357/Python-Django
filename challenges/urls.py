from . import views
from django.urls import path

urlpatterns=[
    path("",views.index),
    path("<int:month>",views.monthly_challenge_num),
    path("<str:month>", views.monthly_challenge, name="month-challenge")
    ]