#We created this entire file for our liking

from django.http import HttpResponse

        #This function outputs text to our homepage using the Http library
def homePageView(request):
    return HttpResponse("Hello sample program, glad to see you are working")