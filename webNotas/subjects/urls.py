from django.urls import path
from . import views

urlpatterns = [
    path('',views.subjects,name="subjects"),
    path('asignatura-anio/<subject_year>/',views.s_year,name="s_year"),
]