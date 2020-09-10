#Made file and added all this
#We import each of our pages from our views.py file

from django.urls import path
from .views import HomePageView, AboutPageView, ClothingPageView

#Our urlpatterns adds the link to that path so we can access the page

urlpatterns = [
    path('about/', AboutPageView.as_view(), name="about"),
    path('clothing/', ClothingPageView.as_view(), name="clothing"),
    path('', HomePageView.as_view(), name="home"),
    ]