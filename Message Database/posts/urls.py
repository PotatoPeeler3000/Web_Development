#Created this file and added everything to it
from django.urls import path
from .views import HomePageView

#This adds the homepageview to our urlpatterns as 'home' in the URL

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    ]
