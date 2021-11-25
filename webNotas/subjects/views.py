from django.shortcuts import render
from .models import Subjects
# Create your views here.
def subjects(request):
    subjects = Subjects.objects.all()
    year_no_repeat=Subjects.objects.dates('created','year')
    context = {
        'subjects': subjects,
        'year_no_repeat':year_no_repeat
    }
    return render(request, "subjects/subjects.html", context)
def s_year(request,subject_year):
    year_no_repeat=Subjects.objects.dates('created','year')
    year=Subjects.objects.filter(created__contains=subject_year)
    context = {
        'year_no_repeat':year_no_repeat,
        'subject_year':subject_year,
        'year':year
    }
    return render(request, "subjects-year/subjects-year.html", context)
