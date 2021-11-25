from django.shortcuts import render
from .models import Projects
# Create your views here.
def projects(request):
    projects = Projects.objects.all()
    year_no_repeat=Projects.objects.dates('created','year')
    context = {
        'projects': projects,
        'year_no_repeat':year_no_repeat
    }
    return render(request, "projects/projects.html", context)

def p_year(request,project_year):
    year_no_repeat=Projects.objects.dates('created','year')
    year=Projects.objects.filter(created__contains=project_year)
    context = {
        'year_no_repeat':year_no_repeat,
        'project_year':project_year,
        'year':year
    }
    return render(request, "projects-year/projects-year.html", context)