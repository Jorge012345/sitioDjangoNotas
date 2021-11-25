from django.urls import path
from . import views

urlpatterns = [
    path('',views.projects,name="projects"),
    path('proyecto-anio/<project_year>/',views.p_year,name="p_year"),

]