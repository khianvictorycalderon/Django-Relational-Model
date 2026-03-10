from django.shortcuts import HttpResponse

# Create your views here.
def demo(_):
    return HttpResponse("API is working!")