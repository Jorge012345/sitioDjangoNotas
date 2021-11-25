from django.shortcuts import render
from .models import ImagesCover,Main
# Create your views here.
def home(request):
    imges_cover = ImagesCover.objects.all()
    main = Main.objects.all()
    context = {
        'imges_cover': imges_cover,
        'main': main
    }
    return render(request, "home/home.html", context)


