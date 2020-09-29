from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .models import Resource
# Create your views here.

def resource(request):
    resources = Resource.objects.all()
    return render(request, 'resources.html', {'resources': resources})
