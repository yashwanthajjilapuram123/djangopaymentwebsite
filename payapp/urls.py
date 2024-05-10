from django.contrib import admin
from django.urls import path, include
from payapp import views

app_name = 'payapp'

urlpatterns = [
    # path("", views.index, name="payapp"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]