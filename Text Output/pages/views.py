#pages/views/py

from django.http import HttpResponse

# Create your views here.

def homePageView(request):
    return HttpResponse("Hello Winston! Hope your pong assignemnt works!!")
