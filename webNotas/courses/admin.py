from django.contrib import admin
from .models import Courses

# Register your models here.

class CoursesAdmin(admin.ModelAdmin):
   readonly_fields = ('created', 'updated')



admin.site.register(Courses,CoursesAdmin)