#We make this file and add everything to it
from django.urls import path
from .views import homePageView

urlpatterns = [
    path('', homePageView, name="home")     #Sets our home page to 'home'
    ]