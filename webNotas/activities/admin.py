from django.contrib import admin
from .models import News,Videos
# Register your models here.
class ActivitiesAdmin(admin.ModelAdmin):
   readonly_fields = ('created', 'updated')




admin.site.register(News,ActivitiesAdmin)
admin.site.register(Videos,ActivitiesAdmin)