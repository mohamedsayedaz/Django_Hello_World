from django.urls import path
from .views import *

urlpatterns = [
    path("", homePageView, name="home"),
    path("about", aboutPageView, name="about"),
    path("contact", contactPageView, name="contact"),
]
