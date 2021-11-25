from django.shortcuts import render
from .models import News,Videos
# Create your views here.
def activities(request):
    news=News.objects.all()
    videos=Videos.objects.all()

    context = {
        'news': news,
        'videos':videos
    }
    return render(request, "activities/activities.html", context)
def new(request,new_id):
    new=News.objects.filter(id=new_id)
    
    context = {
        'new': new
    }
    return render(request, "new/new.html", context)