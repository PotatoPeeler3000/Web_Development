from django.urls import path
from .views import HomePageView, AboutPageView, ClothingPageView


urlpatterns = [
    path('about/', AboutPageView.as_view(), name="about"),
    path('clothing/', ClothingPageView.as_view(), name="clothing"),
    path('', HomePageView.as_view(), name="home"),
    ]