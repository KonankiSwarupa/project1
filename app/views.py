from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def coffee(request):
                    return HttpResponse('Worst coffee available in starbucks')