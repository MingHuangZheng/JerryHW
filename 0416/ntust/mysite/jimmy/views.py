from django.shortcuts import render_to_response
from django.http import HttpResponse
# Create your views here.

from .models import Information
def index(request):
    information = Information.objects.all()
    return render_to_response('jimmy/info.html',locals())