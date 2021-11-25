from django.urls import path
from . import views

urlpatterns = [
    path('',views.activities,name="activities"),
    path('noticia/<new_id>/',views.new,name="new"),
]