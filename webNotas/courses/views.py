from django.shortcuts import render
from .models import Courses
# Create your views here.
def courses(request):
    courses = Courses.objects.all()
    year_no_repeat=Courses.objects.dates('created','year')
    context = {
        'courses': courses,
        'year_no_repeat':year_no_repeat
    }
    return render(request, "courses/courses.html", context)

def c_year(request,course_year):
    year_no_repeat=Courses.objects.dates('created','year')
    year=Courses.objects.filter(created__contains=course_year)
    context = {
        'year_no_repeat':year_no_repeat,
        'course_year':course_year,
        'year':year
    }
    return render(request, "courses-year/courses-year.html", context)