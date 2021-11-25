from django.urls import path
from . import views

urlpatterns = [
    path('',views.courses,name="courses"),
    path('curso-anio/<course_year>/',views.c_year,name="c_year"),
]