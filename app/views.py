from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
# Create your views here.
from django.db.models import Q
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
    LWO=Webpage.objects.filter(name__startswith='r')
    LWO=Webpage.objects.filter(name__endswith='d')
    LWO=Webpage.objects.filter(name__contains='a')
    LWO=Webpage.objects.filter(name__in=('MSD','ronaldo'))
    LWO=Webpage.objects.filter(name__regex='^M\w{6}')
    LWO=Webpage.objects.all()
    LWO=Webpage.objects.filter(Q(table_name='foot ball') & Q(name__startswith='r'))
    LWO=Webpage.objects.all()
    LWO=Webpage.objects.filter(Q(table_name='circket') | Q(name__startswith='M'))
    LWO=Webpage.objects.all()
    d={'LWO':LWO}
    return render(request,'dispaly_webpage.html',d)


def dispaly_access(request):
    LAO=AccessRecords.objects.all()
    LAO=AccessRecords.objects.filter(date='1999-11-01')    
    LAO=AccessRecords.objects.filter(date__year='2022')
    LAO=AccessRecords.objects.filter(date__month='1')    
    LAO=AccessRecords.objects.filter(date__day='14')    
    LAO=AccessRecords.objects.filter(date__gte='1999-11-01')
    LAO=AccessRecords.objects.filter(date__lte='1999-11-01')
    LAO=AccessRecords.objects.filter(date__year__gte='1999')
    d={'LAO':LAO}
    return render(request,'display_access.html',d)

def update_webpage(request):
    #Webpage.objects.filter(table_name='Boxing').update(name='Naresh',url='https://Naresh.in')
    #Webpage.objects.filter(name='ABCDE').update(table_name='Foot Ball')
    T=Topic.objects.get_or_create(topic_name='Cricket')[0]
    T.save()
    Webpage.objects.update_or_create(name='ABD',defaults={'table_name':T,'url':'https://ABD.in'})
    LWO=Webpage.objects.all()
    d={'LWO':LWO}
    return render(request,'dispaly_webpage.html',d)


def delete_webpage(request):
    #Webpage.objects.filter(table_name='Cricket').delete()
    
    Webpage.objects.all().delete()
    LWO=Webpage.objects.all()
    d={'LWO':LWO}
    return render(request,'dispaly_webpage.html',d)
