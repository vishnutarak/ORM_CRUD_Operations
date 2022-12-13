from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
# Create your views here.

def display_Topic(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    return render(request,'display_Topic.html',d)

def dispaly_webpage(request):
    LWO=Webpage.objects.all()
    LWO=Webpage.objects.filter(table_name='circket')
    LWO=Webpage.objects.exclude(table_name='circket')
    LWO=Webpage.objects.all().order_by('name')
    LWO=Webpage.objects.order_by('-name')
    LWO=Webpage.objects.all()[:3:]
    LWO=Webpage.objects.all().order_by(Length('name'))
    LWO=Webpage.objects.all().order_by(Length('name').desc())
   
    d={'LWO':LWO}
    return render(request,'dispaly_webpage.html',d)


def dispaly_access(request):
    LAO=AccessRecords.objects.all()
    d={'LAO':LAO}
    return render(request,'display_access.html',d)