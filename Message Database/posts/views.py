#Cleared this file then added everything to this file

from django.views.generic import ListView
from .models import Post

#This allows us to see the posts from the home page
class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts_list'
