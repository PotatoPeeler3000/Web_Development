#We created our templates here
#This doesn't use our HttpResponse because we are using templates

from django.views.generic import TemplateView

#We use template classes to create additional pages on our webpage

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class ClothingPageView(TemplateView):
    template_name = 'clothing.html'